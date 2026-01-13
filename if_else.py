if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")                 # Odd number
    else:
        if 2 <= n <= 5:
            print("Not Weird")         # Even and 2–5
        elif 6 <= n <= 20:
            print("Weird")             # Even and 6–20
        else:
            print("Not Weird")         # Even and >20
