
#Mini Project: Student Grade Tracker
class Student():
    def __init__(self, studentName):
        self.name = studentName
        self.listName = []

    def add_grade(self, grade):
        self.listName.append(grade)

    def average_grade(self):
        if self.listName:
            return sum(self.listName) / len(self.listName)
        return 0

    def report(self):
        print(f'{self.name} Average grade are {self.average_grade():2f}')


Student1 = Student("Deepak")
Student1.add_grade(85)
Student1.add_grade(92)
Student1.add_grade(78)

Student1.report()

