# Class and Instance Attributes

"""
class.attr
obj.attr

"""
class Student:
 def __init__(self,name,sub,marks):
     
     college_name = "ABC College"

     self.name = name
     self.sub  = sub
     self.marks = marks

     print("Adding new student in Database..")
    
s1 = Student("Prafull","Bio",89)
print(s1.name)