from geometric_object import Circle
from geometric_object import Rectangle

def main():
    # Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    print("Circle...")
    displayObject(c)
    print("Rectangle...")
    displayObject(r)

#deze nieuwe functie wordt gebruikt in de main()
# Display geometric object properties
def displayObject(g):
    #deze 2 worden voor zowel circle als rectangle geprint
    print("Area is", g.getArea())
    print("Perimeter is", g.getPerimeter())

    #een van eze 2 wordt maar geprint afhankelijk van wat het object is
    #als het object een circle is => print diameter
    if isinstance(g, Circle):
        print("Diameter is", g.getDiameter())
    #als object rectangle is => print width en height
    elif isinstance(g, Rectangle):
        print("Width is", g.getWidth())
        print("Height is", g.getHeight())


main()  # Call the main function