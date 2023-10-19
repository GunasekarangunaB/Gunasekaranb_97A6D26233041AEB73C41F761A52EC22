def sort_students(students):
    sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)
    return sorted_students


class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("John", "001", 3.8),
    Student("Jane", "002", 3.5),
    Student("Bob", "003", 3.9),
    Student("Alice", "004", 4.0)
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(student.name, student.roll_number, student.cgpa)