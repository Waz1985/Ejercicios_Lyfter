-- Creation

CREATE TABLE
    Productos (
        idProducto INTEGER PRIMARY KEY AUTOINCREMENT,
        Codigo TEXT NOT NULL UNIQUE,
        Nombre TEXT,
        Precio NUMERIC(10, 2),
        FechaIngreso TEXT,
        Marca TEXT
    );

CREATE TABLE
    Facturas (
        idFactura INTEGER PRIMARY KEY AUTOINCREMENT,
        NumeroFactura INTEGER NOT NULL,
        FechaCompra TEXT,
        CorreoComprador TEXT,
        MontoTotal NUMERIC(10, 2)
    );

CREATE TABLE IF NOT EXISTS
    Producto_Factura (
        idProducto INTEGER NOT NULL,
        idFactura INTEGER NOT NULL,
        Cantidad INTEGER NOT NULL,
        MontoTotalLinea NUMERIC(10, 2),
        PrecioUnitario NUMERIC(10, 2),
        PRIMARY KEY (idProducto, idFactura),
        FOREIGN KEY (idProducto) REFERENCES Productos (idProducto) ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (idFactura) REFERENCES Facturas (idFactura) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

CREATE TABLE IF NOT EXISTS
    Producto_Carrito (
        idProducto INTEGER NOT NULL,
        idCarrito INTEGER NOT NULL,
        Cantidad INTEGER NOT NULL,
        PRIMARY KEY (idProducto, idCarrito),
        FOREIGN KEY (idProducto) REFERENCES Productos (idProducto) ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (idCarrito) REFERENCES Carrito (idCarrito) ON DELETE NO ACTION ON UPDATE NO ACTION
    );

PRAGMA foreign_keys = ON;

CREATE INDEX IF NOT EXISTS idx_pf_idFactura ON Producto_Factura (idFactura);

CREATE INDEX IF NOT EXISTS idx_pf_idProducto ON Producto_Factura (idProducto);

-- Modification

ALTER TABLE Facturas
    ADD telefono_cliente INTEGER DEFAULT 0

ALTER TABLE Facturas
    ADD codigo_empleado INTEGER DEFAULT 0

-- Queries

-- 1
SELECT * FROM productos
-- 2
SELECT * FROM productos WHERE Precio > 50000
-- 3 
SELECT pf.*,f.NumeroFactura, f.FechaCompra, f.CorreoComprador
FROM Producto_Factura pf
JOIN Facturas f ON f.idFactura = pf.idFactura
WHERE pf.idProducto = 2
ORDER BY f.FechaCompra
-- 4
SELECT 
    p.idProducto, p.Codigo, p.Nombre, SUM(pf.Cantidad) AS TotalUnidadesCompradas, 
    SUM(pf.MontoTotalLinea) AS TotalMontoComprado
FROM Producto_Factura pf
JOIN Productos p ON p.idProducto = pf.idProducto
GROUP BY p.idProducto, p.Codigo, p.Nombre
ORDER BY TotalMontoComprado DESC;
-- 5
SELECT * FROM Facturas
WHERE  correoComprador = 'ana@gmail.com'
ORDER BY FechaCompra
-- 6
SELECT * FROM Facturas
WHERE NumeroFactura = 1005

ALTER TABLE Facturas
RENAME COLUMN telefono_cliente TO TelefonoCliente;