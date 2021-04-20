import pygame
from cell import Cell
from random import randint

class Field:
    def __init__(self, height, width, how_many_mines):
        self.height=height
        self.width=width
        self.how_many_mines=how_many_mines

        self.create_a_field()
        self.find_neighbours()
    
    def create_a_field(self):
        self.field=[[ Cell() for w in range(self.width) ] for h in range(self.height)]
        for _ in range(self.how_many_mines):
            while True:
                x = randint(0, self.width-1)
                y = randint(0, self.height-1)
                if self.field[y][x].mine == False:
                    self.field[y][x].turn_into_a_mine()
                    break
    
    def find_neighbours(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.list_neighbours(y,x)
    
    def list_neighbours(self, y, x):
        neighbours = []
        for n_y in range(y - 1, y + 2):
            for n_x in range(x - 1, x + 2):
                if n_y == y and n_x == x:
                    continue
                if n_y < 0 or n_x < 0:
                    continue
                if n_y > (self.height-1):
                    continue
                if n_x > (self.width-1):
                    continue
                else:
                    neighbours.append((n_y,n_x))
        self.field[y][x].mark_neighbours(neighbours)
        self.check_neighbours(y,x)
    
    def check_neighbours(self, y ,x):
        neighbour_mines_amount=0
        for neighbour in self.field[y][x].neighbours:
            if self.is_cell_a_mine(neighbour[0],neighbour[1]) == True:
                neighbour_mines_amount+=1
        self.field[y][x].mark_neigbour_mines(neighbour_mines_amount)
    
    def open_cell(self, y, x):
        if self.field[y][x].is_opened() == False:
            if self.field[y][x].neighbour_mines == 0:
                self.field[y][x].open()
                self.open_empty_neighbours(y,x)
            else:
                self.field[y][x].open()

    def open_empty_neighbours(self, y, x):
        for neighbour in self.field[y][x].neighbours:
            if self.field[neighbour[0]][neighbour[1]].is_opened() == False:
                if self.field[neighbour[0]][neighbour[1]].is_a_mine() == False:
                    self.open_cell(neighbour[0],neighbour[1])
    
    def open_all(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.field[y][x].open()
    
    def mark_a_cell(self, y, x):
        if self.field[y][x].is_opened() == False:
            if self.field[y][x].is_not_marked() == True:
                self.field[y][x].mark_flagg()
            elif self.field[y][x].is_flagged() == True:
                self.field[y][x].mark_questionmark()
            elif self.field[y][x].is_questionmark() == True:
                self.field[y][x].remove_markings()
    
    def blow_up_a_mine(self, y, x):
        self.field[y][x].blow_up()
    
    
    def is_cell_a_mine(self, y, x):
        if self.field[y][x].is_a_mine() == True:
            return True
        return False
    
    def is_cell_opened(self, y, x):
        if self.field[y][x].is_opened() == True:
            return True
        return False

    
    
