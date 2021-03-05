from .. models.base_model_ import Model


class Internship(Model):
    def __init__(self, name_internship, category , when, where_plz, company_name, duration):
        self.swagger_types = {"name_internship": str, "category": str, "when": str, "where_plz": str, "company_name": str, "duration": str}
        self.attribute_map = {"name_internship": 'name_internship', "category": 'category', "when": 'when' , "where_plz": 'where_plz', "company_name": 'company_name', "duration": 'duration'}
        self.name_internship = name_internship
        self.category = category
        self.when = when
        self.where_plz = where_plz
        self.company_name = company_name
        self.duration = duration