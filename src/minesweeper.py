import pygame
from gamemenu import GameMenu
class MainMenu:
    def __init__(self):
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.gamemenu_button = pygame.Rect(50, 75, 400, 100)
        self.gamemenu_text = "PLAY"
        self.highscores_button = pygame.Rect(50, 250, 400, 100)
        self.highscores_text = "HIGHSCORES"
        self.instructions_button = pygame.Rect(50, 425, 400, 100)
        self.instructions_text = "HELP"
        self.button_color = (180, 180, 180)
        self.background_color = (50, 50, 50)
        #self.font = pygame.font.SysFont(None, 50)
        pygame.init()
        self.loop()

    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
        # button_text = self.font.render(text, True, (0, 0, 0))
        # x=button.left + 100
        # y=button.top + 25
        # self.screen.blit(button_text, x, y)
    def click(self, position):
        if self.gamemenu_button.collidepoint(position):
            GameMenu()
        if self.highscores_button.collidepoint(position):
            print("highscores")
        if self.instructions_button.collidepoint(position):
            print("help")

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
        self.draw_button(self.highscores_button)
        self.draw_button(self.instructions_button)

        pygame.display.flip()

    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()

MainMenu()
