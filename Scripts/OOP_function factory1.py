def add_factory(k): # take argument - and transmitt it to function
	def adder(n): # take argument and do smth 
		return n + k # returns function result
	return adder # return function

add3 = add_factory(3)
a100add = add_factory(100) # external function value


print(add3(5))
print (a100add(40)) # internal function value