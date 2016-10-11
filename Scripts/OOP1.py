Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Monkey:
	def eat(self):
		print ('Yummy')

		
>>> m1 = Monkey()
>>> eat
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    eat
NameError: name 'eat' is not defined
>>> m1.age = 5
>>> m1.eat
<bound method Monkey.eat of <__main__.Monkey object at 0x02C947B0>>
>>> m1.age
5
>>> m1.eat()
Yummy
>>> from datetime import date
>>> date.today
<built-in method today of type object at 0x53F4B978>
>>> date.today()
datetime.date(2016, 9, 8)
>>> date.today().year
2016
>>> class Pet:
	pass

>>> p1 = Pet()
>>> p1.legs = 4
>>> p1.name = 'Fido'
>>> p1.age = 5
>>> p1.__dict__
{'age': 5, 'name': 'Fido', 'legs': 4}
>>> p1.__dict__['eyes'] = 'brown'
>>> p1.__dict__
{'name': 'Fido', 'legs': 4, 'eyes': 'brown', 'age': 5}
>>> type(p1)
<class '__main__.Pet'>
>>> class Person:
	def age(self):
		return 2016 - self.YOB

	
>>> p1 = Person()
>>> p1.YOB = 1985
>>> p1.age()
31
>>> p1.__dict__
{'YOB': 1985}
>>> Person.__dict__
mappingproxy({'__doc__': None, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__module__': '__main__', 'age': <function Person.age at 0x00865198>})
>>> class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

>>> 
>>> dog1 = Dog('Fido', 3)
>>> dog1
<__main__.Dog object at 0x02C94FD0>
>>> dog1.name
'Fido'
>>> dog1 = Dog('Fido', 3, legs=8)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dog1 = Dog('Fido', 3, legs=8)
TypeError: __init__() got an unexpected keyword argument 'legs'
>>> class Dog:
	def __init__(self, name = 'Aggy', age = 30):
		self.name = name
		self.age = age
