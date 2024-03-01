# Privet (like) attributes amd methods 
"""
Conceptual implementation in  python
Privet attributes and methods are meant to be used only within the class and are not accessinle from ouutside the clss.

"""


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


def reset_pass(self):
     print(self._acc_pass)

acc1 = Account(12345,5432321)


print(acc1.acc_no)
print(acc1.reset_pass)



#(When we use doubble underscore the then this called privet function)


class Person:
    __name = "anonymous"
    
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello

p1 = Person()
print(p1.welcome)