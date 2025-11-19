import math

#parent class = super class = object class
class GeometricObject:
    def __init__(self, color="green", filled=True, bold=True):
        self.__color = color
        self.__filled = filled
        self.__bold = bold

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    #__str__ is called a string method
    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled) + " and bold: " + str(self.__bold)

#child class = subclass
class Circle(GeometricObject):
    def __init__(self, radius, color="green", filled=True, bold=True):
        super().__init__(color, filled, bold)
        #een datafield specifiek voor circle
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getDiameter(self):
        return 2 * self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    #voeg radius toe aan het resultaat
    def printCircle(self):
        print(super().__str__() + " radius: " + str(self.__radius))

    #override __str__ method defined in GeometricObject
    def __str__(self):
        return super().__str__() + " radius: " + str(self.__radius)

#child class = subclass
class Rectangle(GeometricObject):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        #voeg datafields toe specifiek voor rectangle
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = self.__height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    #bij de rectangle subclass wordt de string function niet opnieuw gedefinieerd omdat er niks aan veranderd (de width en height worden er niet aan toegevoegd)