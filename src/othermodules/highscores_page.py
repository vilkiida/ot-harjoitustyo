import pygame
from databasemodules.highscore_handling import Highscores

class HighscorePage:
    def __init__(self, difficulty:str):
        self.db = Highscores()
        self.difficulty = difficulty
        self.running = False
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.back_button = pygame.Rect(75, 500, 350, 50)
        self.erase_button = pygame.Rect(75, 420, 350, 50)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
        self.font = None
        self.font_smaller = None
    def run_highscore_page(self):
        pygame.init()
        pygame.display.set_caption("MINESWEEPER - highscores-" + self.difficulty)
        self.font = pygame.font.SysFont("Arial", 30)
        self.font_smaller = pygame.font.SysFont("Arial", 20)
        self.running = True
        self.loop()
    def click(self, position):
        if self.back_button.collidepoint(position):
            self.running = False
        if self.erase_button.collidepoint(position):
            self.erase_scores()
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
        self.draw_button(self.back_button, self.button_color)
        self.draw_button_text("BACK", self.font, self.back_button.left+135, self.back_button.top+9)
        self.draw_button(self.erase_button, (246, 86, 86))
        self.draw_button_text("ERASE SCORES", self.font, self.erase_button.left+70, self.erase_button.top+9)
        if self.difficulty == "mediumhard":
            self.draw_title(70, 50)
        else:
            self.draw_title(125, 50)
        self.draw_scoreboard()
        pygame.display.flip()
    def loop(self):
        while self.running:
            self.check_events()
            self.draw_screen()
    def draw_title(self, x_value, y_value):
        title_text="Highscores for " + self.difficulty+ " :"
        title = self.font.render(title_text, True, (220, 220, 220))
        self.screen.blit(title, (x_value, y_value))
    def draw_button(self, button, button_color):
        pygame.draw.rect(self.screen, button_color, button)
    def draw_button_text(self, text, font, x_value, y_value):
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def get_highscores(self):
        return self.db.get_high_scores(self.difficulty)
    def erase_scores(self):
        self.db.erase_scores(self.difficulty)
    def draw_scoreboard(self):
        scores = self.get_highscores()
        x_value=63
        y_value=150
        for i in range(0, 5):
            try:
                time = scores[i]
                hours = time // 3600
                time - hours*3600
                minutes = time // 60
                seconds = time - minutes*60
                score_time = ('%d:%d:%d' %(hours, minutes, seconds))
                rank = f"{i+1}."
                score_text = f"{rank:55}{score_time}"
            except:
                rank = f"{i+1}."
                score_text = f"{rank}   ----------------- NO SCORE -----------------"
            score = self.font_smaller.render(score_text, True, (220, 220, 220))
            self.screen.blit(score, (x_value, y_value))
            y_value += 40    
