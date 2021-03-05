from .. models.base_model_ import Model


class Apprenticeship(Model):
    def __init__(self, degree , when, where_plz, grade):
        self.swagger_types = {"degree": str, "when": str, "where_plz": str, "grade": str}
        self.attribute_map = {"degree": 'degree', "when": 'when', "where_plz": 'where_plz', "grade": 'grade'}
        self.degree = degree
        self.when = when
        self.where_plz = where_plz
        self.grade = grade
