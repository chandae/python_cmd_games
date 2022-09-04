import time
import sys

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def intro():
    print(" Welcome to Tic Tac Toe in Python by @Chanda ".center(100, '*'))
    print("Actual board on the left, keys on the right. Enjoy!".center(100))

def print_board(move='', player=''):
    global board

    if move and player:board[move] = player

    print()
    print(f"{board[1]} | {board[2]} | {board[3]} \t 1 | 2 | 3".center(100))
    print("--+---+-- \t --+---+--".center(100))
    print(f"{board[4]} | {board[5]} | {board[6]} \t 4 | 5 | 6".center(100))
    print("--+---+-- \t --+---+--".center(100))
    print(f"{board[7]} | {board[8]} | {board[9]} \t 4 | 5 | 6".center(100))
    print()

def slots_done():
    if any([slot[1] == ' ' for slot in board.items()]):
        return False
    return True

def game_won(player):
    """Return True if player is a winner on this TTTBoard."""
    global board
    b, p = board, player
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b[1] == b[2] == b[3] == p) or  # Across the top
            (b[4] == b[5] == b[5] == p) or  # Across the middle
            (b[7] == b[8] == b[9] == p) or  # Across the bottom
            (b[1] == b[4] == b[7] == p) or  # Down the left
            (b[2] == b[5] == b[8] == p) or  # Down the middle
            (b[3] == b[6] == b[9] == p) or  # Down the right
            (b[3] == b[5] == b[7] == p) or  # Diagonal
            (b[1] == b[5] == b[9] == p))    # Diagonal

def main():
    global board

    intro()
    print_board()
    player = 'X'

    while True:
        try:
            # Check if there are stil open slots on the game board
            if slots_done():
                response = input("Tough match. Draw. Do you want a rematch (yes or no): ")
                if response == 'yes':
                    # reset game board
                    board = {n: ' ' for n in range(1, 10)}
                    print_board()
                else: break

            move = input(f"Player {player} your move. Use 'exit' to quit: ")
            if move == 'exit':
                break
            while int(move) not in (i for i in range(1, 10)):
                move = input(f"Invalid move player {player}: Try again. Use 'exit' to quit: ")
            while board[int(move)] != ' ':
                move = input(f"Slot already taken player {player}: Try again. Use 'exit' to quit: ")

            print_board(int(move), player)
            if game_won(player):
                response = input(f"CONGRATULATIONS! PLAYER {player} has won. Do you want a rematch (yes or no): ")
                if response == 'yes':
                    # reset game board
                    board = {n: ' ' for n in range(1, 10)}
                    print_board()
                else: break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        except KeyboardInterrupt:
            break
    print('\nThanks for playing!')
    print('Quitting game...')
    time.sleep(2)
    sys.exit()

if __name__ == '__main__':
    main()
