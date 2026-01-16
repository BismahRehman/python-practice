def cal(F):
    C = (F-32) *(5/9)
    return C
def feh(C): 
    F =  C*(9/5) + 32
    return F
var =input("do yout to convert Celsius to Fahrenheit or Fahrenheit to Celcius")
if var.strip()  == "Celsius to Fahrenheit":
    temp= int(input("enter a celsius"))
    Fahrenheit = cal(temp)
    print(Fahrenheit)
elif var.strip() == "Fahrenheit to Celcius":
    temp= int(input("enter a Fahrenheit  temperature"))
    Celcius= feh(temp)
    print(Celcius)

