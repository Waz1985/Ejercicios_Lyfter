DO $$
DECLARE
  v_invoice_id INT := 1;  -- <- factura a retornar
BEGIN
  BEGIN
    -- 1) Verificar factura existe
    IF NOT EXISTS (SELECT 1 FROM "Invoices" WHERE "idInvoice" = v_invoice_id) THEN
      RAISE EXCEPTION 'Factura % no existe', v_invoice_id;
    END IF;

   -- Evitar doble retorno
    IF EXISTS (
      SELECT 1 FROM "Invoices"
      WHERE "idInvoice" = v_invoice_id AND "status" = 'Retornada'
    ) THEN
      RAISE EXCEPTION 'Factura % ya fue retornada', v_invoice_id;
    END IF;

    -- 2) Aumentar stock según cantidades de la compra
    UPDATE "Products" p
    SET "stock" = p."stock" + ii."quantity"
    FROM "InvoiceItems" ii
    WHERE ii."idInvoice" = v_invoice_id
      AND ii."idProduct" = p."idProduct";

    -- 3) Marcar factura como retornada
    UPDATE "Invoices"
    SET "status" = 'Retornada'
    WHERE "idInvoice" = v_invoice_id;

    RAISE NOTICE 'Retorno exitoso. Factura % marcada como Retornada', v_invoice_id;

  EXCEPTION
    WHEN OTHERS THEN
      RAISE;
  END;
END $$;

