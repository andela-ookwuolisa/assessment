from shape import IShape

class Rectangle(IShape):
    '''
    Software entities (classes, modules, functions, etc)
    should be open for extension, but closed for 
    modification.

    We add a Shape abstract class
    Now the ShapePrinter class remains intact when 
    we add a new shape type.
    The existing code is not modified.
    '''
    
    def __init__(self, width,height)
        self.width = width
        self.height = height
    
    def draw(self):
        #draw shape

class Square(IShape):
    def __init__(self, size)
        self.size = size

    def draw(self):
        #draw shape

class ShapePrinter:
    def drawShape(self, shape):
        shape.draw()
