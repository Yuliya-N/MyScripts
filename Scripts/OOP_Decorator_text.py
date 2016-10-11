
def b(f):
	def wrapper(*args, **kwargs):
		return '<b>'+ f(*args, **kwargs) + '</b>' # returns text with tags added
	return wrapper
def i(f):
	def wrapper(*args, **kwargs):
		return '<i>'+ f(*args, **kwargs) + '</i>' # returns text with tags added
	return wrapper

def div(color): # decorators one in another
	def wrapper(f):
		def wrapped(*args, **kwargs):
			return '<div style="background-color: {}">'.format(color)+ f(*args, **kwargs) + '</div>' # returns text with tags added
		return wrapped
	return wrapper

@b #2 decorators if they work properly and do not change func
@i
@div("#6FB") # decorators one in another
def get_day():
	return 'Monday'

with open ('html_test.html', 'w') as f:
	f.write(get_day())
	
print(get_day())
