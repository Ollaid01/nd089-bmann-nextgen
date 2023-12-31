# Dictionaries and Identity Operators
# A dictionary is a mutable data type that stores mappings of unique keys to values. 
# In general, dictionaries look like key-value pairs, separated by commas.
# Dictionaries are mutable, but their keys need to be any immutable type, like strings, integers, or tuples.
# It's not even necessary for every key in a dictionary to have the same type! 
# We can look up values in the dictionary using square brackets "[]" around the key

# Quiz Question
# Which of these could be used as the key for a dictionary? (Choose all that apply.) Hint: Dictionary keys must be immutable.
# str ? int ? list ? float ?
# Each of these types except for list can be used as a key. Since lists can be changed by adding and removing elements, they are mutable.

# Quiz Question

# What happens if we look up a value that isn't in the dictionary? 
# Create a test dictionary and use the square brackets to look up a value that you haven't defined. What happens?
# A KeyError occurs

# get with a Default Value

# Dictionaries have a related method that's also useful, get(). get() looks up values in a dictionary, but unlike looking up values with square brackets, get() returns None (or a default value of your choice) if the key isn't found. 
# If you expect lookups to sometimes fail, get() might be a better tool than normal square bracket lookups.
# like elements.get('kryptonite', 'There\'s no such element!'). 
# In the last example we specified a default value (the string 'There's no such element!') to be returned instead of None when the key is not found.

# Checking for Equality vs. Identity: == vs. is :
# Quiz Question

# What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

# True, True, True, False! 
# List a and list b are equal and identical. 
# List c is equal to a (and b for that matter) since they have the same contents. 
# But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. 
# That is the difference between checking for equality vs. identity.

# Quiz: More With Dictionaries
# Context

# Use the dictionary below to answer ALL of the questions regarding dictionaries. Consider you have a dictionary named animals that looks like this:

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

# Let's try a few ideas with this dictionary! If you want to try any of the code yourself, you can test it in the coding space from earlier in the lesson.

# Quiz Question
# Question 1

# Match each description to the value it describes.
# The data type of the keys in the dictionary.

# string

# The data type of the values in the dictionary.

# list

# The result of animals['dogs'].

# [20, 10, 15, 8, 32, 15]

# The result of animals['dogs'][3].

# 8

# The result of animals[3]

# Error

# The result of animals['fish']

# [0.3, 0.5, 0.8, 0.3, 1]

# You will soon learn how to use dictionary methods to perform tasks, such as pull values from keys, 
# sort values by keys, add values to the dictionary, and many other tasks that make data structures critical for data science.

"""
Check for Understanding: Data Structures
Check for Understanding

Let's pause again to do a quick check for understanding.

Quiz Question

Which of the following statements about tuples are true? Select all that apply.

"""

"""
A set is defined with curly braces, {}, but it isn't the only data structure that does; dictionaries do as well! However, the difference is that a set is defined as a sequence of elements separated by commas:
set_example = {element1, element2, element3}
while a dictionary is defined as a sequence of key, value pairs marked with colons, separated by commas:
dict_example = {key1: value1, key2: value2, key3: value3}.

Note: if you define a variable with an empty set of curly braces like this: a = {}, Python will assign an empty dictionary to that variable. You can always use set() and dict() to define empty sets and dictionaries as well.

As of Python 3.7, dictionaries in Python are ordered.


A dictionary is a mutable, ordered data structure that contains mappings of keys to values (Note: As of Python 3.7, dictionaries in Python are ordered). Because these keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error.


Each item in a dictionary contains two parts (a key and a value), the items in a dictionary are not ordered, and we have seen in this lesson examples of nested dictionaries.

Because dictionaries are not ordered, they are not sortable. And you do not add items to a dictionary with .append.
"""