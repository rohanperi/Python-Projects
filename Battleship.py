 #Amazing Python Game!
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Welcome to Battleship! When guessing, remember that the rows start from 0 and go to 4!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print ("Turn ", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You won the game by sinking the battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
        break
    elif guess_row not in range(5) or guess_col not in range(5):
        print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print ("You guessed that one already.")
    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == 3:
            print ("Game Over")



input("press Enter to exit")
