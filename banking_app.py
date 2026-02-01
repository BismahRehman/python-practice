from abc import ABC, abstractmethod
import json
import hashlib
import os

file='data.json'

# ====================================
# create custom error handling classes
# ====================================

class UserAlreadyExistsError(Exception):
    pass

class UserCannotExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass
class InvalidAccountError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class DataCorruptionError(Exception):
    pass

# ====================================
# create User classes
# ====================================
class User:
    def __init__(self,username,hashed_password,user_id):
        self.username=username
        self.hashed_password=hashed_password
        self.user_id=user_id

    def to_dic(self):  #this method is store user data in user dictionary  in json file
        return{
            'user_id':self.user_id,
            'username':self.username,
            'password':self.hashed_password,
            "accounts": []
        }

# =========================
# create account classes
# ========================
class Account(ABC):   # this class is used to make different operation on account
 def __init__(self,user_id,account_id,account_type,balance):
        self.user_id=user_id
        self.account_type=account_type
        self.account_id=account_id
        self._balance=balance


 def deposit(self,amount):
     if amount<0:  # if amount less than zero then raise expectation 
         raise InvalidAmountError ("amount must be greater then zero")

     
     self._balance+=amount
     return True
    
    
 @property  # property method  method to attribute
 def get_balance(self):
     return self._balance

 @abstractmethod # absstraction method must used in child class using method overriding
 def withdraw(self,amount):
     pass
# ====================================
# create saving account sub classes
# ====================================
class SavingAccount(Account): # make a subclass of account
    def withdraw(self,amount):
     
        if amount<0:    # if amount less than zero then raise expectation 
           raise InvalidAmountError ("amount must be greater then zero")
      
        if self._balance<amount:   # if amount greater than current balance then raise expectation 
           raise  InsufficientFundsError ("invalid Transaction")
      
        self._balance-=amount

        return True
      
        

# ====================================
# create current account sub classes
# ====================================
class CurrentAccount(Account):
    def withdraw(self,amount):
      
        if amount<0:    # if amount less than zero then raise expectation 
             raise InvalidAmountError ("amount must be greater then zero")
      
        if (self._balance-500)<amount:  # if amount limit exceeded, then raise expectation 
            raise  InsufficientFundsError ("invalid Transaction")
    
        self._balance-=amount

        return True
      
        


# ====================================
# create Transaction classes
# ====================================
class Transaction:
    def __init__(self,user_id,account_id,amount,transaction_type):
        self.user_id=user_id
        self.account_id=account_id
        self.amount=amount
        self.transaction_type=transaction_type

    def to_dic(self):   #this method is store transaction data in transaction dictionary  in json file
        return {
            "user_id":self.user_id,
            "account_id":self.account_id,
            "amount":self.amount,
            "transaction_type":self.transaction_type
        }

# ====================================
# create create account classes  
# ====================================
class CreateAccount:
    def __init__(self,user_id,account_id,account_type,balance):
        self.user_id=user_id
        self.account_id=account_id
        self.account_type=account_type
        self.balance=balance

    def to_dic(self):     #this method is store account data in account dictionary  in json file
        return {
            "user_id": self.user_id,
            "account_id": self.account_id,
            "account_type": self.account_type,
            "balance": self.balance
        }
# ====================================
# create Database classes
# ====================================     
class DataBase:
    def __init__(self,file_path):
        self.file_path=file_path
        self._initialize() # this call  _initialize(self) method

    def _initialize(self):
        if not  os.path.exists(self.file_path):
            with open (self.file_path,"w") as f:
                json.dump({"user" :[],"account":[],"transaction":[]},f) # make three type of list in json file
          

    def load_data(self):
        try:
         with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError: # if file can't load then raise expection
            raise DataCorruptionError("JSON data corrupted!")
           
    
    def save_data(self, data):  # used for save data
        with open (self.file_path,"w") as f:
            json.dump(data, f, indent=4)

