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
    
    def is_a_mine(self):
        return self.mine
    
    def is_opened(self):
        return self.opened
    
    def is_flagged(self):
        if self.questionmark == False:
            if self.flagged == True:
                return True
        return False
    
    def is_not_marked(self):
        if self.flagged == False:
            if self.questionmark == False:
                return True
        return False
    
    def is_questionmark(self):
        if self.flagged == False:
            if self.questionmark == True:
                return True
        return False

    def turn_into_a_mine(self):
        self.mine = True
    
    def mark_neighbours(self, neighbours):
        self.neighbours = neighbours
    
    def mark_neigbour_mines(self, neighbour_mines):
        self.neighbour_mines = neighbour_mines

    def open(self):
        if self.opened == True:
            pass

        else:
            self.opened = True
            if self.mine == False:
                if self.neighbour_mines == 0:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-opened.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 1:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-1.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 2:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-2.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 3:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-3.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 4:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-4.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 5:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-5.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 6:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-6.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 7:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-7.png"))
                    self.rect=self.image.get_rect()
                elif self.neighbour_mines == 8:
                    self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-8.png"))
                    self.rect=self.image.get_rect()

            else:
                self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-mine.png"))
                self.rect=self.image.get_rect()
    
    def mark_flagg(self):
        self.flagged = True
        self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-flag.png"))
        self.rect = self.image.get_rect()
    
    def mark_questionmark(self):
        self.flagged = False
        self.questionmark = True
        self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-qm.png"))
        self.rect = self.image.get_rect()

    def remove_markings(self):
        self.flagged = False
        self.questionmark = False
        self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-unopened.png")) 
        self.rect = self.image.get_rect()
    
    def blow_up(self):
        self.image = pygame.image.load(os.path.join(dirname, "assets", "ms-mine2.png"))
        self.rect = self.image.get_rect()
    
