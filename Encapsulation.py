class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number= account_number
        self.__balance=balance
        
    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        print( self.__balance)
    def deposite_amount(self,amount):
        if amount> 0 :
          self.__balance= self.__balance + amount
          print ("your amount deposite succesfully")
          self.get_balance
    def withdraw_amount(self  , amount):
        if amount <= self.__balance:
          self.__balance=self.__balance - amount
          print("your amount withdraw successfully")
          self.get_balance




obj=BankAccount(12345,10000)


obj.withdraw_amount(100)
obj.get_balance()
obj.deposite_amount(100)
obj.get_balance()
       
