class Parent:
    def feature(self):
        print("Feature from Parent")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.feature()  # Output: Feature from Parent
obj2.feature()  # Output: Feature from Parent
