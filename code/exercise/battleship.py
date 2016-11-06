#/usr/bin/env python3


from random import randint
from sys import exit
from collections import namedtuple
import functools


def color_it(color=None):

    ENDC = '\033[0m'

    def decorator(func):
        @functools.wraps(func)

        def wrapper(*args, **kwargs):
            print(color)
            func(*args, **kwargs)
            print(ENDC)
        return wrapper

    return decorator


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def print_turn(current, maximum):
    print ("Turn {0} of {1}".format(current, maximum))

def print_intro():
    print("\n === Let's play Battleship! === \n")

@color_it(color=Colors.WARNING)
def print_oob():
    print("Whoa, that's not even in the ocean!")

@color_it(color=Colors.OKBLUE)
def print_guess():
    print("You guessed that one already.")

@color_it(color=Colors.OKGREEN)
def print_hit():
    print("Congratulations! You sunk my battleship!")

@color_it(color=Colors.WARNING)
def print_miss():
    print("You missed my battleship!")


class Board:

    def __init__(self, size=5):

        self.size = size
        self.board = []

        self.initialize_board(size)


    def initialize_board(self, size):

        for x in range(5):
            self.board.append(["O"] * size)


    def print_board(self):

        for row in self.board:
            print("  ".join(row))


    def random_row(self):

        return randint(0, len(self.board) - 1)


    def random_col(self):

        return randint(0, len(self.board[0]) - 1)


class Ship:

    def __init__(self, row, col):

        self.row = row
        self.col = col


class Guess:

    def __init__(self, row, col):

        self.row = row
        self.col = col


def is_out_of_boundary(guess, board):

    max_size = board.size - 1
    out_of_boundary = (guess.row < 0 or guess.row > max_size) or (guess.col < 0 or guess.col > max_size)

    if out_of_boundary:
        print_oob()
        return True
    else:
        return False


def check_for_hit(guess, ship, board):

    if is_out_of_boundary(guess, board):
        return

    guessed_already = (board.board[guess.row][guess.col] == "X")
    sunk_battleship = guess.row == ship.row and guess.col == ship.col

    if sunk_battleship:
        print_hit()
        exit(0)

    elif guessed_already:
        print_guess()

    else:
        print_miss()
        board.board[guess.row][guess.col] = "X"


def main(debug=False):

    max_turns = 5
    board_size = 5

    board = Board(board_size)

    ship = Ship(
        board.random_row(),
        board.random_col())

    if debug:
        print('Where the ship at:')
        print('Row: {0} Col: {1}'.format(ship.row, ship.col))

    print_intro()

    for turn in range(max_turns):

        print_turn(str(turn+1), str(max_turns))

        board.print_board()

        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        guess = Guess(guess_row, guess_col)

        check_for_hit(guess, ship, board)


if __name__ == "__main__":
    main()
