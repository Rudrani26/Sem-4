class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def cal_Salary(self, salary, hoursWorked):
        overtime = 0
        if hoursWorked > 50:
            overtime = hoursWorked - 50

        overtimeAmount = overtime * (salary/50)
        self.salary = salary + overtimeAmount

    def assign_Department(self, department):
        self.department = department

    def print_employee_details(self):
        print("ID         :", self.id)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Salary     :", self.salary)


E1 = Employee(1, "Rudrani", "Human Resoruce", 20000)
E2 = Employee(2, "Upadnya", "Java Team", 40000)
E3 = Employee(3, "Aarti", "Sales", 30000)
E4 = Employee(4, "Yojak", "Design", 50000)

print("<---- Original Employee Details --->")

E1.print_employee_details()
E2.print_employee_details()
E3.print_employee_details()
E4.print_employee_details()

E1.assign_Department("Sexy")
E3.cal_Salary(30000, 78)

print("<--- Updated Employee Details --->")

E1.print_employee_details()
E2.print_employee_details()
E3.print_employee_details()
E4.print_employee_details()
