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
    def __init__(self, account_id, user_id,account_type, balance):
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

          account = Account(account_id=account_id, user_id=user_id,account_type=account_type,balance=0)
          Data_base.save_data(self.data_base["account"].update(account.to_dict))
          print (f"your account is created with {account_id} id")


        
          for user  in data["user"]:
              if user[user_id]in data["user"]:
                   user[account_id].append(account_type)
                   
            
               
     
class Bank:
        def __init__(self,data_base):
             self.data_base=data_base

        def get_account_data(self,account_data):
             data= self.data_base.load_data
             for account_data in data["account"]:
                  if account_data["account_type"]=="saving"  :
                       return( SavingsAccount(
                        account_id=account_data["account_id"],
                        user_id= account_data["user_id"],
                        balance=account_data["balance"]                            
                       ))
                  if account_data["account_type"]=="saving"  :
                       return( CurrentAccount(
                        account_id=account_data["account_id"],
                        user_id= account_data["user_id"],
                        balance=account_data["balance"] 
     
                       ))
                  
        def deposit(self, account_id, amount):
         data = self.data_service.load_data()  # load database  for read

         for acc in data["accounts"]:   # takes accounts form database
            if acc["account_id"] == account_id:  # check account id match or not
                account = self._get_account_object(acc) #    call self._get_account_object method  and return data from database
                                                           # also create a saving or current account object
                account.deposit(amount)    #Calls the deposit method of that account object.
                acc["balance"] = account.get_balance()   #Updates the balance in the database dictionary

                txn = Transaction(      # make transaction object
                    f"T{len(data['transactions']) + 1}",    # give transaction_id
                    account_id,        # account_id
                    "DEPOSIT",         # transaction type
                    amount               #amount
                )
                data["transactions"].append(txn.to_dict())   # update transaction data into database in transaction part
                self.data_service.save_data(data)  # save updated data 
                print(" Deposit successful!")
                return

        def withdraw(self, account_id, amount):
          data = self.data_service.load_data()  # load database  for read

          for acc in data["accounts"]:     # takes accounts form database
            if acc["account_id"] == account_id:   # check account id match or not
                account = self._get_account_object(acc)   #    call self._get_account_object method  and return data from database
                                                           # also create a saving or current account object
                account.withdraw(amount)              #Calls the deposit method of that account object.
                acc["balance"] = account.get_balance()     #Updates the balance in the database dictionary


                txn = Transaction(     # make transaction object
                    f"T{len(data['transactions']) + 1}",  # give transaction_id
                    account_id,  # account_id
                    "WITHDRAW",  # transaction type
                    amount       #amount
                )
                data["transactions"].append(txn.to_dict())    # update transaction data into database in transaction part
                self.data_service.save_data(data)  # save updated data 
                print(" Withdrawal successful!")
                return

        def check_balance(self, account_id):
         data = self.data_service.load_data()    # load database  for read
         for acc in data["accounts"]:    # takes accounts form database
            if acc["account_id"] == account_id:    # check account id match or not 
                print(f" Current Balance: {acc['balance']}")

        def transaction_history(self, account_id):
         data = self.data_service.load_data()    # load database  for read
         print("\n--- Transaction History ---")
         for txn in data["transactions"]:     # takes transactions form database
            if txn["account_id"] == account_id:        # check account id match or not
                print(txn)


# =======================
# Main CLI
# =======================
data_service = Data_base(DATA_FILE)
auth_service = Auth(data_service)
banking_service = Bank(data_service)

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose option: ")

    try:
         if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                print("1. Savings Account\n2. Current Account")
                acc_choice = input("Choose account type: ")
                acc_type = "SAVINGS" if acc_choice == "1" else "CURRENT"
                auth_service.register_user(username, password, acc_type)

         elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                user = auth_service.login(username, password)
                print("Login successful!")

                while True:
                    print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Logout")
                    opt = input("Choose: ")

                    if opt == "1":
                        amt = float(input("Amount: "))
                        banking_service.deposit(user["account_id"], amt)

                    elif opt == "2":
                        amt = float(input("Amount: "))
                        banking_service.withdraw(user["account_id"], amt)

                    elif opt == "3":
                        banking_service.check_balance(user["account_id"])

                    elif opt == "4":
                        banking_service.transaction_history(user["account_id"])

                    elif opt == "5":
                        break

         elif choice == "3":
                print("Goodbye!")
                break

    except Exception as e:
            print(" Error:", e)


