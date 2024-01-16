# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!

#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/

# <3, Juno
# """

# print(snake_string * how_many_snakes)

# eval buil-in function
# num = 30
# name = eval("num * 3")
# print(name)

# ###  

# names = str(input("Enter names separated by commas: ")).title().split(",")
# assignments = str(input("Enter assignments counts separated by commas: ")).split(",")
# grades = str(input("Enter a grades separated by commas: ")).split(",")

# ## message string to be used for each student
# ## HINT: use .format() with this string in your for loop
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. Your current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))


# Catch Error using try/expect bloc 
# while True:
#     try:
#         x = int(input("Enter a number : "))
#         break
#     except (KeyboardInterrupt, ValueError):
#         print("That\'s not a valid number !")
#     finally:
#         print("\n Attempted inputs. \n")

# Print Error Message

try:
    x = 4/0
except ValueError:
    print("\n That\'s not a number ! \n")
except ZeroDivisionError as e:
    print("\n Error occurs is : {} !".format(e))
finally:
    print("\n Attempted inputs. \n")