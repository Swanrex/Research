def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score_display):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_display.keys())
    print("\t   ", players[0], "\t    ", score_display[players[0]])
    print("\t   ", players[1], "\t    ", score_display[players[1]])

    print("\t--------------------------------\n")


# Function to check if any player has won
def win_check(player_pos, cur_player):
    # All possible winning combinations
    win_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loops to see if any players has got 3 in a row
    for x in win_lines:
        if all(y in player_pos[cur_player] for y in x):
            return True  # Return True if any winning combination satisfies
    return False  # Return False if no combination is satisfied


def check_draw(player_pos):  # Function to check if the game is drawn
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


def single_game(cur_player):    # Function for a single game of Tic Tac Toe
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)

        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Bad input, Try Again")
            continue

        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Bad input, Try Again")
            continue

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("Place has already been filled, Select a different spot")
            continue

        # Updating grid status
        values[move - 1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call to check if someone has won
        if win_check(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won this match.")
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")

    # Stores the player who chooses X and O
    cur_player = player1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit
    while True:

        # Player choice Menu
        print("Turn to choose for", cur_player)
        print("Type 1 for X")
        print("Type 2 for O")
        print("Type 3 to Quit the program")

        # Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Bad input, Try Again\n")
            continue

        # Conditions for player choice
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Bad input, Try Again\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice - 1])

        # Edits the scoreboard according to the winner
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

# This TicTacToe was found on askpython from a person named Aprataksh Anand.
# I've always wanted to create a new game similar to this, a simple easy to play
# game based around true information like chess, Though in actuality such a game
# like that would be best made in an area of complexity *between* tictactoe and chess.
