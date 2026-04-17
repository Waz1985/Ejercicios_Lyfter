from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship
from db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Numeric(10, 2), nullable=False)
    entry_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)

    invoice_items = relationship("InvoiceItem", back_populates="product")