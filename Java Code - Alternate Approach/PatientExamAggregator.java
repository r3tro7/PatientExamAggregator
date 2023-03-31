import java.io.*;
import java.util.*;

public class PatientExamAggregator {

    // Map to store patient records
    private Map<Integer, String> patients = new LinkedHashMap<>();

    // Map to store exam records
    private Map<Integer, Integer> exams = new HashMap<>();

    // Function to add a new patient record
    public void addPatient(int id, String name) {
        if (!patients.containsKey(id)) {
            patients.put(id, name);
        }
    }

    // Function to add a new exam record
    public void addExam(int patientId, int examId) {
        if (patients.containsKey(patientId) && !exams.containsKey(examId)) {
            exams.put(examId, patientId);
        }
    }

    // Function to delete a patient record and all associated exam records
    public void deletePatient(int id) {
        patients.remove(id);
        exams.entrySet().removeIf(entry -> entry.getValue() == id);
    }

    // Function to delete an exam record
    public void deleteExam(int id) {
        exams.remove(id);
    }

    // Function to print a summary of all patients and their exam counts
    public void printPatientSummary() {
        for (Map.Entry<Integer, String> patient : patients.entrySet()) {
            int id = patient.getKey();
            String name = patient.getValue();
            int examCount = (int) exams.values().stream().filter(x -> x == id).count();
            System.out.println("Name: " + name + ", Id: " + id + ", Exam Count: " + examCount);
        }
    }

    // Function to process a single instruction from the input file
    public void processInstruction(String instruction) {
        String[] segments = instruction.split(" ");
        String command = segments[0];
        int id;
        String name;
        switch (command) {
            case "ADD":
                String recordType = segments[1];
                switch (recordType) {
                    case "PATIENT":
                        id = Integer.parseInt(segments[2]);
                        name = String.join(" ", Arrays.copyOfRange(segments, 3, segments.length));
                        addPatient(id, name);
                        break;
                    case "EXAM":
                        int patientId = Integer.parseInt(segments[2]);
                        int examId = Integer.parseInt(segments[3]);
                        addExam(patientId, examId);
                        break;
                }
                break;
            case "DEL":
                recordType = segments[1];
                switch (recordType) {
                    case "PATIENT":
                        id = Integer.parseInt(segments[2]);
                        deletePatient(id);
                        break;
                    case "EXAM":
                        int examId = Integer.parseInt(segments[2]);
                        deleteExam(examId);
                        break;
                }
                break;
        }
    }

    // Function to process the entire input file
    public void processInstructions(List<String> instructions) {
        for (String instruction : instructions) {
            processInstruction(instruction);
        }
    }


    //reads files and provides list of instructions
    public List<String> readInstructions(String filename) {
        List<String> instructions = new ArrayList<>();

        try {
            File inputFile = new File(filename);
            FileReader fr = new FileReader(inputFile);

            BufferedReader br = new BufferedReader(fr);
            String line;
            while( (line = br.readLine()) != null) {
                instructions.add(line);
            }

            fr.close();
        } catch (IOException e) {
            System.out.printf("exception occurred: " + e.getMessage());
        }

        return instructions;
    }

    // Sample test cases
    public static void main(String[] args) {
        PatientExamAggregator aggregator = new PatientExamAggregator();
        aggregator.processInstructions( aggregator.readInstructions("input5.txt"));
        aggregator.printPatientSummary();
    }
}