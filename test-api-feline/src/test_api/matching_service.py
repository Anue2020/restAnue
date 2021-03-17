from test_api.db_connector import DBConnector


class MatchingService:

    def __init__(self):
        self.db_connector = DBConnector(host_name='localhost', user_name='root', user_password='3FTEDZZd',
                                        db_name='AnueTest')

    def update_student_with_matching_scores(self, student_json):
        #todo: first get eligible uni data from database based on basic requirements: desired_study_field, location
        #
        pass

    def _get_eligible_unis(self, student_json):
        eligible_unis_based_on_education_level = self.db_connector.get_data_for_eligible_unis_from_db(student_json["education_level"])
        #todo: definine matching algorithm logic
        #a function which returns a score representing how similar two descriptions are -e.g. description from student['']
        pass