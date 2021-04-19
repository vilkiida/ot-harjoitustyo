import pygame
import os 

dirname = os.path.dirname(__file__)

class Cell:
    def __init__(self):
        self.mine=False
        self.opened=False
        self.flagged=False
        self.questionmark=False

        if self.opened == False:
            self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-unopened.png"))
            self.rect=self.image.get_rect()

    def turn_into_a_mine(self):
        self.mine = True
    
    def open(self):
        if self.opened == True:
            pass

        else:
            if self.mine == False:
                self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-opened.png"))
                self.rect=self.image.get_rect()

            else:
                self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-mine.png"))
                self.rect=self.image.get_rect()
    
