from .conftest import auth_header


def test_admin_can_create_and_update_product(client, admin_token):
    create_response = client.post(
        "/products",
        headers=auth_header(admin_token),
        json={"name": "Dog food", "sku": "DOG-FOOD", "price": "25.99", "stock": 10},
    )
    product = create_response.get_json()

    assert create_response.status_code == 201
    assert product["stock"] == 10

    update_response = client.put(
        f"/products/{product['id']}",
        headers=auth_header(admin_token),
        json={"stock": 15},
    )

    assert update_response.status_code == 200
    assert update_response.get_json()["stock"] == 15


def test_product_validation_rejects_negative_stock(client, admin_token):
    response = client.post(
        "/products",
        headers=auth_header(admin_token),
        json={"name": "Toy", "sku": "TOY-1", "price": "3.00", "stock": -1},
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Price and stock cannot be negative"
