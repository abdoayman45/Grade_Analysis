from os import system, name
from time import sleep
from sys import exit

def cls():
    system('cls' if name == 'nt' else 'clear')

class GradeAnalysisApp:
    def __init__(self):
        self.grade_list = []
        self.max_grade = 0
        self.min_grade = 0
        self.subject_name = ""
        self.professor_name = ""
        self.grade_average_var = 0

    def client_information(self):
        while True:
            try:
                self.professor_name = input("Enter your name: ").strip().capitalize()
                self.subject_name = input("Enter the name of your subject: ").strip().capitalize()
                if self.professor_name.isalpha() and self.subject_name.isalpha():
                    self.max_grade = int(input("Enter the maximum grade: "))
                    self.min_grade = int(input("Enter the minimum grade: "))
                    break
                else:
                    print("Sorry, Professor. The fields for your name and the subject must only contain letters.")
            except ValueError:
                print("Sorry, Professor. The fields for maximum grade and minimum grade must only contain numbers.")

    def add_grade(self):
        cls()
        print(f"I hope the grades are good today, Professor {self.professor_name}\n")
        adding = True
        while adding:
            while True:
                cls()
                try:
                    self.student_name = input("Enter the name of the student: ").strip().capitalize()
                    self.student_grade = int(input("Enter the grade of the student: "))
                    if (0 <= self.student_grade <= self.max_grade) and (self.student_name.isalpha()):
                        break
                    elif (self.student_grade < 0 or self.student_grade > self.max_grade):
                        print(f"\nINVALID GRADE, Enter only between '0' and {self.max_grade}")
                        sleep(3)
                    else:
                        print("\nEnter only letters for the name.\n")
                        sleep(3)
                except ValueError:
                    print("\nINVALID GRADE, Enter only numbers.\n")
                    sleep(3)
            self.grade_list.append({'name': self.student_name, 'grade': self.student_grade})
            print("\nThe grade has been successfully added.\n")
            again = input("Do you want to add another student? (y/n): ").lower()
            if again == 'n':
                adding = False
                cls()

    def calculate(self):
        cls()
        print(f"\nI hope the success percentage in {self.subject_name} is the highest.\n")
        if self.grade_list:
            while True:
                cls()
                print("1. Success Percentage.")
                print("2. Failure Percentage.")
                print("3. Grade Average.")
                print("4. Grade Classification.")
                print("5. Student with the Highest Grade.")
                print("6. Student with the Lowest Grade.")
                print("7. Back to Main Menu.")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.success_percentage()
                elif choice == "2":
                    self.failure_percentage()
                elif choice == "3":
                    self.calculate_average()
                elif choice == "4":
                    self.classification()
                elif choice == "5":
                    self.highest_grade()
                elif choice == "6":
                    self.lowest_grade()
                elif choice == "7":
                    cls()
                    self.start_loop()
                else:
                    print("\nINVALID CHOICE, Please try again.\n")
                    sleep(1)
        else:
            print("\nYou have no grades in the list. Try adding some first, then come back.\n")
            sleep(1)

    def success_percentage(self):
        cls()
        def filter_success_percentage(index):
            return index['grade'] > self.min_grade

        filtered_list = list(filter(filter_success_percentage, self.grade_list))
        percentage = (len(filtered_list) / len(self.grade_list)) * 100
        print(f"\nThe Success Percentage: {round(percentage, 3)}%\n")
        input("Press 'Enter' to continue: ")

    def failure_percentage(self):
        cls()
        def filter_failure_percentage(index):
            return index['grade'] < self.min_grade

        filtered_list = list(filter(filter_failure_percentage, self.grade_list))
        percentage = (len(filtered_list) / len(self.grade_list)) * 100
        print(f"\nThe Failure Percentage: {round(percentage, 3)}%\n")
        input("Press 'Enter' to continue: ")

    def calculate_average(self):
        cls()
        self.grade_average_var = sum([i['grade'] for i in self.grade_list]) / len(self.grade_list)
        print(f"\nThe average: {round(self.grade_average_var, 3)}\n")
        students_above_average = []
        for i in self.grade_list:
            if i['grade'] >= self.grade_average_var:
                students_above_average.append(i['name'])
        joined_list = '\n'.join(students_above_average)
        print(f"All students with grades above the average:\n{joined_list}\n")
        input("Press 'Enter' to continue: ")

    def classification(self):
        cls()
        print("1. Ascending Order.")
        print("2. Descending Order.")
        print("3. Back to Calculation Menu.")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3"]:
            print("\nYou must choose between (1, 2, 3) only.\n")
            choice = input("Enter your choice: ")
        if choice == "1":
            self.classify_ascending()
        elif choice == "2":
            self.classify_descending()
        elif choice == "3":
            self.calculate()

    def classify_ascending(self):
        sorted_grades = sorted(self.grade_list, key=self.filter_classification_key)
        print("\nAll grades in ascending order:\n")
        for i in sorted_grades:
            print(f"The grade: {i['grade']} ---> {i['name']}")
            print('-' * 30)
        input("Press 'Enter' to continue: ")

    def filter_classification_key(self, index):
        return index['grade']

    def classify_descending(self):
        sorted_grades = sorted(self.grade_list, reverse=True, key=self.filter_classification_key)
        print("\nAll grades in descending order:\n")
        for i in sorted_grades:
            print(f"The grade: {i['grade']} ---> {i['name']}")
            print('-' * 30)
        input("Press 'Enter' to continue: ")

    def highest_grade(self):
        cls()
        highest = max([i['grade'] for i in self.grade_list])
        print(f"\nStudents who scored the highest grade:\n")
        for n, i in enumerate(self.grade_list, start=1):
            if i['grade'] == highest:
                print(f"{n}. Name: {i['name']} ---> Scored {highest}\n")
        input("Press 'Enter' to continue: ")

    def lowest_grade(self):
        cls()
        lowest = min([i['grade'] for i in self.grade_list])
        print(f"\nStudents who scored the lowest grade:\n")
        for n, i in enumerate(self.grade_list, start=1):
            if i['grade'] == lowest:
                print(f"{n}. Name: {i['name']} ---> Scored {lowest}\n")
        input("Press 'Enter' to continue: ")

    def add_points(self):
        if self.grade_list:
            cls()
            def filter_below_max(index):
                return index['grade'] < self.max_grade

            def map_points(index, point):
                index['grade'] += int(point)
                return index

            def filter_equal_max(index):
                return index['grade'] == self.max_grade

            print(f"\nThank you for this step, Professor {self.professor_name}\n")
            while True:
                try:
                    points = int(input("Enter how many points you want to add for each student: "))
                    if points > 0:
                        break
                    else:
                        print("Points must be greater than '0'.")
                except ValueError:
                    print("Professor, enter only numbers, not letters.")

            filtered_list_1 = list(filter(filter_below_max, self.grade_list))
            filtered_list_2 = list(filter(filter_equal_max, self.grade_list))
            updated_list = list(map(map_points, filtered_list_1, [str(points)] * len(filtered_list_1)))
            for i in updated_list:
                if i['grade'] >= self.max_grade:
                    i['grade'] = self.max_grade - 0.5
            self.grade_list = filtered_list_2 + updated_list
            print(f"\nThe grades have been updated.\n")
            for i in self.grade_list:
                print(f"{i['name']} ---> {i['grade']}")
            input("Press 'Enter' to continue: ")
            cls()
        else:
            print("You have nothing in your list. Please try filling the student list first.")
            sleep(1)

    def start_loop(self):
        while True:
            print("1. Add student grades.")
            print("2. Calculation section.")
            print("3. Add points for student grades.")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_grade()
            elif choice == "2":
                self.calculate()
            elif choice == "3":
                self.add_points()
            elif choice == "4":
                print("Exited.")
                exit()

    def start_app(self):
        print("Welcome to the app for analyzing your students' grades.\n")
        self.client_information()
        cls()
        print(f"\nWelcome, Professor {self.professor_name}. You can analyze the grades of your students in {self.subject_name}.\n")
        self.start_loop()

biology = GradeAnalysisApp()
biology.start_app()
