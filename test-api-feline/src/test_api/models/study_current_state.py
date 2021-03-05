from ..models.base_model_ import Model

class StudyCurrentState(Model):
    def __init__(self, currently_studying , fachfremd , field , degreed , degree_level, reason_why, disabled_support_level):
        self.swagger_types = {"currently_studying": bool, "fachfremd": bool, "field": str, "degreed": bool, "degree_level": str, "reason_why": str, "disabled_support_level": int}
        self.attribute_map = {"currently_studying": "currently_studying", "fachfremd": "fachfremd", "field": "field", "degreed": "degreed", "degree_level": "degree_level", "reason_why": "reason_why", "disabled_support_level": "disabled_support_level"}
        self.currently_studying = currently_studying
        self.fachfremd = fachfremd
        self.field = field
        self.degreed = degreed
        self.degree_level = degree_level
        self.reason_why = reason_why
        self.disabled_support_level = disabled_support_level
