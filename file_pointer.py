#Use read() and tell() to show where the pointer is after reading.
with open ("practice.txt", "r") as f:
    print(f.read(5))
    print(f.tell())

#Use a loop to read the file line by line (even if it’s a single line) 
# and print each line with its pointer position.
with open ("hazrat umer.txt", "r",encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line :
            break
        print (line)
        print(f.tell())   

# Move the pointer to 20th byte using seek().

# Truncate the file from that position.

# Check the new content. 

with open ("practice.txt", "r+") as f:
    f.seek(20)
    f.truncate()
    f.write( "i remove old lines and creates new lines")

#After Exercise 3, move pointer to end (seek(0, 2)) and write:
#  Keep practicing!
# Read the whole file to see the final content.

# 
with open ("practice.txt", "r+") as f:
    f.seek(0,2)
    f.write("Keep practicing! ")
    f.seek(0)
    print( f.read())