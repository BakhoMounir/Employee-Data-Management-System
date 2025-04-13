from csv import reader,writer

class Employee:
   
    def __init__(self, employee_id, name, position, salary, email):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email


    
    def add_emp(self, employee_id, name, position, salary, email):
        new_emp = Employee(employee_id, name, position, salary, email)
        try:
            with open("employees.csv", "a", newline="") as emps:
                emps_writer = writer(emps, delimiter=",")
                emps_writer.writerow([new_emp.employee_id, new_emp.name, new_emp.position, new_emp.salary, new_emp.email])
        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    
    def update_emp(self, employee_id, name=None, position=None, salary=None, email=None):
        try:
            with open("employees.csv", "r", newline="") as emps:
                emp_reader = reader(emps)
                emp_list = [row for row in emp_reader]

            for emp in emp_list:
                if emp[0] == employee_id:
                    if name:
                        emp[1] = name
                    if position:
                        emp[2] = position
                    if salary:
                        emp[3] = salary
                    if email:
                        emp[4] = email

            with open("employees.csv", "w", newline="") as emps:
                emp_writer = writer(emps)
                emp_writer.writerows(emp_list)

        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    
    def delete_emp(self, employee_id):
        try:
            with open("employees.csv", "r", newline="") as emps:
                emp_reader = reader(emps)
                emp_list = [row for row in emp_reader if row[0] != employee_id]

            with open("employees.csv", "w", newline="") as emps:
                emp_writer = writer(emps)
                emp_writer.writerows(emp_list)

        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    
    def search_emp(self, employee_id):
        try:
            with open("employees.csv", "r", newline="") as emps:
                emp_reader = reader(emps)
                for emp in emp_reader:
                    if emp[0] == employee_id:
                        print(f"Employee details:\nID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}, Email: {emp[4]}")
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    
    def list_emps(self):
        try:
            with open("employees.csv", "r", newline="") as emps:
                print(emps.read())
        except FileNotFoundError:
            print("The employees' file doesn't exist.")

