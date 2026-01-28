import json
import os
import hashlib
from abc import ABC, abstractmethod
from datetime import datetime

DATA_FILE = "bank_data1.json"



class UserAlreadyExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class DataCorruptionError(Exception):
    pass

class User:
    def __init__(self, user_id, username, password, account_id,account_type):
        self.user_id = user_id
        self.username = username
        self._password = password
        self.account_id = account_id
        self.account_type=account_type

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self._password,
            self.account_type: self.account_id   
        }


class Account(ABC):
    def __init__(self, account_id, user_id,account_type, balance=0,):
        self.account_id = account_id
        self.user_id = user_id
        self._balance = balance
        self.account_type=account_type
       
    def to_dict(self):
           return {
            "user_id": self.user_id,
            "account_id": self.account_id,
            "account_type":self.account_type,   
            "balance": self._balance
        }

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount

    def get_balance(self):
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        pass



class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if self._balance - amount < 0:
            raise InsufficientFundsError("Insufficient balance.")
        self._balance -= amount



class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if self._balance - amount < -500:
            raise InsufficientFundsError("Overdraft limit exceeded.")
        self._balance -= amount


class Data_base:
       def __init__(self,file_path):
           self.file_path=file_path
           self._initialize_file()

       def _initialize_file(self):
             if not os.path.exists(self.file_path):
                  with open(self.file_path, "w") as file:
                         json.dump({"user ": [],"account":[] ,"transaction": []},file, indent=4)

        
       def load_data(self):
           try:
              with open(self.file_path, "r") as file:
                  return json.load(file)
           except json.JSONDecodeError:
                 raise DataCorruptionError("JSON data corrupted!")
           
       def save_data(self,data):
            with open("data.json", "w") as file:
                 json.dump(data, file, indent=4)

class Transaction:
    def __init__(self,account_id,account_type,user_id,transaction_type,amount ):
              self.account_id=account_id
              self.account_type=account_type
              self.user_id=user_id
              self.transaction_type=transaction_type
              self.amount=amount
              self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               
class Auth:
     def __init__(self,data_base):
          self.data_base=data_base

     def register_user(self,username,password, account_type):
          data= self.data_base.load_data
          for user in data["user"]:
               if user[username]== username:
                    raise  UserAlreadyExistsError ("this username already exist")
               hashed = hashlib.sha256(password.encode()).hexdigest()
               user_id = f"U{len(data["user"])}+1"


               create_account_obj=CreateAccount(self.data_base)
               account_id = create_account_obj.create_account(user_id, account_type)
               user=User(user_id=user_id,account_id=account_id,username=username,password=hashed)
               Data_base.save_data(self.data_base["user"].update(user.to_dict))
          
               
     def login_user(self,username,password):
          data= self.data_base.load_data
          for user in data["user"]:
               if user[username]== username :
                 hashed =  hashlib.sha256(password.encode()).hexdigest()
                 if user[password]==hashed:
                      return user
                 else:
                    raise InvalidCredentialsError("Wrong password.")
          raise InvalidCredentialsError("User not found.")
     
class CreateAccount:
     def __init__(self,data_base):
          self.data_base=data_base

     def create_account(self,user_id,account_type):
          data= self.data_base.load_data
          if account_type=="Saving":
               account_id = f"AS{len(data["account"])}+1"

          elif account_type=="Current":
               account_id = f"AC{len(data["account"])}+1"

          account = Account(account_id=account_id, user_id=user_id,account_type=account_type)
          Data_base.save_data(self.data_base["account"].update(account.to_dict))
          print (f"your account is created with {account_id} id")


        
          for user  in data["user"]:
              if user[user_id]in data["user"]:
                   user[account_id].append(account_type)
                   
            
               
     
class Bank:
        def __init__(self,data_base):
             self.data_base=data_base

        def get_account_data(self):
             data= self.data_base.load_data
             for account in data["account"]:
                  if account["account_type"]=="saving"  :
                       return( SavingsAccount(
                        iser_id=account["account_id"],
                        user_id= account["user_id"],
                            
                       ))
                  if account["account_type"]=="saving"  :
                       return( CurrentAccount(
     
                       ))
                  
        def deposite(self,amount,account_id):
            self.get_account_data()
            a=Account(account_id=account_id,user_id=user_id,account_type=account_type)
            def withdraw(self,amount):
                  def checkbalance(self,amount):
                       
             
                     jj=0


data_service=Data_base(DATA_FILE)
auth=Auth(data_service)
bank=Bank(data_service)


while True:
     
     print("1.Registeration \n2.Login \n3.Exit \n Enter Only Number")
     choose =int(input())
     if choose==1:
          username=input("Enter Username : ")
          password=input("Enter Password : ") 
          print("which account you want to make \n 1.Saving Account \n 2.Current Account")
          acc= int(input())
          if acc==1:
               account_type="Saving"
          elif acc==2:
               account_type="Current"
           
          auth.register_user(username=username,password=password,account_type=account_type)

     elif choose==1 :
          username=input("Enter Username : ")
          password=input("Enter Password : ") 

          user =auth.login_user(username=username,password=password)


           
          print("1.Deposite \n2.Withdraw \n3.Check Balance \n4.Transaction History \n5.Logout 6.create new account \n Enter Only Number")
          choose =int(input())
          
          if choose==1:
               amount= float(input("Enter Amount"))
               bank.deposite(user["account_id"],amount)
               



               
  
     
                  



             


             
     

                
          

           
           
           
               

        