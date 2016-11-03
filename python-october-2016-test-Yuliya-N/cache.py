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
from datetime import datetime


class lru_cache:
    def __init__(self, cache_size=3):
        self.cache_size = cache_size
        self.cache_dict = {} # HW one dictionary with lists of values [res,count]
        # self.cache_times = {}

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args):
            if args in self.cache_dict:
                print(self.cache_dict[args][1])
                print("Change time")
                self.cache_dict[args][1] = datetime.now()
                print(self.cache_dict[args][1])
                res = self.cache_dict[args][0]
                return 'Result: {}'.format(res), 'dict: {}'.format(self.cache_dict)
            else:
                res = f(*args)
                # self.cache_times[args] = 0
                if len(self.cache_dict) >= self.cache_size:
                    print('Cache overflow')
                    # min(iterator, key = function that returns one argument) and that compares by min
                    oldest_key = min(self.cache_dict, key=getitem(self.cache_dict.get, 1))
                    self.cache_dict.pop(oldest_key)
                    # self.cache_times.pop(oldest_key)
                self.cache_dict[args] = [res, datetime.now()]
                #self.cache_times[args] = datetime.now()
            return 'Result: {}'.format(res), 'dict: {}'.format(self.cache_dict)
        return wrapper


@lru_cache(2)
def heavy_func(x):
    """
     Function Description: slow function to test lru_cache
    """
    sleep(x)
    print(x)
    return x


# x = lru_cache(3)
print(heavy_func(10))
print(heavy_func(10))
print(heavy_func(2))
print(heavy_func(1))
# print(heavy_func(1))
# print(heavy_func(4))
# print(heavy_func(4))
# print(x.__dict__)
#help(heavy_func)
#print(heavy_func)
# heavy_func(3)


if __name__ == '__main__':
    l = lru_cache(32)
    assert l.cache_size == 32
