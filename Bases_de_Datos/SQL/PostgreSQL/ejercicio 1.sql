
DROP TABLE IF EXISTS "InvoiceItems";
DROP TABLE IF EXISTS "Invoices";
DROP TABLE IF EXISTS "Products";
DROP TABLE IF EXISTS "Users";

CREATE TABLE "Users" (
  "idUser"   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  "userName" TEXT NOT NULL,
  "email"    TEXT NOT NULL UNIQUE
);

CREATE TABLE "Products" (
  "idProduct"   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  "productName" TEXT NOT NULL,
  "price"       NUMERIC(10,2) NOT NULL,
  "stock"       INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE "Invoices" (
  "idInvoice"   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  "idUser"      INTEGER NOT NULL,
  "invoiceDate" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "total"       NUMERIC(10,2) NOT NULL DEFAULT 0,
  "status"      TEXT NOT NULL DEFAULT 'Activa',
  CONSTRAINT fk_invoices_user
    FOREIGN KEY ("idUser") REFERENCES "Users"("idUser")
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE "InvoiceItems" (
  "idInvoice" INTEGER NOT NULL,
  "idProduct" INTEGER NOT NULL,
  "quantity"  INTEGER NOT NULL DEFAULT 1,
  "unitPrice" NUMERIC(10,2) NOT NULL,
  "lineTotal" NUMERIC(10,2) NOT NULL,
  PRIMARY KEY ("idInvoice", "idProduct"),
  CONSTRAINT fk_items_invoice
    FOREIGN KEY ("idInvoice") REFERENCES "Invoices"("idInvoice")
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT fk_items_product
    FOREIGN KEY ("idProduct") REFERENCES "Products"("idProduct")
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS idx_invoices_user
ON "Invoices"("idUser");

CREATE INDEX IF NOT EXISTS idx_items_product
ON "InvoiceItems"("idProduct");


INSERT INTO "Users" ("userName", "email") VALUES
('Juan Pérez', 'juan.perez@email.com'),
('María González', 'maria.gonzalez@email.com'),
('Carlos Ramírez', 'carlos.ramirez@email.com'),
('Ana López', 'ana.lopez@email.com'),
('Luis Fernández', 'luis.fernandez@email.com'),
('Sofía Herrera', 'sofia.herrera@email.com'),
('Daniel Morales', 'daniel.morales@email.com'),
('Valeria Castro', 'valeria.castro@email.com');

INSERT INTO "Products" ("productName", "price", "stock") VALUES
('Laptop Lenovo IdeaPad 5', 550000.00, 10),
('Mouse Logitech M185', 8500.00, 50),
('Teclado Mecánico Redragon', 42000.00, 25),
('Monitor Samsung 24"', 125000.00, 15),
('Disco SSD Kingston 1TB', 68000.00, 30),
('Audífonos Sony WH-CH520', 45000.00, 20),
('Router TP-Link AX1500', 72000.00, 18),
('Webcam Logitech C920', 52000.00, 12),
('Impresora HP DeskJet 2775', 49000.00, 8),
('Tablet Samsung Galaxy Tab A8', 210000.00, 14);