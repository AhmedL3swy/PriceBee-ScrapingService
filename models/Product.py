import time
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
    def __init__(self, prod_id: int = 0, domainId: int = 1, productlink1: str = "", status: str = "", 
                 lastUpdated: datetime = datetime.utcnow(), lastScraped: datetime = datetime.utcnow(), id: int = 0, 
                 name_Local: str = "", name_Global: str = "", description_Local: str = "", description_Global: str = "", 
                 price: float = 0.0, rating: float = 0.0, is_available: bool = True, brand: str = "", images: List[str] = []):
        self.prod_id = prod_id
        self.domainId  = domainId
        self.productlink1 = productlink1
        self.status = status
        self.lastUpdated = lastUpdated
        self.lastScraped = lastScraped
        self.id = id
        self.name_Local = name_Local
        self.name_Global = name_Global
        self.description_Local = description_Local
        self.description_Global = description_Global
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
