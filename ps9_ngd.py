# 6.00 Problem Set 9
#
# Name: Natalie
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: lenght base of triangle
        height: the length of the hieght of the triangle
        creates a right triangle only
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        Returns the area of the right triangle
        """
        return (self.base * self.height * .5)
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal is they have the same base and height
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self,shapes_list):
        """
        Initialize any needed variables
        shapes_list: an iterative item containing possible shapes to put into the set
        """
        set_holder=[]#an iterative list that will hold the shapes
        for shape in shapes_list: 
            in_list=False #assume not already in list
            for uniq_shape in set_holder:
                if shape == uniq_shape: #if that shape is the same as any in the shape holder
                    in_list=True #it is in the list
                    break #once in list dont need to keep looking
            if not in_list: #if not in list already
                set_holder.append(shape) #add to list
        self.set=set(set_holder) #returns a set that holds unique shapes
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        in_set=False #assums not in set
        for uniq_shape in self.set: #for each unique shape in the set
            if sh == uniq_shape: #if sh is the same as another shape 
                in_set=True #then it is in the set
                break #once in set, dont need to keep looking
        if not in_set: #if it is not in set
            self.set.add(sh) #add to set
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.copy_set=self.set.copy() #each time iter is called it makes a new shallow copy of the set to be used by next
        return self #returns self including the copy
    def next(self):
        """
        Is needed to iterate through the shape set
        """
        if not self.copy_set: #if the copy of the set is empty
            del self.copy_set #removes the copy of the set made in iter
            raise StopIteration #ends the iteration
        return self.copy_set.pop() #return and remove from copy an element of the set
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        cr_str_holder='' #holds all the circles text
        sq_str_holder='' #holds all the squares test
        tr_str_holder='' #holds all the triangles text
        for shape in self: #for each shaple
            if isinstance(shape,Circle): #if it is an instance of a Circle
                cr_str_holder += str(shape) #add to circle list
                cr_str_holder += '\n' #add a return
            elif isinstance(shape,Square):
                sq_str_holder += str(shape)
                sq_str_holder += '\n'
            elif isinstance(shape, Triangle):
                tr_str_holder += str(shape)
                tr_str_holder += '\n'
        return (cr_str_holder + sq_str_holder + tr_str_holder).strip() #add all strings together and remove last '\n'
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest_shape=(Circle(0),) #initate a tuple with the first object having a area of 0
    for shape in shapes: #for each shape in the shapeSet
        if shape.area() > largest_shape[0].area(): #if the area of that shape is larger than the current largest
            largest_shape=(shape,) #replace the list with the new largest shape as the only item
        elif shape.area() == largest_shape[0].area(): #if the shape as the same area as the current largest
            largest_shape +=(shape,) #add that shape to the list
    return largest_shape #return a tuple of the largest shapes by area
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    inputFile = open(filename) 
    SetShapes=ShapeSet([]) #initate an empty set of shapes
    for line in inputFile:
        line=line.strip() #remove '\n'
        parts=line.split(',') #split by ','
        if len(parts)==3: #if there are three parts can only be a triangle
            SetShapes.addShape(Triangle(float(parts[1]),float(parts[2])))
        elif parts[0]=='circle': #if labled a circle
            SetShapes.addShape(Circle(float(parts[1])))
        elif parts[0]=='square': #if labled a square
            SetShapes.addShape(Square(float(parts[1])))
    return SetShapes
        

##Test
ss=readShapesFromFile("shapes.txt")
print ss
big=findLargest(ss)
for e in big: print e        
  
        
