class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in responde to a command."""
        print(self.name.title() + ' rooled over!')

    
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print("My dog's name is " + my_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + ' years old.')

my_dog.sit()
my_dog.roll_over()