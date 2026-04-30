# PetShop API - Flask, PostgreSQL, Redis

Backend API for managing users, products, carts, sales, invoices, refunds, stock, and cache for a pet product e-commerce store.

## Stack

- Flask
- Flask-SQLAlchemy as the ORM
- PostgreSQL as the main database
- Redis for cache
- Flask-JWT-Extended for token authentication
- pytest for unit testing

## Initial Setup

1. Create the `.env` file from `.env.example`.
2. Start PostgreSQL and Redis:

```powershell
docker compose up -d
```

3. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

4. Initialize the tables through the ORM:

```powershell
flask --app run.py init-db
```

5. Run the server:

```powershell
flask --app run.py run
```

The API is available at `http://127.0.0.1:5000`.

## Database Ports

This project maps PostgreSQL to `localhost:5433` because the computer already has a local PostgreSQL service using `5432`.

Default connection:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5433/petshop
```

## Administrator User

The first user registered through `/auth/register` is created with the `admin` role. All following users are created with the `client` role. An administrator can create other admin users through `POST /users`.

## Main Endpoints

### Auth

- `POST /auth/register`: register a user.
- `POST /auth/login`: return an `access_token`.

### Users

- `GET /users/me`: get the authenticated user.
- `GET /users`: list users, admin only.
- `GET /users/<id>`: get a user, admin only.
- `POST /users`: create a user, admin only.
- `PUT /users/<id>`: update a user, admin only.
- `DELETE /users/<id>`: deactivate a user, admin only.

### Products

- `GET /products`: list active products.
- `GET /products/<id>`: get a product.
- `POST /products`: create a product, admin only.
- `PUT /products/<id>`: update a product, admin only.
- `DELETE /products/<id>`: deactivate a product, admin only.

### Carts

- `POST /carts`: create an open cart.
- `GET /carts`: list the authenticated user's carts.
- `GET /carts/<id>`: get one owned cart.
- `POST /carts/<id>/items`: add a product.
- `PUT /carts/<id>/items/<item_id>`: update quantity.
- `DELETE /carts/<id>/items/<item_id>`: remove a product.

### Invoices and Sales

- `POST /invoices/from-cart/<cart_id>`: convert a cart into a sale.
- `GET /invoices`: list owned invoices; admins can see all invoices.
- `GET /invoices/<invoice_number>`: get an invoice.
- `POST /invoices/<invoice_number>/refund`: refund an invoice and restore stock, admin only.

Use the token like this:

```http
Authorization: Bearer <access_token>
```

## Cache

The project uses Redis in normal execution and `SimpleCache` during tests.

- `GET /products`: cached for 120 seconds. Invalidated when products are created, updated, deleted, sold, or refunded.
- `GET /products/<id>`: cached for 300 seconds. Invalidated when that product or its stock changes.
- `GET /invoices/<invoice_number>`: cached for 600 seconds. Invalidated when a refund is processed.

The TTL values are short because stock and sales data can change frequently.

## Tests

Run:

```powershell
.\scripts\run_tests.ps1
```

Or directly:

```powershell
pytest
```

The tests cover registration/login, permissions, product validation, invoice creation, stock reduction, refunds, and expected error scenarios.

## Documentation

The Entity-Relationship diagram and normalization notes are in [docs/ERD.md](docs/ERD.md).
