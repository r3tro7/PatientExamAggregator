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

    #-----Starting of add_patient() Method-----#
    def add_patient(self, id: str, name: str) -> None:
        """
        Function to add Patient Record to the System
        Parameters:
            id(str): Patient ID
            name(str): Patient Name
        """
        if id not in self.patients:
            self.patients[id] = Patient(id, name)
    #-----Ending of add_patient() Method-----#

    #-----Starting of add_exam() Method-----#
    def add_exam(self, patient_id: str, exam_id: str) -> None:
        """
        Function to add Examination Record to the System
        Parameters:
            patiend_id(str): Patient ID
        """
        if patient_id in self.patients and exam_id not in self.exams:
            self.patients[patient_id].exams.append(Exam(exam_id))
            self.exams[exam_id] = self.patients[patient_id]
    #-----Ending of add_exam() Method-----#

#---------------Ending of PatientExamSystem Class---------------#