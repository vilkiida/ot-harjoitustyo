import pygame
from game import Game
from field import Field

class GameMenu:
    def __init__(self):
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.easy_button = pygame.Rect(50, 75, 400, 100)
        self.easy = (9, 9, 10)
        self.mediumhard_button = pygame.Rect(50, 250, 400, 100)
        self.mediumhard = (16, 16, 40)
        self.expert_button = pygame.Rect(50, 425, 400, 100)
        self.expert = (16, 30, 99)
        self.button_color = (140, 140, 150)
        self.background_color = (70, 70, 70)
        self.cell_size=50
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 50)
        self.loop()
    def click(self, position):
        if self.easy_button.collidepoint(position):
            easy_field = Field(self.easy[0], self.easy[1], self.easy[2])
            Game(easy_field,self.cell_size)
        if self.mediumhard_button.collidepoint(position):
            mediumhard_field = Field(self.mediumhard[0], self.mediumhard[1], self.mediumhard[2])
            Game(mediumhard_field, self.cell_size)
        if self.expert_button.collidepoint(position):
            expert_field = Field(self.expert[0], self.expert[1], self.expert[2])
            Game(expert_field, self.cell_size)
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_text(self, text, x, y):
        button_text = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x, y))
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.click(position)
    def draw_screen(self):
        self.screen.fill(self.background_color)
        self.draw_button(self.easy_button)
        self.draw_text("EASY", self.easy_button.left+140, self.easy_button.top+25)
        self.draw_button(self.mediumhard_button)
        self.draw_text("MEDIUMHARD", self.mediumhard_button.left+28, self.mediumhard_button.top+25)
        self.draw_button(self.expert_button)
        self.draw_text("EXPERT", self.expert_button.left+108, self.expert_button.top+25)
        pygame.display.flip()
    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()
    