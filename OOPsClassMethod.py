# Class Method

"""
A ckass method is bound to the class and recives the class as an inmplicit first argumetn.
Note - static method can't access or modigy class state and generally for utility

"""

class Person:
    name = "anonymous"

    # def changeName(self,name):
    #     self.name = name

    ### OR ###

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Prafull")
print(p1.name)
print(Person.name)
