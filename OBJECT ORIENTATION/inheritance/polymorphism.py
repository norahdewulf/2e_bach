from geometric_object import Circle
from geometric_object import Rectangle

def main():
    # Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    displayObject(c)
    displayObject(r)
    print("Are the circle and rectangle the same size?", isSameArea(c, r))

#deze nieuwe functies kunnen in de main() gebruikt worden
# Display geometric object properties
def displayObject(g):
    #note (door confusion van mezelf): de __str__ is een method dus ook oproepen zoals een method
    print(g.__str__())

# Compare the areas of two geometric objects
def isSameArea(g1, g2):
    return g1.getArea() == g2.getArea()

main() # Call the main function