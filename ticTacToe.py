 
import random
from pprint import pprint

debug = True

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    if debug == True:
        print '*** inputPlayerLetter***'

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print 'Do you want to be X or O?' 
        letter = raw_input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if debug == True:
        print '*** whoGoesFirst ***'

    print 'Would you like to go first? (yes or no)'
    response = raw_input().lower()

    if response == 'no':
        return 'computer'
    else:
        return 'player'

def drawBoard(board):
    # This function prints out the board that it was passed.
    if debug == True:
        print '*** drawBoard ***'

    print 'board = ' 
    print theBoard

    columns = [range(1 + BOARDSIZE*i, BOARDSIZE+1 + BOARDSIZE*i) for i in range(BOARDSIZE)]
    print 'columns:'
    print columns

    rows = [range(1 + BOARDSIZE*i, BOARDSIZE+1 + BOARDSIZE*i) for i in range(BOARDSIZE)]
    print 'rows:'
    pprint (rows)

    #horiz
    #topleft
    #topright
    #cross

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print '   |   |'
    print ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8]
    print '   |   |'
    print '-----------'
    print '   |   |' 
    print ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5]
    print '   |   |'
    print '-----------'
    print '   |   |'
    print ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2]
    print '   |   |'

def getPlayerMove(board):
    # Let the player type in his move.
    if debug == True:
        print '*** getPlayerMove ***'

    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print 'What is your next move? (1-9)'
        move = raw_input()
    return int(move)

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    if debug == True:
        print '*** isSpaceFree ***'
        print 'theBoard[move]:'
        print theBoard[move-1]

    if theBoard[move-1] != None:
        return True
    else:
        return false

    #return board[move] == ' '

def makeMove(board, letter, move):
    if debug == True:
        print '*** makeMove ***'
        print 'board:',board
        print 'letter',letter
        print 'move',move


    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.

    if debug == True:
        print '*** isWinner ***'

    #this sucks. let's do list comprehension.

    columns = [[range (1 + BOARDSIZE*i, BOARDSIZE+1 + BOARDSIZE*i, BOARDSIZE) for i in range(BOARDSIZE)] for i in range(BOARDSIZE)]
    print 'columns'
    print columns

    rows = [range(1 + BOARDSIZE*i, BOARDSIZE+1 + BOARDSIZE*i) for i in range(BOARDSIZE)]
    print 'rows:'
    pprint (rows)

    diagonal = []


    '''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
    '''

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    if debug == True:
        print '*** getBoardCopy ***'

    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    if debug == True:
        print 'chooseRandomMoveFromList'

    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if debug == True:
        print 'getComputerMove'

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    '''
Win: If the player has two in a row, they can place a third to get three in a row.
Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
Fork: Create an opportunity where the player has two threats to win (two non-blocked lines of 2).
Blocking an opponent's fork:
Option 1: The player should create two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork. For example, if "X" has a corner, "O" has the center, and "X" has the opposite corner as well, "O" must not play a corner in order to win. (Playing a corner in this scenario creates a fork for "X" to win.)
Option 2: If there is a configuration where the opponent can fork, the player should block that fork.
Center: A player marks the center. (If it is the first move of the game, playing on a corner gives "O" more opportunities to make a mistake and may therefore be the better choice; however, it makes no difference between perfect players.)
Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
Empty corner: The player plays in a corner square.
Empty side: The player plays in a middle square on any of the 4 sides.
    '''

    #TODO: fix this later when expanding to n
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    if debug == True:
        print 'isBoardFull'

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    if debug == True:
        print 'playAgain'

    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')

print 'Welcome to Tic Tac Toe!'
print 'How big do you want the board to be? (n x n)'
BOARDSIZE = int(raw_input())

while True:
    # Reset the board
    
    theBoard = []
    for i in range (1, BOARDSIZE^2):
        theBoard.append(str(i))
    print theBoard
    
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print 'The ' + turn + ' will go first.'
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print 'Hooray! You have won the game!'
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print 'The game is a tie!'
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print 'The computer has beaten you! You lose.'
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print 'The game is a tie!'
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
