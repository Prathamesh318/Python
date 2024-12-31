class Parent:
    def feature(self):
        print("Feature from Parent")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class GrandChild(Child1, Child2):
    pass

obj = GrandChild()
obj.feature()  # Output: Feature from Parent (due to Method Resolution Order - MRO)
