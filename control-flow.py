"""
Truth Value Testing

If we use a non-boolean object as a condition in an if statement in place of the boolean expression, Python will check for its truth value and use that to decide whether or not to run the indented code. By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

Here are most of the built-in objects that are considered False in Python:

    constants defined to be false: None and False
    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    empty sequences and collections: "", (), [], {}, set(), range(0)


"""

is_cold = True

if is_cold or not is_cold:
    print("the weather is cold or not is cold !")

# bad example
weather = "rain"

if weather == "snow" or "rain":
    print("Wear boots!")

# Truth value testing
"""
In this code, errors has the truth value True
 because it's a non-zero number, so the error message is printed.
This is a nice, succinct way of writing an if statement.
"""
errors = 0

if errors:
    print("You have {} errors to fix !".format(errors))
    print(f'You have {errors} errors to fix !')
else:
    print("No errors to fix !")

# Quiz: Boolean Expressions for Conditions
# Question : Imagine an air traffic control program that tracks three variables, altitude, speed, and propulsion which for a particular airplane have the values specified below.
altitude = 10000
speed = 250
propulsion = "Propeller"
# For each of the following boolean expressions, work out whether it evaluates to True or False and match the correct value.
print(altitude < 1000 and speed > 100)
print((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000)
print(not (speed > 400 and propulsion == "Propeller"))
print((altitude > 500 and speed > 100) or not propulsion == "Propeller")

"""
Quiz: Using Truth Values of Objects

The code below is the solution to the Which Prize quiz you've seen previously. You're going to rewrite this based on what you've learned about truth values.
"""
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)  #  "Congratulations! You won a wafer-thin mint!"