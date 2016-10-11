class MyClass:
	def __init__(self):
		self.calls = []
	def __call__(self, number):
		self.calls.append(number)
		return sum(self.calls) / len(self.calls)


avg = MyClass()
print(avg(3))
print(avg(5))
print(avg(1))

