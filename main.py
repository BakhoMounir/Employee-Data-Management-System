from EmployeeManager import EmployeeManager
import Employee
from os import stat, path
from csv import writer
# Function to check if the password file is empty.
def emptyPassFile(file_name):
    password = open(file_name)
    #from OS library
    if stat("password.txt").st_size == 0:  
        return True
    else:
        return False


# Main function that drives the program.
def main():
    try:
        with open("password.txt", "r+") as password_file:
            if emptyPassFile("password.txt"): 
                password = input("Enter the password (cannot be empty):\n")
                while password == "":  
                    password = input("Enter the password (cannot be empty):\n")
                password_file.write(password)
                manager_password = password  
            else:
                manager_password = password_file.readline().strip()

    except FileNotFoundError:
        with open("password.txt", "w") as password_file:
            # Set the new password
            new_password = input("Set a new password: ")
            password_file.write(new_password)
            manager_password = new_password  

    attempts = 3
    while attempts > 0:
        entered_password = input("Enter the manager password (or type 'forgot' to exit):\n")
        if entered_password == "forgot":
            print("Exiting... Please contact support to reset the password.")
            exit()
        elif entered_password == manager_password:
            break
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempt(s) left.")

    if attempts == 0:
        print("Too many incorrect attempts. Exiting...")
        exit()

    manager = EmployeeManager()

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
            

            if not path.exists("employees.csv"):
                with open("employees.csv", "w", newline="") as f:
                    csv_writer = writer(f)
                    csv_writer.writerow(["employee_id", "name", "position", "salary", "email"])

            employee_id = input("Enter a unique Employee ID: ")
            with open("employees.csv", "r", newline="") as emps:
                existing_ids = {line.strip().split(",")[0] for line in emps if line.strip()}
            
            while employee_id in existing_ids:
                employee_id = input("This Employee ID is already taken. Enter a unique Employee ID: ")

            name = input("Enter Name: ")
            position = input("Enter Position: ")

            while True:
                try:
                    salary = int(input("Enter Salary: "))
                    if salary >= 0:
                        break
                except ValueError:
                    pass
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
            if not name:  
                name = None

            # Ensure position is not left blank (must be entered)
            position = input("Enter new position (or leave blank to keep current): ")
            if not position: 
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
                    salary = None  
                    break

            # Ensure email contains '@' symbol before accepting input
            while True:
                email = input("Enter new email (or leave blank to keep current): ")
                if email and "@" in email:  # Validates that email contains '@'
                    break
                elif email == "":
                    email = None  
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
# Exit the program
        elif choice == "6":
            print("Exiting...")
            break  

        else:
# Invalid choice handling

            print("Invalid choice. Try again.")  
if __name__ == "__main__":
    main() 
