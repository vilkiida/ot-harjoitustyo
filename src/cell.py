import os
import pygame
DIRNAME = os.path.dirname(__file__)
class Cell:
    def __init__(self):
        self.mine = False
        self.opened = False
        self.flagged = False
        self.questionmark = False
        self.neighbours = []
        self.neighbour_mines = None
        if not self.opened:
            self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-unopened.png"))
    def is_a_mine(self):
        return self.mine
    def is_opened(self):
        return self.opened
    def is_flagged(self):
        if not self.questionmark:
            if self.flagged:
                return True
        return False
    def is_not_marked(self):
        if not self.flagged:
            if not self.questionmark:
                return True
        return False
    def is_questionmark(self):
        if not self.flagged:
            if self.questionmark:
                return True
        return False
    def turn_into_a_mine(self):
        self.mine = True
    def mark_neighbours(self, neighbours):
        self.neighbours = neighbours
    def mark_neigbour_mines(self, neighbour_mines):
        self.neighbour_mines = neighbour_mines
    def open(self):
        if self.opened:
            pass
        else:
            self.opened = True
            if not self.mine:
                if self.neighbour_mines == 0:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-opened.png"))
                elif self.neighbour_mines == 1:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-1.png"))
                elif self.neighbour_mines == 2:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-2.png"))
                elif self.neighbour_mines == 3:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-3.png"))
                elif self.neighbour_mines == 4:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-4.png"))
                elif self.neighbour_mines == 5:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-5.png"))
                elif self.neighbour_mines == 6:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-6.png"))
                elif self.neighbour_mines == 7:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-7.png"))
                elif self.neighbour_mines == 8:
                    self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-8.png"))
            else:
                self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-mine.png"))
    def mark_flagg(self):
        self.flagged = True
        self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-flag.png"))
    def mark_questionmark(self):
        self.flagged = False
        self.questionmark = True
        self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-qm.png"))
    def remove_markings(self):
        self.flagged = False
        self.questionmark = False
        self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-unopened.png"))
    def blow_up(self):
        self.image = pygame.image.load(os.path.join(DIRNAME, "assets", "ms-mine2.png"))
