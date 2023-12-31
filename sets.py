"""
Les messages d'erreur 'set' object is not subscriptable et 'set' object is not callable en Python proviennent de tentatives d'utiliser un objet de type set (ensemble) d'une manière qui n'est pas supportée par sa conception. Voici ce que chaque message signifie et pourquoi il se produit :
1. 'set' object is not subscriptable

Ce message d'erreur se produit lorsque vous essayez d'accéder à un élément d'un ensemble (set) en utilisant l'indexation, ce qui n'est pas possible avec les ensembles en Python. Contrairement aux listes ou aux tuples, les ensembles ne sont pas des séquences ordonnées et n'ont donc pas d'index.

Exemple de Code Provoquant l'Erreur :

python

mon_ensemble = {1, 2, 3}
element = mon_ensemble[0]  # Erreur: les ensembles ne sont pas indexables

Correction :

Si vous avez besoin d'accéder à des éléments par index, envisagez d'utiliser une liste ou un tuple. Si vous utilisez un ensemble, vous pouvez le parcourir avec une boucle, mais vous ne pouvez pas accéder à des éléments spécifiques par un indice.
2. 'set' object is not callable

Ce message d'erreur apparaît lorsque vous essayez de "appeler" un ensemble comme s'il s'agissait d'une fonction. Cela peut se produire si vous utilisez des parenthèses après le nom d'un ensemble, ce qui est la syntaxe pour appeler une fonction ou une méthode en Python.

Exemple de Code Provoquant l'Erreur :

python

mon_ensemble = {1, 2, 3}
resultat = mon_ensemble()  # Erreur: on ne peut pas "appeler" un ensemble

Correction :

Vérifiez que vous n'utilisez pas des parenthèses après le nom d'un ensemble quand vous ne souhaitez pas appeler une fonction ou une méthode. Si votre intention est d'appeler une méthode spécifique de l'ensemble, assurez-vous d'utiliser le bon nom de méthode avec les parenthèses appropriées, par exemple, mon_ensemble.add(4).
A set is a mutable data structure - you can modify the elements in a set with methods like add and pop. A set is an unordered data structure, so you can't index and slice elements like a list; there is no sequence of positions to index with!

One of the key properties of a set is that it only contains unique elements. So even if you create a new set with a list of elements that contains duplicates, Python will remove the duplicates when creating the set automatically.

En résumé, ces messages d'erreur sont des rappels des restrictions sur la façon dont les ensembles peuvent être utilisés en Python. Les ensembles sont des collections non ordonnées et non indexées de données uniques et ne supportent pas l'indexation ou l'appel comme les fonctions.
"""

# set is a data for collection : mutable - unordered - unique element
# methods: add, pop remove aleatoire element because unordered, in 

# Quiz Question 1

# What would the output of the following code be?

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))  # 10 ? 6 ? 4 ? 0? Error ?


# Quiz Question 2

# Consider the following code:

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

# After executing this code, will the number 5 be a part of the set b?
# That's right. When you pop an element from a set a random element is removed (remember that sets, unlike lists, are unordered so there is no "last element"). The number 5 may or may not be removed.

# Quiz Question

# Is the following statement true or false?
# A set is the only data structure defined with curly braces: {}
# Set: mutable, ordered, indexing, dupplicate ?


"""
Sets are not ordered, so the order in which items appear can be inconsistent, and you add items to sets with .add. Like dictionaries and lists, sets are mutable.

No item can appear more than once in a set and you cannot sort sets. For duplication and sorting, a list would be more appropriate.
"""
