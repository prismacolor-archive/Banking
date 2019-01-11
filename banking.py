class BankAccount():
    
    def __init__ (self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self):
        amount = float(input("How much would you like to deposit?"))
        self.balance = self.balance + amount
        print("Your new balance is {}".format(self.balance))
        
    def withdrawal(self):
        amount = float(input("How much would you like to deposit?"))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount
            print("Your new balance is {}".format(self.balance))
            
    def print_balance(self, balance):
        raise NotImplementedError ("Please define function.") 
            
    def __str__(self):
        raise NotImplementedError ("Please define function")


class CheckingAccount(BankAccount):
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def transfer(self, balance, amount, savings):
        balance = balance - amount
        savings.balance = savings.balance + amount
        print("Your new checking account balance is {}".format(balance))
        
    def __str__(self):
        return f"Account Holder:{self.owner} \n Current Checking Account Balance:{self.balance}"


checking = CheckingAccount("Gandalf", 500)


class SavingsAccount(BankAccount):
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def transfer(self, balance, amount, checking):
        balance = balance - amount
        checking.balance = checking.balance + amount
        print("Your new savings account balance is {}".format(balance))
        
    def __str__(self):
        return f"Account Holder:{self.owner} \n Current Savings Account Balance:{self.balance}"

savings = SavingsAccount("Gandalf", 1500)