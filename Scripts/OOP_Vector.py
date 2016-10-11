import math
class Vector2D:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b
	def __repr__(self):
		return 'Vector2D({}, {})'.format(self.x, self.y)
	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y +other.y)
		# sum = (self.x + other.x, self.y + other.y)
		# print ('Result = Vector2D{}'.format(sum))
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	def __neg__(self):
		return Vector2D(-self.x, -self.y)
	def __mul__(self, other):
		return Vector2D(self.x*other, self.y*other)
	def __abs__(self):
	 	# return math.sqrt(self.x**2 + self.y**2)
	 	# return (self.x**2 + self.y**2)**0.5
	 	return math.hypot(self.x, self.y)

# v1 = Vector2D(3, 4)
# v2 = Vector2D(-4, 7)
# v3 = Vector2D(1, 3)
# print (v1, v2)
# print (v1 + v2)
# print (v1 == v2)
# print (v1 == v3)
# print(abs(v1))
# print(v2 + -v2)
# print(-v2)
# print (v3*5)


if __name__ == '__main__':
	v = Vector2D(3,2)
	assert v.x == 3
	assert str(v) == 'Vector2D(3,2)'
	assert abs(Vector2D(3,4)) == 5