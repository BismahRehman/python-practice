# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input())
for i in range(test_case):
    a= int(input())
    set_a= set(map(int,input().split()))
    b= int(input())
    set_b= set(map(int,input().split()))
   
    if set_a.issubset(set_b):
        print("True")
    else:
        print("False")    