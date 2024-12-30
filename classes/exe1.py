class Employee:
    
    name="p"
    def __init__(self, emp_name, emp_id, bp,hra, pf):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.bp=bp
        self.hra=hra
        self.pf=pf

    def gross_salary(self):
        self.gp=self.bp+self.hra
        self.np=self.gp-self.pf

    def display(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Gross Pay: {self.gp}")
        print(f"Net Pay: {self.np}")
        
    def __str__(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Gross Pay: {self.gp}")
        print(f"Net Pay: {self.np}")
        
        return ""



emp_name = input("Enter emp name: ")
emp_id = input("Enter emp ID: ")
bp = float(input("Enter Basic Pay:"))
hra = float(input("Enter house Rent allowance: "))
pf = float(input("Enter provident fund: "))

employee = Employee(emp_name, emp_id, bp,hra, pf)

  
  
# print(employee.__doc__)
# print(employee.__dir__)
# print(employee.__dict__)

print("Emplo"+employee.name)
employee.gross_salary()
# employee.display()

print(employee)
