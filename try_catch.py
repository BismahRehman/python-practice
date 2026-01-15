T= int(input())
i =1
while i<= T:
    number = input()
    sep = number.split()
    try:
        a= int(sep[0])
        b= int(sep[1])
        div = a//b
        print (div)
    except Exception as e:
        
        print ("Error Code:",e)
    i=i+1

