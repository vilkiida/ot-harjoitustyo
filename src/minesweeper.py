import pygame
from level import Level

LEVEL_MAP= [[0,0,0,0,1,0,0,0],
            [0,1,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,1,0,0,1,0,0,0],
            [0,1,0,0,0,1,0,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0]]

CELL_SIZE = 50
class Main:
    def __init__(self):
        self.height = len(LEVEL_MAP)
        self.width = len(LEVEL_MAP[0])
        self.display_height = self.height * CELL_SIZE
        self.display_width = self.width * CELL_SIZE

        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        pygame.display.set_caption("Minesweeper!")

        self.level = Level(LEVEL_MAP, CELL_SIZE)

        pygame.init()

        self.loop()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    def draw(self):

        self.level.all_sprites.draw(self.display)
        pygame.display.flip()

    def loop(self):
        while True:
            self.check_events()
            self.draw()

if __name__ == "__main__":
    Main()