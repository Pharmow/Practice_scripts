# Employee Management System

employee_records = {}

def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter employee department: ")
    salary = input("Enter employee salary: ")
    employee_records[emp_id] = {"name": name, "department": department, "salary": salary}
    print("Employee record added successfully.")

def view_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id in employee_records:
        print("Employee ID:", emp_id)
        print("Name:", employee_records[emp_id]["name"])
        print("Department:", employee_records[emp_id]["department"])
        print("Salary:", employee_records[emp_id]["salary"])
    else:
        print("Employee record not found.")

def delete_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id in employee_records:
        del employee_records[emp_id]
        print("Employee record deleted successfully.")
    else:
        print("Employee record not found.")

while True:
    print("\nEmployee Management System\n")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Delete Employee")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid choice (1-4).")
