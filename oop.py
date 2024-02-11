"""
Object-Oriented Programming (OOP) Vocabulary

    class - a blueprint consisting of methods and attributes
    object - an instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, a blue shirt, etc. However, as you'll see later in the lesson, objects can be more abstract.
    attribute - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.
    method - an action that a class or object could take
    OOP - a commonly used abbreviation for object-oriented programming
    encapsulation - one of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. Encapsulation allows you to hide implementation details much like how the scikit-learn package hides the implementation of machine learning algorithms.

In English, you might hear an attribute described as a property, description, feature, quality, trait, or characteristic. All of these are saying the same thing.

Here is a reminder of how a class, object, attributes and methods relate to each other.

Function vs Method
A function and a method look very similar. They both use the def keyword. They also have inputs and return outputs. The difference is that a method is inside of a class whereas a function is outside of a class.
"""

class Shirt:
    def __init__(self, color, size, price, style):
        self.color = color
        self.size  = size
        self.price = price
        self.style = style
    
    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)

new_shirt = Shirt('red', 'M', 14.99, "short sleeve")
print(new_shirt.__dict__)

class Shirts:
  def __init__(self, shirt_color, shirt_size, shirt_size, shirt_price):
      self-color = color.orange
      self.size = shirt_size
      self-style = shirt_style
      self.price = shirt_price

new_shirt = Shirts('red', 'M', 14.99, "short sleeve")
print(new_shirt.__dict__)