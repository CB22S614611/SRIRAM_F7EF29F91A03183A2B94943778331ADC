class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def display_balance(self):
        return f"Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder}\nAccount Balance: ${self.__account_balance}"

# Create an instance of the BankAccount class
account = BankAccount("123456", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
print(account.deposit(500))  # Deposit $500
print(account.withdraw(200))  # Withdraw $200
print(account.display_balance())  # Display the account balance