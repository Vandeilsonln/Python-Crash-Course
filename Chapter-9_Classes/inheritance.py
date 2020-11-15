from dog import Car


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, bs):
        """
        Initialize atributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Batery(bs)


class Batery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        # Initialize the battery's attributes.
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        # Print a statement about the range this battery provides.
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "this car can go approximately " + str(range) + " miles on a full charge"
        return message


if __name__ == '__main__':
    my_tesla = ElectricCar('Tesla', 'Model S', 2016, 85)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    print(my_tesla.battery.battery_size)
    print(my_tesla.battery.get_range())