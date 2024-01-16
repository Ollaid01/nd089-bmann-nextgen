# Function with default argument 
def cylinder_volume(height, radius=5):
    pi = 3.14
    return height * pi * radius ** 2


# it is possible to pass value by 2 ways : position and name.

#1 - Pass in arguments  by position 
print(cylinder_volume(10))
print(cylinder_volume(10, 7))

#2 - Pass by in arguments by name
print(cylinder_volume(radius=10, height=7))


# scope 

# egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()

print('*' * 20)

"""
You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. 
They are helpful for creating quick functions that aren’t needed later in your code. 
This can be especially useful for higher order functions, or functions that take in other functions as arguments.
"""
# lambda expression : function dont have a name, taking another function as argument
def double(x):
    return x * 2

print(double(5))

# equivalent of double function in lambda expression
double_fn = lambda x : x * 2
print(double_fn(5))

# lambda with with multiple parameters
double_multiParam = lambda x, y, z : x * 2 * y * z
print(double_multiParam(4, 6, 2))

print('*' * 20)


