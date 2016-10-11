# x = raw_input('Enter Number: ')
# i = 1
# k = 2
# def multi_tab():
# while k <= x:	
# 	while i <= x:
# 			print ('  ' k * i '|  ')
# 			i = i + 1
def table(x):
	d1 = range (1, x+1)
	d2 = range (1, x+1)
	table = []
	
	for j in d1:
		line = []
		for i in d2:
			line.append(j * i)
		table.append(line)

	for k in table:
		print(k)
table(6)	
