x = raw_input('Enter Number: ')
try:
	x = float(x)
	print(100/x)
except (ValueError, ZeroDivisionError):
	print("It's not a correct number")

	

	