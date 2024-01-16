book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
results_dict = {}

for word in book_title:
    if word not in results_dict:
        results_dict[word] = 1
    else:
        results_dict[word] += 1

print(results_dict)


# using get method

for world in book_title:
    results_dict[word] = results_dict.get(word, 0) + 1

print(results_dict)

# Iterating Through Dictionaries with For Loops

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
    print(key)

print("\n Using key/value iteration: \n")
# If you wish to iterate through both keys and values, you can use the built-in method items like this
for key, value in cast.items():
    print("Actor: {} | Role: {} \n".format(key, value))


# while loop for factoriel calculation
number = 6
product = 1
current = 1

while current <= number:
    product *= current
    current += 1

print(product)

# factoriel using for loop
product = 1
for num in range(2, number+1):
    product *= num

print(product)

"""
You need to make sure the while loop:

    - has a condition expression that will be assessed, and when satisfied, will allow you to exit the loop
    - affects the value of the condition variable(s) in each iteration of the loop.
"""

# ZIP : zip returns an iterator that combines multiple iterables into one sequence of tuples. 
# Each tuple contains the elements in that position from all the iterables
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for l, n in zip(letters, nums):
    print("{}, {}".format(l, n))

# unzip
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print("{} {}".format(letters, nums))

# Enumerates
letters = ['a', 'b', 'c', 'd', 'e']
for indice, letter in enumerate(letters):
    print(indice, letter)

# Zip Lists to a Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
print(dict(zip(cast_names, cast_heights)))
      
# Unzip Tuples to list of tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
print(list(zip(*cast)))

# Transpose with Zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose  = tuple(zip(*data))
print(data_transpose)

# Enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i, caracter in enumerate(cast):
    cast[i] = caracter + " " + str(heights[i])
    
print(cast)
