from .conftest import auth_header


def _create_product(client, token, stock=5):
    response = client.post(
        "/products",
        headers=auth_header(token),
        json={"name": "Collar", "sku": "COLLAR-1", "price": "7.50", "stock": stock},
    )
    return response.get_json()


def test_checkout_creates_invoice_and_reduces_stock(client, admin_token, client_token):
    product = _create_product(client, admin_token, stock=5)
    cart = client.post("/carts", headers=auth_header(client_token)).get_json()
    client.post(
        f"/carts/{cart['id']}/items",
        headers=auth_header(client_token),
        json={"product_id": product["id"], "quantity": 2},
    )

    invoice_response = client.post(
        f"/invoices/from-cart/{cart['id']}",
        headers=auth_header(client_token),
        json={
            "billing_address": "San Jose",
            "payment_method": "SINPE",
            "payment_reference": "ABC123",
        },
    )
    invoice = invoice_response.get_json()

    assert invoice_response.status_code == 201
    assert invoice["total"] == 15.0
    assert invoice["items"][0]["quantity"] == 2

    product_response = client.get(f"/products/{product['id']}", headers=auth_header(client_token))
    assert product_response.get_json()["stock"] == 3


def test_refund_restores_stock_and_marks_invoice(client, admin_token, client_token):
    product = _create_product(client, admin_token, stock=4)
    cart = client.post("/carts", headers=auth_header(client_token)).get_json()
    client.post(
        f"/carts/{cart['id']}/items",
        headers=auth_header(client_token),
        json={"product_id": product["id"], "quantity": 3},
    )
    invoice = client.post(
        f"/invoices/from-cart/{cart['id']}",
        headers=auth_header(client_token),
        json={
            "billing_address": "Heredia",
            "payment_method": "SINPE",
            "payment_reference": "XYZ789",
        },
    ).get_json()

    refund_response = client.post(
        f"/invoices/{invoice['invoice_number']}/refund",
        headers=auth_header(admin_token),
    )

    assert refund_response.status_code == 200
    assert refund_response.get_json()["status"] == "refunded"
    product_response = client.get(f"/products/{product['id']}", headers=auth_header(client_token))
    assert product_response.get_json()["stock"] == 4


def test_checkout_rejects_empty_cart(client, client_token):
    cart = client.post("/carts", headers=auth_header(client_token)).get_json()

    response = client.post(
        f"/invoices/from-cart/{cart['id']}",
        headers=auth_header(client_token),
        json={
            "billing_address": "Alajuela",
            "payment_method": "SINPE",
            "payment_reference": "EMPTY",
        },
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "The cart is empty"
