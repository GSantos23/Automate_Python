'''
Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. 
Write a function named isValidChessBoard() that takes a dictionary argument and
returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces
must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space
'9z' . The piece names begin with either a 'w' or 'b' to represent white or
black, followed by 'pawn' , 'knight' , 'bishop' , 'rook' , 'queen' , or 'king' . 

This function should detect when a bug has resulted in an improper chess board.
'''

def isValidChessBoard(chessBoard):
	# Verify correct position	************************************************
	for x in chessBoard.keys():
		if x[1] > 'h':				# if postion is greater than h invalid
			return False
		elif x[1].isnumeric():		# if 2 position of key string is a number invalid 
			return False
		elif x[0] == '9':			# 9 position
			return False


	# Verify white and black pieces only **************************************
	for c in chessBoard.values():
		if c[0] == 'b' or c[0] == 'w':
			isBW = True
		else:
			return False


	# Verify number of paws **************************************************
	wpawn = 0
	bpawn = 0

	for x in chessBoard.values():
		if x =='bpawn':
			bpawn += 1
		elif x == 'wpawn':
			wpawn += 1
	if wpawn > 8 or bpawn > 8:
		return False


	# Verify number of pieces on board ****************************************
	sizeOfDict = len(chessBoard.keys())

	if sizeOfDict > 16:
		return False
	else:
		return True


	# Verify the other pieces *************************************************
	pieces = ['wking', 'bking', 'wpawn' , 'wknight' , 'wbishop' , 'wrook' , 'wqueen',
			  'bpawn' , 'bknight' , 'bbishop' , 'brook' , 'bqueen']

	for y in pieces:
		if x in chessBoard.values():
			if chessBoard[y] not in range(1,3):
				return False


	# Verify if valid position '1a' to '8h'	***********************************
	for x in sample6.keys():
		if x[1] > 'h':				# if postion greater than h invalid
			return False
		elif x[1].isnumeric():		# if 2 position of string a number invalid 
			return False
		elif x[0] == '9':			# 9 position
			return False


	# This part check for bking and wking *************************************
	if 'bking' in chessBoard.values():
		isBKing = True;
	else:
		isBKing = False;

	if 'wking' in chessBoard.values():
		isWKing = True;	
	else:
		isWKing = False;

	if isBKing and isWKing:
		#print('Valid Chess Board')
		return True


#******************************************************************************
sample1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
'''
# Board with more that 16 pieces
sample2 = {'1h': 'bking', '2c': 'wqueen', '3g': 'bbishop', 
			'4h': 'bqueen', '5e': 'wking', '6g': 'bbishop',
			'7g': 'bbishop', '8g': 'bbishop', '9g': 'bbishop',
			'10g': 'bbishop', '11g': 'bbishop', '12g': 'bbishop',
			'13g': 'bbishop', '14g': 'bbishop', '15g': 'bbishop',
			'16g': 'bbishop'
			#'2g': 'bbishop'
		  }

# No white and black
sample3 = {'1h': 'rking', '6c': 'rqueen', '2g': 'rbishop', '5h': 'rqueen', '3e': 'rking'}

# Pawns
sample4 = {'1h': 'wpawn', '2c': 'wpawn', '3g': 'wpawn', '4h': 'wpawn', '5e': 'wpawn',
			'6h': 'wpawn', '7e': 'wpawn', '8h': 'wpawn', '9e': 'wpawn'}
		   

#sample5 = {'1h': 'aking', '6c': 'bqueen', '2g': 'cbishop', '5h': 'dqueen', '3e': 'eking'}
sample5 = {'1h': 'bking', '6c': 'wking'}


# Verify if valid position '1a' to '8h'
sample6 = {'99z': 'king', '6c': 'wing'}
'''

S1 = isValidChessBoard(sample1)
print(S1)
'''
S2 = isValidChessBoard(sample2)
print(S2)
S3 = isValidChessBoard(sample3)
print(S3)
S4 = isValidChessBoard(sample4)
print(S4)
S5 = isValidChessBoard(sample5)
print(S5)
S6 = isValidChessBoard(sample6)
print(S6)
'''
print('Done')

