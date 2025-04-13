👨‍💼 Employee Management System 👩‍💼

This is a simple Employee Management System built with Python 🐍. It helps you manage employee records through a user-friendly menu interface. All employee data is saved in a CSV file 📁 called employees.csv, which is automatically created if it doesn't already exist 🛠️.

✨ Features:

✅ Add Employee – Enter employee ID, name, position, salary, and email
✏️ Update Employee – Modify details of an existing employee
❌ Delete Employee – Remove an employee using their ID
🔍 Search Employee – View details of a specific employee
📋 List Employees – Display all employee records
🚪 Exit – Quit the program

⚙️ How It Works:

Records are stored in employees.csv 📄.

The file is created automatically if it doesn't exist 🆕.

All operations interact with this file to keep data persistent 🔄.

📁 Project Structure:

EmployeeManagementSystem/
├── employees.csv ➡️ Automatically created to store data
├── main.py ➡️ Main Python script
└── README ➡️ Project documentation

🧰 Requirements:

Python 3.x 🐍

No external libraries needed! Just the built-in csv module

▶️ Running the Project:

Open your terminal 💻

Navigate to the project directory 📂

Run the script:

python main.py

🧭 Menu Options:

Select your choice:
1️⃣ Add employee
2️⃣ Update employee
3️⃣ Delete employee
4️⃣ Search for employee
5️⃣ List employees
6️⃣ Exit

Just enter the number of your choice and follow the prompts!

📌 Example CSV Content:

graphql
Copy
Edit
1,John Doe,Manager,50000,john@example.com  
2,Jane Smith,Analyst,45000,jane@example.com
🛡️ Error Handling:

Missing file? No worries, it’ll be created 👍

Searching for a non-existent employee? The system lets you know!

Everything runs smoothly with built-in exception handling ⚠️

🆓 License:

This project is free and open source. Use it, improve it, and have fun! 🎉
