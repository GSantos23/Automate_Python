'''
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with and inserted
before the last item. For example, passing the previous spam list to the
function would return 'apples, bananas, tofu, and cats' . But your function
should be able to work with any list value passed to it. Be sure to test the case
where an empty list [] is passed to your function.
'''

#------------------------------------------------------------------------------
def listWithArguments(param):
    for x in range(len(param)-1):
    	if x < len(param):
    		print(param[x], end=', ')

    print(param[-1])

# ****************************************************************************

spam = ['apples', 'bananas', 'tofu', 'cats']
empty = []

#listWithArguments(empty)
listWithArguments(spam)
print()
