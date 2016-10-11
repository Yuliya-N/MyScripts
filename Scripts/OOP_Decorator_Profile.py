""" @profile decorator returns the time of the function execution.
Optionally, can take the test and return it before the time of execution.
The following code evaluates if the argument is a functiona or a text and navigates to an appropriate behavior:
if callable(arg):
			return wrapper(arg, text = 'Default text')
		else:
			return wrapper
"""

from datetime import datetime
from time import sleep
# from time import time - would be faster

def profile(arg):
	# if callable(arg):
	# 	def wrapped(*args,**kwargs):
	# 		start = datetime.now()
	# 		res = arg(*args,**kwargs)
	# 		end = datetime.now()
	# 		# print(text, end-start)
	# 		print('{} {}'.format ('Default text', end-start))
	# 		return res
	# 	return wrapped
	# else:	
		def wrapper(f, text = arg):
			def wrapped(*args,**kwargs):
				start = datetime.now()
				res = f(*args,**kwargs)
				end = datetime.now()
				
				print('{} {}'.format (text, end-start))
				return res
			return wrapped
		# wrapper(arg, text = 'Default text') returns wrapped
		if callable(arg):
			return wrapper(arg, text = 'Default text')
		else:
			return wrapper

@profile
def talker():
	sleep(1) # delay 1 sec
	print('Talker talks')

@profile('Time is:')
def fibo(k): # fibonacci
	a, b, n = 1, 1, 2
	while n < k: 
		a, b, n = b, a + b, n + 1
	return len(str(b))

# Checks
# x = fibo(50000)
# print(x)
# talker()
