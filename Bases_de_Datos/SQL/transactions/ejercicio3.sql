/*
Construya una transacción para procesar la devolución de un producto. La transacción debe seguir este flujo:
Verificar que la factura existe en la base de datos.
Aumentar el stock del producto en la cantidad que se registró en la compra.
Modificar la factura original para marcarla con el estado de "Retornada".
*/

PRAGMA foreign_keys = ON;

BEGIN;


UPDATE Products
SET stock = stock + (
    SELECT ii.quantity
    FROM InvoiceItems ii
    WHERE ii.idProduct = Products.idProduct
    AND ii.idInvoice = 5
)
WHERE EXISTS (SELECT 1 FROM Invoices WHERE idInvoice = 5)
    AND idProduct IN (SELECT idProduct FROM InvoiceItems WHERE idInvoice = 5);


UPDATE Invoices
SET status = 'Retornada'
WHERE idInvoice = 5
    AND status <> 'Retornada';

COMMIT;
