board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter
    
def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('  |  |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])