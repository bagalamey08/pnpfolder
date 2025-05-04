class Symptom:
    def __init__(self, symptom, disease):
        self.symptom = symptom
        self.disease = disease

class MedicalExpertSystem:
    def __init__(self):
        # Simple set of symptoms and their possible diseases
        self.symptoms = [
            Symptom("fever", "flu"),
            Symptom("cough", "flu"),
            Symptom("headache", "migraine"),
            Symptom("nausea", "migraine"),
            Symptom("chest pain", "heart attack"),
            Symptom("shortness of breath", "heart attack"),
            Symptom("rash", "allergy"),
            Symptom("sneezing", "allergy")
        ]

    def diagnose(self):
        patient_symptoms = []
        print("Welcome to the Medical Expert System!")
        print("Please answer the following questions with 'yes' or 'no'.")
        
        # Asking about symptoms
        for symptom in self.symptoms:
            input_answer = input(f"Do you have {symptom.symptom}? (yes/no): ").strip().lower()
            if input_answer == "yes":
                patient_symptoms.append(symptom.symptom)

        # Providing diagnosis based on symptoms
        if not patient_symptoms:
            print("No symptoms detected. Please consult a healthcare professional for more information.")
        else:
            print("Based on the symptoms you provided, the possible conditions are:")
            self.diagnose_condition(patient_symptoms)

    def diagnose_condition(self, symptoms_list):
        possible_diseases = set()

        # Check each symptom against the list of diseases
        for symptom in symptoms_list:
            for s in self.symptoms:
                if s.symptom == symptom:
                    # Add the disease to the possible diseases list
                    possible_diseases.add(s.disease)

        if not possible_diseases:
            print("Sorry, no known condition matches the symptoms provided.")
        else:
            for disease in possible_diseases:
                print(f"- {disease}")
            print("It is recommended to visit a doctor for further evaluation.")

# Create an instance of the expert system and run it
if __name__ == "__main__":
    system = MedicalExpertSystem()
    system.diagnose()
