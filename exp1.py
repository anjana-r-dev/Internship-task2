#Adding employee info
#import os
def add_employee_details():
    try:
        with open("Employee_details.txt","r") as f:
            print("File opened successfully")
            lines=f.readlines()
    except FileNotFoundError:
            print("File not found")
            lines=[]
    emp_id=input("Enter Employee ID: ")
    #check for duplicate emp_id
    for line in lines:
        data=line.strip().split(",")
        if len(data) != 4:    # skip bad lines
            continue

        if data[1]==emp_id:
             print("Employee ID already exists!")
             return
    emp_name=input("Enter Employee Name: ")
    emp_dept=input("Enter Employee Department: ")
    emp_salary=input("Enter Employee Salary: ")
            
    Employee=f'{emp_name},{emp_id},{emp_dept},{emp_salary}\n'
    with open("Employee_details.txt","a") as f:
        f.write(str(Employee))
# for search function first we need to convert csv-->list by load function
def load_employee_details():
    employees=[]
    try:
        with open("Employee_details.txt","r") as f:
            lines=f.readlines()
            for line in lines:
                data=line.strip().split(",")
                if len(data) != 4:
                    continue
                employee={
                    "name":data[0],
                    "id":data[1],
                    "department":data[2],
                    "salary":data[3]
                }
                employees.append(employee)
    except FileNotFoundError:
        pass
    return employees
# search employee by id
def search_employee_by_id():
    employees = load_employee_details()
    emp_id = input("Enter Employee ID to search: ")
    if len(employees) == 0:
        print("No Employees Found")
    choice =input("Do you want to add employee details? (yes/no) :")

    if choice.lower() == "yes":
        add_employee_details()
        return
    if choice.lower() == "no":
        return
    for employee in employees:

        if employee["id"] == emp_id:

            display_employee(employee)
        else:
            choice =input("Do you want to add employee details? (yes/no) :")

            if choice.lower() == "yes":
                add_employee_details()
                return
            if choice.lower() == "no":
                return
def display_employee(employee):
    print("Employee Details:")
    print(f"Name: {employee['name']}")
    print(f"ID: {employee['id']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: {employee['salary']}")


def main():
    print("1. Add Employee Details")
    print("2. Search Employee Details")
    print("3.exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee_details()
    elif choice == "2":
        search_employee_by_id()
    else:
        print("Thank you!")
        return
    return
if __name__ == "__main__":
    main()