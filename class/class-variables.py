
"""Corey also shows that class variables and instance variables are closely related, and that class variables are kind of 'inherited' to the 'self' variables. To illustrate this, Corey shows an example of 'annual raise of pay'. He initially creates the class variable to show a case where annual raise is equal among all the employees. This variable of 1.04 was accessible through each instance, and also through the class itself(obiviously). That is,
print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_2.anual_rais)
all printed out 1.04.


However, using the ._dict__  thing, Corey shows that the intances, emp_1 and emp_2 does not contain the annual_raise value. Corey explains that if a variable is not found within an instance and programmers try to access the variable, python automatically looks in in the variable of the instance's class, and then the more classes that the instance's class inherits from.


Furthermore, if we access the class variable through an instance and then change it, python creates the variable within the instance. We can check it by using the ._dict_ thing. Corey shows that annual_raise key was created when he manually changed the annual_raise value as 1.05 in the following way.
emp_1.annual_raise = 1.05
however, we know that the class variable remained the same at 1.04, when printing the class variable.
print(Employee.annual_raise"""

class Employee:

    raise_amount = 2

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Vishal', 'Shirke', 10000000)
emp1.raise_amount = 3
emp1.apply_raise()
print(emp1.pay)


emp2 = Employee('Prashant', 'Shirke', 10000000)
emp2.apply_raise()
print(emp2.pay)


class Employee:

    def __init__(self, first_name, last_name, pay):
        self._first_name = first_name
        self.__last_name = last_name
        self.__pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name


emp1 = Employee('Vishal', 'Shirke', 10000000)
print(emp1.get_first_name(), emp1.get_last_name())
emp1.set_first_name('john'), emp1.set_last_name('wil')
print(emp1.get_first_name(), emp1.get_last_name())
print(emp1._first_name)
# print(emp1.get_last_name())