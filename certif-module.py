class Person :
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight
    
P1 = Person(30, 40, 50)
P2 = Person(35, 45, 55)

print(P1 + P2)

