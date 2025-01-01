class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("Prathamesh", 95)

print(f"Original: Name={student.student_name}, Marks={student.marks}")


student.student_name = "Damon"
student.marks = 85

print(f"Modified: Name={student.student_name}, Marks={student.marks}")
