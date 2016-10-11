a, b, n = 1, 1, 2
#fibs = [1, 1]
while n < 100000: # b <= 10**999: # <-- faster; len(str(b)) <= 1000; # b < 10**7
	# c= a+b
	# a=b
	# b=c
	a, b, n = b, a + b, n + 1
	#fibs.append(fibs[-2] + fibs [-1])

print(len(str(b)))

# i = 1
# k = 1
# for k < 10000000:
# 	i = k
# 	t = k + i
# 	k = t

