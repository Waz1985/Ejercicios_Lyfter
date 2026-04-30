"""
Isolated tests for cart operations:
- Adding the same product twice accumulates the quantity into a single item.
- Updating the quantity of an existing item.
- Removing an item from the cart.
- Attempting checkout on an already-completed cart.
"""

from .conftest import auth_header


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _create_product(client, admin_token, sku="PROD-001", stock=10):
    response = client.post(
        "/products",
        headers=auth_header(admin_token),
        json={"name": "Test product", "sku": sku, "price": "10.00", "stock": stock},
    )
    assert response.status_code == 201
    return response.get_json()


def _create_cart(client, token):
    response = client.post("/carts", headers=auth_header(token))
    assert response.status_code == 201
    return response.get_json()


def _add_item(client, token, cart_id, product_id, quantity=1):
    return client.post(
        f"/carts/{cart_id}/items",
        headers=auth_header(token),
        json={"product_id": product_id, "quantity": quantity},
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_adding_same_product_twice_accumulates_quantity(client, admin_token, client_token):
    """Adding the same product twice must sum the quantities into a single cart item."""
    product = _create_product(client, admin_token, stock=10)
    cart = _create_cart(client, client_token)

    _add_item(client, client_token, cart["id"], product["id"], quantity=2)
    response = _add_item(client, client_token, cart["id"], product["id"], quantity=3)

    assert response.status_code == 200
    cart_data = response.get_json()
    assert len(cart_data["items"]) == 1
    assert cart_data["items"][0]["quantity"] == 5


def test_update_item_quantity(client, admin_token, client_token):
    """PUT /carts/<id>/items/<item_id> must update the quantity of the item."""
    product = _create_product(client, admin_token, sku="PROD-002", stock=10)
    cart = _create_cart(client, client_token)
    add_response = _add_item(client, client_token, cart["id"], product["id"], quantity=1)
    item_id = add_response.get_json()["items"][0]["id"]

    update_response = client.put(
        f"/carts/{cart['id']}/items/{item_id}",
        headers=auth_header(client_token),
        json={"quantity": 4},
    )

    assert update_response.status_code == 200
    assert update_response.get_json()["items"][0]["quantity"] == 4


def test_remove_item_from_cart(client, admin_token, client_token):
    """DELETE /carts/<id>/items/<item_id> must remove the item and leave the cart empty."""
    product = _create_product(client, admin_token, sku="PROD-003", stock=10)
    cart = _create_cart(client, client_token)
    add_response = _add_item(client, client_token, cart["id"], product["id"], quantity=2)
    item_id = add_response.get_json()["items"][0]["id"]

    delete_response = client.delete(
        f"/carts/{cart['id']}/items/{item_id}",
        headers=auth_header(client_token),
    )

    assert delete_response.status_code == 200
    assert delete_response.get_json()["items"] == []


def test_checkout_completed_cart_is_rejected(client, admin_token, client_token):
    """Checking out an already-completed cart must return 400."""
    product = _create_product(client, admin_token, sku="PROD-004", stock=10)
    cart = _create_cart(client, client_token)
    _add_item(client, client_token, cart["id"], product["id"], quantity=1)

    checkout_payload = {
        "billing_address": "123 Main St",
        "payment_method": "SINPE",
        "payment_reference": "REF-001",
    }

    # First checkout — must succeed
    first_response = client.post(
        f"/invoices/from-cart/{cart['id']}",
        headers=auth_header(client_token),
        json=checkout_payload,
    )
    assert first_response.status_code == 201

    # Second attempt on the same cart — must fail
    second_response = client.post(
        f"/invoices/from-cart/{cart['id']}",
        headers=auth_header(client_token),
        json=checkout_payload,
    )
    assert second_response.status_code == 400
    assert second_response.get_json()["error"] == "The cart is not open"