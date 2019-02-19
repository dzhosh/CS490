class Employee:
    employee_count = 0
    total_salaries = 0

    @staticmethod
    def average_salary():
        return Employee.total_salaries / Employee.employee_count

    def __init__(self,aname,afamily,asalary,adepartment):
        name = aname
        family = afamily
        salary = asalary
        department = adepartment
        Employee.employee_count += 1
        Employee.total_salaries += asalary


class FullTimeEmployee(Employee):
    def __init__(self,aname,afamily,asalary,adepartment):
        Employee.__init__(self,aname,afamily,asalary,adepartment)


emp1 = Employee("John", "Smith", 20000, "Sales")
emp2 = FullTimeEmployee("Alice","Meyers", 40000, "Management")
emp3 = Employee("Jacob", "Doe", 30000, "Development")

print(Employee.average_salary())
print(Employee.employee_count)