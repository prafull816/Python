#del keyword 
# used to delete onject properties or object itself.
# del s1.name
# del s1

class Student:
    def __init__(self,name):
        self.name = name


s1 = Student("Prafull")
print(s1.name)
del s1.name
print(s1.name)