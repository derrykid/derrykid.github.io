class BankAccount(object):
    """
    Bank account Class for deposit and withdrawl
    """
    defaultAccNumber = 1
    
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough amount")
        else:
            self.balance = self.balance - amount
            print(f"amount withdraw {amount}")
            
    def getBalance(self):
        return self.balance
    
if __name__ == '__main__':
    myObj = BankAccount("Derry", 1000)
    myObj.deposit(500)
    print(myObj.getBalance())
    
    myObj.withdraw(1200)
    print(myObj.getBalance())