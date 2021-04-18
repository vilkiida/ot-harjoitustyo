import pygame
from cell import Cell
from random import randint

class Field:
    def __init__(self, height, width, how_many_mines):
        self.height=height
        self.width=width
        self.how_many_mines=how_many_mines

        self.create_a_field()
    
    def create_a_field(self):
        self.field=[[ Cell() for w in range(self.width) ] for h in range(self.height)]
        for _ in range(self.how_many_mines):
            while True:
                x = randint(0, self.width-1)
                y = randint(0, self.height-1)
                if self.field[y][x].mine == False:
                    self.field[y][x].turn_into_a_mine()
                    break
    
    