# ====================================
# create Bank classes
# ====================================
class Bank:
    def __init__(self,data_file):
        self.data_file=data_file

      
      # --------  register_user  ---------
    def register_user(self,username,password,account_type): # make method user registration 
        data = self.data_file.load_data() # load json file
        for user  in data['user']:  # all user  account one by one in user list in json file
          
          if user["username"]==username: # check username  if not exist then raise expection
            raise UserAlreadyExistsError ("user already exist")
        user_id = f"U{len(data['user']) + 1}"    # make user_id
        hashed= hashlib.sha256(password.encode()).hexdigest() # password convert in to hashed
        user= User(username=username,hashed_password=hashed,user_id=user_id) #make a user class object 
        data['user'].append(user.to_dic()) # add user data in json file in user list
        self.data_file.save_data(data) # save file 
        print(f"you are register with {user_id} id")
        self.createaccount(user_id=user_id,account_type=account_type) # call create account function
        print("Registered successfull")
    
         # --------  createaccount  ---------
    def createaccount(self,user_id,account_type,balance=0):
            
            data = self.data_file.load_data()  # load json file
            for user in data['user']:  # all user  account one by one in user list in json file
                if user_id == user['user_id'] :  # check user id match or not
                  # check selected account type
                  if account_type=="Saving":
                       account_id=f"AS{len(data['account'])+1}"
                  elif account_type=="Current":
                       account_id=f"AC{len(data['account'])+1}"

                  acc=CreateAccount(user_id=user_id,account_id=account_id,account_type=account_type,balance=balance) # make create account object
                  data['account'].append(acc.to_dic()) # add account data to account

                  # add account data in user info
                  user['accounts'].append({
                   "account_id": account_id,
                   "account_type": account_type
                  })

                  self.data_file.save_data(data) # save data 
                  print(f"you are account created  with {account_id} id")



  # --------  login  ---------
    def login(self,username,password):
        data = self.data_file.load_data() # load data
        hashed= hashlib.sha256(password.encode()).hexdigest()  # convert password to hashed 

        for user in data["user"] :  # all user  account one by one in user list in json file
          if user["username"]==username and user["password"]==hashed: # match password and hashed
             print("Login Successfully ")
             return user  
        raise  InvalidCredentialsError("invalid username or password")

        # --------  get_account_data   ---------      
    def get_account_data(self,account_id):
        data = self.data_file.load_data()   # load data

        for acc in data["account"]:   # all  account one by one in account list in json file
            if acc["account_id"]==account_id:  # match account id


                # check account type and return user_id, account_id, account_type, balance
                if acc["account_type"]=="Saving":
                    return  SavingAccount(
                        user_id=acc["user_id"],
                        account_id=acc["account_id"],
                        account_type=acc["account_type"],
                        balance=acc["balance"]  
                    )
                if acc["account_type"]=="Current":
                    return  CurrentAccount(
                        user_id=acc["user_id"],
                        account_id=acc["account_id"],
                        account_type=acc["account_type"],
                        balance=acc["balance"]  
                    )

  # --------  deposit  ---------

    def deposit(self,amount,account_id,user_id):
        data = self.data_file.load_data() # load data

        for user in data["user"]: # all user  account one by one in user list in json file 
            if user["user_id"]==user_id:  # match user id
                for  acc in user['accounts']:  # check all account that hold by user


                    try:
                       if account_id not in acc['account_id']: # if account id cannot match by user account then raise error
                           raise InvalidAccountError (f"{user_id} does not have this id {account_id} account")
                       
                       account=self.get_account_data(account_id) # make object current account or saving account
                       if account.deposit(amount) is True:  # check deposite done successfully or not
                            for acct in data['account']:   #   all   account one by one in account list in json file
                                if acct['account_id']==account_id:  # match account id
                                     acct["balance"] = account.get_balance  # get value  balance and   store in balance key

                            txt=Transaction(user_id=user_id,account_id=account_id,amount=amount,transaction_type="deposit")  # make transaction class object
                            data['transaction'].append(txt.to_dic()) # add transaction data into json file
                            self.data_file.save_data(data)  # save file
                            print("Amount Deposite Succesfully")
                    except InvalidAccountError as e:
                        print (e)

            
  # --------  withdraw   ---------
    def withdraw(self,amount,account_id,user_id):
        data = self.data_file.load_data()  # load data
        for user in data["user"]:    # all user  account one by one in user list in json file 
            if user["user_id"]==user_id:   # match user id
                for  acc in user['accounts']:  # check all account that hold by user
                    try:
                        if account_id not in acc['account_id']: # if account id cannot match by user account then raise error
                          raise InvalidAccountError (f"{user_id} does not have this id {account_id} account")
                        
                        account=self.get_account_data(account_id) # make object current account or saving account
                        if account.withdraw(amount) is True:   # check withdraw done successfully or not
                         for acct in data['account']:   #   all   account one by one in account list in json file
                              if acct['account_id']==account_id:      # match account id
                                acct["balance"] = account.get_balance  # get value  balance and   store in balance key
                         txt=Transaction(user_id=user_id,account_id=account_id,amount=amount,transaction_type="withdraw")# make transaction class object
                         data['transaction'].append(txt.to_dic())  # add transaction data into json file
                         self.data_file.save_data(data)  # save file
                         print("Amount Withdraw Succesfully")
                    except InvalidAccountError as e:
                        print(e)
                    
                    
                    
    

     # --------  get_balance  ---------
    def get_balance(self,account_id):
        data = self.data_file.load_data()   # load data
        for acc in data['account']: # check all account in json file
             if acc['account_id'] == account_id:  # check account id
                user=self.get_account_data(account_id) # create sub class of account object
                print(user.get_balance)
           
        
               
        
  # --------  txt_history  ---------
    def txt_history(self,account_id):
        data = self.data_file.load_data() # load data
        for trans in data["transaction"]:  # check all account in json file
            if trans['account_id']==account_id: # check account id
               print (trans)

