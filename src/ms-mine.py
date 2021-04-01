import pygame
import os

dirname = os.path.dirname("~/ot-harjoitustyo/src")

class Mine(pygame.spirte.Sprite):
    def __init__(self, x=0, y=0, color):
        super().__init__()
        self.image=pygame.image.load(os.path.join(dirname, "assets", "ms-mine.png"))
        self.rect=self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.color=color
