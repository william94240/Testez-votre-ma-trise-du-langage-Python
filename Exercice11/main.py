class BankAccount:
    """
    A class to represent a bank account
    """
    def __init__(self, account_holder: str, balance: float):
        """
        Constructor for the BankAccount class
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        """
        Method to deposit money into the account
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money in the account")

    def display_balance(self):
        """
        Method to display the account balance
        """
        return f"{self.account_holder} has {self.balance} in the account"

