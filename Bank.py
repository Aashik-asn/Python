class account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def show_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Balance: {self.balance}")
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited Rs.{amount}")
    def withdrawal(self,amount):
        if amount<=self.balance:
            print(f"Withdrawn Rs.{amount}")
            self.balance-=amount
        else:
            print("Insufficient Balance")
class savingsaccount(account):
    def __init__(self,name,balance,rate):
        super().__init__(name,balance)
        self.rate=rate
    def add_interest(self):
        interest=self.balance*self.rate/100
        self.balance+=interest
        print(f"Interest Rs.{interest} added")
acc=savingsaccount("Aashik",1000,5)

acc.show_balance()
acc.deposit(500)
acc.withdrawal(500)
acc.add_interest()
acc.show_balance()
