import os

user_input =  ''
turn_cnt = 1
end_game = False
is_digit = True
game_board = ['' for x in range(9)]
xo_marker = 'X' 
iswinner = False

#############
# Functions 
#############

# Display Game Board
def display_game(board): 
    print(board[6:])
    print(board[3:6])
    print(board[:3])

#Test Tic Tac Toe
def game_logic(board):
    a = board[6:]
    b = board[3:6]
    c = board[:3]

    
    

#############
# Main
#############

print("Let's Play Tic-Tac-Toe!")

display_game(game_board)

while end_game == False and turn_cnt < 10:

    if turn_cnt%2:
        xo_marker = 'O'
    else: 
        xo_marker = 'X'
    
    user_input = input("Player, your turn: ")

    if user_input.upper() in ['Q', 'QUIT', 'X', 'EXIT']:
        end_game = True
        print('Sorry to see you go. Thanks for playing!')
    elif user_input.isdigit() and int(user_input) in range(0,10):
        i = int(user_input)-1
        game_board[i] = xo_marker
        display_game(game_board)
        turn_cnt+=1
    else:
        print('Invalid Input. Please enter a number between 1 adnd 9 or enter Q to quit the game.')
    
    #end_game, turn_cnt = check_input(user_input, end_game, turn_cnt, game_board)
    
    