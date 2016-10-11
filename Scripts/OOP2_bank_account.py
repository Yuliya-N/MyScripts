class Account():
	def __init__(self, initial_balance=0):
		self._balance = initial_balance	
	
	@property
	def balance(self):
		return self._balance

	def deposit(self, sum=0):
		self._balance += sum
		print('You have an income {}'.format(sum), '\nYour current balance is:', self._balance)


	def withdraw(self, sum):
		if sum > self._balance:
			print('Not enough money')
		else:
			self._balance -= sum
			print('You have withdrawal {}'.format(sum), '\nYour current balance is:', self._balance)

	def transfer(self, receiver, sum):
		#self.withdraw()
		#receiver.deposit()
		if sum > self._balance:
			print('Not enough money')
		else:
			self._balance -= sum
			receiver._balance += sum

class PaymentAccount():
	def deposit(self):
		print('Deposit is not allowed for the Payment Account')

MyAccount = Account(100)
# MyAccount.balance = 100
# MyAccount.sum = 15
# MyAccount.deposit(15)
MyAccount.withdraw(16)
a = Account(10)
print (a.balance) # returns function like simple attribute, better data abstraction



