# Static Methods
"""
 Methods that don't use the self parameter (wprk at class level)


 class Student:
 @staticmethod # decorator
 def college():
print("XYZ College")


"Decorators allow us to wrap anothehr function in order to extend the bjaviour of the wrapped function, without permanently modifying it"


"""

# Important ( WE can call them to pillar of oops)
"""
Abstraction : Hiding the implementation details of a class and only showing the essential features to the user.

Encapsulation : Wrapping data and functions into a single unit (object).

Inheritance :

Ploymorphism :

"""


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()