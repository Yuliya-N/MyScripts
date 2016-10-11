from random import randint
limit = int(input('Enter upper bounder: '))

towns1 = [randint(1,limit) for i in range(1, limit+1)]
towns2 = [randint(1,limit) for i in range(1, limit+1)]
direct_routs = zip(towns1, towns2)
print(towns1)
print(towns2)
print(list(direct_routs))

departure = int(input('Enter departure number: '))
arrival = int(input('Enter arrival number: '))

if departure not in (towns1 or towns2):
	print('No departure town in a map')
elif arrival not in (towns1 or towns2):
	print('No arrival town in a map')
elif towns1[departure] == towns2[arrival]:
	print('Direct route found')
elif towns2[departure] == towns1[arrival]:
	print('Direct route found')
#elif departure in direct_routs:

#else:

