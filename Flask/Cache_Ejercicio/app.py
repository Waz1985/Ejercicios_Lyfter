from decimal import Decimal
from datetime import datetime

from flask import Flask, request, jsonify, g
from cache import (
    get_cache,
    set_cache,
    delete_cache,
    product_cache_key,
    products_list_cache_key
)

from db import SessionLocal
from jwt_manager import JWTManager
from decorators import require_auth, require_role

from models.user import User
from models.product import Product
from models.invoice import Invoice
from models.invoice_item import InvoiceItem

app = Flask("fruit-store-api")
jwt_manager = JWTManager()

@app.route("/", methods=["GET"])
def root():
    return "<h1>Hello to Fruit Store</h1>", 200

@app.route("/liveness", methods=["GET"])
def liveness():
    return "<p>Fruit Store API is running</p>", 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "USER")

    if not username or not password:
        return jsonify({"error": "Fields 'username' and 'password' are required"}), 400

    if role not in ["ADMIN", "USER"]:
        return jsonify({"error": "Invalid role"}), 400

    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.username == username).first()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 409

        user = User(username=username, password=password, role=role)
        session.add(user)
        session.commit()
        session.refresh(user)

        token = jwt_manager.encode({
            "id": user.id,
            "role": user.role
        })

        if not token:
            return jsonify({"error": "Token generation failed"}), 500

        return jsonify({
            "message": "User registered successfully",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        }), 201

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Fields 'username' and 'password' are required"}), 400

    session = SessionLocal()
    try:
        user = session.query(User).filter(
            User.username == username,
            User.password == password
        ).first()

        if not user:
            return jsonify({"error": "Invalid credentials"}), 401

        token = jwt_manager.encode({
            "id": user.id,
            "role": user.role
        })

        if not token:
            return jsonify({"error": "Token generation failed"}), 500

        return jsonify({"token": token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/me", methods=["GET"])
@require_auth
def me():
    current_user = g.current_user
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "role": current_user.role
    }), 200


# -------------------------
# PRODUCT CRUD - ADMIN ONLY
# -------------------------

@app.route("/products", methods=["POST"])
@require_auth
@require_role("ADMIN")
def create_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    name = data.get("name")
    price = data.get("price")
    entry_date = data.get("entry_date")
    quantity = data.get("quantity")

    if name is None or price is None or entry_date is None or quantity is None:
        return jsonify({"error": "Fields 'name', 'price', 'entry_date', and 'quantity' are required"}), 400

    try:
        parsed_date = datetime.strptime(entry_date, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "entry_date must be in YYYY-MM-DD format"}), 400

    session = SessionLocal()
    try:
        existing_product = session.query(Product).filter(Product.name == name).first()
        if existing_product:
            return jsonify({"error": "Product name already exists"}), 409

        product = Product(
            name=name,
            price=Decimal(str(price)),
            entry_date=parsed_date,
            quantity=int(quantity)
        )

        session.add(product)
        session.commit()
        session.refresh(product)

        try:
            delete_cache(products_list_cache_key())
        except Exception:
            pass

        return jsonify({
            "message": "Product created successfully",
            "data": {
                "id": product.id,
                "name": product.name,
                "price": str(product.price),
                "entry_date": str(product.entry_date),
                "quantity": product.quantity
            }
        }), 201

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/products", methods=["GET"])
@require_auth
@require_role("ADMIN")
def get_products():
    list_key = products_list_cache_key()

    try:
        cached_products = get_cache(list_key)
        print("GET CACHE products:all ->", cached_products)

        if cached_products is not None:
            print("RETURNING /products FROM CACHE")
            return jsonify({
                "source": "cache",
                "data": cached_products
            }), 200
    except Exception as e:
        print("GET CACHE ERROR /products:", e)

    session = SessionLocal()
    try:
        products = session.query(Product).all()

        response_data = [
            {
                "id": product.id,
                "name": product.name,
                "price": str(product.price),
                "entry_date": str(product.entry_date),
                "quantity": product.quantity
            }
            for product in products
        ]

        try:
            set_cache(list_key, response_data)
            print("SET CACHE products:all OK")
        except Exception as e:
            print("SET CACHE ERROR /products:", e)

        return jsonify({
            "source": "database",
            "data": response_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/products/<int:product_id>", methods=["GET"])
@require_auth
@require_role("ADMIN")
def get_product_by_id(product_id):
    cache_key = product_cache_key(product_id)

    try:
        cached_product = get_cache(cache_key)
        print(f"GET CACHE {cache_key} ->", cached_product)

        if cached_product is not None:
            print(f"RETURNING /products/{product_id} FROM CACHE")
            return jsonify({
                "source": "cache",
                "data": cached_product
            }), 200
    except Exception as e:
        print(f"GET CACHE ERROR /products/{product_id}:", e)

    session = SessionLocal()
    try:
        product = session.get(Product, product_id)

        if not product:
            return jsonify({"error": "Product not found"}), 404

        response_data = {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "entry_date": str(product.entry_date),
            "quantity": product.quantity
        }

        try:
            set_cache(cache_key, response_data)
            print(f"SET CACHE {cache_key} OK")
        except Exception as e:
            print(f"SET CACHE ERROR /products/{product_id}:", e)

        return jsonify({
            "source": "database",
            "data": response_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/products/<int:product_id>", methods=["PATCH"])
@require_auth
@require_role("ADMIN")
def update_product(product_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    session = SessionLocal()
    try:
        product = session.get(Product, product_id)

        if not product:
            return jsonify({"error": "Product not found"}), 404

        if "name" in data:
            product.name = data["name"]

        if "price" in data:
            product.price = Decimal(str(data["price"]))

        if "entry_date" in data:
            try:
                product.entry_date = datetime.strptime(data["entry_date"], "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"error": "entry_date must be in YYYY-MM-DD format"}), 400

        if "quantity" in data:
            product.quantity = int(data["quantity"])

        session.commit()
        session.refresh(product)

        try:
            delete_cache(product_cache_key(product_id))
            delete_cache(products_list_cache_key())
        except Exception:
            pass

        return jsonify({
            "message": "Product updated successfully",
            "data": {
                "id": product.id,
                "name": product.name,
                "price": str(product.price),
                "entry_date": str(product.entry_date),
                "quantity": product.quantity
            }
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/products/<int:product_id>", methods=["DELETE"])
@require_auth
@require_role("ADMIN")
def delete_product(product_id):
    session = SessionLocal()
    try:
        product = session.get(Product, product_id)

        if not product:
            return jsonify({"error": "Product not found"}), 404

        session.delete(product)
        session.commit()

        try:
            delete_cache(product_cache_key(product_id))
            delete_cache(products_list_cache_key())
        except Exception:
            pass

        return jsonify({"message": "Product deleted successfully"}), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# -------------------------
# PURCHASE - USER AND ADMIN
# -------------------------

@app.route("/purchase", methods=["POST"])
@require_auth
@require_role("ADMIN", "USER")
def purchase_products():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    items = data.get("items")

    if not items or not isinstance(items, list):
        return jsonify({"error": "Field 'items' is required and must be a list"}), 400

    session = SessionLocal()
    try:
        invoice = Invoice(user_id=g.current_user.id, total=Decimal("0.00"))
        session.add(invoice)
        session.flush()

        total = Decimal("0.00")

        for item in items:
            product_id = item.get("product_id")
            quantity = item.get("quantity")

            if not product_id or not quantity:
                session.rollback()
                return jsonify({"error": "Each item must include 'product_id' and 'quantity'"}), 400

            product = session.get(Product, product_id)

            if not product:
                session.rollback()
                return jsonify({"error": f"Product with id {product_id} not found"}), 404

            if product.quantity < quantity:
                session.rollback()
                return jsonify({"error": f"Insufficient stock for product '{product.name}'"}), 409

            unit_price = Decimal(str(product.price))
            subtotal = unit_price * quantity

            product.quantity -= quantity

            invoice_item = InvoiceItem(
                invoice_id=invoice.id,
                product_id=product.id,
                quantity=quantity,
                unit_price=unit_price,
                subtotal=subtotal
            )
            session.add(invoice_item)

            total += subtotal

        invoice.total = total

        session.commit()
        session.refresh(invoice)

        return jsonify({
            "message": "Purchase completed successfully",
            "invoice": {
                "id": invoice.id,
                "user_id": invoice.user_id,
                "created_at": invoice.created_at.isoformat(),
                "total": str(invoice.total)
            }
        }), 201

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


# -------------------------
# INVOICES
# -------------------------

@app.route("/invoices/my", methods=["GET"])
@require_auth
@require_role("ADMIN", "USER")
def get_my_invoices():
    session = SessionLocal()
    try:
        invoices = session.query(Invoice).filter(Invoice.user_id == g.current_user.id).all()

        result = []
        for invoice in invoices:
            result.append({
                "id": invoice.id,
                "user_id": invoice.user_id,
                "created_at": invoice.created_at.isoformat(),
                "total": str(invoice.total),
                "items": [
                    {
                        "id": item.id,
                        "product_id": item.product_id,
                        "product_name": item.product.name,
                        "quantity": item.quantity,
                        "unit_price": str(item.unit_price),
                        "subtotal": str(item.subtotal)
                    }
                    for item in invoice.items
                ]
            })

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route("/invoices", methods=["GET"])
@require_auth
@require_role("ADMIN")
def get_all_invoices():
    session = SessionLocal()
    try:
        invoices = session.query(Invoice).all()

        result = []
        for invoice in invoices:
            result.append({
                "id": invoice.id,
                "user_id": invoice.user_id,
                "username": invoice.user.username,
                "created_at": invoice.created_at.isoformat(),
                "total": str(invoice.total),
                "items": [
                    {
                        "id": item.id,
                        "product_id": item.product_id,
                        "product_name": item.product.name,
                        "quantity": item.quantity,
                        "unit_price": str(item.unit_price),
                        "subtotal": str(item.subtotal)
                    }
                    for item in invoice.items
                ]
            })

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)