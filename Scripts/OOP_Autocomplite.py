class Trie:
	def __init__(self, words=[]):
		self.list = words
	def __repr__(self):
		return self.list
	def __add__(self, li):
		return self.list.append(li)

t = Trie(['apple', 'ape'])
l = 'ap'
print(t.__dict__)
print(t + l)
print(t.__dict__)