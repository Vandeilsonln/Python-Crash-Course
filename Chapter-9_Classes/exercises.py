class Shop():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_shop(self):
        print('Shop name:', self.name, "| Cuisine Type:", self.cuisine_type)

    def open_shop(self):
        print(f'Welcome to {self.name}! Come in and enjoy your meal!')


if __name__ == "__main__":
    guadalajara = Shop('Guadalajara', 'Mexican')
    guadalajara.describe_shop()
    guadalajara.open_shop()