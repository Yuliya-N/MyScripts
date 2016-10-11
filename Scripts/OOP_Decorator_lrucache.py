from time import sleep
from functools import wraps
from pdb import set_trace

class Lru_cache2:
	def __init__(self, cache_size):
		self.cache_size = cache_size
		self.cache_dict = {} # HW one dictionary with lists of values [res,count]
		self.cache_times = {}
	def __call__(self, f):
		@wraps(f)
		def wrapper(*args):
			#set_trace()
			if args in self.cache_dict:
				self.cache_times[args] = self.cache_times[args] + 1
				return self.cache_dict[args]
			else:
				res = f(*args)
				self.cache_times[args] = 0
				if len(self.cache_times) >= self.cache_size:
					print('Cache overflow')
					# min(iterator, key = function that returns one argument) and that compares by min
					min_times_key = min(self.cache_dict, key = self.cache_dict.get)
					self.cache_dict.pop(min_times_key)
					self.cache_times.pop(min_times_key)
				self.cache_dict[args] = res
				self.cache_times[args] = self.cache_times[args] + 1
			return 'Result: {}'.format(res), 'dict: {}'.format(self.cache_dict), 'times: {}'.format(self.cache_times) 
		return wrapper
	

@Lru_cache2(3)
def slow_func(x):
	"""
	 Function Description: slow function to test cache
	"""
	sleep(x)
	return x
# x = lru_cache2(3)

# print(slow_func(3))
# print(slow_func(3))
# print(slow_func(2))
# print(slow_func(1))
# print(slow_func(1))
# print(slow_func(4))
# print(slow_func(4))
# print(x.__dict__)
#help(slow_func)
#print(slow_func)
slow_func(3)


if __name__ == '__main__':
	l = Lru_cache2(32)
	assert l.cache_size == 32
