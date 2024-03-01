# INHERITANCE
"""
 When one class (child/derived) derives the properties and methods of another calass (parent/base)

 
 in this method  like child access properties of parent class 
properties = attributes (apan properties la attributes mhanto)


"""

# class Car :
#     colour = "black"
#     @staticmethod
#     def start():
#         print("car started ...")

#     @staticmethod
#     def stop():
#         print("Stop car...")

# class ToyotoCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotoCar("fortuner")
# car2 = ToyotoCar("Defender")

# print(car1.colour)

# print(car1.name)



# Types of Inheritance 


"""
There are three types of inheritance 


1] Single inheritance (single base and derived class)
2] Multi-level inheritance (base class access multiple derived class )
3] Multiple inheritance  ( one derived class acces multiple base classes)


"""

# 3] 

class A:
    varA = "Welcome to class A "
class B:
    varB = "Welcome to class B "
class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)