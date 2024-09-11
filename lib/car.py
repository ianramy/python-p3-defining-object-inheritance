from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        # Initialize the Car by calling the Vehicle constructor
        super().__init__(wheel_size, wheel_number)

    def go(self):
        # Car overrides the go() method with a different sound
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
