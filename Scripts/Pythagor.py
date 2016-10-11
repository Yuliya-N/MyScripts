from itertools import count

k = int(raw_input('Please, enter the number of triples:' ))

def pythagor_triples(k): 
	z = 1
	t = []
	# while len(t) < k: 
	# 	z += 1
	# 	for y in range(1, z): 
	# 		for x in range(1, y):
	# 			if (x**2 + y**2) == z**2:
	# 				t.append([x,y,z])
	
	# list comprehention - O(N**3)- algorighm complication
	g = ([x,y,z] for z in count() for y in range(z) for x in range(y) if (x**2 + y**2) == z**2)
	for i in range(k):
		t.append(next(g))
	return t

print(pythagor_triples(k))				
		
# 	m = 2 -- pre-mature optimization, unexplicite
# 	n = 1

# 	x = 1
# 	y = 1
# 	z = 1
# 	i = 1
# 	while i <= k:
# 		x = m**2 - n**2
# 		y = 2*m*n
# 		z = m**2 + n**2
# 		print(x, y, z) 
# 		m += 1
# 		n += 1
# 		i += 1

pythagor_triples(k)

	