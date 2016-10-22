"""
Implement least-recently used cache.
The structure you'll implement should be used as decorator for functions

>>> @lru_cache
... def heavy_func(...):
...     ...

Functions decorated with lru_cache should not run when called, but return
 cached result instead.

Optional argument with "calls to remember" can be passed while decorating:

>>> @lru_cache(10)
... def func(...):
...     ...

 which forces lru_cache to remember only last 10 calls to this function

When used without argument, some default call limit should be used
When there's no space for new result, oldest call result should be evicted.
You can use `functools.lru_cache` as reference interface
 but can't use it directly.

Write tests for your implementation,
 using any standart testing library is a plus.


Bonus: make your cache persistent, so caching works between python runs,
 and cached data saved in filesystem. You may assume single-thread usage
 of your code.
"""
from time import sleep
from functools import wraps
from pdb import set_trace


class lru_cache:
    def __init__(self, cache_size=3):
        self.cache_size = cache_size
        self.cache_dict = {} # HW one dictionary with lists of values [res,count]
        self.cache_times = {}

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args):
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


@lru_cache(10)
def heavy_func(x):
    """
     Function Description: slow function to test lru_cache
    """
    sleep(x)
    print(x)
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
# heavy_func(3)


if __name__ == '__main__':
    l = lru_cache(32)
    assert l.cache_size == 32
