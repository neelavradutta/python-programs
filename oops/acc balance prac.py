class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
        print("TRANSACTION FOR ACCOUNT NUMBER-",acc_no)
        
        
    def get_debit(self,amount):
        self.balance=self.balance-amount
        print("Amount of",amount,"is debited")
    
    def get_credit(self,amount):
        self.balance=self.balance+amount
        print("Amount of",amount,"is credited")
        
    def total_amount(self):
        print("The bank balance is",self.balance)
        
self=Account(10000,'5448F88F')
self.get_credit(500)
self.get_debit(150)
self.total_amount()


self=Account(1420,'122FGF1')
self.get_credit(500)
self.get_debit(150)
self.total_amount()

        