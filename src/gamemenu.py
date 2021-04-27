import pygame
from game import Game
from field import Field

class GameMenu:
    def __init__(self):
        self.running = False
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.easy_button = pygame.Rect(50, 125, 400, 75)
        self.easy = (9, 9, 10)
        self.mediumhard_button = pygame.Rect(50, 250, 400, 75)
        self.mediumhard = (16, 16, 40)
        self.expert_button = pygame.Rect(50, 375, 400, 75)
        self.expert = (16, 30, 99)
        self.back_button = pygame.Rect(75, 500, 350, 50)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
        self.cell_size=50
    def run_menu(self):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 50)
        self.font_small = pygame.font.SysFont("Arial", 30)
        self.running = True
        self.loop()
    def click(self, position):
        if self.easy_button.collidepoint(position):
            self.setup_game(self.easy, "easy")
            self.reset_screen_size()
            self.reset_caption()
        if self.mediumhard_button.collidepoint(position):
            self.setup_game(self.mediumhard, "mediumhard")
            self.reset_screen_size()
            self.reset_caption()
        if self.expert_button.collidepoint(position):
            self.setup_game(self.expert, "expert")
            self.reset_screen_size()
            self.reset_caption()
        if self.back_button.collidepoint(position):
            self.running = False
    def setup_game(self, difficulty, difficulty_text):
        field = Field(difficulty[0], difficulty[1], difficulty[2])
        game=Game(field, self.cell_size, difficulty_text)
        game.run_game()
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_text(self, text, font, x, y):
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x, y))
    def draw_instruction(self, text, x, y):
        instruction = self.font_small.render(text, True, (220,220,220))
        self.screen.blit(instruction, (x, y))
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
        self.draw_text("EASY", self.font, self.easy_button.left+138, self.easy_button.top+11)
        self.draw_button(self.mediumhard_button)
        self.draw_text("MEDIUMHARD", self.font, self.mediumhard_button.left+28, self.mediumhard_button.top+11)
        self.draw_button(self.expert_button)
        self.draw_text("EXPERT", self.font, self.expert_button.left+108, self.expert_button.top+11)
        self.draw_button(self.back_button)
        self.draw_text("BACK", self.font_small, self.back_button.left+135, self.back_button.top+9)
        self.draw_instruction("CHOOSE DIFFICULTY :", 100, 50)
        pygame.display.flip()
    def loop(self):
        while self.running == True:
            self.check_events()
            self.draw_screen()
    def reset_screen_size(self):
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    def reset_caption(self):
        pygame.display.set_caption("MINESWEEPER")
    