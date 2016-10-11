Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Account:
	pass
a = Account()
SyntaxError: invalid syntax
>>> class Account:
	pass
a = Account()
SyntaxError: invalid syntax
>>> class Account():
	def __init__(self, initial_balance=0):
		self.balance = initial_balance

		
>>> a = Account()
>>> class Car:
	def __init__(self, model, color):
		self.vendor, self.color = model.split (' ', 1)
	def __repr__(self):
		return 'Car ({} {}, {})'.format(self.vendor, self.model, self.color)

	
>>> x = Car('Audi TT 2003', color ='Grey')
>>> print (repr(x))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (repr(x))
  File "<pyshell#12>", line 5, in __repr__
    return 'Car ({} {}, {})'.format(self.vendor, self.model, self.color)
AttributeError: 'Car' object has no attribute 'model'
>>> x = Car(model ='Audi TT 2003', color ='Grey')
>>> print (repr(x))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (repr(x))
  File "<pyshell#12>", line 5, in __repr__
    return 'Car ({} {}, {})'.format(self.vendor, self.model, self.color)
AttributeError: 'Car' object has no attribute 'model'
>>> class Car:
	def __init__(self, model, color):
		self.vendor, self.model = model.split (' ', 1)
	def __repr__(self):
		return 'Car ({} {}, {})'.format(self.vendor, self.model, self.color)

	
>>> x = Car('Audi TT 2003', color ='Grey')
>>> print (repr(x))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print (repr(x))
  File "<pyshell#18>", line 5, in __repr__
    return 'Car ({} {}, {})'.format(self.vendor, self.model, self.color)
AttributeError: 'Car' object has no attribute 'color'
>>> class Car:
	def __init__(self, model, color):
		self.vendor, self.model = model.split (' ', 1)
		self.color = color
	def __repr__(self):
		return 'Car ({} {}, {})'.format(self.vendor, self.model, self.color)
