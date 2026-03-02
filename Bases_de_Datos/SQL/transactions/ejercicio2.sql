/*
Construya una transacción para el proceso de compra de un producto. El bloque 
debe realizar las siguientes validaciones y acciones:
Comprobar si hay existencias suficientes del producto.
Confirmar que el usuario que realiza la compra existe en la DB.
Insertar la factura con el usuario relacionado.
Reducir el stock del producto según la cantidad comprada.
*/

PRAGMA foreign_keys = ON;

BEGIN;


INSERT INTO Invoices (idUser, total)
SELECT idUser, 0
FROM Users
WHERE idUser = 1;


INSERT INTO InvoiceItems (idInvoice, idProduct, quantity, unitPrice, lineTotal)
SELECT 
    last_insert_rowid(),
    p.idProduct,
    3,
    p.price,
    p.price * 3
FROM Products p
WHERE p.idProduct = 2
    AND p.stock >= 3;


UPDATE Products
SET stock = stock - 3
WHERE idProduct = 2
    AND stock >= 3;

COMMIT;


