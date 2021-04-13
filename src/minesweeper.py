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

CELL_SIZE = 40

def main():
    height = len(LEVEL_MAP)
    width = len(LEVEL_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE


    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Minesweeper!")

    level = Level(LEVEL_MAP, CELL_SIZE)

    pygame.init()

    level.all_sprites.draw(display)

if __name__ == "__main__":
    main()