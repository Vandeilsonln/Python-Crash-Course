from dog import Car


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize atributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + '-kWh battery.')


if __name__ == '__main__':
    my_tesla = ElectricCar('Tesla', 'Model S', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
