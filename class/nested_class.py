class Student:

	def __init__(self, name, roll_no):
		self.name = name
		self.roll_no = roll_no
		self.lap = self.Laptop()

	def show(self):
		self.lap.show()

	class Laptop:
		def __init__(self):
			self.brand = 'Dell'
			self.cpu = 'i10'
			self.ram = 4

		def show(self):
			print(self.brand)


s1 = Student('Vishal', 1)
s2 = Student('Corey', 2)

print(s1.lap.brand)

l1 = s1.lap
l2 = s2.lap
print(l1, l2)

l1 = Student.Laptop()

s1.show()