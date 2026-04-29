from uuid import uuid4

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..auth import admin_required, current_user
from ..cache_utils import INVOICE_DETAIL_KEY, invalidate_invoice_cache, invalidate_products_cache
from ..extensions import cache, db
from ..models import Cart, Invoice, InvoiceItem

invoices_bp = Blueprint("invoices", __name__)


@invoices_bp.post("/from-cart/<int:cart_id>")
@jwt_required()
def create_invoice_from_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    user = current_user()
    if cart.user_id != user.id:
        return jsonify({"error": "You cannot check out this cart"}), 403
    if cart.status != "open":
        return jsonify({"error": "The cart is not open"}), 400
    if not cart.items:
        return jsonify({"error": "The cart is empty"}), 400

    data = request.get_json() or {}
    required = ["billing_address", "payment_method", "payment_reference"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    for item in cart.items:
        if item.quantity > item.product.stock:
            return jsonify({"error": f"Insufficient stock for {item.product.name}"}), 400

    invoice = Invoice(
        invoice_number=f"INV-{uuid4().hex[:10].upper()}",
        user_id=user.id,
        cart_id=cart.id,
        billing_address=data["billing_address"],
        payment_method=data["payment_method"],
        payment_reference=data["payment_reference"],
        total=cart.total(),
    )
    db.session.add(invoice)
    db.session.flush()

    for item in cart.items:
        subtotal = item.product.price * item.quantity
        item.product.stock -= item.quantity
        db.session.add(
            InvoiceItem(
                invoice_id=invoice.id,
                product_id=item.product_id,
                product_name=item.product.name,
                quantity=item.quantity,
                unit_price=item.product.price,
                subtotal=subtotal,
            )
        )
        invalidate_products_cache(item.product_id)

    cart.status = "completed"
    db.session.commit()
    invalidate_invoice_cache(invoice.invoice_number)
    return jsonify(invoice.to_dict()), 201


@invoices_bp.get("")
@jwt_required()
def list_invoices():
    user = current_user()
    query = Invoice.query.order_by(Invoice.id.desc())
    if user.role != "admin":
        query = query.filter_by(user_id=user.id)
    return jsonify([invoice.to_dict() for invoice in query.all()])


@invoices_bp.get("/<invoice_number>")
@jwt_required()
def get_invoice(invoice_number):
    key = INVOICE_DETAIL_KEY.format(invoice_number=invoice_number)
    cached = cache.get(key)
    user = current_user()
    if cached is not None:
        if user.role != "admin" and cached["user_id"] != user.id:
            return jsonify({"error": "You cannot access this invoice"}), 403
        return jsonify(cached)

    invoice = Invoice.query.filter_by(invoice_number=invoice_number).first_or_404()
    if user.role != "admin" and invoice.user_id != user.id:
        return jsonify({"error": "You cannot access this invoice"}), 403
    payload = invoice.to_dict()
    cache.set(key, payload, timeout=600)
    return jsonify(payload)


@invoices_bp.post("/<invoice_number>/refund")
@admin_required
def refund_invoice(invoice_number):
    invoice = Invoice.query.filter_by(invoice_number=invoice_number).first_or_404()
    if invoice.status == "refunded":
        return jsonify({"error": "The invoice has already been refunded"}), 400
    for item in invoice.items:
        item.product.stock += item.quantity
        invalidate_products_cache(item.product_id)
    invoice.status = "refunded"
    db.session.commit()
    invalidate_invoice_cache(invoice.invoice_number)
    return jsonify(invoice.to_dict())
