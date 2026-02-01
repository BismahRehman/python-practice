from abc import ABC, abstractmethod
import json
import hashlib
import os

file='data.json'

class UserAlreadyExistsError(Exception):
    pass

class UserCannotExistsError(Exception):
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
    def __init__(self,username,hashed_password,user_id):
        self.username=username
        self.hashed_password=hashed_password
        self.user_id=user_id

    def to_dic(self):
        return{
            'user_id':self.user_id,
            'username':self.username,
            'password':self.hashed_password,
            "accounts": []
        }


class Account(ABC):
 def __init__(self,user_id,account_id,account_type,balance):
        self.user_id=user_id
        self.account_type=account_type
        self.account_id=account_id
        self._balance=balance


 def deposit(self,amount):
    print ("hi")
    if amount<0:
         raise InvalidAmountError ("amount must be greater then zero")
    self._balance+=amount
    
    
 @property
 def get_balance(self):
     return self._balance

 @abstractmethod
 def withdraw(self,amount):
     pass

class SavingAccount(Account):
    def withdraw(self,amount):
        if amount<0:
           raise InvalidAmountError ("amount must be greater then zero")
        if self._balance<amount:
           raise  InsufficientFundsError ("invalid Transaction")
        self._balance-=amount
        return True

class CurrentAccount(Account):
    def withdraw(self,amount):
        if amount<0:
             raise InvalidAmountError ("amount must be greater then zero")
        if (self._balance-500)<amount:
            raise  InsufficientFundsError ("invalid Transaction")
        self._balance-=amount
        return True



class Transaction:
    def __init__(self,user_id,account_id,amount,transaction_type):
        self.user_id=user_id
        self.account_id=account_id
        self.amount=amount
        self.transaction_type=transaction_type

    def to_dic(self):
        return {
            "user_id":self.user_id,
            "account_id":self.account_id,
            "amount":self.amount,
            "transaction_type":self.transaction_type
        }


class CreateAccount:
    def __init__(self,user_id,account_id,account_type,balance):
        self.user_id=user_id
        self.account_id=account_id
        self.account_type=account_type
        self.balance=balance

    def to_dic(self):
        return {
            "user_id": self.user_id,
            "account_id": self.account_id,
            "account_type": self.account_type,
            "balance": self.balance
        }
        
class DataBase:
    def __init__(self,file_path):
        self.file_path=file_path
        self._initialize()

    def _initialize(self):
        if not  os.path.exists(self.file_path):
            with open (self.file_path,"w") as f:
                json.dump({"user" :[],"account":[],"transaction":[]},f)
          

    def load_data(self):
        try:
         with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise DataCorruptionError("JSON data corrupted!")
           
    
    def save_data(self, data):
        with open (self.file_path,"w") as f:
            json.dump(data, f, indent=4)

