class Emp_personal_details:
    def __init__(self, emp_name, emp_designation):
        self.emp_name = emp_name
        self.emp_designation = emp_designation

class Emp_salary_details(Emp_personal_details):
    def __init__(self, emp_name, emp_designation, bp, hra, da, gp, np):
        super().__init__(emp_name, emp_designation)
        self.bp = bp
        self.hra = hra
        self.da = da
        self.gp = gp
        self.np = np

employee = Emp_salary_details("pratham", "Manager", 50000, 10000, 5000, 65000, 60000)


print(f"Name:{employee.emp_name}, Designation: {employee.emp_designation}")
print(f"Salary Details: BP: {employee.bp}, HRA: {employee.hra}, DA: {employee.da}, GP: {employee.gp}, NP: {employee.np}")
