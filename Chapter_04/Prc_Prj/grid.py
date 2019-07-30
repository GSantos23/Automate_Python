'''
Say you have a list of lists where each value in the inner lists is a one-character
string, like this:
---------------------------------------

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

-----------------------------------------
You can think of grid[x][y] as being the character at the x- and
y-­coordinates of a “picture” drawn with text characters. The (0, 0) origin
will be in the upper-left corner, the x-coordinates increase going right,
and w the y-coordinates increase going down.
Copy the previous grid value, and write code that uses it to print the image.
--------------------------------

..00.00..
.0000000.
.0000000.
..00000..
...000...
....0....

-------------------------------

Hint: You will need to use a loop in a loop in order to print grid[0][0] ,
then grid[1][0] , then grid[2][0] , and so on, up to grid[8][0] . This will fin-
ish the first row, so then print a newline. Then your program should print
grid[0][1] , then grid[1][1] , then grid[2][1] , and so on. The last thing your
program will print is grid[8][5] .
Also, remember to pass the end keyword argument to print() if you
don’t want a newline printed automatically after each print() call.
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# in range for the value of range of grid
# grid[i][j] -> print original picture range(0,6), range(0,9)
# grid[j][i] -> print heart-shape picture range(0,9), range(0,6)
for i in range(0,6):
    print()
    for j in range(0,9):
        print(grid[j][i], end="")

print()