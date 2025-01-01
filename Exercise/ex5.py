class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(101, "Harry")
student2 = Student(102, "Hermione")


print(f"Student 1: ID={student1.student_id}, Name={student1.student_name}")
print(f"Student 2: ID={student2.student_id}, Name={student2.student_name}")
