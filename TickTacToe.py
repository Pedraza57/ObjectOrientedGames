###BOARDS#############################################################################
board = [' ', '1','2','3','4','5','6','7','8','9',' ']
test_board = ['#','X','O','X','O','X','O','X','O','X']
def display_board(board):
    print (board[7]  + "|" + board[8] + "|" + board [9])
    print (board[4]  + "|" + board[5] + "|" + board [6])
    print (board[1]  + "|" + board[2] + "|" + board [3])
display_board(board)    
#######################################################################################
def player_input():
    marks = ''
    while marks not in ('x', 'o'):
        marks = input('Player 1 chose your mark (x or o): ')
        if marks == 'x':
            return ('x', 'o')
        else:
            return ('o','x') 
    return marks
########################################################################################
def place_marker(board, marker, position):
    board[position] = marker

########################################################################################
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
#########################################################################################
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return f'Player 2 goes first'
    else:
        return f'Player 1 goes first'
#########################################################################################
def space_check(board, position):
    if board[position] == ' ':
        return True
    return False
            

##########################################################################################
def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    return True
########################################################################################
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
########################################################################################
def replay():
    choice = input('play again? enter yes or no: ')
    return choice == 'yes'
#########################################################################################   
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = str(input('Are you ready to play? Enter Yes or No.'))
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #Dsiplay the board
            display_board(theBoard)
            #Chose the position
            position = player_choice(theBoard)
            #place the marker on the postion chosen 
            place_marker(theBoard, player1_marker, position)
            #Check if won
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break


