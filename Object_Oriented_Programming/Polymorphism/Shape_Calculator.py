"""Create a shape calculator system that demonstrates all the 
   polymorphism concepts you've learned in this chapter. 
   Your system should allow users to calculate areas 
   and perimeters for different shapes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Create an abstract Shape base class"""

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        """Concrete method describe()"""
        return f"This is a shape with area {self.area()} and perimeter {self.perimeter()}"


class Circle(Shape):
    """Create a Circle interface (abstract base class)"""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi * self.radius ** 2)

    def perimeter(self):
        return (2 * math.pi * self.radius)

    def __str__(self):
        return f"Circle with radius {self.radius}"


class Rectangle(Shape):
    """Create a Rectangle interface (abstract base class)"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class Triangle(Shape):
    """Create a Triangle interface (abstract base class)"""
    
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return (self.side1 + self.side2 + self.side3) / 2

    def perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    
    def __str__(self):
        return f"Triangle with sides {self.side1}, {self.side2}, and {self.side3}"


class ShapeCalculator:
    """Create a ShapeCalculator class"""

    def process_shape(self, shape):
        print(f"Processing: {shape}")
        print(shape.describe())
        return {"area": shape.area(), "perimeter": shape.perimeter()}


class UnknownShape:
    """Demonstrate duck typing by creating a class"""
    
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def area(self):
        return (self.size ** 2)

    def perimeter(self):
        return (4 * self.size)

    def describe(self):
        return f"This is a {self.name} shape with area {self.area()} and perimeter {self.perimeter()}"
    
    def __str__(self):
        return f"{self.name} with size {self.size}"

        
# Test your implementation 
def test_calculator():
    calculator = ShapeCalculator()
    
    # Test with Circle
    circle = Circle(5)
    print(f"Testing {circle}")
    results = calculator.process_shape(circle)
    print(f"Results: {results}")
    print()
    
    # Test with Rectangle
    rectangle = Rectangle(4, 6)
    print(f"Testing {rectangle}")
    results = calculator.process_shape(rectangle)
    print(f"Results: {results}")
    print()
    
    # Test with Triangle
    triangle = Triangle(3, 4, 5)
    print(f"Testing {triangle}")
    results = calculator.process_shape(triangle)
    print(f"Results: {results}")
    print()
    
    # Test with UnknownShape (duck typing)
    unknown = UnknownShape("Custom", 10)
    print(f"Testing {unknown}")
    results = calculator.process_shape(unknown)
    print(f"Results: {results}")

# Run the test
test_calculator()
