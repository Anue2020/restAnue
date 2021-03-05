from typing import List

from ..models.base_model_ import Model
from .. models.sparetime_request import SpareTimeRequest
from .. models.lifestyle_request import LifeStyleRequest



class SoftCriteria(Model):
    def __init__(self, care_rate , digitalization_level , sparetime_requests , level_socialscore , library_score, university_cafeteria, children_daycare,
                 nature_related_location, is_college_town, is_young_town, lifestyle_requests):


        self.swagger_types = {"care_rate": int , "digitalization_level": int , "sparetime_requests": List[SpareTimeRequest] , "level_socialscore": int , "library_score": int, "university_cafeteria": int, "children_daycare": bool,
                 "nature_related_location": int, "is_college_town": bool, "is_young_town": bool, "lifestyle_requests": List[LifeStyleRequest]}

        self.attribute_map = {"care_rate": "care_rate" , "digitalization_level": "digitalization_level" , "sparetime_offer": "sparetime_offer", "level_socialscore": "level_socialscore" , "library_score": "library_score", "university_cafeteria": "university_cafeteria", "children_daycare": "children_daycare",
                 "nature_related_location": "nature_related_location", "is_college_town": "is_college_town", "is_young_town": "is_young_town", "lifestyle_request": "lifestyle_request"}


        self.care_rate = care_rate
        self.digitalization_level = digitalization_level
        self.sparetime_requests = sparetime_requests
        self.level_socialscore = level_socialscore
        self.library_score = library_score
        self.university_cafeteria = university_cafeteria
        self.children_daycare = children_daycare
        self.nature_related_location = nature_related_location
        self.is_college_town = is_college_town
        self.is_young_town = is_young_town
        self.lifestyle_requests = lifestyle_requests