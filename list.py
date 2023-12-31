# list   : mutable - ordered - 
# method : append(val), pop(indice), in 

# slicing myList[deb:fin:pas] fin pas inclu
# extraire et Modifier des listes avec slicing
# Membership Operators : in / not in
# Mutability
# order
# Applications:
#   Filtrage : sélectionner des éléments spécifiques.
#   Transformation : modifier les éléments.
#   Tranchage : diviser en plusieurs sous-listes.
# 

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things)

list_of_random_things[1] = "tesla" 
print(list_of_random_things)

print(list_of_random_things)
list_of_random_things[0:2] = ["a", "b"]
print(list_of_random_things)

print('*' * 20, end="\n")

# string is immutable, pas modifiable car la seule façon possible est den créer un nouveau - veriable par l'id
mystr = "hello world"
print(mystr, id(mystr), sep=" ")
mystr = 1
print(mystr, id(mystr), sep=" ")

print('*' * 20, end="\n")
# mutable object
my_list = [1, 2, 3]
print(my_list, id(my_list), sep=" ")
my_list.append(5)
print(my_list, id(my_list), sep=" ")

print('*' * 20, end="\n")

my_tuple = (1, 2, 3)
print(my_tuple, id(my_tuple), sep=" ")
my_tuple = my_tuple + (5,)
print(my_tuple, id(my_tuple), sep=" ")

print('*' * 20, end="\n")

# join
new_str = "-".join(["st1", "str2", "str3"])
print(new_str)





