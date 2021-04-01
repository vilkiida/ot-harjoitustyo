import pygame
from ms-1 import Number_1
from ms-2 import Number_2
from ms-3 import Number_3
from ms-4 import Number_4
from ms-5 import Number_5
from ms-6 import Number_6
from ms-7 import Number_7
from ms-8 import Number_8
from ms-flag import Flag
from ms-questionmark import Questionmark
from ms-unopened import Unopened
from ms-opened import Opened
from ms-mine import Mine

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.numbers=pygame.sprite.Group()
        self.cells=pygame.spire.Group()
        self.actions=pygame.sprite.Group()
        self.mines=pygame.sprite.Group()
        self.all_sprites = pygame.spirte.Group()

        self._initialize_sprites(level_map)
    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell=level_map[y][x]
                normalized_x=x * self.cell_size
                normalized_y=y * self.cell_size

                if cell == 0:
                    self.cells.add(Opened(normalized_x, normalized_y))
                elif cell == 1:
                    self.numbers.add(Number_1(normalized_x,normalized_y))
                elif cell == 2:
                    self.numbers.add(Number_2(normalized_x,normalized_y))
                elif cell == 3:
                    self.numbers.add(Number_3(normalized_x,normalized_y))
                elif cell == 4:
                    self.numbers.add(Number_4(normalized_x,normalized_y))
                elif cell == 5:
                    self.numbers.add(Number_5(normalized_x, normalized_y))
                elif cell == 6:
                    self.numbers.add(Number_6(normalized_x,normalized_y))
                elif cell == 7:
                    self.numbers.add(Number_7(normalized_x,normalized_y))
                elif cell == 8:
                    self.numbers.add(Number_8(normalized_x,normalized_y))
                elif cell == 9:
                    self.cells.add(Opened(normalized_x,normalized_y))
                elif cell == 10:
                    self.actions.add(Flag(normalized_x,normalized_y))
                elif cell == 11:
                    self.actions.add(Questionmark(normalized_x,normalized_y))
                elif cell == 12:
                    self.cells.add(Opened(normalized_x,normalized_y))
                    self.mines.add(Mine(normalized_x,normalized_y,None))
                elif cell == 13:
                    self.mines.add(Mine(normalized_x,normalized_y,(255,0,0)))
                               
        self.all_sprites.add(self.cells,self.numbers,self.actions,self.mines)