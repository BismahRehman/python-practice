# N = int(input("enter any number"))
# list = []
# i = 1
# while i<N:
#    print (" what you want in the list \n " \
#     " press 1 for insert \n" \
#     " press 2 for print \n " \
#     " press 3 for remove \n" \
#     " press 4 for append \n " \
#     " press 5 for sort \n " \
#     " press 6 for pop  \n" \
#     " press 7 for reverse \n " )
#    a=  int(input())
#    if a==1 :
#       item = int(input( " Enter any number  you want to insert "))
#       index = int(input( " Enter any index where  you want to insert item "))
#       list.insert(index ,item)
#    if a==2 :
#       print (list)
#    if a==3 :
#       list.remove(item)
#    if a==4 :
#       item = int(input( " Enter any number  you want to append "))
#       list.append(item)
#    if a==5 :
#       list.sort()
#    if a==6 :
#       list.pop()
#    if a==7 :
#       list.reverse()
#    i= i+1


N = int(input("enter any number"))
list = []
i = 1
while i<N:
    command = input()
    apart = command.split(" ")
    if apart[0]=="insert":
        list.insert(int(apart[1]),int(apart[2]))
    if apart[0]== "append":
        list.append(int(apart[1]))
    if apart[0]== "print":
        print(list)
    if apart[0]== "remove":
        list.remove(int(apart[1]))
    if apart[0]== "sort":
        list.sort()
    if apart[0]== "pop":
        list.pop()
    if apart[0]== "reverse":
        list.reverse()
    i=i+1
    