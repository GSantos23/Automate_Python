'''
Write code that prints Hello if 1 is stored in spam , prints Howdy if 2 is
stored in spam , and prints Greetings! if anything else is stored in spam .
'''

print('Please type a value for: ')
spam = input()
if spam == str(1):
    print('Hello')
elif spam == str(2):
    print('Howdy')
else:
    print('Greetings!')

