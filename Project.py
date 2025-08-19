# Student Report Card System


class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return "A"
        elif 70 <= self.marks <= 89:
            return "B"
        elif 50 <= self.marks <= 69:
            return "C"
        elif 35 <= self.marks <= 49:
            return "D"
        elif 0 <= self.marks <= 34:
            return "F"
        else:
            return "Invalid Marks"

    def __str__(self):
        return f"Subject : {self.name}\nMarks : {self.marks}\nGrade : {self.grade}\n"


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subjects = {}
        print(f"\nStudent Created Successfully!")
        print(f"Name : {self.name}\nRoll No. : {self.roll_no}\n")

    def add_subject(self, subject):
        try:
            if not isinstance(subject, Subject):
                raise TypeError
            self.subjects[subject.name] = subject
            print(f"Added subject : {subject.name}\n")
        except TypeError:
            print("Error: Invalid subject type")

    def view_report(self):
        print(f"\n----------- Report Card -----------")
        print(f"Roll No. : {self.roll_no} | Name : {self.name}\n")
        if not self.subjects:
            print("No subjects added yet.\n")
        else:
            for subject in self.subjects.values():
                print(subject)
        print("-----------------------------------\n")

    def update_marks(self, subject_name, new_marks):
        try:
            self.subjects[subject_name].marks = int(new_marks)
            self.subjects[subject_name].grade = self.subjects[subject_name].calculate_grade(
            )
            print(f"Marks updated for {subject_name}\n")
        except KeyError:
            print("Error: Subject not found")
        except ValueError:
            print("Error: Marks must be a number")

    def remove_subject(self, subject_name):
        try:
            del self.subjects[subject_name]
            print(f"Subject '{subject_name}' removed successfully.\n")
        except KeyError:
            print("Error: Subject not found")

    def search_subject(self, subject_name):
        if subject_name in self.subjects:
            print("\nSubject Found:")
            print(self.subjects[subject_name])
        else:
            print(f"Error: Subject '{subject_name}' not found.\n")


# ---------------------- MENU ----------------------
print("\n Welcome to Student Report Card System ")
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

card = Student(name, roll_no)

while True:
    print("----- MENU -----")
    print("1. Add Subject")
    print("2. Update Marks")
    print("3. Remove Subject")
    print("4. View Report")
    print("5. Search Subject")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sub_name = input("Enter subject name: ")
        try:
            marks = int(input("Enter marks (0-100): "))
            card.add_subject(Subject(sub_name, marks))
        except ValueError:
            print("Error: Marks must be a number between 0–100.\n")

    elif choice == "2":
        sub_name = input("Enter subject to update: ")
        try:
            marks = int(input("Enter new marks: "))
            card.update_marks(sub_name, marks)
        except ValueError:
            print("Error: Marks must be a number between 0–100.\n")

    elif choice == "3":
        sub_name = input("Enter subject to remove: ")
        card.remove_subject(sub_name)

    elif choice == "4":
        card.view_report()

    elif choice == "5":
        sub_name = input("Enter subject to search: ")
        card.search_subject(sub_name)

    elif choice == "6":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, try again.\n")
