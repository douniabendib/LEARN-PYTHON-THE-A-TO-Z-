"""
Create a ShapeFactory class that can produce different geometric shapes. 
Your factory should support creating "circle", "rectangle", and "triangle" shapes.

Each shape should have:

Appropriate attributes (e.g., radius for circle, length and width for rectangle)
An area() method that calculates and returns the area of the shape
A perimeter() method that calculates and returns the perimeter of the shape
Your task is to implement:

A base Shape class
Three shape classes: Circle, Rectangle, and Triangle
The ShapeFactory class with a create_shape method
The create_shape method should take the shape type as its first parameter, 
followed by the necessary dimensions for that shape.

When an invalid shape type is provided, raise a ValueError 
with the message: "Invalid shape type: {shape_type}"

For calculation purposes:

Use 3.14159 for pi
For triangle area, you can use a simplified formula for the specific case of 
a right triangle: (base * height)/2
"""
class Shape:

    def __init__(self):
        pass
    
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        
    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def perimeter(self):
        return self.base + self.height + int((self.base ** 2 + self.height ** 2) ** 0.5)


class ShapeFactory:
    def create_shape(self, shape_type, *args):
        if shape_type.lower() == "circle":
            return Circle(args[0])
        elif shape_type.lower() == "rectangle":
            return Rectangle(args[0], args[1])
        elif shape_type.lower() == "triangle":
            return Triangle(args[0], args[1])
        else:
            raise ValueError(f"Invalid shape type: {shape_type}")


factory = ShapeFactory()

circle = factory.create_shape("circle", 5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = factory.create_shape("rectangle", 4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

triangle = factory.create_shape("triangle", 3, 4)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())
