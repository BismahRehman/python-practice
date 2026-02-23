# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int(input())
set_a= set(map(int,input().split()))
m= int(input())
for i in range(m):
     operation = input().split()
     set_b= set(map(int,input().split()))
     
     
     if operation[0]=="intersection_update":
         set_a.intersection_update(set_b)
         
         
     if operation[0]=="update":
        set_a.update(set_b)
      
     if operation[0]=="symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)
       
        
     if operation[0]=="difference_update":  
        set_a.difference_update(set_b)
        
print(sum(set_a))

    
