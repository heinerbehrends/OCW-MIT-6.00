# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")
    def __cmp__(self, other):
        if self.area() < other.area(): return -1
        elif self.area() > other.area(): return 1
        else: return 0
        
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
    

    def __repr__(self):
        return 'Square with side %.1f' % (self.side,)


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
    def __repr__(self):
        return 'Circle with radius %.1f' % (self.radius,)
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
        base: base of the triangle
        height: height of the triangle
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        "returns area of the triangle"
        return self.base * self.height / 2
    def __str__(self):
        return "Triangle with base %.1f and height %.1f" %(self.base, self.height)
    def __repr__(self):
        return 'Triangle with base %.1f and height %.1f' % (self.base, self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if their base and height are equal.
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height    
        

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(object):
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shapeSet = []
        self.place = None
        ## TO DO
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if type(sh) != Circle and type(sh) != Triangle and type (sh) != Square:
            raise TypeError("This is not a valid shape")
        for shape in self.shapeSet:
            if shape == sh: raise ValueError("Duplicate shape")
        self.shapeSet.append(sh)
        ## TO DO
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self
    def next(self):
        if self.place >= len(self.shapeSet):
            raise StopIteration
        self.place += 1
        return self.shapeSet[self.place - 1]
        ## TO DO
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        printStringCircle = ""
        printStringSquare = ""
        printStringTriangle = ""
        for shape in self.shapeSet:
            if type(shape) == Circle:
                printStringCircle += str(shape), "\n"
            if type(shape) == Square:
                printStringSquare += str(shape), "\n"
            if type(shape) == Triangle:
                printStringTriangle += str(shape), "\n"
        return printStringCircle + printStringSquare + printStringTriangle
        ## TO DO
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    sortedShapes = sorted(shapes)
    resultTuple = ()
    resultTuple += (sortedShapes[-1],)
    for i in range(-2, -len(sortedShapes), -1):
        if sortedShapes[-1].area() == sortedShapes[i].area():
            resultTuple += (sortedShapes[i],)
        else:
            break
##    largestAreas =  []
##    resultTuple = ()
##    shapeAreaDict = {}
##    for shape in shapes:
##        shapeAreaDict[shape] = shape.area()
####    print shapeAreaDict
##    maxArea = max(shapeAreaDict.values())
####    print maxArea
##    largestAreas += [key for key, val in shapeAreaDict.items() if val == maxArea]
##    for item in largestAreas:
##        resultTuple += (item,)
    return resultTuple

    


##    largestAreas += (max(shapeAreaDict.iterkeys(), key=(lambda key: shapeAreaDict[key])), )
##    return largestAreas
        
    ## TO DO

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    shapeSet = ShapeSet()
    inFile = open(filename, 'r', 0)
    for line in inFile:
        if line.rstrip("\n").split(",")[0] == "circle":
            shapeSet.addShape(Circle(line.rstrip("\n").split(",")[1]))
        elif line.rstrip("\n").split(",")[0] == "square":
            shapeSet.addShape(Square(line.rstrip("\n").split(",")[1]))
        elif line.rstrip("\n").split(",")[0] == "triangle":
            shapeSet.addShape(Triangle(line.rstrip("\n").split(",")[1], line.rstrip("\n").split(",")[2]))
    return shapeSet


        
##        dataList.append(line.rstrip("\n").split(","))
##    print dataList
##    for item in dataList:
##        if item[0] == "circle":
##            circleDataList.append(item[1])
##        if item[0] == "square":
##            squareDataList.append(item[1])
##        if item[0] == "triangle":
##            triangleDataList.append((item[1], item[2]))
##    print circleDataList, squareDataList, triangleDataList
##    for value in circleDataList:
##        shapeSet.addShape(Circle(value))
##    for value in squareDataList:
##        shapeSet.addShape(Square(value))
##    for valuePair in triangleDataList:
##        shapeSet.addShape(Triangle(valuePair[0], valuePair[1]))
    

shapeSet1 = readShapesFromFile("shapes2.txt")
##print shapeSet1
print findLargest(shapeSet1)

print


    ## TO DO

##square0 = Square(9)
##square1 = Square(5)
##square2 = Square(2)
##circle0 = Circle(4.3)
##circle1 = Circle(8.1)
##triangle0 = Triangle(2,3)
##circle2 = Circle(3.5)
##shapeSet1 = ShapeSet()
##shapeSet1.addShape(circle0)
##shapeSet1.addShape(circle1)
##shapeSet1.addShape(circle2)
##shapeSet1.addShape(square0)
##shapeSet1.addShape(square1)
##shapeSet1.addShape(square2)
##shapeSet1.addShape(triangle0)
##print shapeSet1
