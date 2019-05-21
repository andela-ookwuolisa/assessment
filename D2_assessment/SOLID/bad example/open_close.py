'''
Software entities (classes, modules, functions, etc)
should be open for extension, but closed for 
modification.

We can see that every time we want to draw a distinct shape we 
will have to modify the drawShape method of the ShapePrinter 
to accept a new shape.

As new types of shapes come to draw, the ShapePrinter class 
will be more confusing and fragile to changes.
'''


class Rectangle:
    def __init__(self, width,height)
        self.width = width
        self.height = height

class Square:
    def __init__(self, size)
        self.size = size

class ShapePrinter:
    def drawShape(self, shape):
        if isinstance(shape, Rectangle):
            #Draw Rectangle...
         elif isinstance(shape, Square): 
            #Draw Square...
