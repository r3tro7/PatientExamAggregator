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
    Manages the Patient Record System.
    """
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.exams: Dict[str, Patient] = {}

    #-----Starting of add_patient() Method-----#
    def add_patient(self, id: str, name: str) -> None:
        """
        Function to add Patient Record to the System.
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
        Function to add Examination Record to the System.
        Parameters:
            patiend_id(str): Patient ID
        """
        if patient_id in self.patients and exam_id not in self.exams:
            self.patients[patient_id].exams.append(Exam(exam_id))
            self.exams[exam_id] = self.patients[patient_id]
    #-----Ending of add_exam() Method-----#

    #-----Starting of del_patient() Method-----#
    def del_patient(self, id: str) -> None:
        """
        Function to delete patient Record from the system.
        Parameters:
            id(str): Patient ID
        """
        if id in self.patients:
            for exam in self.patients[id].exams:
                self.exams.pop(exam.id, None)
            self.patients.pop(id, None)
    #-----Ending of del_patient() Method-----#

    #-----Starting of del_exam() Method-----#
    def del_exam(self, id: str) -> None:
        """
        Function to delete Examination record from the System.
        Parameters:
            id(str): Examination ID
        """
        if id in self.exams:
            self.exams[id].exams = [exam for exam in self.exams[id].exams if exam.id != id]
            self.exams.pop(id, None)
    #-----Ending of del_exam() Method-----#

    #-----Starting of get_patients_summary() Method-----#
    def get_patients_summary(self) -> List[str]:
        """
        Function to generate a Patient Record Summary.
        Returns:
            summary(List): List containing all Records for a Patient
        """
        summary = []
        for id, patient in self.patients.items():
            summary.append(f"Name: {patient.name}, Id: {patient.id}, Exam Count: {len(patient.exams)}")
        return summary
    #-----Ending of get_patients_summary() Method-----#

#---------------Ending of PatientExamSystem Class---------------#

#---------------Starting of process_file() Method---------------#
def process_file() -> None:
    """
    Function to Process the input.txt file and Generate a summary for all patients on the Systems.
    The function also generates an output.txt file with the summary and also outputs the summary on the console.
    """
    system = PatientExamSystem()
    input_file_path = input("Enter input file path: ")
    if input_file_path == "":
        input_file_path = "input.txt"
    output_file_path = input("Enter output file path: ")
    if output_file_path == "":
        output_file_path = "output.txt"
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            tokens = line.strip().split()
            if tokens[0] == "ADD":
                if tokens[1] == "PATIENT":
                    system.add_patient(tokens[2], " ".join(tokens[3:]))
                elif tokens[1] == "EXAM":
                    system.add_exam(tokens[2], tokens[3])
            elif tokens[0] == "DEL":
                if tokens[1] == "PATIENT":
                    system.del_patient(tokens[2])
                elif tokens[1] == "EXAM":
                    system.del_exam(tokens[2])

        summary = system.get_patients_summary()
        for patient in summary:
            output_file.write(patient + '\n')
            print(patient)
#---------------Ending of process_file() Method---------------#

if __name__ == '__main__':
    process_file()