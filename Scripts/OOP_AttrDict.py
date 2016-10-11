class AttrDict(dict): # naslidujemos vid slovnyka
		
	def __getattr__(self, name):
		try:
			return self[name]
		except KeyError:
			raise AttributeError
		
	def __setattr__(self, name, value):
		self[name] = value
	
x = AttrDict()
x['key1'] = 1
x['key2'] = 2
print(x.key1, x.key2)
