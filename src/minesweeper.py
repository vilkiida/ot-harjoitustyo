import pygame
from gamemenu import GameMenu
from highscores_menu import HighscoresMenu
from instructions import Instruction
class MainMenu:
    def __init__(self):
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.gamemenu_button = pygame.Rect(50, 75, 400, 100)
        self.highscores_button = pygame.Rect(50, 250, 400, 100)
        self.instructions_button = pygame.Rect(50, 425, 400, 100)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
        pygame.init()
        pygame.display.set_caption("MINESWEEPER")
        self.font = pygame.font.SysFont("Arial", 50)
        self.loop()
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_text(self, text, x_value, y_value):
        button_text = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def click(self, position):
        if self.gamemenu_button.collidepoint(position):
            game_menu = GameMenu()
            game_menu.run_menu()
        if self.highscores_button.collidepoint(position):
            highscore_menu = HighscoresMenu()
            highscore_menu.run_menu()
            self.reset_caption()
        if self.instructions_button.collidepoint(position):
            instruc = Instruction()
            instruc.run_instructions()
            self.reset_caption()
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
        self.draw_button(self.gamemenu_button)
        self.draw_text("PLAY", self.gamemenu_button.left+140, self.gamemenu_button.top+25)
        self.draw_button(self.highscores_button)
        self.draw_text("HIGHSCORES", self.highscores_button.left+33, self.highscores_button.top+25)
        self.draw_button(self.instructions_button)
        self.draw_text("HELP", self.instructions_button.left+140, self.instructions_button.top+25)
        pygame.display.flip()
    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()
    def reset_caption(self):
        pygame.display.set_caption("MINESWEEPER")
MainMenu()
