class Pycharm:

	def execute(self):
		print('Compiling')
		print('Running')

class MyEditor:

	def execute(self):
		print('Spell Check')
		print('Compiling')
		print('Running')


class Laptop:

	def code(self, ide):
		ide.execute()


ide = Pycharm()
ide1 = MyEditor()

lap1 = Laptop()
lap1.code(ide1)