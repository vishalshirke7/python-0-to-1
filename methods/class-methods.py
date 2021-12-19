# Key Takeaways
# Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
# https://www.geeksforgeeks.org/classmethod-in-python/

"""
Firstly, a regular method is the type of method that we are used to seeing since the start of OOP tutorials. It is accessible through both the class and the instance, which means that we can call for the method in both
Employee.method()
and
emp_1.method()
they automatically have the instance as the first positional argument, as self.
Secondly, class methods are the type of method used when a method is not really about an instance of a class, but the class itself. To create a class method, just add '@classmethod' a line before creating the class method. The class is automatically the first argument to be passed in, and is represented as 'cls' instead of 'class'. This is because 'class' is already assigned to be something else in Python. There are 2 ways of using the class method as far as Corey has shown.
First is modifying the class variable. Corey modified the 'raise_amount' class variable using a class method. Just remember that to access a class variable, we have to write 'cls.' before specifying the actual name. For example, as 'cls.raise_amount' as in the video.
Second is making an alternative constructor. Sometimes people have information of their specific instances of the class available in a specific format. Corey shows an example of this where first and last names and pay are separated by a hyphen. Corey creates a class method that returns the class with the specific values passed in that are obtained by using split() method to the string passed in. User of the script can now automatically create a new instance without having to parse the string at '-'.
Corey then moves on to cover static methods. Static methods are different from regular methods an class methods in that it doesn't have a class or instance that is automatically passed in as a firs positional argument. They can be created by adding '@staticmethod' a line before defining the method. These are methods that have a logical connection to the Class, but does not need a class or instance as an argument. Corey says that it is better to make sure we create a static method rather then class or regular method when we are sure that we don't make use of the class or instance within the method.
"""

# An OBJECT as well as a CLASS can call class methods
class MyClass:

    @classmethod
    def classmethod(cls):
        return 'class method called', cls


obj = MyClass()
print(obj.classmethod())
print(MyClass.classmethod())


# Class Methods
class Employee:

    raise_amount = 2

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #Alternative constructors
    @classmethod
    def format_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)

emp1 = Employee('Vishal', 'Shirke', 10000000)
emp2 = Employee('Prashant', 'Shirke', 10000000)
print(Employee.set_raise_amount(3) == emp1.set_raise_amount(3))
print(emp1.raise_amount)
print(emp2.raise_amount)

# Similar to Datetime module
emp1_str = 'vishal-shirke-555555'
Employee.format_string(emp1_str)


