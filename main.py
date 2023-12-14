class Person:
    def __init__(self):
        self.name = input("Enter name: ")
        self.gender = input("Enter gender: ")
        self.mobile_number = input("Enter mobile number: ")

class Department:

    def __init__(self):
        self.department_name = input("Enter department name: ")
        self.faculty = input("Enter faculty: ")
        self.short_description = input("Enter short description: ")

class Student(Person, Department):

    def __init__(self):
        Person.__init__(self)
        Department.__init__(self)
        self.registration_number = input("Enter registration number: ")
        self.student_course = input("Enter student course: ")
        self.duration_of_course = input("Enter duration of the course: ")

    def enter_marks(self):
        self.unit_name = input("Enter unit name: ")
        self.unit_code = input("Enter unit code: ")
        self.course_work_mark = int(input("Enter course work mark (out of 40): "))
        self.exam_mark = int(input("Enter exam mark (out of 60): "))

    def student_grade(self):
        total_marks = self.course_work_mark + self.exam_mark
        if 70 <= total_marks <= 100:
            return "First Class Honours"
        elif 60 <= total_marks <= 69:
            return "Second Class Honours, Upper Division"
        elif 50 <= total_marks <= 59:
            return "Second Class Honours, Lower Division"
        else:
            return "Pass"

    def display_student_info(self):
        print("Registration Number:", self.registration_number)
        print("Name:", self.name)
        print("Department:", self.department_name)
        print("Course:", self.student_course)
        print("Unit Name:", self.unit_name)
        print("Unit Code:", self.unit_code)
        print("Course Work Marks:", self.course_work_mark)
        print("Exam Marks:", self.exam_mark)
        print("Class:", self.student_grade())

# Driver code
if __name__ == "__main__":
    student = Student()
    student.enter_marks()
    student.display_student_info()
