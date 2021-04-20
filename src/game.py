import pygame
import os
from field import Field

class Game:
    def __init__(self, field, cell_size):
        self.field=field
        self.cell_size=cell_size
        self.field_width=field.width
        self.field_height=field.height
        self.screen_width=self.cell_size*self.field_width
        self.screen_height=self.cell_size*self.field_height

        self.screen=pygame.display.set_mode((self.screen_width,self.screen_height))

        pygame.init()

        self.loop()
    
    def game_over(self, y, x):
        self.field.open_all()
        self.field.blow_up_a_mine(y,x)
        
    def game_won(self):
        self.field.open_all()
    
    def check_for_win(self):
        victory=True
        for y in range(0,self.field_height):
            for x in range(0,self.field_width):
                if self.field.is_cell_a_mine(y,x) == False:
                    if self.field.is_cell_opened(y,x) == False:
                        victory = False
        return victory


    def left_click(self, position):
        x = position[0] // self.cell_size
        y = position[1] // self.cell_size
        if self.field.field[y][x].is_a_mine() == True:
            self.game_over(y,x)
        else:
            if self.check_for_win() == False:
                self.field.open_cell(y,x)
            else:
                self.game_won()
            
    
    def right_click(self, position):
        x = position[0] // self.cell_size
        y = position[1] // self.cell_size
        self.field.mark_a_cell(y,x)
    

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position=pygame.mouse.get_pos()
                    self.left_click(position)
                if event.button == 3:
                    position=pygame.mouse.get_pos()
                    self.right_click(position)

    def draw_screen(self):
        self.screen.fill((255,0,0))
        for y in range(self.field_height):
            for x in range(self.field_width):
                cell=self.field.field[y][x]
                self.screen.blit(cell.image, (x*self.cell_size, y*self.cell_size))

        pygame.display.flip()
    
    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()


if __name__ ==  "__main__":
    board=Field(10,8,12)
    Game(board,50)

