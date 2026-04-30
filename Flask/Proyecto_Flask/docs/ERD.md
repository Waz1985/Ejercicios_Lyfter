# Entity-Relationship Diagram

```mermaid
erDiagram
    USERS ||--o{ CARTS : owns
    USERS ||--o{ INVOICES : receives
    CARTS ||--o{ CART_ITEMS : contains
    PRODUCTS ||--o{ CART_ITEMS : appears_in
    CARTS ||--|| INVOICES : becomes
    INVOICES ||--o{ INVOICE_ITEMS : contains
    PRODUCTS ||--o{ INVOICE_ITEMS : sold_as

    USERS {
        int id PK
        string name
        string email UK
        string password_hash
        string role
        bool is_active
        datetime created_at
        datetime updated_at
    }

    PRODUCTS {
        int id PK
        string name
        text description
        string sku UK
        numeric price
        int stock
        bool is_active
        datetime created_at
        datetime updated_at
    }

    CARTS {
        int id PK
        int user_id FK
        string status
        datetime created_at
        datetime updated_at
    }

    CART_ITEMS {
        int id PK
        int cart_id FK
        int product_id FK
        int quantity
        datetime created_at
        datetime updated_at
    }

    INVOICES {
        int id PK
        string invoice_number UK
        int user_id FK
        int cart_id FK
        text billing_address
        string payment_method
        string payment_reference
        string status
        numeric total
        datetime created_at
        datetime updated_at
    }

    INVOICE_ITEMS {
        int id PK
        int invoice_id FK
        int product_id FK
        string product_name
        int quantity
        numeric unit_price
        numeric subtotal
        datetime created_at
        datetime updated_at
    }
```

## Normalization

The database is separated by responsibility:

- `users` stores identity, credentials, and role information.
- `products` stores catalog data and current stock.
- `carts` represents a user's shopping cart, while `cart_items` stores added products without repeating columns.
- `invoices` stores the final sale, while `invoice_items` preserves the historical details of each sold product.

`invoice_items` stores `product_name`, `unit_price`, and `subtotal` even though it also references `products`. This preserves the historical value of a purchase if the product name or price changes after invoicing.

## Business Rules

- Only administrators can create, update, or deactivate users and products.
- Clients can read products and manage their own carts.
- An invoice can only be created from an owned, open cart that contains products.
- During checkout, the API validates stock and then reduces product stock.
- Only administrators can process refunds, and refunds restore product stock.
- User and product deletes are logical deletes through `is_active`, which preserves invoice history.

## Cache and Invalidation

Product read endpoints are cached because they are frequently requested and do not change on every request. They are invalidated when a product is created, updated, or deactivated, and also when a sale or refund changes stock.

Single-invoice reads are cached because invoice content is usually stable. The cache is invalidated when a refund is processed because the invoice status changes.
