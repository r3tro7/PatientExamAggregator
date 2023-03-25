from typing import Dict, List

#---------------Starting of Patient Class---------------#
class Patient:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.exams: List[Exam] = []
#---------------Ending of Patient Class---------------#

#---------------Starting of Exam Class---------------#
class Exam:
    def __init__(self, id: str):
        self.id = id
#---------------Ending of Exam Class---------------#

#---------------Starting of PatientExamSystem Class---------------#
class PatientExamSystem:
    """
    Manages the Patient Record System
    """
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.exams: Dict[str, Patient] = {}

#---------------Ending of PatientExamSystem Class---------------#