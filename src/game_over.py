import pygame
class GameOver:
    def __init__(self, was_won, time, field, cell_size):
        self.was_won = was_won
        self.time = time
        self.field = field
        self.cell_size = cell_size
        self.running = False
        self.screen_height = self.cell_size * self.field.height
        self.screen_width = self.cell_size * self.field.width
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    def run_game_over(self):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 50)
        self.running = True
        self.loop()
    def loop(self):
        while self.running:
            self.check_events()
            self.draw_screen()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.click(position)
    def draw_screen(self):
        self.screen.fill((255, 0, 0))
        for y_value in range(self.field_height):
            for x_value in range(self.field_width):
                cell = self.field.field[y_value][x_value]
                self.screen.blit(cell.image, (x_value*self.cell_size, y_value*self.cell_size))
        
        pygame.display.flip()
    




    
