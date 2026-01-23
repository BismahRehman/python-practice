book_list={}
member_list={}

#add book datA
def add_booK():
    title= input("enter book title").split()
    author = input ("enter author name").split()
    ISBN = int(input("enter book ISBN Number"))
    avability = True
    booK_dic( title, author, avability, ISBN)

def booK_dic( title, author, avability, ISBN):
    book_dic={}
    book_dic["title"]=title
    book_dic["author"]=author
    book_dic["avability"]=avability
    book_list[ISBN]=book_dic

# add member data
def add_memeber():
    name=input("enter the name").split()
    member_id=int( input ("enter the member id "))
    list_of_borrow_book=[]
    member_dic( name, list_of_borrow_book, member_id)
    
def member_dic( name, list_of_borrow_book, member_id):
    member_dic={}
    member_dic["name"]= name
    member_dic["list_of_borrow_book"]=list_of_borrow_book
    member_list[member_id]=member_dic



def borrow_booK():
    borrow_book_member_id=int(input("enter your member id"))
    borrow_booK_ISBN_number=int(input("enter the book ISBN number"))
     
    if borrow_booK_ISBN_number  in book_list:
         if borrow_book_member_id not in member_list:
      

            if book_list[borrow_booK_ISBN_number]['avability']==True:
               book_list[borrow_booK_ISBN_number]['avability']=False
               member_list[borrow_book_member_id]['list_of_borrow_book'].append(borrow_booK_ISBN_number)
               print("you borrow book successfully")
            else:
                print("book is alread borrowed")
         else:
            print("book  not  found")
    else:          
        print( "member not found")
                

def return_book():
    borrow_book_member_id=int(input("enter your member id"))
    borrow_booK_ISBN_number=int(input("enter the book ISBN number"))
    if borrow_book_member_id  in book_list:
        
         if borrow_booK_ISBN_number  in member_list:
        
    
             if borrow_booK_ISBN_number in  member_list[borrow_book_member_id]['list_of_borrow_book']:
       
                 book_list[borrow_booK_ISBN_number]['avability']=True
                 member_list[borrow_book_member_id]['list_of_borrow_book'].remove(borrow_booK_ISBN_number)
                 print ("you return book successful")
             else:
               print("you can't borrow this book")
         else:
            print( "member not found")
        
    else:
        print("book  not  found")
       

def view_all_book():
    for isbn, details in book_list.items():
        print("ISBN:", isbn,
              "Title:", details["title"],
              "Available:", details["avability"])
        

def view_all_member():
    for member_id, details in member_list.items():
        print("member_id:", member_id,
              "name:", details["name"],
              "Their_borrowed_book:", details["list_of_borrow_book"])


while True:
  n=int( input( "what you want \n" 
    "press 1 to add new member \n " 
    "press 2 to add new book \n" 
    "press 3 to borrow a book \n" 
    "press 4 to return a book \n" 
    "press 5 to check total book and their availiabilities \n" 
    "press 6 to check all member and their borrow book \n"
    "press 7 to quit "))
  


  if n==1:
        add_memeber()
  elif n==2:
        add_booK()
  elif n==3:
        borrow_booK()
  elif n==4:
        return_book()
  elif n==5:
     print(book_list)
     view_all_book()
  elif n==6:
    print(member_list)
    view_all_member()
  elif n==7:
    break
  else:
     print("you enter wrong number")