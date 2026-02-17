# In this challenge, the user enters a string and a substring. You have to print the number
#  of times that the substring occurs in the given string. String traversal will take place
#  from left to right, not from right to left.

# # NOTE: String letters are case-sensitive.


# def count_substring(string, sub_string):
#     string= list(set (string))
#     sub_string = list(set (sub_string))
#     n=0
#     for s in range(len(sub_string)):
#         if sub_string[s] in  string:
#             n= n+1
#     return n


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


def count_substring(string, sub_string):
    le=len(sub_string)
    n=0
    for l in range(len(string)):
       if sub_string == string[l:le]:
           n= n+1
       le=le+1 
       
    return n


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)