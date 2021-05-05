"""A collection of OOP examples"""
import pandas as pd

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]

class BareMinimumClass:
    pass

class Car:
    """An example of a class with attributes and methods"""

    def __init__(self, fuel, maxspeed, speed=0):
        """
        Constructor for Car class.
        We have a `fuel` and `maxspeed` attribute.
        """
        self.fuel = fuel
        self.maxspeed = maxspeed
        self.speed = speed

    def setSpeed(self, new_speed):
        """set speed to new_speed"""
        if new_speed > self.maxspeed:
            return "You cannot exceed the maxspeed"
        else:
            self.speed = new_speed

    def __repr__(self):
        return "The car speed is {} and it has {} fuel".format(self.speed, self.fuel)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        """Social Media User Attributes"""
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100

    def __repr__(self):
        return f"my name is {self.name}"

# Parent class
class Animal:
    def __init__(self, name, weight, diet_type):
        """A general representation of animals"""
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = str(diet_type)

    def run(self):
        return "Vroom Vroom me go quick"

    def eat(self, food):
        return "Huge fan of that {}".format(food)

# Child class, inheriting from parent class
class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps):
        super().__init__(name, weight, diet_type)
        self.num_naps = num_naps

    def run(self):
        """This overrides the run method in the Animal class"""
        return "I am sloth - I go slow"

    def say_something(self):
        """This is not a method within Animal"""
        return "This is a sloth of typing"


print("This is outside of the if name is main")


# Need to run the file in order to run this code
# Put code in here if you don't want functions to run when you import
# __name__ == "__main__" is True when you run .py file, it's false when you import the file
if __name__ == "__main__":
    print("This is inside of the if name is main")
    user1 = SocialMediaUser(name="George Washington",
                            location="Djibouti", upvotes=2)
    user2 = SocialMediaUser(
        name="Carlos", location="West Virginia", upvotes=200204345345345)
    user3 = SocialMediaUser(
        name="Carlitta", location="Northwest Virginia")  # has zero upvotes
    print(f'user1 is named {user1.name} with {user1.upvotes} upvotes!')
    # is_popular should return False
    print(f'Is user1 popular? {user1.is_popular()}')
    user1.recieve_upvotes(200)
    print(f'user1 received 200 upvotes and should now be popular')
    # is_popular should return True
    print(f'Is user1 popular? {user1.is_popular()}')

    df = MyDataFrame({'a': 1, 'b': 2})
    print(df)


