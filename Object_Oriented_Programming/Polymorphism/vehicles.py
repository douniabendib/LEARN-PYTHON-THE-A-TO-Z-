class Vehicle:
    """Create a base Vehicle class"""

    def __init__(self, make, model):
        """Attributes for make and model"""
        self.make = make
        self.model = model

    def start(self):
        """method start()"""
        return "Vehicle started"

    def fuel_efficiency(self):
        """ method fuel_efficiency() that returns 0"""
        return 0


class Car(Vehicle):
    """Create first child classes"""

    def start(self):
        return "Car engine started"

    def fuel_efficiency(self):
        return 25


class Motorcycle(Vehicle):
    """Create second child classes"""

    def start(self):
        return "Motorcycle engine roared to life"

    def fuel_efficiency(self):
        return 40


class Truck(Vehicle):
    """Create third child classes"""

    def start(self):
        return "Truck diesel engine started"

    def fuel_efficiency(self):
        return 15

    
def vehicle_info(vehicle):
    return f"{vehicle.make} {vehicle.model}: {vehicle.start()}, Efficiency: {vehicle.fuel_efficiency()} mpg"


# Test with different vehicles
vehicles = [
    Car("Toyota", "Camry"),
    Motorcycle("Harley", "Davidson"),
    Truck("Ford", "F-150"),
    Vehicle("Generic", "Vehicle")
]

for v in vehicles:
    print(vehicle_info(v))
