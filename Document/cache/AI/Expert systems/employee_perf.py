class Employee:
    def __init__(self, name):
        self.name = name
        self.work_quality = 0
        self.communication = 0
        self.punctuality = 0
        self.teamwork = 0
        self.initiative = 0
        self.overall_rating = ""

class EmployeePerformanceEvaluationSystem:
    def __init__(self):
        self.employees = []

    def evaluate_employee(self):
        name = input("Enter employee's name: ")

        # Create an employee object
        emp = Employee(name)

        # Input performance ratings for the employee
        print(f"Rate {emp.name} on the following criteria (1 to 10):")

        emp.work_quality = int(input("Work Quality: "))
        emp.communication = int(input("Communication: "))
        emp.punctuality = int(input("Punctuality: "))
        emp.teamwork = int(input("Teamwork: "))
        emp.initiative = int(input("Initiative: "))

        # Calculate the overall rating based on the scores
        self.calculate_overall_rating(emp)

        # Add the evaluated employee to the system
        self.employees.append(emp)

        print(f"Evaluation for {emp.name} has been recorded successfully!\n")

    def calculate_overall_rating(self, emp):
        # Calculate the average of all ratings
        average_score = (emp.work_quality + emp.communication + emp.punctuality +
                         emp.teamwork + emp.initiative) // 5

        # Assign the overall rating based on the average score
        if average_score >= 9:
            emp.overall_rating = "Excellent"
        elif average_score >= 7:
            emp.overall_rating = "Good"
        elif average_score >= 5:
            emp.overall_rating = "Needs Improvement"
        else:
            emp.overall_rating = "Unsatisfactory"

    def display_evaluations(self):
        if not self.employees:
            print("No employee evaluations available.\n")
            return

        print("\nEmployee Performance Evaluations:")
        for emp in self.employees:
            print(f"Employee: {emp.name}")
            print(f"Work Quality: {emp.work_quality}")
            print(f"Communication: {emp.communication}")
            print(f"Punctuality: {emp.punctuality}")
            print(f"Teamwork: {emp.teamwork}")
            print(f"Initiative: {emp.initiative}")
            print(f"Overall Rating: {emp.overall_rating}\n")

    def display_menu(self):
        while True:
            print("\nEmployee Performance Evaluation System Menu:")
            print("1. Evaluate an employee")
            print("2. Display all employee evaluations")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.evaluate_employee()
            elif choice == 2:
                self.display_evaluations()
            elif choice == 3:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    # Create an instance of the Expert System and run it
    system = EmployeePerformanceEvaluationSystem()
    system.display_menu()

if __name__ == "__main__":
    main()
