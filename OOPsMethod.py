# Methods
"""
 Methods are a=fynctionns that belong to objects.

"""



# Creating class

class Student:
    college_name = "ABX College"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

        def welcome(self):
            print("Welcome Student", self.name)

        def get_marks(Self):
            return self.marks
        
s1 = Student("Prafull", 98)
s1.welcome()
print(s1.get_marks)
