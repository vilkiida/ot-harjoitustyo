import pygame
import os 

dirname = os.path.dirname(__file__)

class Cell(pygame.sprite.Sprite):
    def __init__(self, bomb:bool, opened:bool, flagged:bool, x=0, y=0):
        super().__init__()
        self.bomb=bomb
        self.opened=opened
        self.flagged=flagged
        #self.neighbour_bombs
        
        #unopened
        if self.opened == False:
            self.image=pygame.image.load(os.path.join(dirname, "assets", "ms-unopened.png"))
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
        #opened bomb
        elif self.opened == True and self.bomb == True:
            self.image=pygame.image.load(os.path.join(dirname, "assets", "ms-mine-png"))
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
        #opened empty
        elif self.opened == True and self.bomb == False:
            self.image=pygame.image.load(os.path.join(dirname, "assets", "ms-opened.png"))
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y

