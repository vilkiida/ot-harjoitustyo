import pygame

class Instruction:
    def __init__(self):
        self.running = False
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.back_button = pygame.Rect(75, 500, 350, 50)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
    def run_instructions(self):
        pygame.init()
        pygame.display.set_caption("MINESWEEPER - help")
        self.font = pygame.font.SysFont("Arial", 30)
        self.font_smaller = pygame.font.SysFont("Arial", 20)
        self.running = True
        self.loop()
    def click(self, position):
        if self.back_button.collidepoint(position):
            self.running = False
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
        self.draw_button(self.back_button)
        self.draw_button_text("BACK", self.font, self.back_button.left+135, self.back_button.top+9)
        self.draw_title(142, 50)
        self.draw_instructions()
        pygame.display.flip()
    def loop(self):
        while self.running == True:
            self.check_events()
            self.draw_screen()
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_button_text(self, text, font, x, y):
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x, y))
    def draw_title(self, x, y):
        title = self.font.render("HOW TO PLAY :", True, (220, 220, 220))
        self.screen.blit(title, (x, y))
    def draw_instructions(self):
        line1 = self.font_smaller.render("The goal is to clear the field without opening", True, (220, 220, 220))
        self.screen.blit(line1, (63, 150))
        line2 = self.font_smaller.render("a cell that has a mine in it. Open a cell by", True, (220, 220, 220))
        self.screen.blit(line2, (63, 180))
        line3 = self.font_smaller.render("using the left click. Mark a cell with a flag", True, (220, 220, 220))
        self.screen.blit(line3, (63, 210))
        line4 = self.font_smaller.render("by using the righ click. Another right click", True, (220, 220, 220))
        self.screen.blit(line4, (63, 240))
        line5 = self.font_smaller.render("marks a questionmark. If a cell is empty it", True, (220, 220, 220))
        self.screen.blit(line5, (63, 270))
        line6 = self.font_smaller.render("doesn't have mines around it. If a cell has a", True, (220, 220, 220))
        self.screen.blit(line6, (63, 300))
        line7 = self.font_smaller.render("number, it means that there are that many", True, (220, 220, 220))
        self.screen.blit(line7, (63, 330))
        line8 = self.font_smaller.render("mines around the cell. Lose the game by", True, (220, 220, 220))
        self.screen.blit(line8, (63, 360))
        line9 = self.font_smaller.render("opening a cell that contains a mine.", True, (220, 220, 220))
        self.screen.blit(line9, (63, 390))