# help()
class Employee(object):
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    pass

dev1 = Developer('Vishal', 'Shirke', 100000000)
dev2 = Developer('Corey', 'Schafer', 200000000)

print(help(Developer))