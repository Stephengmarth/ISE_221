import math
# 1.	Create the class Point to represent and manipulate a points in 2D Cartesian space
# 2.	Add an initializer method: (<__init__> function that acts like a constructor. set intial values and automatic exicution)
#	    it will define the points coordinate values
#	    the variables of the coordinate should be hidden (<__variable.name> Double underscore before variable name makes it private.)
#       (<def> is used to define a function)
#       Use <self.> for attribute to specific object
class Point:
   def __init__(self, x, y):
        self.__x = x
        self.__y = y

# 3.	Add getter and setter methods
#       def get_x(self): 
#           return self.__x (returns private variable)

   def get_x(self):
        return self.__x

   def get_y(self):
        return self.__y

#       def set_x(self, x):
#           self.__x = x(sets new value for private variable)

   def set_x(self, x):
        self.__x = x

   def set_y(self, y):
        self.__y = y

# 4.	Add the method distanceFromOrigin to calculate the distance between the point and the origin (method function inside of class)
#       d=√((x2 – x1)² + (y2 – y1)²) x1 and y1 are zero, math.sqrt(x**2+y**2)

   def distanceFromOrigin(self):
        return math.sqrt(self.__x**2 + self.__y**2)

# 5.	Add the method distanceFromPoint to calculate the distance between the point and another point (it should take the other point as an argument)
#       d=√((x2 – x1)² + (y2 – y1)²) (point_x - otherpoint_x)**2 + (point_y - other_point_y)**2

   def distanceFromPoint(self, other_point):
        return math.sqrt((self.__x - other_point.get_x())**2 + (self.__y - other_point.get_y())**2)

# 6.	Add the method reflect_x that returns a new point, one which is the reflection of the point about the y-axis. For example, Point(3, 5).reflect_x() is (-3, 5). 
#       horizontal flip flip the x 

   def reflect_x(self):
        return Point(-self.__x, self.__y)

# 7.	Add the method slope_from_origin which returns the slope of the line joining the origin to the point
#       m = (y2 - y1) / (x2 - x1)
#       origin is 0,0 so the pont x,y is the slope. 
#       if x is zero there is no slope.
#       Use raise instead of print for error handeling. This stops the program. raise needs a exception class, ValueError. 
#       You can make your own expeption classes
#       class SlopeError(Exception):
#           pass 

   def slope_from_origin(self):
        if self.__x == 0:
            raise ValueError("This line is undefined, x = 0")
        return self.__y / self.__x

# 8.	The equation of a straight line is “y = mx + b”, (or perhaps “y = mx + c”). The coefficients a and b completely describe the line. Write a method in the Point class
#       so that if a point instance is given another point, it will compute the equation of the straight line joining the two points. It must return the two coefficients as a tuple of two values.
#       y=mx+b
#       b=y-mx
#       m=(y-b)/x

   def lineEquation(self, other_point):
        m = (self.__y - other_point.get_y()) / (self.__x - other_point.get_x())
        b = self.__y - m * self.__x
        return m, b

# 9.	Add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move in the x, y direction the number of units given.
#       x=x+dx
#       y=y+dy
#       += redifines the variable with the addition
#       x+=dx, y+=dy

   def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
# 10.	We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height. Create a class definition for a Rectangle class using this idea.

class Rectangle:
    
    def __init__(self, lowerLeftCorner, width, height):
        self.lowerLeftCorner = lowerLeftCorner
        self.width = width
        self.height = height
# 11.	Add the following accessor methods to the Rectangle class: getWidth, getHeight, __str__
#       return f is for a formatted string. 
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def __str__(self):
        return f"Rectangle(lowerLeftCorner=({self.lowerLeftCorner.get_x()}, {self.lowerLeftCorner.get_y()}), width={self.width}, height={self.height})"

# 12.	Add a method area to the Rectangle class that returns the area of any instance
#       A=w*h

    def area(self):
        return self.width * self.height

# 13.	Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance
#       p=(w*2)+(h*2)

    def perimeter(self):
        return 2 * (self.width + self.height)

# 14.	Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance
#       h=w,w=h or h,w = w,h

    def transpose(self):
        self.width, self.height = self.height, self.width

# 15.	Write a new method in the Rectangle class to test if a Point falls within the rectangle. For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has
#       open upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded, and from [0 to 5) in the y direction.
#       So it does not contain the point (10, 2). These tests should pass
#       tur or false, 0 is inclusive, <= 
#       corner(0,0) <= pointx < corner plus width
#       corner(0,0) <= pointy < corner plus height

    def rectanglePoint(self, point):
        return (self.lowerLeftCorner.get_x() <= point.get_x() < self.lowerLeftCorner.get_x() + self.width and
                self.lowerLeftCorner.get_y() <= point.get_y() < self.lowerLeftCorner.get_y() + self.height)


def main():
   
    # POINTS
    p1 = Point(12, 9)
    p2 = Point(4, 5)

    print("Point 1:", p1.get_x(),",", p1.get_y())
    print("Point 2:", p2.get_x(),",", p2.get_y())

    print("Distance from origin:", p1.distanceFromOrigin())
    print("Distance from P1 to P2:", p1.distanceFromPoint(p2))

    reflected = p1.reflect_x()

    print("P1 Horixontal flip:", reflected.get_x(),",",reflected.get_y())

    print("Slope from origin to P1:", p1.slope_from_origin())

    m, b = p1.lineEquation(p2)
    print(f"Line equation between P1 and P2: y = {m}x + {b}")

    p1.move(2, -3)
    print("Moved P1:", p1.get_x(),",", p1.get_y())

    # RECTANGLE
    rect = Rectangle(Point(0, 0), 10, 5)
    print(rect)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())

    rect.transpose()
    print("Transposed rectangle:", rect)

    point_inside = Point(3, 2)
    point_outside = Point(12, 12)

    print("The point is inside rectangle:", rect.rectanglePoint(point_inside))
    print("The point is inside rectangle:", rect.rectanglePoint(point_outside))

if __name__ == "__main__":
    main()
    