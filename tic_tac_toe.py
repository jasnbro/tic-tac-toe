import os

user_input =  ''
xo_marker = 'X'
turn_cnt = 1
end_game = False
iswinner = False
game_board = ['' for x in range(9)]

#############
# Functions 
#############

# Displays Game Board
def display_game(board): 
    print(board[6:])
    print(board[3:6])
    print(board[:3])

# Tests if Tic Tac Toe winner has been found
def game_logic(board):
    a = board[6:]
    b = board[3:6]
    c = board[:3]
    
    winner = True

    if winner == False and game_over(board) == True:
        print("Game Tied")
        return True
    if winner == False and game_over(board) == False:
        display_game(board)
        return False
    else:
        print("We have a winner!") 
        return True

# Determines whether to end the game based on user input
def quit_game(user_input):
    if user_input.upper() in ['Q', 'QUIT', 'X', 'EXIT']:
        print('Sorry to see you go. Thanks for playing!')
        return True
    else: 
        return False

# Checks the game board to determine if all slots have been filled - meaning that the game is over
def game_over(board):
    if "" not in board:
        return True
    else: 
        return False

# Checks the user input for validity
def valid_input(user_input):
    if user_input in ['Q', 'QUIT', 'X', 'EXIT']:
        return True
    elif user_input.isdigit() and int(user_input) in range(1,10):
        return True
    else:
        print("Invalid Input. Please enter a number between 1 adnd 9 or enter Q to quit the game. \n")
        return False
    


#############
# Main
#############

print("Let's Play Tic-Tac-Toe!")

display_game(game_board)

while end_game == False:

    display_game(game_board)

    xo_marker = ('O' if turn_cnt % 2 else 'X')

    user_input = input("Player {}, your turn: ".format(xo_marker))

    while valid_input(user_input) == False and game_over(game_board) == False: 
            user_input = input("Player {}, your turn: ".format(xo_marker))
    else: 
        if quit_game(user_input):
            end_game = True
        else:
            game_board[int(user_input)-1] = xo_marker
            end_game = game_logic(game_board)
        
print("\nThe winner is {} !".format(xo_marker))
print("Thanks for playing, Goodbye!"))