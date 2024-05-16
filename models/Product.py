class ItemData:
    def __init__(self, title=None, price=None, rating=None, description=None, images=None):
        self.title = title
        self.price = price
        self.rating = rating
        self.description = description
        self.images = images

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "rating": self.rating,
            "description": self.description,
            "images": self.images
                            }

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
