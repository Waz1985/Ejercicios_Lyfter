from .conftest import auth_header, register


def test_first_registered_user_is_admin(client):
    response = register(client, "Admin", "admin@example.com")

    assert response.status_code == 201
    assert response.get_json()["user"]["role"] == "admin"


def test_client_cannot_create_product(client, client_token):
    response = client.post(
        "/products",
        headers=auth_header(client_token),
        json={"name": "Arena", "sku": "ARENA-01", "price": "12.50", "stock": 5},
    )

    assert response.status_code == 403
    assert response.get_json()["error"] == "You do not have permission to perform this action"


def test_login_rejects_invalid_password(client):
    register(client, "Admin", "admin@example.com")

    response = client.post("/auth/login", json={"email": "admin@example.com", "password": "bad"})

    assert response.status_code == 401
    assert response.get_json()["error"] == "Invalid credentials"
