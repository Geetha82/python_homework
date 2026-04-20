# Task 5: Extending a Class
import math

# Task 5: step 2
# Create class Point to represent a point in 2d space
class Point:
    # with x and y values passed to the __init__() method. 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # include method for equality
    def __eq__(self, other):
      # Checks if two points have the same coordinates
      if not isinstance(other, Point):
        return False
      return self.x == other.x and self.y == other.y

    # include methods for string
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # include methods for Euclidian distance to another point
    def distance(self, other):
       return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
# Task 5: step 3
# Create a class called Vector 
class Vector(Point):
   
    # method to override the string representation so Vectors print differently than Points
    def __str__(self):
       return f"Vector<{self.x}, {self.y}>"
   
    # Override the + operator so that it implements vector addition, 
    def __add__(self, other):
        if isinstance(other, Vector):
            # summing the x and y values and returning a new Vector
           return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
# Task 5: step 4
# Print results which demonstrate all of the classes and methods which have been implemented
if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(0, 0)

    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"P1 equals P3 : {p1 == p3}")
    print(f"Distance between P1 and P2: {p1.distance(p2)}")

    print("_" * 10)

    #Vector
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")

    # Vector addition
    v3 = v1 + v2
    print(f"Sum of V1 and V2: {v3}")

    # Vector inheriting distance from Point
    print(f"Distance from origin for V1: {p1.distance(v1)}")

   
       



