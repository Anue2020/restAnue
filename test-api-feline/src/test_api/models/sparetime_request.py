from .. models.base_model_ import Model


class SpareTimeRequest(Model):
    def __init__(self, activity_name, distance, category):
        self.swagger_types = {"activity_name": str, "distance": float, "category": str}
        self.attribute_map = {"activity_name": 'activity_name', "distance": 'distance', "category": 'category'}
        self.activity_name = activity_name #e.g. rowing
        self.distance = distance #e.g. within 10km
        self.category = category #e.g. Sport
