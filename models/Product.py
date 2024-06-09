class ItemData:
    def __init__(self, name_Global=None, price=None, rating=None, description_Global=None, images=None):
        self.name_Global = name_Global
        self.price = price
        self.rating = rating
        self.description_Global = description_Global
        self.images = images

    def to_dict(self):
        return {
            "name_Global": self.name_Global,
            "price": self.price,
            "rating": self.rating,
            "description_Global": self.description_Global,
            "images": self.images
                            }
from datetime import datetime
from typing import List


class ProductDetailDTO:
    prod_id: int
    domain_id: int
    product_link1: str
    status: str
    last_updated: datetime
    last_scraped: datetime
    id: int
    name_local: str
    name_global: str
    description_local: str
    description_global: str
    price: float
    rating: float
    is_available: bool
    brand: str
    images: List[str]

    def __init__(self, prod_id: int = None, domain_id: int = None, product_link1: str = None, status: str = None, last_updated: datetime = None, last_scraped: datetime = None, id: int = None, name_local: str = None, name_global: str = None, description_local: str = None, description_global: str = None, price: float = None, rating: float = None, is_available: bool = None, brand: str = None, images: List[str] = None):
        self.prod_id = prod_id
        self.domain_id = domain_id
        self.product_link1 = product_link1
        self.status = status
        self.last_updated = last_updated
        self.last_scraped = last_scraped
        self.id = id
        self.name_local = name_local
        self.name_global = name_global
        self.description_local = description_local
        self.description_global = description_global
        self.price = price
        self.rating = rating
        self.is_available = is_available
        self.brand = brand
        self.images = images


class ItemPrice:
    def __init__(self, price=None):
        self.price = price

    def to_dict(self):
        return {
            "price": self.price
        }
class ItemImages:
    def __init__(self, images=None):
        self.images = images

    def to_dict(self):
        return {
            "images": self.images
        }
#https://www.jarir.com/sa-en/default-category/msi-clae-a1m-gaming-consoles-and-handheld-631416.html
