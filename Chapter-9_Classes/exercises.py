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


########################################################


class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Admin(User):
    def __init__(self, name, age):
        super().__init__(name=name, age=age)
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        for i in self.privileges:
            print(i)

if __name__ == "__main__":
    admin = Admin('Van', 22)
    admin.show_privileges()