database=DataBase(file)
bank=Bank(database)


while True:
    print("Enter only number \n1.Register \n2.Login \n3.Exist")
    choose= input()
    if choose=="1":
        username=input("Enter username ")
        password=input("Enter password ")
        print ("1.Saving Account \n2.Current Account")
        account=input()
        if account=="1":
            account_type="Saving"
        if account=="2":
            account_type="Current"
        try:
          
            bank.register_user(username,password,account_type)
          
        except  UserAlreadyExistsError as e:
            print(e)

    elif choose=="2":
        username=input("Enter username ")
        password=input("Enter password ")
        try:
         user=bank.login(username,password)
        
        
         while True:
             print("Enter only number \n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Check Transaction History \n5.Create Account \n6.Logout")
             choose=input()
             if choose==1:
                 amount=int(input("Enter Amount "))
                 account_id=input("Enter Account ID ")
                 try :
                   bank.deposit(amount,account_id,user['user_id'])
                 except InvalidAmountError as e :
                     print(e)   

             elif choose=="2":
                 amount=int(input("Enter Amount "))
                 account_id=input("Enter Account ID ")
                 try:
                  try :
                   bank.withdraw(amount,account_id,user['user_id'])
                  except InvalidAmountError as e :
                     print(e)
                 except InsufficientFundsError as e :
                     print(e)
                

             elif choose=="3":
                 account_id=input("Enter Account ID ")
                 bank.get_balance(account_id)
                 

             elif choose=="4":
                 account_id=input("Enter Account ID ")
                 bank.txt_history(account_id)
                 

             elif choose=="5":
                 print ("1.Saving Account \n2.Current Account ")
                 account=int(input())
                 if account==1:
                    account_type="Saving"
                 if account==2:
                    account_type="Current"
                 bank.createaccount(user['user_id'],account_type)
                 

             elif choose=="6":
                 break
               
             else:
                 print ("Enter invalid number")
        except InvalidCredentialsError as e:
                 print(e)
                 

    elif choose=="3":
        break

    else:
         print ("Enter invalid number")

