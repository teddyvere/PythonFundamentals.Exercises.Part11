from datetime import date
from enum import Enum

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, first_name: str):
        self.first_name = first_name

    def update_last_name(self, last_name: str):
        self.last_name = last_name

    def update_dob(self, dob: date):
        self.dob = dob

    def update_status(self, alive: AliveStatus):
        self.alive = alive

class Instructor(Person):
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus, instructor_id: dict):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = instructor_id

class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus, student_id: dict):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = student_id

class ZipCodeStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus, student_id: dict):
        super().__init__(first_name, last_name, dob, alive, student_id)

class HighSchoolStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus, student_id: dict):
        super().__init__(first_name, last_name, dob, alive, student_id)

class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor: Instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor_id: dict):
        self.instructors = [instructor for instructor in self.instructors if instructor.instructor_id != instructor_id]

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student_id: dict):
        self.students = [student for student in self.students if student.student_id != student_id]

    def print_instructors(self):
        print("Instructors:")
        for instructor in self.instructors:
            print(f"{instructor.first_name} {instructor.last_name}")

    def print_students(self):
        print("Students:")
        for student in self.students:
            print(f"{student.first_name} {student.last_name}")

# Test for Classroom
def test_classroom():
    classroom = Classroom()
    instructor = Instructor("John", "Doe", date(1980, 1, 1), AliveStatus.Alive, {"id": 1})
    student = Student("Jane", "Smith", date(2000, 2, 2), AliveStatus.Alive, {"id": 2})

    classroom.add_instructor(instructor)
    classroom.add_student(student)

    assert len(classroom.instructors) == 1
    assert len(classroom.students) == 1

    classroom.remove_instructor({"id": 1})
    classroom.remove_student({"id": 2})

    assert len(classroom.instructors) == 0
    assert len(classroom.students) == 0

test_classroom()