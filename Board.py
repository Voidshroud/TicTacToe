import numpy
from constants import *


class Board:

    def __init__(self):
        self.squares = numpy.zeros((ROWS, COLUMNS))
        self.empty_squares = self.squares
        self.marked_squares = 0

    def check_victory_conditions(self):

        # Return 0 for Tie
        # Return 1 for Player 1 win
        # Return 2 for Player 2 win

        for col in range(COLUMNS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]

        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            return self.squares[1][1]

        return 0

    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def square_is_empty(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_squares(self):
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.square_is_empty(row, col):
                    empty_squares.append((row, col))

        return empty_squares

    def isfull(self):
        return self.marked_squares == 9

    def isempty(self):
        return self.marked_squares == 0