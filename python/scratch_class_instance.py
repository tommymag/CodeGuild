class person:

	def __init__(self, name, age='unknown'):
		self.name = name
		self.age = age

	def __repr__(self):
		return self.name

	# def pretty_print(name, age):
	# 	print()

bob = person('Bob', 55)
tom = person('Tom')

print(bob)
print(bob.age)
print(bob, bob.age)
print(bob.__repr__())
print(tom.age)