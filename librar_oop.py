class Library:
    member={}
    booK={}
    def borrow_book(self,borrow_book_id, borrow_book_member_id):
        if borrow_book_id in self.booK:
            if borrow_book_member_id in self.member:
                if self.booK[borrow_book_id]['avability']==True:
                     self.booK[borrow_book_id]['avability']=False
                     self.member[borrow_book_member_id]['list_of_borrow_book'].append(borrow_book_id)
                     print("you borrow book successsfully")
                else:
                    print ("this book is already book")
            else:
                print ("member not found")
        else: 
            print ("book not found")



    def return_book(self,borrow_book_id, borrow_book_member_id):
        if borrow_book_id in self.booK:
            if borrow_book_member_id in self.member:
                if borrow_book_id in self.member[borrow_book_member_id]['list_of_borrow_book']:
                    self.booK[borrow_book_id]['avability']=True
                    self.member[borrow_book_member_id]['list_of_borrow_book'].remove(borrow_book_id)
                    print ("you return book successful")
                else:
                    print("you don't borrow book")
            else:
                print("member not found")
        else:
            print("book not found")
            
    def view_all_book(self):
        for isbn,details in self.booK.items():
             print("ISBN :",isbn,
                  "author :",details['author'],
                  "avability :",details['avability'],
                  )
    def view_all_member(self):
        for id, details in self.member.items():
           print("mrmber_id:", id,
              "name:", details["name"],
              "list_of_borrow_book:", details["list_of_borrow_book"])
class Book:
    def __init__(self,title,author,ISBN):
       self.title =title
       self.author=author
       self.ISBN=ISBN
       self.avability=True
       list_dic={}
       list_dic["title"]=self.title
       list_dic["author"]=self.author
       list_dic["avability"]=self.avability
       Library.booK[self.ISBN]=list_dic
class Member:
    def __init__(self, name, member_id,):
        self.name=name
        self.member_id=member_id
        self.list_of_borrow_book=[]
        member_dic={}
        member_dic['name']=self.name
        member_dic['list_of_borrow_book']=self.list_of_borrow_book
        Library.member[self.member_id]=member_dic

b=[]
m=[]
Lib=Library()
b=Book("alii","author",123)
m=Member("ali",100)
Lib.borrow_book(13,10)
Lib.view_all_book()
Lib.view_all_member()
Lib.return_book(13,10)
Lib.view_all_book()
Lib.view_all_member()

# while True:
#   n=int( input( "what you want \n" 
#     "press 1 to add new member \n " 
#     "press 2 to add new book \n" 
#     "press 3 to borrow a book \n" 
#     "press 4 to return a book \n" 
#     "press 5 to check total book and their availiabilities \n" 
#     "press 6 to check all member and their borrow book \n"
#     "press 7 to quit "))
#   if n==1:
#         member_name= input("enter your name").split()
#         member_id = int(input("enter you memeber id"))
#         obj=Member(member_name,member_id)
#         m.append(obj)
#   elif n==2:
#       book_title= input("enter book title").split()
#       author = (input("enter the book author")).split()
#       ISBN = int(input("enter the book ISBN number"))
#       obj=Book(book_title,author,ISBN)
#       m.append(obj)       
#   elif n==3:
#         borrow_booK_member_id = int(input("enter you memeber id"))
#         borrow_booK_ISBN = int(input("enter the book ISBN number"))
#         Library.borrow_book(borrow_booK_ISBN,borrow_booK_member_id )
#   elif n==4:
#         borrow_booK_member_id = int(input("enter you memeber id"))
#         borrow_booK_ISBN = int(input("enter the book ISBN number"))
#         Library.return_book(borrow_booK_ISBN,borrow_booK_member_id )
#   elif n==5:
#      print(book_list)
#      Library.view_all_book()
#   elif n==6:
#     print(member_list)
#     Library.view_all_member()
#   elif n==7:
#     break
#   else:
#      print("you enter wrong number")