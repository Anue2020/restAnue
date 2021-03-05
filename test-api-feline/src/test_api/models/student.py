# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict, Any  # noqa: F401




#todo: regroup into Basti's directories /education/..
from .contact import Contact
from .school import School
from .language import Language
from .internship import Internship
from .apprenticeship import Apprenticeship
from .study_current_state import StudyCurrentState
from .soft_criteria import SoftCriteria
from .study_interest import StudyInterest
from .income import Income
from .base_model_ import Model


class Student(Model):
    def __init__(self, studentId, contact, geschlecht, nationality, education_level,
                 languages, internships, apprenticeships, wartesemester, study_current_state, soft_criterias, income):
        self.swagger_types = {'studentId': str, 'contact': Contact, 'geschlecht': str, 'nationality': str, 'education_level': School,
                              'languages': List[Language], 'internships': List[Internship], 'apprenticeship': List[Apprenticeship], 'wartesemester': int,
                              "study_interest": List[StudyInterest],'study_current_state': StudyCurrentState, 'soft-criteria': SoftCriteria, "income": List[Income]}
        self.attribute_map = {
            'studentId': 'studentId',
            'contact': 'contact',
            'geschlecht': 'geschlecht',
            'nationality': 'nationality',
            'education_level': 'education_level',
            'languages': 'languages',
            'internships': 'internships',
            'apprenticeship': 'apprenticeship',
            'wartesemester': 'wartesemester',
            'study_current_state': 'study_current_state',
            'soft-criteria': 'soft-criteria',
            'income': 'income'}

        self.id = studentId
        self.contact = contact
        self.geschlecht = geschlecht
        self.nationality = nationality
        self.education_level = education_level
        self.languages = languages
        self.internships = internships
        self.apprenticeships = apprenticeships
        self.wartesemester = wartesemester #diff von Abi - Now
        self.study_current_state = study_current_state
        self.soft_criterias = soft_criterias
        self.income = income
        #todo: should status of student be stored in self?

    @classmethod
    def from_dict(cls, dictionary: Dict[str, Any]) -> 'Student':
        """Returns the dict as a model
        """
        return util.deserialize_model(dictionary, cls)

    @property
    def id(self) -> int:
        """get id of this Student"""
        return self.id

    @id.setter
    def id(self, studentId: int):
        """set id of this Student"""
        self.id = studentId

    @property
    def contact(self) -> Contact:
        """get the contact info of student"""
        return self.contact

    @contact.setter
    def contact(self, contact: Contact):
        """Sets contact information of this student"""
        self.contact = contact

    @property
    def contact(self) -> Contact:
        """get the contact info of student"""
        return self.contact

    @contact.setter
    def contact(self, contact: Contact):
        """Sets contact information of this student"""
        self.contact = contact

