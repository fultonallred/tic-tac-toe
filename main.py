# W01 Prove: Developer (tic-tac-toe game)
# Author: Fulton Allred

# Prime numbers assigned to each space: 
# [1, 2, 3, 4,  5,  6,  7,  8,  9]
# [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Win_cases is a list of win conditions calculated by multiplying 
# unique prime numbers rows, columns, or diaganols.


prime_positions = [2, 3, 5, 7, 11, 13, 17, 19, 23]
win_cases = [30, 1001, 7429, 238, 627, 1495, 506, 935]
x_positions = []
o_positions = []

def main():
    current_turn = 1
    current_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Start the main game loop.
    still_playing = True
    while still_playing:

        # Determine whos turn it is.
        current_player = determine_player(current_turn)

        # Draw game board with current positions.
        draw_board(current_positions)

        # Get move from player.
        current_player = determine_player(current_turn)
        new_position = get_position(current_player)

        # Update current game board.
        current_positions = update_board(current_positions, new_position, current_player)

        # Check for a win.
        gameover, victor = determine_gameover(x_positions, o_positions)

        # Advance turn count.
        current_turn += 1

        # At gomeover, print board and display victor or tie.
        if gameover:

            draw_board(current_positions)

            if victor == None:
                print("It's a tie.")

            elif victor != None:
                print(f"{victor} wins! Good game.")

            still_playing = False

def draw_board(positions):
    """This function draws the game board using a list of positions 
    from 1 to 9.
    
    Parameters: position_list - a list of all x's, o's, or unclaimed positions
    Return: none"""
    
    # Used to advance through the positions list during the loops.
    num = 0

    print("-----------------------------------------------------------------")

    # First loop determines rows.
    for n in range(1, 4):
        # Second loop determines columns.
        for i in range(1, 4):
            if i == 3:
                print(positions[num], end="")
            else:
                print(positions[num], end="|")
            num += 1
        print("")

        # If statement prevents this from drawing after the last row.
        if n < 3:
            print("-+-+-")
    
    print()

def determine_player(turn):
    """This function determines which player's turn it is.
    
    Parameters: turn - the turn number
    Return: player - whos turn it is"""
    
    # Determine if turn # is even or odd.
    if turn % 2 == 0:
        player = "O"

    elif turn % 2 != 0:
        player = "X"

    return player

def get_position(current_player):
    """This function gets an x or o input from a player
    
    Parameters: player - whos turn it is, expects either "X" or "O" """

    print(f"It is {current_player}'s turn.")
    new_position = int(input("Please choose a position (1-9): ")) - 1

    # Add new move to either x or o's list of positions.
    if current_player == "X":
        x_positions.append(prime_positions[new_position])

    elif current_player == "O":
        o_positions.append(prime_positions[new_position])

    return new_position

def update_board(positions, new_position, player):
    """This function replaces a number position with x or o.
    
    Parameters: positions - the list of positions up to now
    new_position - the position selected by current player
    player - the current player, either "X" or "O"
    
    Return: updated_positions - the new positions on the board"""

    positions[new_position] = player

    return positions

def determine_gameover(x_positions, o_positions):
    """This function determines if a win condition is met.
    
    Parameters: x_positions - the current x_positions
    o_positions - the current o positions
    
    Return: gameover (bool) - if the game is over or not
    victor (str) - either "X" or "O" """

    gameover = False
    victor = None

    # Get the product of each prime assigned to x positions.
    x_prod = 1
    for i in x_positions:
        x_prod = x_prod * i

    # See if any win_cases factor into x_prod evenly.
    for i in win_cases:
        remainder = x_prod % i

        if remainder == 0:
            gameover = True
            victor = "X"

     # Get the product of each prime assigned to o positions.
    o_prod = 1
    for i in o_positions:
        o_prod = o_prod * i

    # See if any win_cases factor into o_prod evenly.
    for i in win_cases:
        remainder = o_prod % i

        if remainder == 0:
            gameover = True
            victor = "O"

    if len(x_positions) + len(o_positions) == 9:
        gameover = True
    
    total_moves = len(x_positions) + len(o_positions)
    return gameover, victor


main()