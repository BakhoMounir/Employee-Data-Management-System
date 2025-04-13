from Employee import Employee
from csv import writer
class EmployeeManager:
    def __init__(self):
        if not "employees.csv":  
            try:
                with open("employees.csv", "w", newline="") as emps:
                    emps_writer = writer(emps, delimiter=",")
                    emps_writer.writerow(["employee_id", "name", "position", "salary", "email"])
            except FileNotFoundError:
                print("Can't create or find the file.")

    def add_emp(self, employee_id, name, position, salary, email):
        emp = Employee(employee_id, name, position, salary, email)
        emp.add_emp(employee_id, name, position, salary, email)

    def update_emp(self, employee_id, name=None, position=None, salary=None, email=None):
        emp = Employee(employee_id, name, position, salary, email)
        emp.update_emp(employee_id, name, position, salary, email)

    def delete_emp(self, employee_id):
        emp = Employee(employee_id, "", "", "", "")
        emp.delete_emp(employee_id)


    def search_emp(self, employee_id):
        emp = Employee(employee_id, "", "", "", "")
        emp.search_emp(employee_id)

    def list_emps(self):
        emp = Employee("", "", "", "", "")
        emp.list_emps()
