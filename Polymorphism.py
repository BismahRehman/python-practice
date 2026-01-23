class Notification:

    def send(self,message):
        print ( f"{message}your message will be send")
class EmailNotification(Notification):
     def send( self,message):
        print ( f"{message}your EmailNotification will be send")
class SMSNotification(Notification):
    def send(self, message):
        print ( f"{message}your SMSNotificatio will be send")
class PushNotification(Notification):
    def send(self ,message):
        print ( f"{message}your PushNotification will be send")
n= Notification()
e = EmailNotification()
s= SMSNotification()
p= PushNotification()

for i in (n,e,s,p):
    i.send("hello")