'''
Say you have a list value like this:
---------------------------------------------
spam = ['apples', 'bananas', 'tofu', 'cats']
---------------------------------------------
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats' . But your func-
tion should be able to work with any list value passed to it.
'''

def commaList(listVal):
    for i in range(len(listVal)-1):
        print(listVal[i], end=', ')
    print('and ' + str(listVal[-1]))



spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['Zophie', 'Pooka', 'Simon', 'Lady Macbeth', 'Fat-Tail', 'Miss Cleo']
commaList(spam)
print()
commaList(spam2)
print()