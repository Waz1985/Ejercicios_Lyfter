DO $$
DECLARE
  v_user_id    INT := 1;  
  v_product_id INT := 2;  
  v_qty        INT := 3;  

  v_stock      INT;
  v_price      NUMERIC(10,2);
  v_invoice_id INT;
BEGIN
  BEGIN
    -- 1) Validar usuario existe
    IF NOT EXISTS (SELECT 1 FROM "Users" WHERE "idUser" = v_user_id) THEN
      RAISE EXCEPTION 'Usuario % no existe', v_user_id;
    END IF;

    -- 2) Validar producto existe y traer stock + precio
    SELECT "stock", "price"
    INTO v_stock, v_price
    FROM "Products"
    WHERE "idProduct" = v_product_id
    FOR UPDATE;

    IF NOT FOUND THEN
      RAISE EXCEPTION 'Producto % no existe', v_product_id;
    END IF;

    -- 3) Validar stock suficiente
    IF v_stock < v_qty THEN
      RAISE EXCEPTION 'Stock insuficiente. Producto %, Stock %, Solicitud %',
        v_product_id, v_stock, v_qty;
    END IF;

    -- 4) Insertar factura
    INSERT INTO "Invoices" ("idUser", "total", "status")
    VALUES (v_user_id, 0, 'Activa')
    RETURNING "idInvoice" INTO v_invoice_id;

    -- 5) Insertar detalle (una línea)
    INSERT INTO "InvoiceItems" ("idInvoice", "idProduct", "quantity", "unitPrice", "lineTotal")
    VALUES (v_invoice_id, v_product_id, v_qty, v_price, v_price * v_qty);

    -- 6) Reducir stock
    UPDATE "Products"
    SET "stock" = "stock" - v_qty
    WHERE "idProduct" = v_product_id;

    -- 7) Actualizar total de la factura
    UPDATE "Invoices"
    SET "total" = (
      SELECT COALESCE(SUM("lineTotal"), 0)
      FROM "InvoiceItems"
      WHERE "idInvoice" = v_invoice_id
    )
    WHERE "idInvoice" = v_invoice_id;

    RAISE NOTICE 'Compra exitosa. Factura creada: %', v_invoice_id;

  EXCEPTION
    WHEN OTHERS THEN
      RAISE;
  END;
END $$;
