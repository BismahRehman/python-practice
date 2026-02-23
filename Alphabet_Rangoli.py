# a="edcb"
# b="abcde"

# for i in range(len(a)+1):
#   print(f"{a[0:i]}+{b[-i-1:]}")
# for i in range(len(a)):
#   print(f"{a[:-i-1]}{b[i+1:5]}")

def print_rangoli(size):
    # your code goes here
      h=(size*4)-3
      b=[]
      for i in range(size):
            b.append(chr(97+i))

      a=b.copy()
      a.remove(a[0])
      a.reverse()
    

      for i in range(len(a)+1):
             c=a[0:i]+b[-i-1:]
             print("-".join(c).center(h,"-"))

      for i in range(len(a)):
             c=a[:-i-1]+b[i+1:size]
             print("-".join(c).center(h,"-")) 
   
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)