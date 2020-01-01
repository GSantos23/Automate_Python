'''
Write a short program that prints the numbers 1 to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using
a while loop.
'''

#'''
print('Using for loop')
for  i in range(1,11):
    print(i, end=' ')       # end='', allow to print in the same line

print()

print('Using while loop')
j = 1
while j < 11:
    print(j, end=' ')
    j = j + 1

print()