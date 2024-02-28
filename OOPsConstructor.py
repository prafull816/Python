# Constructor
"""
__init__Function

Constructor
 All Classes have a function called _init_(), Which is always executed when the class is being initiated.


 # Creating class


 class Stuednt:
 def __init__(self,Fullname):
 self.name = Fullname


  #  Creating Object

  s1 = Student("Prafull Wahatule)
  print(s1.name)


" This self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. "

"""

# class Student:
#     name = "Prafull Wahatule"
#     def __init__(self):
#      print("Adding new student in Database..")
    
# s1 = Student()


class Student:

    # Defult constructor (this constructor is not necessory)
    def __init__(self):
       pass

    # Parameterized constructor
    def __init__(self,name,sub,marks):
     self.name = name
     self.sub  = sub
     self.marks = marks

     print("Adding new student in Database..")
    
s1 = Student("Prafull","Bio",89)
print(s1.name, s1.sub, s1.marks)
# print(s1.sub)
# print(s1.marks)

s2 = Student("Vedant","Che",90)
print(s2.name, s2.sub, s2.marks)
# print(s2.sub)
# print(s2.marks)

s3 = Student("Rohan","Phy",88)
print(s3.name, s3.sub, s3.marks)
# print(s3.sub)
# print(s3.marks)