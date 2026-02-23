# Enter your code here. Read input from STDIN. Print output to STDOUT

def design(string):
    a = string.split()
    b= int(a[0])//2
    c= int(a[1])
    
    for i in range(0,b):
        
        l=(i*".|.")+".|."+(i*".|.")
        print(l.center(c,"-"))
  
    print("WELCOME".center(c,"-"))
    for i in range(b):
        l=((b-i-1)*".|.")+".|."+((b-i-1)*".|.")
        print(l.center(c,"-"))

s= input()
design(s)