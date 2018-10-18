'''
We add a Shape abstract class
Now the ShapePrinter class remains intact when we add a new shape type.
The existing code is not modified.
'''

class Shape:
    def draw(self):
        #draw shape

class Rectangle(Shape):
    def __init__(self, width,height)
        self.width = width
        self.height = height
    
    def draw(self):
        #draw shape

class Square(Shape):
    def __init__(self, size)
        self.size = size

    def draw(self):
        #draw shape

class ShapePrinter:
 
    def drawShape(self, shape):
        shape.draw()
