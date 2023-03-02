'''
import math

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def magnitude(self):
        mag = math.sqrt(self.x**2 + self.y**2)
        return(mag)
    
    def __lt__(self,vec2):
        return self.magnitude() < vec2.magnitude()
      
vector1 = (9,8)
vector2 = (3,4)
   
if vector1 < vector2 :
    print("True")
else:
    print("False")
'''

from abc import ABC, abstractmethod
class Banking:
    @abstractmethod
    def calculate(self):
        pass
    def update(self):
        pass
        
class Customer(Banking):
    def __init__(self,name,acc_type,balance):
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
        
    def calculate(self):
        if self.acc_type == 'Savings' :
            return (print(self.balance * 0.04))
        elif self.acc_type == 'Current':
            return (print(self.balance * 0.06))
        else :
            print("Invalid account")
            
    def update(self):
        if self.balance > 100000:
            self.balance += self.balance * 0.02
            print(f"Balance is above 1lakh : {self.balance}")
        else :
            print("Balance below 1lakh")
        
    def cal_show(self):
        print(f"Name:{self.name}")
        print(f"Account Type:{self.acc_type}")
        print(f"Balance:{self.balance}")
             
cust1 = Customer("Rudrani","Savings",1200000)
cust1.cal_show()
print(cust1.calculate())
print(cust1.update())
print("-------------------")
cust2 = Customer("Rudrani","Current",10000)
cust2.cal_show()
print(cust2.calculate())
print(cust2.update())

class Employee(Banking):
    def __init__(self,name,emp_class,basic_salary,years):
        self.name = name
        self.emp_class = emp_class
        self.salary = basic_salary
        self.years = years

    def calculate(self):
        if self.emp_class == 1 :
            da = 1.21 * self.salary
        elif self.emp_class == 2 :
            da = 1.15 * self.salary
        else :
            print("Invalid employee class")
            
        hra = 0.3 * self.salary
        gross_sal = self.salary + da + hra
        return gross_sal
        
        
    def update(self):
        if self.years > 15:
            gross_sal += 0.2 * gross_sal
            return print(f"Service above 15 years : {gross_sal}")
        else :
            print("Service below 15 years")
        
    def cal_show(self):
        print(f"Name:{self.name}")
        print(f"Employee Class:{self.emp_class}")
        print(f"Salary:{self.salary}")

print("-------------------")
emp1 = Employee("Rudrani",1,10000,10)
emp1.cal_show()
print(emp1.calculate())
print(emp1.update())

print("-------------------")
emp2 = Employee("Rudrani",2,10000,18)
emp2.cal_show()
print(emp2.calculate())
print(emp2.update())

