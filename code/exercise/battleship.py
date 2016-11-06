#/usr/bin/env python3


from random import randint
from sys import exit


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


def print_intro():

    intro = "\n === Let's play Battleship! === \n"
    print(intro)


def print_turn(current, maximum):

    print ("Turn {0} of {1}".format(current, maximum))


def check_for_hit(guess, ship, board):

    max_size = board.size - 1
    out_of_boundary = (guess.row < 0 or guess.row > max_size) or (guess.col < 0 or guess.col > max_size)

    if out_of_boundary:
        print("Whoa, that's not even in the ocean!\n")
        return


    guessed_already = (board.board[guess.row][guess.col] == "X")
    sunk_battleship = guess.row == ship.row and guess.col == ship.col

    if sunk_battleship:
        print("Congratulations! You sunk my battleship!")
        exit(0)

    elif guessed_already:
        print("You guessed that one already.")

    else:
        print("You missed my battleship!")
        board.board[guess.row][guess.col] = "X"


def main(debug=False):

    max_turns = 5
    board_size = 5

    board = Board(board_size)

    ship_row = board.random_row()
    ship_col = board.random_col()

    ship = Ship(ship_row, ship_col)

    if debug:
        print('Where the ship at:')
        print('Row: {0} Col: {1}'.format(ship.row, ship.col))

    print_intro()
    board.print_board()

    for turn in range(max_turns):

        print_turn(str(turn+1), str(max_turns))

        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        guess = Guess(guess_row, guess_col)

        check_for_hit(guess, ship, board)

        board.print_board()


if __name__ == "__main__":
    main(True)
