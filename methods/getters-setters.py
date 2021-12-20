# https://www.geeksforgeeks.org/getter-and-setter-in-python/
# Problem is that if we change a instance variable it is not reflected in another
class Employee1:


    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# e1 = Employee1('Vishal', 'Shirke')
# e1.first = 'Prashant'
# print(e1.fullname())
# print(e1.email)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        print("Getter Called")
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, fullname):
        self.first, self.last = fullname.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None 

e1 = Employee('Vishal', 'Shirke')
# e1.first = 'Prashant'
# print(e1.email)
# print(e1.fullname)
e1.fullname = 'Vishal Shirke'
print(e1.email)
print(e1.fullname)
del  e1.fullname