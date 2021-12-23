"""https://docs.python.org/3/library/enum.html"""

from enum import Enum     
# from aenum import Enum  
Animal = Enum('Animal', 'ant bee cat dog')

Animal.ant  # returns <Animal.ant: 1>
Animal['ant']  # returns <Animal.ant: 1> (string lookup)
Animal.ant.name  # returns 'ant' (inverse lookup)


class Animal(Enum):
	dog = 1
	cat = 2
	lion = 3


print ("The string representation of enum member is : ",end="")
print (Animal.dog)

print ("The repr representation of enum member is : ",end="")
print (repr(Animal.dog))

# printing the type of enum member using type()
print ("The type of enum member is : ",end ="")
print (type(Animal.dog))

# printing name of enum member using "name" keyword
print ("The name of enum member is : ",end ="")
print (Animal.dog.name)

# Python code to demonstrate enumerations
# iterations and hashing
# importing enum for enumerations

# creating enumerations using class
class Animal(Enum):
	dog = 1
	cat = 2
	lion = 3

# printing all enum members using loop
print ("All the enum values are : ")
for Anim in (Animal):
	print(Anim)

# Hashing enum member as dictionary
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

# checking if enum values are hashed successfully
if di=={Animal.dog : 'bark',Animal.lion : 'roar'}:
	print ("Enum is hashed")
else: print ("Enum is not hashed")


Accessing Modes : Enum members can be accessed by two ways
1. By value :- In this method, the value of enum member is passed.
2. By name :- In this method, the name of enum member is passed.
Separate value or name can also be accessed using “name” or “value” keyword.
Comparison : Enumerations supports two types of comparisons
1. Identity :- These are checked using keywords “is” and “is not“.
2. Equality :- Equality comparisons of “==” and “!=” types are also supported.

# Python code to demonstrate enumerations
# Access and comparison

# importing enum for enumerations
import enum

# creating enumerations using class
class Animal(enum.Enum):
	dog = 1
	cat = 2
	lion = 3

# Accessing enum member using value
print ("The enum member associated with value 2 is : ",end="")
print (Animal(2))

# Accessing enum member using name
print ("The enum member associated with name lion is : ",end="")
print (Animal['lion'])

# Assigning enum member
mem = Animal.dog

# Displaying value
print ("The value associated with dog is : ",end="")
print (mem.value)

# Displaying name
print ("The name associated with dog is : ",end="")
print (mem.name)

# Comparison using "is"
if Animal.dog is Animal.cat:
	print ("Dog and cat are same animals")
else : print ("Dog and cat are different animals")

# Comparison using "!="
if Animal.lion != Animal.cat:
	print ("Lions and cat are different")
else : print ("Lions and cat are same")
