# Define a circle class to create a cirecle with radus r using the constructor.
# Define and area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self,radius):
        self.redius = radius

    def area(self):
        return 3.14 * self.redius ** 2
    
    def perimeter(self):
        return 2 * self.redius
    
c1 = Circle(31)
print(c1.area)
print(c1.perimeter)