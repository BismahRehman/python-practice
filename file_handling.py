#Read a large text file line by line using a generator.
def read_file():
    f=open("hazrat umer.txt","r", encoding="utf-8")
    for line in f:
       yield line
      
    f.close()
for i in read_file():
    print (i)


#Create a file and write your name
with open ("text.txt","x")as f:
    f.write("my name is bismah")

#Read the file and print content
with open ("text.txt","r")as f:
     file=f.read()
     print(file)

#Append your city in same file
with open ("text.txt","a")as f:
     file=f.append("/n i belong to lahore")
     print(file)

