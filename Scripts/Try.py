"""
 Description of program: lfu_cache - list frequently used
 Params: positional..., keyword...
 Result resurns...
"""
def outer (f):
	def wrapper (*args, **kwargs):
		print ('Wrapper before call')
		return f(*args, **kwargs)
		# print ('Wrapper after call') - nothing returns after return
	return wrapper

@outer
def talker(a,b, c):
	print ('Talker talks')
	return a + b + c

# x = outer(talker)

# print(talker(*[10, 20, 30]))
# print(talker(**{ 'a': 't', 'b': 'g', 'c': 'u'}))
# func = lambda: 42
# print(__name__)
# if __name__ == '__main__':
# 	print("I'm running")
