# Bank Account: BankAccount class banao. Deposit, withdraw aur balance check karne ke methods implement karo. 

class BankAccount :

  # constructor
  def __init__(self, name, balance):
    self.name  = name
    self.balance = balance

  # Display Profile
  def profileDisplay(self) :
    print("Account Holder Name : ",self.name)
    print("Initial Balance : ",self.balance)
  
  #  Deposite function
  def deposite(self) :
    amount = int(input("Enter an amount to Deposite : "))
    if amount > 0 :
      self.balance += amount
      print("Deposited : ",amount)
    else :
      print("Invalid amount")

  # Withdraw
  def withdraw(self) :
    amount = int(input("Enter an amount to Withdraw : "))
    if amount > 0  and amount <= self.balance :
      self.balance -= amount
      print("Withdrawn : ",amount)
    elif amount > self.balance :
      print("Insufficient Balance")
    else :
      print("Invalid amount")
      
  # Display balance
  def displayBalance(self):
     print("Final Balance : ",self.balance)


BankAccount1 = BankAccount("Ankush", 1000)
BankAccount1.profileDisplay()
BankAccount1.deposite()
BankAccount1.withdraw()
BankAccount1.displayBalance()