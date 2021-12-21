# WAY 1
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, 'JackRussellTerrier')
buddy = Dog("Buddy", 9, 'Dachshund')
jack = Dog("Jack", 3, 'Bulldog')
jim = Dog("Jim", 5, 'Bulldog')
# print(miles.speak('Woof'))
# print(buddy.speak('boo'))
# print(jack.speak('Yaaa'))
# print(jim.speak('boo'))

# WAY 2
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# print(miles.species)
# print(buddy.name)
# print(jack)
jim.speak('Woof')


# Extend parent functionality

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says : {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

# To use parent function
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


jack = JackRussellTerrier("jack", 4)
dach = Dachshund("Buddy", 9)
bully = Bulldog("Jack", 3)
big_bully = Bulldog("Jim", 5)
print(jack.speak())