import pygame
from cell import Cell

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.mines=pygame.sprite.Group()
        self.empties=pygame.sprite.Group()
        #self.numebers=pygame.sprite.Group()

        self.all_sprites=pygame.sprite.Group()

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
                    #unopened empty
                    self.empties.add(Cell(False, False, False, normalized_x,normalized_y))
                elif cell == 1:
                    #unopened mine
                    self.mines.add(Cell(True, False, False, normalized_x, normalized_y))
                elif cell == 2:
                    #opened empty
                    self.empties.add(Cell(False, True, False, normalized_x,normalized_y))
                elif cell == 3:
                    #opened mine
                    self.mines.add(Cell(True, True, False, normalized_x, normalized_y))
                #...
        

        self.all_sprites.add(self.mines,self.empties)