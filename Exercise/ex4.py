class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")


student = Student(1, "Selena", "10th Grade")

student.display_attributes()
