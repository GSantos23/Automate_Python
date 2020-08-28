while True:
	print('Enter you age: ')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for age')

while True:
	print('Select a new password (letters and numbers only):')
	password = input()
	if password.isalnum():
		break
	print('Passwords can only have letters and numbers')