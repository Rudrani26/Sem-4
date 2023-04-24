class BankAccount:
    def __init__(self, name, accountNumber, dateofOpening, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.dateofOpening = dateofOpening
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after Deposit : ", self.balance)

    def withdraw(self, amount):
        if self.balance <= 10000:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Balance after Withdrawal : ", self.balance)

    def checkBalance(self):
        print("Bank Balance : ", self.balance)

    def printbankDetails(self):
        print("Name             : ", self.name)
        print("Account Number   : ", self.accountNumber)
        print("Date of Openeing : ", self.dateofOpening)
        print("Bank Balance     : ", self.balance)


acc1 = BankAccount("Rudrani", 92645, "26-05-2003", 2000)
acc2 = BankAccount("Upadnya", 98755, "09-06-1997", 26000)
acc3 = BankAccount("Aarti", 90874, "14-05-1971", 520000)
acc4 = BankAccount("Yojak", 99127, "05-12-1964", 59000)

print("Customer Details ======>")
acc1.printbankDetails()
acc2.printbankDetails()
acc3.printbankDetails()
acc4.printbankDetails()

acc1.withdraw(1000)
acc2.deposit(20500)
acc3.withdraw(7000)
acc4.deposit(9000)

print("Updated Customer Details ======>")
acc1.printbankDetails()
acc2.printbankDetails()
acc3.printbankDetails()
acc4.printbankDetails()
