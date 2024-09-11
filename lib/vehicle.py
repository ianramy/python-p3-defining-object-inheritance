class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        # Initialize the wheel_size and wheel_number
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        # Vehicle's method to simulate movement
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        # Method to simulate filling the tank
        return "filling up!"
