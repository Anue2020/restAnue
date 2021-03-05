
from .. models.base_model_ import Model

class Income(Model):
    def __init__(self, income_type, income_amount):
        self.swagger_types = {'income_type': str, "income_amount": float}
        self.attribute_map = {'income_type': "income_type", "income_amount": "income_amount"}
        self.income_type = income_type
        self.income_amount = income_amount
