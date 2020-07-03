board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter
    
def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def isWinner(bo, letter):
    return((bo[7] == letter and bo[8] == letter and bo[9] == letter) or
	(bo[4] == letter and bo[5] == letter and bo[6] == letter) or
	(bo[1] == letter and bo[2] == letter and bo[3] == letter) or
    (bo[1] == letter and bo[4] == letter and bo[7] == letter) or
	(bo[2] == letter and bo[5] == letter and bo[8] == letter) or
	(bo[3] == letter and bo[6] == letter and bo[9] == letter) or
    (bo[1] == letter and bo[5] == letter and bo[9] == letter) or
	(bo[3] == letter and bo[5] == letter and bo[7] == letter))
