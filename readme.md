# Patient Record System
A simple service written in Python that reads in a text file containing patient and exam records, allows for adding or deleting records, and outputs a summary of patients in the system including their identifiers, names, and the number of exams they have gone through.

# Technical Specifications
- [Python 3](https://www.python.org/downloads/)

# How to Run the project
1. Navigate to the project directory using the command `cd <project directory>`
2. Place your input file in the project directory
3. Run the program using the command `python3 PatientExamAggregator.py`
4. Once you run the project, Enter the file path for the input and output files
5. The program will output the summary of the patients in the system to the console and also generate an `output.txt` file with sumary output

# Input File Instructions
- Add a patient record: `ADD PATIENT <patient_id> <patient_name>`
- Add an exam record: `ADD EXAM <patient_id> <exam_id>`
- Delete a patient record: `DEL PATIENT <patient_id>`
- Delete an exam record: `DEL EXAM <exam_id>`
