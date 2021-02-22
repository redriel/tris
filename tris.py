# Tic-tac-toe game written in python
# v1.0
# Author: Redriel
#
# This is a simple tic-tac-toe game
# The grid is shown on the terminal.
# Players can choose a cell using numbers between 1 and 9.

# This function checks for win conditions
def check_board():
    if (
        grid[0] == grid[1] == grid[2] != " " or
        grid[3] == grid[4] == grid[5] != " " or
        grid[6] == grid[7] == grid[8] != " " or
        grid[0] == grid[3] == grid[6] != " " or
        grid[1] == grid[4] == grid[7] != " " or
        grid[2] == grid[5] == grid[8] != " " or
        grid[0] == grid[4] == grid[8] != " " or
        grid[2] == grid[4] == grid[6] != " "
    ):
        return True
    return False

# This function prints the current state of the board
def print_board():
    print('\n'*50)
    print(f' {grid[0]} | {grid[1]} | {grid[2]}')
    print('-----------')
    print(f' {grid[3]} | {grid[4]} | {grid[5]}')
    print('-----------')
    print(f' {grid[6]} | {grid[7]} | {grid[8]}')

# This function takes the player input.
# If the input is invalid, the function recall itself recursively.
# The function returns true if the player move leads to a win, false otherwise
def get_player_input(sign):
    cell = (int(input("Pick a cell: "))) - 1
    if cell in range (0,9) and grid[cell] == " ":
        return set_marker(cell, sign)
    else:
        print("ERROR: Invalid value or cell")
        get_player_input(sign)

# This function set the player input on the board, then checks if the move leads to a win
def set_marker(cell, sign):
    grid[cell] = sign
    return check_board()

# Variables
grid = [" "]*9
game = True
print_board()

# Main loop of the game
while game:
    if get_player_input("x"):
        print_board()
        print("X player won!")
        break
    else:
        print_board()

    if get_player_input("o"):
        print_board()
        print("O player won!")
        break
    else:
        print_board()
