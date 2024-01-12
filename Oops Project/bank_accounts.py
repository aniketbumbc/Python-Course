class BalanaceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount {self.name} created.")
        print(f"Balance =  ${self.balance:.2f}. \n")

    def getBalace(self):
        print(f"\n Account {self.name} and balance: ${self.balance}")

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposite completed")
        self.getBalace()

    def vaiableTranscation(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanaceException(f"Sorry, The account {
                self.name} has only a balance of ${self.balance:.2f}")

    def withDraw(self, amount):
        try:
            self.vaiableTranscation(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete successfully.")
            self.getBalace()
        except BalanaceException as error:
            print(f"\n Withdraw interrupted: {error}")
