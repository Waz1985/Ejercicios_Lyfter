PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Customer (
  idCustomer     INTEGER PRIMARY KEY AUTOINCREMENT,
  Name           TEXT NOT NULL,
  CustomerPhone  TEXT DEFAULT '+506 0000-0000'
);

CREATE TABLE IF NOT EXISTS "Order" (
  idOrder              INTEGER PRIMARY KEY AUTOINCREMENT,
  SpecialRequest       TEXT,
  DeliveryTime         TEXT NOT NULL,
  Address              TEXT DEFAULT 'Alajuela',
  Customer_idCustomer  INTEGER NOT NULL,
  FOREIGN KEY (Customer_idCustomer) REFERENCES Customer(idCustomer)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS idx_order_customer
ON "Order" (Customer_idCustomer);

CREATE TABLE IF NOT EXISTS Item (
  idItem     INTEGER PRIMARY KEY AUTOINCREMENT,
  Cantidad   INTEGER NOT NULL DEFAULT 1,
  ItemName   TEXT NOT NULL,
  Price      NUMERIC
);

CREATE TABLE IF NOT EXISTS ItemOrder (
  IdItemOrder   INTEGER PRIMARY KEY AUTOINCREMENT,
  Item_idItem   INTEGER NOT NULL,
  Order_idOrder INTEGER NOT NULL,
  FOREIGN KEY (Item_idItem) REFERENCES Item(idItem)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (Order_idOrder) REFERENCES "Order"(idOrder)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS idx_itemorder_order
ON ItemOrder (Order_idOrder);

CREATE INDEX IF NOT EXISTS idx_itemorder_item
ON ItemOrder (Item_idItem);

CREATE UNIQUE INDEX IF NOT EXISTS uq_itemorder_item_order
ON ItemOrder (Item_idItem, Order_idOrder);
