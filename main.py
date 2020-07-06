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
    
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    printBoard('Sorry, this place is occupied')
            else:
                print('Please type a number between 1 and 9')
        except:
            print('Please type a number')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break
        
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie game!')
            else:
                insertLetter('O', move) 
                print('Computer placed an \'O\' in position ', move, ':')
                printBoard(board)
        else:
            print('You won!')
            break
    
    if isBoardFull(board):
        print('Tie game!')   
   
main()