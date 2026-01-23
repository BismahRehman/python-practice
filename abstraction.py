from abc import ABC, abstractmethod

# class Vechile(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vechile):
#     def start(self):
#         print("car is started")
    
#     def stop(self):
#          print("car is stoped")

# class Bike(Vechile):
#     def start(self):
#          print("bike is started")

#     def stop(self):
#         print("bike is started")


# b=Bike()
# c=Car()




# c.start()
# c.stop()
# b.start()
# b.stop()

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
    @abstractmethod
    def refund(self,amount):
        pass
    def validate_amount(self,amount):
        return  amount > 0 
    
class CreditCardPayment(Payment):
    def pay(self, amount):
        if self.validate_amount(amount)==True:
            print ( " you payment done successfully using credit card")
        else :
            print ("your amount is zero")
    def refund(self, amount):
        if self.validate_amount(amount)==True:
            print ( " you payment refund successfully using credit card")
        else :
            print ("your amount is zero")

class JazzCashPayment(Payment):
     def pay(self, amount):
        if self.validate_amount(amount)==True:
             print ( " you payment done successfully using JazzCash")
        else :
            print ("your amount is zero")

     def refund(self, amount):
        if self.validate_amount(amount)==True:
            print ( " you payment refund successfully using JazzCash")
        else :
            print ("your amount is zero")
j=JazzCashPayment()
c=CreditCardPayment()
c.pay(100)
c.refund(50)
j.refund(100)
c.pay(100)
c.pay(0)

