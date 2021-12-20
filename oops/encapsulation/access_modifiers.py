# PUBLIC MEMBER     =========================================================>

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

emp = Employee('Jessa', 10000)

print("Name: ", emp.name, 'Salary:', emp.salary)

emp.show()


# PRIVATE MEMBER      =========================================================>
# 1. using public method
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

emp = Employee('Jessa', 10000)
emp.show()

# 2. Using name mangling
class Employee:
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

emp = Employee('Jessa', 10000)
print('Name:', emp.name)
print('Salary:', emp._Employee__salary)


# PROTECTED MEMBER   =========================================================>

class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)