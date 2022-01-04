"""
Python has a set of built-in methods and __call__ is one of them. The __call__ method enables Python programmers to write classes where 
the instances behave like functions and can be called like a function. 
When the instance is called as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
object() is shorthand for object.__call__()

Before getting into application of __call__() we need to understand what a callable object is.
A callable object is one which can be called like a function.
In Python, __call__() is used to resolve the code associated with a callable object. 
Any object can be converted to a callable object just by writing it in a function call format. 
An object of that kind invokes the __call__() method and executes the code associated with it. 
This doesn’t make the object not to work like a normal one. The object can be used as a normal is used.
One thing to keep in mind is the object is itself used as a function, so syntax should be right.
"""


class Example:
	def __init__(self):
		print("Instance Created")
	
	# Defining __call__ method
	def __call__(self):
		print("Instance is called via special method")

# Instance created
e = Example()

# __call__ method will be called
e()


class Product:
	def __init__(self):
		print("Instance Created")

	# Defining __call__ method
	def __call__(self, a, b):
		print(a * b)

# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)