class Bank:
    def __init__(self,data_file):
        self.data_file=data_file

    def register_user(self,username,password,account_type):
        data = self.data_file.load_data()
        for user  in data['user']:
          
          if user["username"]==username:
            raise UserAlreadyExistsError ("user already exist")
        user_id = f"U{len(data['user']) + 1}"   
        hashed= hashlib.sha256(password.encode()).hexdigest()
        user= User(username=username,hashed_password=hashed,user_id=user_id)
        data['user'].append(user.to_dic())
        self.data_file.save_data(data)
        print(data['user'])
        self.createaccount(user_id=user_id,account_type=account_type)
    

    def createaccount(self,user_id,account_type,balance=0):
            data = self.data_file.load_data()
            for user in data['user']:
               if user['user_id'] != user_id:
                   raise UserCannotExistsError("user cannot exist")
               if account_type=="Saving":
                       account_id=f"AS{len(data['account'])+1}"
               elif account_type=="Current":
                       account_id=f"AC{len(data['account'])+1}"
            acc=CreateAccount(user_id=user_id,account_id=account_id,account_type=account_type,balance=balance)
            data['account'].append(acc.to_dic())
            user['accounts'].append({
                   "account_id": account_id,
                   "account_type": account_type
                })
            self.data_file.save_data(data)

         

    def login(self,username,password):
        data = self.data_file.load_data()
        hashed= hashlib.sha256(password.encode()).hexdigest()
        for user in data["user"]:
            if user["username"]==username or user["password"]==hashed:
              return user
            else :
                raise  InvalidCredentialsError("invalid username or password")
            
    def get_account_data(self,account_id):
        data = self.data_file.load_data()
        for acc in data["account"]:
            if acc["account_id"]==account_id:
                if acc["account_type"]=="Saving":
                    return  SavingAccount(
                        user_id=acc["user_id"],
                        account_id=acc["account_id"],
                        account_type=acc["account_type"],
                        balance=acc["balance"]  
                    )
                if acc["account_type"]=="Current":
                    return  SavingAccount(
                        user_id=acc["user_id"],
                        account_id=acc["account_id"],
                        account_type=acc["account_type"],
                        balance=acc["balance"]  
                    )

    def deposit(self,amount,account_id,user_id):
        data = self.data_file.load_data()
        for user in data["user"]:
            if user["user_id"]==user_id:
                for  acc in user['accounts']:
                      if account_id not in acc['account_id']:
                          print(user['accounts'])
                account=self.get_account_data(account_id)
                account.deposit(amount)
                for acct in data['account']:
                    if acct['account_id']==account_id:
                      acct["balance"] = account.get_balance

                txt=Transaction(user_id=user_id,account_id=account_id,amount=amount,transaction_type="deposit")
                data['transaction'].append(txt.to_dic())
                self.data_file.save_data(data)

            

    def withdraw(self,amount,account_id,user_id):
        data = self.data_file.load_data()
        for user in data["user"]:
            if user["user_id"]==user_id:
                for  acc in user['accounts']:
                      if acc['account_id']==account_id:
                       print(user['accounts'])
                account=self.get_account_data(account_id)
                account.withdraw(amount) 
                for acct in data['account']:
                     if acct['account_id']==account_id:
                       acct["balance"] = account.get_balance

                txt=Transaction(user_id=user_id,account_id=account_id,amount=amount,transaction_type="withdraw")
                data['transaction'].append(txt.to_dic())
                self.data_file.save_data(data)
    


    def get_balance(self,account_id):
        data = self.data_file.load_data()
        for acc in data["account"]:
            if acc["account_id"]==account_id:
                user=self.get_account_data(account_id)
                print(user.get_balance)

    def txt_history(self,account_id):
        data = self.data_file.load_data()
        for trans in data["transaction"]:
            if trans['account_id']==account_id:
                print (trans)

                


database=DataBase(file)
bank=Bank(database)


while True:
    print("Enter only number \n1.Register \n2.Login \n3.Exist")
    choose= int(input())
    if choose==1:
        username=input("Enter username ")
        password=input("Enter password ")
        print ("1.Saving Account \n2.Current Account")
        account=int(input())
        if account==1:
            account_type="Saving"
        if account==2:
            account_type="Current"
        try:
         bank.register_user(username,password,account_type)
        except  UserAlreadyExistsError as e:
            print(e)

    elif choose==2:
        username=input("Enter username ")
        password=input("Enter password ")
        user=bank.login(username,password)
        print (user)
        while True:
             print("Enter only number \n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Check Transaction History \n5.Create Account \n6.Logout")
             choose=int(input())
             if choose==1:
                 amount=int(input("Enter Amount "))
                 account_id=input("Enter Account ID ")
                 try:
                  bank.deposit(amount,account_id,user['user_id'])
                 except  UserAlreadyExistsError as e:
                  print(e)
                 
                    

             elif choose==2:
                 amount=int(input("Enter Amount "))
                 account_id=input("Enter Account ID ")
                 try:
                   bank.withdraw(amount,account_id,user['user_id'])
                 except  UserAlreadyExistsError as e:
                  print(e)

             elif choose==3:
                 account_id=input("Enter Account ID ")
                 bank.get_balance(account_id)

             elif choose==4:
                 account_id=input("Enter Account ID ")
                 bank.txt_history(account_id)

             elif choose==5:
                 user_id=input("Enter User Id ")
                 print ("1.Saving Account \n2.Current Account ")
                 account=int(input())
                 if account==1:
                    account_type="Saving"
                 if account==2:
                    account_type="Current"
                 bank.register_user(username,password,account_type)

             elif choose==5:
                 break
               
             else:
                 print ("Enter invalid number")
                 

    elif choose==3:
        break

    else:
         print ("Enter invalid number")

