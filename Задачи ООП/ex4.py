class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__interest_rate = 0
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Пополнение: + {amount}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"Снятие: - {amount}")
        else:
            print("Недостаточно средств на счете!")

    def add_interest(self):
        interest = self.__balance * (self.__interest_rate / 100)
        self.__balance += interest
        self.__transactions.append(f"Начисление процентов: +{interest}")

    def history(self):
        print("История операций:")
        for transaction in self.__transactions:
            print(transaction)

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.set_interest_rate(1.5)
account.deposit(1000)
account.withdraw(500)
account.add_interest()
account.history()
print("Баланс счёта:", account.get_balance())