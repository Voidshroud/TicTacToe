import copy
import random


class AI:

    def __init__(self, player=2):
        self.player = player

    def random(self, board):
        empty_squares = board.get_empty_squares()
        random_index = random.randrange(0, len(empty_squares))
        return empty_squares[random_index]

    def minimax(self, board, maximizing):

        case = board.check_victory_conditions()

        if case == 1:
            return 1, None

        if case == 2:
            return -1, None

        elif board.isfull():
            return 0, None

        if maximizing:
            max_evaluation = -10
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                evaluation = self.minimax(temp_board, False)[0]
                if evaluation > max_evaluation:
                    max_evaluation = evaluation
                    best_move = (row, col)

            return max_evaluation, best_move

        elif not maximizing:
            min_evaluation = 10
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                evaluation = self.minimax(temp_board, True)[0]
                if evaluation < min_evaluation:
                    min_evaluation = evaluation
                    best_move = (row, col)

            return min_evaluation, best_move

    def evaluate(self, main_board):
        evaluation, move = self.minimax(main_board, False)
        return move
    