size = int(input())
room= list(map(int,input().split()))
captain=[]
order_room = set(room)
for i in order_room:
    member = room.count(i)
    if member!=size:
        captain.append(i)      
for i in captain:
    print(i)
    