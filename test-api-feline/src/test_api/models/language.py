from .. models.base_model_ import Model


class Language(Model):
    def __init__(self, language, language_level, language_certification, kind_certification, german_certification):
        self.swagger_types = {"language": str, "language_level": str, "language_certification": bool , "kind_certification": str, "german_certification": bool}
        self.attribute_map = {"language": "language", "language_level": "language_level", "language_certification": "language_certification", "kind_certification":"kind_certification" , "german_certification": "german_certification"}
        self.language = language
        self.language_level = language_level
        self.language_certification = language_certification
        self.kind_certification = kind_certification
        self.german_certification = german_certification