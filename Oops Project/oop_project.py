from bank_accounts import *

Dave = BankAccount(1000, "Dave")
# Sara = BankAccount(2000, "Sara")

# Dave.getBalace()
# Sara.getBalace()


# Dave.deposite(3000)
# Dave.withDraw(1000)

# Dave.transfer(1500, Sara)

# Jim = InterestRewardAccount(1000, "Jim")

# Jim.getBalace()
# Jim.deposite(2000)

# Jim.transfer(500, Dave)

Blaze = SavingAccount(5000, 'Blaze')
Blaze.getBalace()
Blaze.deposite(1000)

Blaze.transfer(4000, Dave)
Blaze.getBalace()
