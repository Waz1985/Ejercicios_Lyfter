from .extensions import cache

PRODUCT_LIST_KEY = "products:list"
PRODUCT_DETAIL_KEY = "products:detail:{product_id}"
INVOICE_DETAIL_KEY = "invoices:detail:{invoice_number}"


def invalidate_products_cache(product_id=None):
    cache.delete(PRODUCT_LIST_KEY)
    if product_id is not None:
        cache.delete(PRODUCT_DETAIL_KEY.format(product_id=product_id))


def invalidate_invoice_cache(invoice_number=None):
    if invoice_number is not None:
        cache.delete(INVOICE_DETAIL_KEY.format(invoice_number=invoice_number))
