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

    def transfer(self, amount, account):
        try:
            print('\n***************\n\n Begining Transfer 🎉')
            self.vaiableTranscation(amount)
            self.withDraw(amount)
            account.deposite(amount)
            print('\n****\n\n Transfer Complete ✅')
        except BalanaceException as error:
            print(f'\n Transfer interrupted... {error} ❌')


class InterestRewardAccount(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + amount + (amount * 1.05)
        print(f'Deposite Compelete ****')
        self.getBalace()


class SavingAccount(InterestRewardAccount):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5

    def withDraw(self, amount):
        try:
            self.vaiableTranscation(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n WithDraw Complete")
        except BalanaceException as error:
            print(f'With Draw Interupted: {error}')
