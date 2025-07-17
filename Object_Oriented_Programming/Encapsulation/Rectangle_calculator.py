class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return (self._width * self._height)
    
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    @property
    def dimensions(self):
        return (self._width, self._height)

    @dimensions.setter
    def dimensions(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("Dimensions must be a tuple of (width, height)")
        width, height = value
        self.width = width  # This will validate width
        self.height = height  # This will validate height
    
    @dimensions.deleter
    def dimensions(self):
        self._width, self._height = 1, 1
        

# Test the Rectangle class
rect = Rectangle(5, 3)
print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area}, Perimeter: {rect.perimeter}")

# Test the dimensions property
print(f"Dimensions: {rect.dimensions}")
rect.dimensions = (10, 8)
print(f"New area: {rect.area}")

# Test validation
try:
    rect.width = -2
except ValueError as e:
    print(f"Validation error: {e}")

# Test deleter
del rect.dimensions
print(f"After reset: {rect.dimensions}")
