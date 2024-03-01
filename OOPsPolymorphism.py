# Polymorphism : Operator Overloading

"""
When the sa,e operator is allowed to have differnt meaning according to the context.

operators and dunder(useing underscore means dunder = underscore) functions
a+b # addition    a.__add__(b)
a-b # subtraction    a.__sub__(b)
a*b # multiplication    a.__mul____(b)
a/b # division    a.__truediv____(b)
a%b # module    a._____mod_(b)

"""

# print(1+2)
# print(type(1))


# print("Prafull"+"Wahtule") # concatenate
# print(type("Prafull"))
# print([1,2,3,4,5,6,7]) # merge
# print(type([1,2,3,4]))


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def sub(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
    
num1 =  Complex(1,3)
num1.showNumber()

num2 =  Complex(4,6)
num2.showNumber()

num3 =  num1 - num2
num3.showNumber()