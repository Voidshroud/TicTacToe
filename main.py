import sys
import pygame
from constants import *
from Board import Board
from AI import AI

class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = "Singleplayer"
        self.difficulties = ("Easy", "Medium", "Impossible")
        self.current_difficulty = "Medium"
        self.running = True
        self.show_lines()

    def isover(self):
        return self.board.isfull()

    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_shape(row, col)
        self.next_turn()

    def change_gamemode(self):
        self.gamemode = "Singleplayer" if self.gamemode == "Multiplayer" else "Multiplayer"

    def show_lines(self):
        screen.fill(BG_COLOUR)
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOUR, (SQ_SIZE, 10), (SQ_SIZE, (HEIGHT - 10)), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOUR, ((2 * SQ_SIZE), 10), ((2 * SQ_SIZE), (HEIGHT - 10)), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOUR, (10, SQ_SIZE), ((WIDTH - 10), SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOUR, (10, (2 * SQ_SIZE)), ((WIDTH - 10), (2 * SQ_SIZE)), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def draw_shape(self, row, col):

        if self.player == 1:

            start_first_line = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + OFFSET)
            end_first_line = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
            start_second_line = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
            end_second_line = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + OFFSET)

            pygame.draw.line(screen, SHAPE_COLOUR, start_first_line, end_first_line, SHAPE_WIDTH)
            pygame.draw.line(screen, SHAPE_COLOUR, start_second_line, end_second_line, SHAPE_WIDTH)

        elif self.player == 2:

            center = (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2)
            pygame.draw.circle(screen, SHAPE_COLOUR, center, RADIUS, SHAPE_WIDTH)

    def check_for_winner(self):
        for col in range(COLUMNS):
            if self.board.squares[0][col] == self.board.squares[1][col] == self.board.squares[2][col] != 0:
                self.running = False
                print(f"The winner is: Player {int(self.board.squares[0][col])}")

        for row in range(ROWS):
            if self.board.squares[row][0] == self.board.squares[row][1] == self.board.squares[row][2] != 0:
                self.running = False
                print(f"The winner is: Player {int(self.board.squares[row][0])}")

        if self.board.squares[0][0] == self.board.squares[1][1] == self.board.squares[2][2] != 0:
            self.running = False
            print(f"The winner is: Player {int(self.board.squares[1][1])}")

        if self.board.squares[0][2] == self.board.squares[1][1] == self.board.squares[2][0] != 0:
            self.running = False
            print(f"The winner is: Player {int(self.board.squares[1][1])}")

        elif self.isover() and self.running is True:
            self.running = False
            print("Game ended in a Tie!")

        if self.running is False:
            print("Press [R] to reset the game board.")

    def reset(self):
        self.__init__()


def main():

    game = Game()
    board = game.board
    ai = game.ai

    print(WELCOME_MESSAGE)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai
                    print(f"------> The board has been cleared <------\n\n"
                          f"{INSTRUCTIONS_MESSAGE}")

                if event.key == pygame.K_g:
                    game.change_gamemode()
                    print(f"Gamemode changed to: '{game.gamemode}'")

                if event.key == pygame.K_s:
                    if board.isempty():
                        print("Going second!")
                        if game.gamemode == "Singleplayer":
                            print("AI is thinking....")
                        game.next_turn()
                    else:
                        print("Please [R]eset the board before changing the turn order.")

                if event.key == pygame.K_d:
                    if game.gamemode == "Singleplayer":
                        if game.difficulties.index(game.current_difficulty) == len(game.difficulties) - 1:
                            game.current_difficulty = game.difficulties[0]
                            print(f"Difficulty changed to '{game.current_difficulty}'.")
                        else:
                            game.current_difficulty = game.difficulties[game.difficulties.index(game.current_difficulty) + 1]
                            print(f"Difficulty changed to '{game.current_difficulty}'.")
                    else:
                        print("Difficulty can only be changed in 'Singleplayer' gamemode.")

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and game.running:
                pos = event.pos
                row = pos[1] // SQ_SIZE
                col = pos[0] // SQ_SIZE

                if board.square_is_empty(row, col):
                    game.make_move(row, col)
                    game.check_for_winner()

        if game.gamemode == "Singleplayer" and game.player == ai.player and game.running:
            pygame.display.update()

            if game.current_difficulty == "Impossible":
                row, col = ai.evaluate_impossible_difficulty(board)
            elif game.current_difficulty == "Medium":
                row, col = ai.evaluate_medium_difficulty(board)
            elif game.current_difficulty == "Easy":
                row, col = ai.evaluate_easy_difficulty(board)

            game.make_move(row, col)
            game.check_for_winner()

        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOUR)
main()
