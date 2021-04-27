import pygame
class Game:
    def __init__(self, field, cell_size, title):
        self.title = title
        self.running = False
        self.game_lost = False
        self.game_won = False
        self.field = field
        self.cell_size = cell_size
        self.field_width = field.width
        self.field_height = field.height
        self.screen_width = self.cell_size*self.field_width
        self.screen_height = self.cell_size*self.field_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    def run_game(self):
        while True:
            pygame.init()
            pygame.display.set_caption(f"MINESWEEPER - {self.title}")
            self.running = True
            self.loop()
            break
        return
    def game_over_lost(self, y_value, x_value):
        self.field.open_all()
        self.field.blow_up_a_mine(y_value, x_value)
        self.game_lost = True
    def game_over_won(self):
        self.field.open_all()
        self.game_won = True
    def check_for_win(self):
        victory = True
        for y_value in range(0, self.field_height):
            for x_value in range(0, self.field_width):
                if not self.field.is_cell_a_mine(y_value, x_value):
                    if not self.field.is_cell_opened(y_value, x_value):
                        victory = False
        return victory
    def left_click(self, position):
        x_value = position[0] // self.cell_size
        y_value = position[1] // self.cell_size
        if self.field.field[y_value][x_value].is_a_mine():
            if not self.field.field[y_value][x_value].is_flagged():
                if not self.field.field[y_value][x_value].is_questionmark():
                    self.game_over_lost(y_value, x_value)
        else:
            if not self.check_for_win():
                self.field.open_cell(y_value, x_value)
            else:
                self.game_over_won()
    def right_click(self, position):
        x_value = position[0] // self.cell_size
        y_value = position[1] // self.cell_size
        self.field.mark_a_cell(y_value, x_value)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.game_lost:
                        self.running = False
                    if self.game_won:
                        self.running = False
                    else:
                        position = pygame.mouse.get_pos()
                        self.left_click(position)
                if event.button == 3:
                    position = pygame.mouse.get_pos()
                    self.right_click(position)
    def draw_screen(self):
        self.screen.fill((255, 0, 0))
        for y_value in range(self.field_height):
            for x_value in range(self.field_width):
                cell = self.field.field[y_value][x_value]
                self.screen.blit(cell.image, (x_value*self.cell_size, y_value*self.cell_size))
        pygame.display.flip()
    def loop(self):
        while self.running:
            self.check_events()
            self.draw_screen()
