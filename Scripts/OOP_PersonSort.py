class Person:
	def __init__(self, first, last):
		self._first = first
		self._last = last
	def __repr__(self):
		return 'Person('+ self._first + ',' + self._last +')'
	def __eq__(self, other):
		return self._first == other._first and self._last == other._last
	def __lt__(self, other):
		if self._last != other._last:
			return self._last < other._last
		else:
			return self._first < other._first
	def __gt__(self, other):
		if self._last != other._last:
			return self._last > other._last
		else:
			return self._first > other._first


p1 = Person('Yuliya', 'Nykytenko')
p2 = Person('Alexandr', 'Nykytenko')
p3 = Person('Nadia','Khimchak')

name_list = [p1, p2, p3]
name_list.sort()
print(name_list)