import os

user_input =  ''
turn_cnt = 0
end_game = False
game_board = ['' for x in range(9)]

#############
# Functions 
#############

# Check input for valid  
def check_input(user_input, info, cnt):
    x = info
    y = cnt

    if user_input.upper() == 'Q' or user_input.upper() == 'QUIT':
        x = True
        print('Sorry to see you go. Thanks for playing!')
    elif user_input.isdigit() and int(user_input) in range(0,10): 
        y+=1
    else:
        print('Invalid Input. Please enter a number between 1 adnd 9 or enter Q to quit the game.')

    return x, y

# Display Game Board
def display_game(board): 
    print('board')

#############
# Main
#############

print("Let's Play Tic-Tac-Toe!")

while end_game == False and turn_cnt < 9:
    user_input = input("Player, your turn: ")

    end_game, turn_cnt = check_input(user_input, end_game, turn_cnt)