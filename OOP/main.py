class Employee:
    def __init__(self):
        self.names = input("Enter Employee Name: ")
        self.designation = input("Enter Employee Department: ")
        self.department = input("Enter Employee Department: ")

    def display(self):
        print(f"Employee Name is : {self.names}")
        print(f"Employee designation is : {self.designation}")
        print(f"Employee department is : {self.department}")

    def bonus(self):
        if  self.department.lower() == "IT":
            print("Bonus")
        else:
            print("No bonus")

#
# n = input("Enter Employee Name: ")
# d = input("Enter Employee Department: ")
# des = input("Enter Employee Department: ")

emp1 = Employee()
emp1.display()

