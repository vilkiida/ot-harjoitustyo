import pygame
# import os
from field import Field

class Game:
    def __init__(self, field, cell_size):
        self.field=field.field
        self.cell_size=cell_size
        self.field_width=field.width
        self.field_height=field.height
        self.screen_width=self.cell_size*self.field_width
        self.screen_height=self.cell_size*self.field_height

        self.screen=pygame.display.set_mode((self.screen_width,self.screen_height))

        pygame.init()

        self.loop()

    def left_click(self, position):
        x = position[0] // self.cell_size
        y = position[1] // self.cell_size
        self.field[y][x].open()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                self.left_click(position)

    def draw_screen(self):
        self.screen.fill((0,0,0))
        for y in range(self.field_height):
            for x in range(self.field_width):
                cell=self.field[y][x]
                self.screen.blit(cell.image, (x*self.cell_size, y*self.cell_size))

        pygame.display.flip()
    
    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()


if __name__ ==  "__main__":
    board=Field(10,8,12)
    Game(board,50)

