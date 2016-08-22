#The __init__ method is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.
# Notice the double underscore both in the beginning and at the end in the name.


class Person(object):
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print 'Hello, my name is', self.name

p = Person('Swaroop')
p.sayHi()