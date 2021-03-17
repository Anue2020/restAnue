import mysql
from mysql.connector.django.base import Error


class DBConnector:

    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name

    def _create_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

    def _execute_query(self, query:str):
        #query is SQL query written out
        connection = self._create_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def add_new_student_to_db(self, studentId):
        sql_string = f'INSERT INTO Student(studentId) VALUES {studentId}'
        return self._execute_query(sql_string)

    def update_student_from_json(self, student):
        pass

    def get_student_record_by_id(self, studentId):
        pass

    def get_data_for_eligible_unis_from_db(self, education_level):
        #todo: clarify how eligibility could be limited by other factors
        query = f"""
        SELECT * FROM Hochschule WHERE Hochschule.education_entry_level <= {education_level}
         """
        # ideally query returns eligible_unis_data as list of dictionaries with fields according to standardized info of all universities
        # [{"hochschuleId": ..., hochschule_name: ...,location: ..., education_entry_level: ..., language_primary: ..., language_1: ...,study_field_1: ..., study_field_2: ..., study_field_3:..., study_field_4: ..., study_field_5: ...)}]
        eligible_unis_data = self.db_connector.execute_query(query)
        return eligible_unis_data



