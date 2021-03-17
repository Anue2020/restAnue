'''The controller contains one function for every CRUD method defined at specific endpoint in specification.yml;
so if another endpoint will be added (e.g. /universities) with its specific CRUD methods, these need to be defined in a controller as well
'''
import json
import string
from random import random

import connexion
import requests

from test_api.db_connector import DBConnector
from test_api.student import Student


class StudentService:
    def __init__(self):
        self.db_connector =DBConnector(host_name='localhost', user_name='root', user_password='3FTEDZZd', db_name= 'AnueTest' )

    def add_student(self):
        """Add a new student; body is a dictionary with attributes to be added for specific student
        """
        studentId = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        student_json = connexion.request.get_json()#todo: how the body parameters defined by schemas are generated?
        if isinstance(student_json, list):
            student_json = student_json[0]
        student_json['studentId'] = studentId
        try:
            self.db_connector.add_new_student_to_db(studentId)
            return {}, 200
        except Exception:
            raise

    def update_student(self, student_update_json):
        """Update an existing student; body is a dictionary with attributes to be overwritten or added for specific student
        """

        if connexion.request.is_json:
            body = connexion.request.get_json()
            try:
                #todo: create update_student_from_json function in db_connector to store new fiels in db
                # (update record in DB by reading key,values from json file provided in body of post command and convert keys to columns and fields to values)
                self.db_connector.update_student_from_json(student_update_json)
                #todo: get all fields from database as json to return in response
                student_full_json = self.db_connector.get_student_record_by_id(student_update_json["studentId"])
                #todo: check if sufficient info is available/ define minimum of questions answered & start matching service
                self._post_student_to_matcher(student_full_json)

                response = json.dumps(student_full_json), 200
            except KeyError:
                response = {}, 404
            return response


    def _post_student_to_matcher(self, student_json):
        #matcher called once a minimum of questions are answered
        #todo: define minimum of questions answered
        return requests.post(f'https://anue.eu/student/{student_json["studentId"]}/matcher', data = student_json)


    def get_student(self, studentId):
        """get a student including all related info if available through Id"""
        try:
            student_dict = self.db_connector.get_student_record_by_id(studentId)
            # todo: create get_student_by_id function in db_connector, should return a Student object build from records in db
            student = Student(studentId=student_dict["id"], contact=student_dict["contact"], geschlecht= student_dict["geschlecht"], nationality = student_dict["nationality"],
                               education_level = student_dict["education_level"], languages=student_dict["languages"], internships = student_dict["internships"],
                               apprenticeships = student_dict["apprenticeships"], wartesemester = student_dict["wartesemester"], study_current_state = student_dict["study_current_state"],
                               soft_criterias = student_dict["soft_criterias"], income = student_dict["income"], matching_scores = student_dict['matching_scores'])
            #todo: start microservice matcher here??
            response = json.dumps(student_dict), 200
            #todo: should return a json with all fields, including matching scores?
        except KeyError:
            response = {}, 404

        return response

