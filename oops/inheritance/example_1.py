# # # Inheritance
# # # Refer WSGI exception module of python
# # # Simple Inheritance
# # class Employee(object):
# #     raise_amt = 1.04

# #     def __init__(self, first, last, pay):
# #         self.first = first
# #         self.last = last
# #         self.email = first + '.' + last + '@email.com'
# #         self.pay = pay

# #     def fullname(self):
# #         return f'{self.first} {self.last}'

# #     def apply_raise(self):
# #         self.pay = int(self.pay * self.raise_amt)


# # class Developer(Employee):
# #     raise_amt = 2
# #     pass

# # # dev1 = Developer('Vishal', 'Shirke', 100000000)
# # # dev2 = Developer('Corey', 'Schafer', 200000000)
# # # print(dev1.pay) 
# # # print(dev2.pay)  
# # # dev1.apply_raise()
# # # print(dev1.pay) 
# # # print(dev2.pay)  


# # # MRO - use help() mehtod
# # # # Addiitonal work in child class
# # class Employee(object):
# #     raise_amt = 1.04

# #     def __init__(self, first, last, pay):
# #         self.first = first
# #         self.last = last
# #         self.email = first + '.' + last + '@email.com'
# #         self.pay = pay

# #     def fullname(self):
# #         return f'{self.first} {self.last}'

# #     def apply_raise(self):
# #         self.pay = int(self.pay * self.raise_amt)

# # class Developer(Employee):
    
# #     def __init__(self, first, last, pay, prog_lang):
# #         super().__init__(first, last, pay)
# #         # OR
# #         # Employee.__init__(self, first, last, pay)
# #         self.prog_lang = prog_lang

# # dev1 = Developer('Vishal', 'Shirke', 100000000, 'Python')
# # dev2 = Developer('Corey', 'Schafer', 200000000, 'Java')
# # print(dev1.email, dev1.prog_lang) 
# # print(dev2.email, dev2.prog_lang)


# # # Big example

# # class Manager(Employee):

# #     def __init__(self, first, last, pay, employees=None):
# #         super().__init__(first, last, pay)
# #         if employees is None:
# #             self.employees = []
# #         else:
# #             self.employees = employees

# #     def add_emp(self, emp):
# #         if emp not in self.employees:
# #             self.employees.append(emp)

# #     def remove_emp(self, emp):
# #         if emp in self.employees:
# #             self.employees.remove(emp)

# #     def print_emps(self):
# #         for emp in self.employees:
# #             print('-->', emp.fullname())


# # dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# # dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# # mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# # print(mgr_1.email)

# # mgr_1.add_emp(dev_2)
# # mgr_1.remove_emp(dev_2)

# # mgr_1.print_emps()



# class TestClass:


#     var1 = "hello"


#     def __init__(self):


#         self.var2 = "computer"


#         self.var_type = type(self.var2)


#     def test_incrementer(self, x):


#         return x+1


# test = TestClass()


# print(test.__dict__)


# incrementor = test.test_incrementer(1)


# setattr(test, "var2", incrementor)


# print(test.__dict__)


# class DynamicPatching:

#     def function(self):

#         print("Hi function")

#     def patcher():

#         print("Hi patcher")

# d = DynamicPatching()
# print(isinstance(d, DynamicPatching))