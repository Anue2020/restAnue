from .. models.base_model_ import Model



class School(Model):
    def __init__(self, degree_category, when, where_plz, grade):
        self.swagger_types = {'degree_category': str, 'when': str, 'where_plz': str, 'grade': float}
        self.attribute_map = {'degree_category': 'degree_category', 'when': 'when' , 'where_plz': 'where_plz' , 'grade': 'grade'}
        self.degree_category = degree_category
        self.when = when
        self.where_plz = where_plz
        self.grade = grade
