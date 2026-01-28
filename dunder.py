# class A:
#     def __init__(self,name,grades):
#         self.name=name
#         if grades is None:
#             self.grades = []
#         else:
#             self.grades = grades

        
#     def __len__(self):
#         return len(self.grades)
    

#     def __iter__(self):
#          self.grades = 1
#          return self
    
#     def __next__(self):
#         x = self.grades
#         self.a += 1
#         return x
    
#     def __contains__(self):
#         if self.grades:
#             return True
    
#     def __eq__(self, other):
#         return self.name == other.name and self.grades == other.grades
    
#     def __lt__(self, other):
#         return "YES"
    
#     def __hash__(self):
#         return hash((self. name, self.grades))
    
#     def __call__(self):
#         if not self.grades:
#             return 0.0
#         return sum(self.grades) / len(self.grades)
    
# s1=A("ali",[10 ,20 ,13])
# s2=A("ahmad",[23,12,23])
# s3=A("moin",[23,34,12])
# print(len(s1.grades))
# print(next(iter(s1.grades)))
# print  (12 in s1.grades)
# print(s1 == s2)
# print (hash(s1.name))
# print()

