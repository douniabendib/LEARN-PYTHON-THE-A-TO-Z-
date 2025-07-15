import math


class Shape:
    """Create the Shape parent class"""

    def __init__(self, color):
        """Initialize with a color parameter"""
        self.color = color

    def area(self):
        """Implement an area method that returns 0"""
        return 0

    def describe(self):
        """Implement a describe method"""
        print(f"Color: {self.color}")
        print(f"Area: {self.area()}")
        print("Describe output:")
        print(f"This is a {self.color} shape.")


class Circle(Shape):
    """Create a Circle class that inherits from Shape"""

    def __init__(self, color, radius):
        """Initialize with color and radius parameters"""
        super().__init__(color)
        self.radius = radius

    def area(self):
        """Override the area method to return the correct circle area"""
        return math.pi * self.radius ** 2

    def describe(self):
        """Override the describe method"""
        print(f"Color: {self.color}")
        print(f"Radius: {self.radius}")
        print(f"Area (rounded): {self.area():.2f}")
        print("Describe output:")
        print(f"This is a {self.color} circle with radius {self.radius}.")


class Square(Shape):
    # Your code here
    def __init__(self, color, side_length):
        """Initialize with color and side_length parameters"""
        super().__init__(color)
        self.side_length = side_length
    
    def area(self):
        """Override the area method to return the correct square area"""
        return self.side_length ** 2

    def describe(self):
        """Override the describe method"""
        print(f"Color: {self.color}")
        print(f"Side length: {self.side_length}")
        print(f"Area (rounded): {self.area():.2f}")
        print("Describe output:")
        print(f"This is a {self.color} square with side length {self.side_length}.")


# Example usage
if __name__ == "__main__":
    shape = Shape("Green")
    shape.describe()
    print()

    circle = Circle("Red", 5)
    circle.describe()
    print()

    square = Square("Blue", 4)
    square.describe()
