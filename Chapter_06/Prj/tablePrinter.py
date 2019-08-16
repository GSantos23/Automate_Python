"""
Table Printer
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:

---------------------------------------------------------------------------
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
----------------------------------------------------------------------------

Your printTable() function would print the following:

----------------------------------------------------------------------------        
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
-----------------------------------------------------------------------------

Hint: Your code will first have to find the longest string in each of the
inner lists so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers. The
printTable() function can begin with colWidths = [0] * len(tableData) , which
will create a list containing the same number of 0 values as the number
of inner lists in tableData . That way, colWidths[0] can store the width of the
longest string in tableData[0] , colWidths[1] can store the width of the lon-
gest string in tableData[1] , and so on. You can then find the largest value in
the colWidths list to find out what integer width to pass to the rjust() string
method.
"""

def printTable(table):
    ''' Returns a well-organized list of list '''
    maximum = [0] * len(table)    # width of longest string tableData[0]

    for i in range(len(table)):
        maximum[i] = max(len(x) for x in table[i]) 
    #print(maximum)  # list with maximum string for rjust()

    '''
    DONT FORGET Author:
        To access a list of list, you can use multiple indexes (page 81)

        spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
        >>> spam[0]
        ['cat', 'bat']
        >>> spam[0][1]
        'bat'
        >>> spam[1][4]
        50
    '''
    for j in range(len(table[0])):
        for k in range(len(table)):
            print(table[k][j].rjust(maximum[k]), end=' ')  
        print()


#******************************************************************************

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)