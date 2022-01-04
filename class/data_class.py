from dataclasses import dataclass
# Normal Class

class Person:

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


person1 = Person('Vishal', 'SDE2', 24)
person2 = Person('Prashant', 'Manager', 31)
person3 = Person('Amit', 'Electrician', 26)

print(id(person2))
print(id(person3))
print(person1)
print(person2 == person3)


@dataclass
class Person:
    name: str
    job: str
    age: int

    # def __init__(self, name, job, age):
    #   self.name = name
    #   self.job = job
    #   self.age = age


person1 = Person('Vishal', 'SDE2', 24)
person2 = Person('Prashant', 'Manager', 31)
person3 = Person('Amit', 'Electrician', 26)

print(id(person2))
print(id(person3))
print(person1)
print(person2 == person3)

