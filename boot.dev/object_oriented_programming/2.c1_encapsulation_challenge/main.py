"""
PROTECTING BANK INFORMATION
You are a software developer who has been hired by a small community bank to help them automate their banking operations. The bank currently uses paper-based record-keeping and manual calculations, which makes it difficult to keep track of account balances and transactions.

CHALLENGE
Complete the BankAccount class.

CONSTRUCTOR
Initialize private instance variables __account_number to account_number, and __balance to initial_balance.

PUBLIC GETTERS
Define getter methods get_account_number, and get_balance that return the values of the private variables.

DEPOSIT METHOD
It should accept an amount as input and add it to the account balance.

If the deposit amount isn't positive, it should raise a ValueError exception with the message Cannot deposit zero or negative funds. Otherwise, it should add the amount to the balance.

WITHDRAW METHOD
It should accept an amount and check if there is enough money in the account for the withdrawal.

If the withdrawal amount isn't positive, it should raise a ValueError exception with the message Cannot withdraw zero or negative funds. Then, if there are not enough funds it should raise a ValueError exception with the message Insufficient funds. Otherwise, it should deduct the amount from the balance.
"""


class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw zero or negative funds")

        if self.__balance < amount:
            raise ValueError("Insufficient funds")

        self.__balance -= amount
