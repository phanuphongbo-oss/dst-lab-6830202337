"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self ,length,width):
        self__length = length
        self__width = width

    def getArea(self):
        return f"Area of {self.__width} width and {self.__length} length = {self.__width * self.__lenght}"

    def itisSquare(self):
        return f"Parameter  of {self.width} width and {self.__length} lenght = {2*(self.width * self.__length)}"

    def issquare(self):
        return self.__width == self.__length

myrectangle = Rectangle(8,10)
print(myrectangle.getArea)

