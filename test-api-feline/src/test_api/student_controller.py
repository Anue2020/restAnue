'''The controller contains one function for every CRUD method defined at specific endpoint in specification.yml;
so if another endpoint will be added (e.g. /universities) with its specific CRUD methods, these need to be defined in a controller as well
'''

import json
import string
from random import random

import connexion
import requests

from test_api.models.student import Student


def add_student():
    """Add a new student; body is a dictionary with attributes to be added for specific student
    """
    studentId = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    return requests.post(url = "www.anue.eu/student/", json= json.dumps({"studentId": studentId}))

def update_student(student):
    """Update an existing student; body is a dictionary with attributes to be overwritten or added for specific student
    """
    if connexion.request.is_json:
        body = student.from_dict(connexion.request.get_json())
        try:
            requests.post(url = f"www.anue.eu/student/{student.id}", data = body)
            response = {}, 200
        except KeyError:
            response = {}, 404
        return response


def get_student(studentId):
    """get a student including all related info if available through Id"""
    try:
        student_info_json = requests.get(url = f"www.anue.eu/student/{studentId}").json()
        student = Student.from_dict(student_info_json)
        response = Student(studentId=student.id, contact=student.contact, geschlecht= student.geschlecht, nationality = student.nationality,
                           education_level = student.education_level, languages=student.languages, internships = student.internships,
                           apprenticeships = student.apprenticeships, wartesemester = student.wartesemester, study_current_state = student.study_current_state,
                           soft_criterias = student.soft_criterias, income = student.income), 200
    except KeyError:
        response = {}, 404

    return response

