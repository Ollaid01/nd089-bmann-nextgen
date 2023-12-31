"""
For Loops

Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.

An iterable is an object that can return one of its elements at a time. This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.
"""

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for city in cities:
    print(city)
print("Done !")

"""
You can name iteration variables however you like. A common pattern is to give the iteration variable and iterable the same names, except the singular and plural versions respectively (e.g., 'city' and 'cities').
"""

# Using the range() Function with for Loops
"""
Using the range() Function with for Loops

range() is a built-in function used to create an iterable sequence of numbers. You will frequently use range() with a for loop to repeat an action a certain number of times. Any variable can be used to iterate through the numbers, but Python programmers conventionally use i, as in this example:
"""
# range(start=0, stop, step=1)

for i in range(3):
    print("hello!")

print('\n')

"""
Notes on using range():

    If you specify one integer inside the parentheses withrange(), it's used as the value for 'stop,' and the defaults are used for the other two.
    e.g. - range(4) returns 0, 1, 2, 3
    If you specify two integers inside the parentheses withrange(), they're used for 'start' and 'stop,' and the default is used for 'step.'
    e.g. - range(2, 6) returns 2, 3, 4, 5
    Or you can specify all three integers for 'start', 'stop', and 'step.'
    e.g. - range(1, 10, 2) returns 1, 3, 5, 7, 9
"""

# Creating and Modifying Lists
## Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print([city for city in capitalized_cities])

"""
Modifying a list is a bit more involved, and requires the use of the range() function.

We can use the range() function to generate the indices for each value in the cities list. This lets us access the elements of the list with cities[index] so that we can modify the values in the cities list in place.
"""
for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)


print('\n')

# Quiz Question
# Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?
"""
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)
"""
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# for index in range(len(names)):
#     names[index] = names[index].lower().replace(" ", "_")
for name in names:
    name = name.lower().replace(" ", "_")
print(names)

print(list(range(0, -5)))

# quiz
# Quiz Question
# If you want to create a new list called lower_colors, where each color in colors is lower cased, which code line should be added into the for loop in the code block above?
colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())  # #finish this part
print(lower_colors)

# That's right. color.lower() will turn each string to a lower case word, and then you can append them to your empty list created at the top.

# Building Dictionaries