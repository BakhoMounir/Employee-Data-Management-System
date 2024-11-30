import csv
import os

class Employee:
    # Initializes the Employee object with provided attributes.
    def __init__(self, employee_id, name, position, salary, email):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email


class EmployeeManager:
    # Initializes the EmployeeManager and creates the CSV file if it doesn't exist.
    def __init__(self):
        if not "employees.csv":  # This condition will always be false
            try:
                with open("employees.csv", "w", newline="") as emps:
                    emps_writer = csv.writer(emps, delimiter=",")
                    emps_writer.writerow(["employee_id", "name", "position", "salary", "email"])
            except FileNotFoundError:
                print("Can't create or find the file.")

    # Adds a new employee to the CSV file.
    def add_emp(self, employee_id, name, position, salary, email):
        new_emp = Employee(employee_id, name, position, salary, email)
        try:
            with open("employees.csv", "a", newline="") as emps:
                emps_writer = csv.writer(emps, delimiter=",")
                emps_writer.writerow([new_emp.employee_id, new_emp.name, new_emp.position, new_emp.salary, new_emp.email])
        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    # Updates an existing employee's details.
    def update_emp(self, employee_id, name=None, position=None, salary=None, email=None):
        try:
            with open("employees.csv", "r", newline="") as emps:
                emp_reader = csv.reader(emps)
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
                emp_writer = csv.writer(emps)
                emp_writer.writerows(emp_list)

        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    # Deletes an employee from the CSV file by employee_id.
    def delete_emp(self, employee_id):
        try:
            with open("employees.csv", "r", newline="") as emps:
                emp_reader = csv.reader(emps)
                emp_list = [row for row in emp_reader if row[0] != employee_id]

            with open("employees.csv", "w", newline="") as emps:
                emp_writer = csv.writer(emps)
                emp_writer.writerows(emp_list)

        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    # Searches for an employee by employee_id and displays their details.
    def search_emp(self, employee_id):
        try:
            with open("employees.csv", "r", newline="") as emps:
                emp_reader = csv.reader(emps)
                for emp in emp_reader:
                    if emp[0] == employee_id:
                        print(f"Employee details:\nID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}, Email: {emp[4]}")
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("The employees' file doesn't exist.")

    # Lists all employees by printing the entire content of the CSV file.
    def list_emps(self):
        try:
            with open("employees.csv", "r", newline="") as emps:
                print(emps.read())
        except FileNotFoundError:
            print("The employees' file doesn't exist.")

# Function to check if the password file is empty.
def emptyPassFile(file_name):
    password = open(file_name)
    if os.stat("password.txt").st_size == 0:  # Checks if file is empty by file size.
        return True
    else:
        return False

# Main function that drives the program.
def main():
    try:
        with open("password.txt", "r+") as password_file:
            if emptyPassFile("password.txt"):  # If file is empty, ask for password input.
                password = input("Enter the password (cannot be empty):\n")
                while password == "":  
                    password = input("Enter the password (cannot be empty):\n")
                
                password_file.write(password)
                manager_password = password  
            else:
                manager_password = password_file.readline().strip()  # Read the existing password.

    except FileNotFoundError:
        with open("password.txt", "w") as password_file:
            new_password = input("Set a new password: ")
            password_file.write(new_password)
            manager_password = new_password  # Set the new password

    while True:
        password = input("Enter the manager password: ")
        if password == manager_password:
            break  # Exit loop when correct password is entered
        print("Incorrect password. Try again.")  # If incorrect password, prompt again

    manager = EmployeeManager()  # Create the employee manager
    while True:
        #menu
        choice = input(
            "Select your choice:\n"
            "1- Add employee\n"
            "2- Update employee\n"
            "3- Delete employee\n"
            "4- Search for employee\n"
            "5- List employees\n"
            "6- Exit\n"
            "Your choice: "
        )
        
        if choice == "1":
            employee_id = input("Enter a unique Employee ID: ")

            with open("employees.csv", "r", newline="") as emps:
                for emp in emps:
                    emp_fields = emp.strip().split(",")  
                    while employee_id == emp_fields[0]:  # Check if Employee ID is unique
                        employee_id = input("This Employee ID is already taken. Enter a unique Employee ID: ")
                        emps.seek(0)
                        break  

            name = input("Enter Name: ")
            position = input("Enter Position: ")
            while True:
                try:
                    salary = int(input("Enter Salary: "))
                    if salary < 0:
                        continue
                    break
                except ValueError:
                    print("Enter a valid salary as a number.")
            while True:
                email = input("Enter Email: ")
                if "@" in email:
                    break
                print("Enter a valid email with '@'.")
            manager.add_emp(employee_id, name, position, salary, email)

        if choice == "2":
            employee_id = input("Enter Employee ID to update: ")
            
            # Ensure name is not left blank (must be entered)
            name = input("Enter new name (or leave blank to keep current): ")
            if not name:  # If no name is provided, keep the existing name.
                name = None

            # Ensure position is not left blank (must be entered)
            position = input("Enter new position (or leave blank to keep current): ")
            if not position:  # If no position is provided, keep the existing position.
                position = None

            # Ensure salary is an integer and not left blank
            while True:
                salary_input = input("Enter new salary (or leave blank to keep current): ")
                if salary_input:
                    try:
                        salary = int(salary_input)
                        if salary >= 0:
                            break
                        else:
                            print("Salary must be a positive number.")
                    except ValueError:
                        print("Please enter a valid integer for salary.")
                else:
                    salary = None  # If left blank, retain the existing salary
                    break

            # Ensure email contains '@' symbol before accepting input
            while True:
                email = input("Enter new email (or leave blank to keep current): ")
                if email and "@" in email:  # Validates that email contains '@'
                    break
                elif email == "":
                    email = None  # If left blank, retain the existing email
                    break
                else:
                    print("Please enter a valid email containing '@'.")

            manager.update_emp(employee_id, name, position, salary, email)


        elif choice == "3":
            employee_id = input("Enter Employee ID to delete: ")
            manager.delete_emp(employee_id)

        elif choice == "4":
            employee_id = input("Enter Employee ID to search: ")
            manager.search_emp(employee_id)

        elif choice == "5":
            manager.list_emps()

        elif choice == "6":
            print("Exiting...")
            break  # Exit the program

        else:
            print("Invalid choice. Try again.")  # Invalid choice handling

if __name__ == "__main__":
    main()  # Start the program when the script is run.
