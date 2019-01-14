
# DESIGNING THE BOARD ON THE SCREEN

from IPython.display import clear_output

def display_board(board):
    print('     ' + '|' + '         ' + '|')
    print(board[7] + '    ' + '|' + '    ' +  board[8] + '    ' +  '|' + '    ' + board[9])
    print('     ' + '|' + '         ' + '|')
    print('---------------------')
    print('     ' + '|' + '         ' + '|')
    print(board[4] + '    ' + '|' + '    ' +  board[5] + '    ' +  '|' + '    ' + board[6])
    print('     ' + '|' + '         ' + '|')
    print('---------------------')
    print('     ' + '|' + '         ' + '|')
    print(board[1] + '    ' + '|' + '    ' +  board[2] + '    ' +  '|' + '    ' + board[3])
    print('     ' + '|' + '         ' + '|')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)    


#TAKING THE INPUT FROM THE USER TO USE 'X' OR 'O'

def player_input():
    print('Welcome to TicTacToe')
    marker = ' '
    while marker!='X' and marker!='O':
        marker = input("Player 1 : Enter to choose 'X' or '0' : ").upper()
    
    if(marker == 'X'):
        player1 = 'X'
        player2 = 'O'
    
    else:
        player1 = 'O'
        player2 = 'X'
    
    return (player1 , player2)
    

print(player_input())    




#PLACING THE MARKER ON BOARD ACCORDING TO THE  PLAYER.
def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)
    

place_marker(test_board,'$',8)


# Condition for winning the Game.
def win_check(board, mark):
    #check for all rows , columns and diagonals
    return (board[7] == mark and board[8] == mark and board[9] == mark or
            board[4] == mark and board[5] == mark and board[6] == mark or
            board[1] == mark and board[2] == mark and board[3] == mark or 
            board[7] == mark and board[4] == mark and board[1] == mark or
            board[8] == mark and board[5] == mark and board[2] == mark or
            board[9] == mark and board[6] == mark and board[3] == mark or
            board[7] == mark and board[5] == mark and board[3] == mark or
            board[9] == mark and board[5] == mark and board[1] == mark)
            