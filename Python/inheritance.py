class Employee:
    def __init__(self, first_name, last_name, age, basic_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.basic_salary = basic_salary
        self.email = first_name + "." + last_name + "@gmail.com"

    def show(self):
        print(f"Name:{self.first_name}{self.last_name}")
        print(f"Age:{self.age}")
        print(f"Salary:{self.basic_salary}")
        print(f"Email:{self.email}")


class Developer(Employee):
    def __init__(self, first_name, last_name, age, basic_salary, lang):
        super().__init__(first_name, last_name, age, basic_salary)
        self.language = lang

    def show(self):
        super().show()
        print(f"Language:{self.language}")


class Manager(Employee):
    def __init__(self, first_name, last_name, age, basic_salary, subordinates):
        super().__init__(first_name, last_name, age, basic_salary)
        self.subordinates = subordinates

    def show(self):
        super().show()
        print(f"Subordinates:{self.subordinates}")

    def addEmp(self, newEmp):
        self.subordinates.append(newEmp)


emp1 = Manager("Rudrani", "Chavarkar", 30, 50000,
               ["Aarti", "Yojak", "Upadnya", ])

emp1.show()
emp1.addEmp("Chinmay")
print("\nAfter update of an emplyee: ")
emp1.show()
