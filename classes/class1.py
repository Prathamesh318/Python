class Bike:
    name=""
    gear=0

    def getNames(self):
        print(self.name+" "+self.gear)


bike1=Bike()
bike1.name="Bike2"
bike1.gear="gear"

bike2=Bike()

bike2.name="Bike2"
bike2.gear="gear2"

bike2.getNames()
bike1.getNames()