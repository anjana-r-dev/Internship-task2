#simple program on write , read, append mode of file i/o
def main():
    emp_name=input("enter name")
    age=input("enter age")
    record=f"\n{emp_name},{age}"# string manipulation it separates substring by adding ,

    return record   
if __name__=="__main__":
   record=main()

with open("Axcend.txt","a") as f:
    f.write(record)
#using dict to store the file returns
import os
def view_employee():

    if not os.path.exists("Axcend.txt"):
        print("No records found.")
        return
    print("\n--- Employee List ---")

    with open("Axcend.txt", "r") as f:
       
        lines = f.readlines()

    for line in lines:
        record= line.split(",")


        emp = {
            "emp_name": record[0],
            "age": record[1]
        }

        print(emp)
view_employee()
# List + File Read/Write Example
# Add employee (list → file)
def add_employee():
    with open("Axcend.txt", "a") as f:
        name = input("Enter name: ")
        age = input("Enter age: ")

        employee = [name, age]     # List

        record = ",".join(employee) + "\n"
        f.write(record)
        print(type(employee))
add_employee()
print("Employee added.")
