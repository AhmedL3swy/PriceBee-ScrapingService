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

    def __dict__(self):
        return {
            "prod_id": self.prod_id,
            "domainId": self.domainId,
            "productlink1": self.productlink1,
            "status": self.status,
            "lastUpdated": self.lastUpdated,
            "lastScraped": self.lastScraped,
            "id": self.id,
            "name_Local": self.name_Local,
            "name_Global": self.name_Global,
            "description_Local": self.description_Local,
            "description_Global": self.description_Global,
            "price": self.price,
            "rating": self.rating,
            "is_available": self.is_available,
            "brand": self.brand,
            "images": self.images
        }

    def __str__(self):
        return (f"ProductDetailDTO(prod_id={self.prod_id}, domainId={self.domainId}, productlink1={self.productlink1}, "
                f"status={self.status}, lastUpdated={self.lastUpdated}, lastScraped={self.lastScraped}, id={self.id}, "
                f"name_Local={self.name_Local}, name_Global={self.name_Global}, description_Local={self.description_Local}, "
                f"description_Global={self.description_Global}, price={self.price}, rating={self.rating}, "
                f"is_available={self.is_available}, brand={self.brand}, images={self.images})")
