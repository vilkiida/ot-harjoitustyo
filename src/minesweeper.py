import pygame
from game import Game
from field import Field

easy=(9,9,10)
mediumhard=(16,16,40)
expert=(16,30,99)

class Main:
    def __init__(self, difficulty):
        self.height=difficulty[0]
        self.width=difficulty[1]
        self.mine_amount=difficulty[2]

        self.board=Field(self.height,self.width,self.mine_amount)
    def run_game(self):
        Game(self.board, 50)


if __name__ == "__main__":
    minesweeper=Main(easy)
    minesweeper.run_game()