class Shop():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_shop(self):
        print('Shop name:', self.name, "| Cuisine Type:", self.cuisine_type)

    def open_shop(self):
        print(f'Welcome to {self.name}! Come in and enjoy your meal!')
    
    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, increment):
        self.number_served += increment


if __name__ == "__main__":
    guadalajara = Shop('Guadalajara', 'Mexican')
    guadalajara.describe_shop()
    guadalajara.open_shop()
    print(guadalajara.number_served)
    guadalajara.set_number_served(50)
    print(guadalajara.number_served)
    guadalajara.increment_number_served(15)
    print(guadalajara.number_served)