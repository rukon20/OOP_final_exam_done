# m a r rukon

class Bank:
    Bank_balance = 500
    
    def __init__(self, name):
        self.name = name
        self.Total_loan = 0
        

class Person:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
       
class User(Person):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.balance = 0
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        Bank.Bank_balance += amount
        self.history.append(f"diposit = {amount}")
       
    def withdraw(self, amount):
        if Bank.Bank_balance == 0:
            print("the bank is bankrupt")
        else:
            if self.balance < amount:
                print("insufficient balance")
            else:
                print(f"take this {amount}")
                self.balance -= amount
                Bank.Bank_balance -= amount
                self.history.append(f"withdraw = {amount}")
                
    def take_loan(self, amount, bank):
        if Bank.Bank_balance == 0:
            print("the bank is bankrupt")
        else:
            if self.balance * 2 < amount:
                print("it is not possiable")
            else:
                print(f"you gave {amount}")
                self.balance += amount
                self.history.append(f"take loan = {amount}")
                bank.Bank_balance -= amount
                bank.Total_loan += amount
        
    def check_balance(self):
        print(f"your balance = {self.balance}")
    
    def show_history(self):
        if len(self.history) == 0:
            print("no history created")
        else:
            print(self.history)
    
    def transfar_money(self, obj, amount):
        if(self.balance < amount):
            print("insufficient balance")
        else:
            self.balance -= amount
            obj.balance += amount
            self.history.append(f"transfar balance = {amount}")
        
        
class Admin(Person):
    def __init__(self, email, password):
        super().__init__(email, password)
        
    def check_Bank_balance(self, bank):
        print(f"total available balance of the bank = {bank.Bank_balance}")
        
    def check_total_loan(self, bank):
        print(f"Bank has given total loan = {bank.Total_loan}")
        
    # def permission_for_loan(self, )
# -------------------------------------------------
# ------------ create objects ---------------------
bank = Bank("asa bank")
admin = Admin("admin1@gmail.com", 1234)
user = User("user1@gmail.com", 1234)
rajin = User("rajin@gmail.com", 1234)
# -------------------------------------------------
# ----------------- run operations ----------------
user.deposit(500)
user.check_balance()
user.transfar_money(rajin, 100)
rajin.check_balance()
user.check_balance()
admin.check_Bank_balance(bank)

user.take_loan(100, bank)

admin.check_Bank_balance(bank)
admin.check_total_loan(bank)

user.withdraw(100)
user.check_balance()
user.take_loan(1000, bank)
user.check_balance()
user.show_history()

