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