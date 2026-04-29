import pytest

from app import create_app
from app.config import TestingConfig
from app.extensions import db


@pytest.fixture()
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


def register(client, name, email, password="secret123"):
    return client.post(
        "/auth/register",
        json={"name": name, "email": email, "password": password},
    )


def login(client, email, password="secret123"):
    response = client.post("/auth/login", json={"email": email, "password": password})
    return response.get_json()["access_token"]


def auth_header(token):
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture()
def admin_token(client):
    register(client, "Admin", "admin@example.com")
    return login(client, "admin@example.com")


@pytest.fixture()
def client_token(client, admin_token):
    register(client, "Client", "client@example.com")
    return login(client, "client@example.com")
