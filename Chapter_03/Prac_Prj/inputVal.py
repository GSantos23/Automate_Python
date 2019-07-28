'''
Add try and except statements to the previous project to detect whether the
user types in a noninteger string. Normally, the int() function will raise a
ValueError error if it is passed a noninteger string, as in int('puppy') . In the
except clause, print a message to the user saying they must enter an integer.
'''
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return (number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)
        return (3 * number + 1)


print('Enter number:  ')

try:
    value = collatz(int(input()))
    value2 = 0                        # Add dummy value to swap value during loop

    while value2 != 1:
        value2 = collatz(value)
        value = value2

except (ValueError, NameError):      # Possible error to catch 
    print('You must use an integer')