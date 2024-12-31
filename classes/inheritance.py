class Animal:
    name=""
    type=""
    def setDetails(self,name,type1):
        self.name=name
        self.type=type1
        
    
class Dog(Animal):
    description=""
    
    def setDescription(self,str):
        self.description=str
        
    def getDetails(self):
        print("Name"+self.name)
        print("Type"+self.type)
        print("Details"+self.description)
        
        
dog1=Dog()
dog1.name="Fluppy"

dog1.type="German Shepheard"

dog1.description="Loyal"

dog2=Dog()

dog2.setDetails("Chickoo","Bull dog")
dog2.setDescription("Powerful")

dog1.getDetails()
dog2.getDetails();


        