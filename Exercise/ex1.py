class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()


print(isinstance(student_instance, Student)) 
print(isinstance(marks_instance, Marks))   


print(issubclass(Student, object)) 
print(issubclass(Marks, object))   
