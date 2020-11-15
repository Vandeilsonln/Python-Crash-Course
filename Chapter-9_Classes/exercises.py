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



class IceCreamStand(Shop):
    def __init__(self, name, cuisine_type):
        super().__init__(name=name, cuisine_type=cuisine_type)
        self.flavors = ['Chocolate', 'Strawberry', 'Passion fruit', 'Lemon', 'Nutella', 'Kinder', 'Blueberry']

    def show_flavors(self):
        print("These are our available flavors at the moment:")

        for i in self.flavors:
            print(i) 


if __name__ == "__main__":
    iceCreamShop = IceCreamStand('My Shop', 'Dessert')
    iceCreamShop.show_flavors()