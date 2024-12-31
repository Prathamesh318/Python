class Parent1:
    def feature1(self):
        print("Feature 1 from Parent1")

class Parent2:
    def feature2(self):
        print("Feature 2 from Parent2")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.feature1()  # Output: Feature 1 from Parent1
obj.feature2()  # Output: Feature 2 from Parent2
