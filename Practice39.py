# Create Account class with 2 attributes - blance and account no. 
# Crete methods for debit, credit and printing the balance.



class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self, amount):
        self.balance =- amount
        print("Rs.",amount,"was debited")
        print("Total Balance = ", self.get_balance)

    def creadit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance = ", self.get_balance)

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.creadit(2000)
acc1.creadit(100000)

