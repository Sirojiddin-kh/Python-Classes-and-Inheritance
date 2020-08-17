#Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)

class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
    def increase(self):
        self.apple_quantity = self.apple_quantity +1



basket1 = AppleBasket(apple_quantity=4, apple_color="red")
print(basket1)
basket1.increase()
print(basket1)