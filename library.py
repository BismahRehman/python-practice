
book_list={}
member_list={}

  

def book():
   title= input ( " enter the detail of book" \
   "enter booK Title")
   author =input( "Enter book author")
   ISBN= input ( "Enter the ISBN") 
   availability = True
   book_dic(title, author, ISBN, availability)



def book_dic(title, author, ISBN, availability):
    book_dic={}
    book_dic['title']=title
    book_dic['author']=author
    book_dic['availability']=availability 
    print(book_dic)
    book_list[ISBN]=book_dic
    print(book_list)



def mem():
   name= input("Enter your name")
   member_id=input("Enter the Member id ")
   li_of_borrow_book=[]
   mem_dic(name, member_id,li_of_borrow_book)


def mem_dic(name, member_id,li_of_borrow_book):
    mem_dic={}
    mem_dic['name']=name
    mem_dic['list_of_borrow_book']=li_of_borrow_book
    print(mem_dic)
    member_list[member_id]=mem_dic
    print(member_list)

def  borrow_book():
    borrow_member_id =input("enter you member id")
    borrow_booK_ISBN=input("enter book ISBN")
    for book in book_list:
       if book_list[book]==borrow_booK_ISBN:
          print(book_list[book])
       


m=0
while m<= 10:
  n=int( input( "what you want" \
    "press 1 to add new member " \
    "press 2 to add new book" \
    "press 3 to borrow a book" \
    "press 4 to return a book" \
    "press 5 to check a availiables book" \
    "press 6 to check a booked book" \
    "press 7 to check total book and their availiabilities" \
    "press 8 to check register members" \
    "press 9 to check all member and their borrow book"))
  


  if n==1:
        mem()
  elif n==2:
        book()
  elif n==3:
    borrow_book()

  elif n==4:
    mem()
  elif n==5:
    mem()
  elif n==6:
    mem()
  elif n==7:
    print(book_list)
  elif n==8:
    mem()
  elif n==9:
    print(member_list)

m=m+1


   