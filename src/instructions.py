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
        self.font = None
        self.font_smaller = None
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
        while self.running:
            self.check_events()
            self.draw_screen()
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_button_text(self, text, font, x_value, y_value):
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def draw_title(self, x_value, y_value):
        title = self.font.render("HOW TO PLAY :", True, (220, 220, 220))
        self.screen.blit(title, (x_value, y_value))
    def draw_instructions(self):
        line1_text = "The goal is to clear the field without opening"
        line2_text = "a cell that has a mine in it. Open a cell by"
        line3_text = "using the left click. Mark a cell with a flag"
        line4_text = "by using the righ click. Another right click"
        line5_text = "marks a questionmark. If a cell is empty it"
        line6_text = "doesn't have mines around it. If a cell has a"
        line7_text = "number, it means that there are that many"
        line8_text = "mines around the cell. Lose the game by"
        line9_text = "opening a cell that contains a mine."
        line1 = self.font_smaller.render(line1_text, True, (220, 220, 220))
        self.screen.blit(line1, (63, 150))
        line2 = self.font_smaller.render(line2_text, True, (220, 220, 220))
        self.screen.blit(line2, (63, 180))
        line3 = self.font_smaller.render(line3_text, True, (220, 220, 220))
        self.screen.blit(line3, (63, 210))
        line4 = self.font_smaller.render(line4_text, True, (220, 220, 220))
        self.screen.blit(line4, (63, 240))
        line5 = self.font_smaller.render(line5_text, True, (220, 220, 220))
        self.screen.blit(line5, (63, 270))
        line6 = self.font_smaller.render(line6_text, True, (220, 220, 220))
        self.screen.blit(line6, (63, 300))
        line7 = self.font_smaller.render(line7_text, True, (220, 220, 220))
        self.screen.blit(line7, (63, 330))
        line8 = self.font_smaller.render(line8_text, True, (220, 220, 220))
        self.screen.blit(line8, (63, 360))
        line9 = self.font_smaller.render(line9_text, True, (220, 220, 220))
        self.screen.blit(line9, (63, 390))
        