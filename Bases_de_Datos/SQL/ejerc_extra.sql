-- 1 -- Crear categorías y ajustar productos
CREATE TABLE
    Categoria (
        idCategoria INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL UNIQUE,
        Descripcion TEXT
    );

ALTER TABLE Productos
ADD COLUMN idCategoria INTEGER
INSERT INTO
    Categoria (Nombre)
VALUES
    ('Periféricos', 'Mouse, Teclado, Monitores'),
    ('Almacenamiento', 'Disco Duro, Tarjetas SD'),
    (
        'Computo',
        'Equipos de Escritorio, Laptops, Gaming'
    ),
    ('Redes', '	Router, Modem, Antenas');

UPDATE Productos
SET
    idCategoria = (
        SELECT
            idCategoria
        FROM
            Categoria
        WHERE
            Nombre = 'Periféricos'
    )
WHERE
    Nombre LIKE '%Mouse%'
    OR Nombre LIKE '%Teclado%'
    OR Nombre LIKE '%Monitor%'
    OR Nombre LIKE '%Webcam%'
    OR Nombre LIKE '%Audífono%'
    OR Nombre LIKE '%Audifono%';

UPDATE Productos
SET
    idCategoria = (
        SELECT
            idCategoria
        FROM
            Categoria
        WHERE
            Nombre = 'Almacenamiento'
    )
WHERE
    Nombre LIKE '%SSD%'
    OR Nombre LIKE '%HDD%'
    OR Nombre LIKE '%Disco%'
    OR Nombre LIKE '%Memoria%';

UPDATE Productos
SET
    idCategoria = (
        SELECT
            idCategoria
        FROM
            Categoria
        WHERE
            Nombre = 'Redes'
    )
WHERE
    Nombre LIKE '%Router%'
    OR Nombre LIKE '%WiFi%'
    OR Nombre LIKE '%Wifi%';

UPDATE Productos
SET
    idCategoria = (
        SELECT
            idCategoria
        FROM
            Categoria
        WHERE
            Nombre = 'Computo'
    )
WHERE
    Nombre LIKE '%Laptop%'
    OR Nombre LIKE '%Computadora%';

SELECT * FROM Productos

-- 2 -- Carga de productos y filtros básicos

INSERT INTO Productos (Codigo, Nombre, Precio, FechaIngreso, Marca, idCategoria) VALUES
('P001','Mouse inalámbrico', 15000, '2026-01-05 10:15:00','Logitech', 1),
('P002','Teclado mecánico', 65000, '2026-01-06 11:20:00','Keychron', 1),
('P003','Monitor 24"', 120000, '2026-01-07 09:00:00','Samsung', 1),
('P004','Audífonos BT', 48000, '2026-01-08 14:10:00','Sony', 1),
('P005','Disco SSD 1TB', 90000, '2026-01-10 16:30:00','Kingston', 2),
('P006','Laptop 14"', 450000, '2026-01-12 08:45:00','Lenovo', 3),
('P007','Webcam 1080p', 52000, '2026-01-15 13:05:00','Logitech', 1),
('P008','Router WiFi 6', 75000, '2026-01-18 18:25:00','TP-Link', 4),
('P009','Mouse Gaming', 18000, '2026-01-12 10:15:00','Havit', 1),
('P010','Teclado Gaming', 75000, '2026-01-15 11:20:00','Havit', 1)

SELECT * FROM Productos

SELECT * FROM productos WHERE Precio > 50000

SELECT * FROM Productos WHERE Nombre LIKE '%apple%'

SELECT * FROM Productos ORDER BY Precio DESC LIMIT 5

-- 3 -- Campos nuevos en facturas y actualización

ALTER TABLE Facturas
    ADD telefono_cliente TEXT DEFAULT 'N/A'

ALTER TABLE Facturas
    ADD CodigoCajero TEXT DEFAULT 'N/A'

UPDATE Facturas
SET
    telefono_cliente = '+506 8585-5858',
    CodigoCajero = 'Caj0101'
WHERE
    CorreoComprador = 'ana@gmail.com';

UPDATE Facturas
SET
    telefono_cliente = '+506 9595-5959',
    CodigoCajero = 'Caj0102'
WHERE
    CorreoComprador = 'carlos@gmail.com';

UPDATE Facturas
SET
    telefono_cliente = '+506 5959-9595',
    CodigoCajero = 'Caj0103'
WHERE
    CorreoComprador = 'maria@gmail.com';

UPDATE Facturas
SET
    telefono_cliente = '+506 5858-8585',
    CodigoCajero = 'Caj0104'
WHERE
    CorreoComprador = 'sofia@gmail.com';

SELECT * FROM Facturas WHERE telefono_cliente = 'N/A'

SELECT * FROM Facturas WHERE idFactura = 1

-- 4 -- Correcciones de datos en productos

ALTER TABLE Productos
    ADD Cantidad INTEGER DEFAULT 0

UPDATE Productos
SET
    Cantidad = 0
WHERE
    Precio <= 0;

UPDATE Productos
SET
    Precio = Precio + 100
WHERE
    Cantidad < 10;

UPDATE Productos
SET
    Cantidad = Cantidad - 1
WHERE
    idProducto = 3;

SELECT * FROM Productos
ORDER BY idProducto ASC LIMIT 10