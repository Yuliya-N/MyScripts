F = int(input('Please, enter number: '))
# fa = xrange(1, f)
# while i < f:
 	
def fact(x):
	f = 1
	if x <= 1:
		return 1
	else:
		for i in range(2,x):
			f = f * (i+1)
		return f
	# if x == 0:
	# 	return 1 # stops recursion when 0
	# return x * fact(x-1)

print (fact(F))