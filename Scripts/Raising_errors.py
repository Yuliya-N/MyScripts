def a():
	return b() + 1

def b():
	return c() + 2

def c():
	try:
		return d() + 3
	except ZeroDivisionError:
		print('Zero division at c() level')
		raise

def d():
	return 1/0

print (a())