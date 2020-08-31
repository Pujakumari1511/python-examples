import datetime
import pytz


class Account:
    """ simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__transaction_list = [(Account._current_time(), balance, "opening balance")]
        print("Account created for " + self.__name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            # self.show_balance()
            self.__transaction_list.append((Account._current_time(), amount, "Deposited"))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_list.append((Account._current_time(), amount, "withdrawn"))
        else:
            print("The amount must be greater then zero and no more then your account balance")
        # self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount, tran_type in self.__transaction_list:
            print("{}: {} {} 0n {} (local time was {})".format(self.__name, amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    puja = Account("Puja", 0)

    puja.deposit(1000)
    puja.withdraw(500)
    puja.show_transactions()

    akash = Account("Akash", 800)
    akash.__balance = 200
    akash.deposit(100)
    akash.withdraw(100)
    akash.show_transactions()
    akash.show_balance()
    print(akash.__dict__)
    akash._Account_balance = 40
    akash.show_balance()
