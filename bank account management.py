class Bank:
    def __init__(self, account_no, amount):
        self.account_no = account_no
        self.amount = amount

    def current_amount(self):
        return self.amount

    def deposit(self):
        deposited_value = int(input("enter the deposited amount: "))
        self.amount = self.amount + deposited_value
        return self.amount

    def withdrawl(self):
        withdrawl_value = int(input("enter the withdwarlal amount: "))
        self.amount = self.amount - withdrawl_value
        return self.amount

acc = int(input("enter the account number: "))
money = int(input("enter the amount: "))
z = Bank(acc ,money)
print("1.Current balance \n 2. Deposit \n 3.Withdrawl")
c=1
while(c==1):
    i = int(input("enter your choice: "))
    if i==1:
        print("Current balance of",acc,"is",z.current_amount())
    elif i == 2:
        print("After deposit amount: ",z.deposit())
    elif i == 3:
        print("After Withdrawl amount: ",z.withdrawl())
    else:
        print("wrong choice......")
    c = int(input("Enter 1 for more changes"))
#print("account number: ", acc, "balance: ",money )
        
