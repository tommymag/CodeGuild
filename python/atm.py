
# Let’s represent an ATM with a class containing two attributes: a balance and an
 # interest rate. A newly created account will default to a balance of 0 and an interest 
 # rate of 0.1%. Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won’t put the 
# account in the negative
# withdraw(amount) withdraws the amount from the account and returns it


class BankAccount:
    def __init__(self, balance=0):
        print("Welcome to Your Bank!")

        f_name = input("What is your first name?: ")
        l_name = input("Your last name?: ")
        balance = 0

        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.balance = balance
        self.setup()
        self.repl()

    def repl(self):
        print("Welcome to Your Bank!")

        valid_inputs = ['deposit', 'd', 'withdraw', 'w', 'check balance', 'b', 'history', 'h', 'exit', 'x']
        while True:
            while True:
                op = input("What would you like to do? \n((d)eposit, (w)ithdraw, check (b)alance, or e(x)it): ").strip().lower()
                if op in valid_inputs:
                    break

            if op in ['exit', 'x']:
                print('Goodbye!')
                break

            elif op in ['deposit', 'd', 'withdraw', 'w']:
                while True:
                    op = 'deposit' if op.startswith('d') else 'withdraw'
                    try:
                        amount = int(input(f"How much would you like to {op}: ").strip('$'))
                        break
                    except ValueError:
                        print('Invalid input.')

                if op == 'deposit':
                    self.deposit(amount)

                elif op == 'withdraw':
                        if self.check_withdrawal(amount) is True:
                            # yesno = ['yes'. 'y', 'no', 'n']
                            while True:
                                tw = input("Good news! You have enough money! Would you like to complete the withdrawal?\n((y)es or (n)o: ").strip().lower()
                                if tw in [y, Y, yes, Yes]:
                                    withdraw()
                                    print("Here is your " + str(amount) + " dollars. You have " + str(self.balance) + " dollars remaining.")
                                    break
                                elif tw in [n, N, no, No]:
                                    print("withdrawal cancelled")
                                    break
                        else:
                            print("Sorry, you currently don't have enough funds for this transaction.")
                            

            elif op in ['check balance', 'b']:
                    self.check_balance()

    def setup(self):
        print('You have created an account for {}.'.format(self.full_name))

    def check_balance(self):
        print('Your balance is {}.'.format(self.balance))

    def deposit(self, amount):
       self.balance += amount 

    def check_withdrawal(self, amount):
        return self.balance > amount

    def withdraw(self, amount):
        self.balance -= amount
        return amount


# account1 = BankAccount('Chris', 'Jones',6000)
# account2 = BankAccount('No', 'Name',50000)
my_account = BankAccount()