from .. models.base_model_ import Model


class StudyInterest(Model):
    def __init__(self, category, where_plz, category_university_location, target_degree, preferred_study_language, abroad_term_opportunity):
        self.swagger_types = {"category": str, "where_plz": str, "category_university_location": int, "target_degree": str, "preferred_study_language": str, "abroad_term_opportunity": bool}
        self.attribute_map = {"category": "category", "where_plz": "where_plz", "category_university_location": "category_university_location", "target_degree": "target_degree", "preferred_study_language": "preferred_study_language", "abroad_term_opportunity": "abroad_term_opportunity"}
        self.category = category
        self.where_plz = where_plz
        self.category_university_location = category_university_location
        self.target_degree = target_degree
        self.preferred_study_language = preferred_study_language
        self.abroad_term_opportunity = abroad_term_opportunity
