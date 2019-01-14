
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
  
  
#random module to randomly decide which player goes first. 

import random

def choose_first():
    flip.randomint(0 , 1)
    
    if(flip == 0):
        return 'Player 1'
    else:
        return 'Player 2'
      
      
#returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return(board[position] == ' ')
  

#checks if the board is full and returns a boolean value

def full_board_check(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    
    return True
  
# asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.


def player_choice(board):
    position = 0
    
    while position not  in [1,2,3,4,5,6,7,8,9] and not space_check(board , position):
        position = int(input('Choose a position : (1-9)'))
    
    return position
  
  
#asks the player if they want to play again and returns a boolean True if they do want to play again.


            