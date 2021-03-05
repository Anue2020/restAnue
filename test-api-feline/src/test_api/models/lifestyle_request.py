from ..models.base_model_ import Model

class LifeStyleRequest(Model):
    def __init__(self, lifestyle_product_name , distance , density , category , sub_category):

        self.swagger_types = {"lifestyle_product_name": str, "distance": float, "density": int, "category": str, "sub_category": str}
        self.attribute_map = {"lifestyle_product_name": 'lifestyle_product_name', "distance": 'distance', "density": 'density', "category": 'category', "sub_category": 'sub_category'}

        self.lifestyle_product_name = lifestyle_product_name
        self.distance = distance
        self.density = density
        self.category = category
        self.sub_category = sub_category

