""" Moduuli, joka sisältää luokan Instruction
"""
import pygame
class Instruction:
    """ Luokka, joka vastaa peliohjesivusta
    Attributes:
        running: boolean-arvo, joka kuvaa onko peliohje sivu käynnissä
        screen_height: Lukuarvo, joka kuvaa ruudun korkeutta pikseleinä.
        screen_width: Lukuarvo, joka kuvaa ruudun leveyttä pikseleinä.
        screen: kuvaa pygamen kuvaruutua.
        back_button: rect-olio, joka kuvaa sivun back näppäintä
        button_color: tuple, joka kuvaa sivun näppäimen väriä.
        background_color: tuple, joka kuvaa sivun taustaväriä.
        font: kuvaa sivulla käytettävää fonttia, aluksi arvo None.
        font_smaller: kuvaa sivulla käytettävää fonttia, aluksi arvo None.
    """
    def __init__(self):
        """ Luokan konstruktori
        """
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
        """ Käynnistää ohje sivun.
        """
        pygame.init()
        pygame.display.set_caption("MINESWEEPER - help")
        self.font = pygame.font.SysFont("Arial", 30)
        self.font_smaller = pygame.font.SysFont("Arial", 20)
        self.running = True
        self.loop()
    def left_click(self, position):
        """ Käsittelee vasemman hiiren näppäimen painalluksesta seuraavat toimenpiteet.
        Args:
            position: Tuple, joka kuvaa koordinaatteja pisteeseen, jossa hiiri oli klikkaus hetkellä
        """
        if self.back_button.collidepoint(position):
            self.running = False
    def check_events(self):
        """ Tarkastaa kaikki oleelliset tapahtumat
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.left_click(position)
    def draw_screen(self):
        """ Piirtää näytön
        """
        self.screen.fill(self.background_color)
        self.draw_button(self.back_button)
        self.draw_button_text("BACK", self.font, self.back_button.left+135, self.back_button.top+9)
        self.draw_title(142, 50)
        self.draw_instructions()
        pygame.display.flip()
    def loop(self):
        """Silmukka, joka aina valikon käynnissä ollessa tarkastaa
            vuorotellen tapahtuneet tapahtumat ja piirtää näytön
        """
        while self.running:
            self.check_events()
            self.draw_screen()
    def draw_button(self, button):
        """ Piirtää ruudulle parametrina annetun näppäimen.
        Args:
            button: rect-olio, joka kuvaa näppäintä
        """
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_button_text(self, text, font, x_value, y_value):
        """ Piirtää ruudulle tekstit näppäimelle parametrien mukaisesti.
        Args:
            text: Merkkijonoarvo, joka kuvaa tekstin sisältöä.
            font: kuvaa käytettävää fottia.
            x_value: Lukuarvo, joka kuvaa tekstin kohdan x-koordinaattia
            y_value: Lukuarvo, joka kuvaa tekstin kohdan y-koordinaattia
        """
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def draw_title(self, x_value, y_value):
        """ Piirtää otsikon parametreinä annettuun kohtaan.
        Args:
            x_value: Lukuarvo, joka kuvaa otsikon kohdan x-koordinaattia
            y_value: Lukuarvo, joka kuvaa otsikon kohdan y-koordinaattia
        """
        title = self.font.render("HOW TO PLAY :", True, (220, 220, 220))
        self.screen.blit(title, (x_value, y_value))
    def draw_instructions(self):
        """ Piirtää ruudulle peliohjeen
        """
        lines = []
        lines.append("The goal is to clear the field without opening")
        lines.append("a cell that has a mine in it. Open a cell by")
        lines.append("using the left click. Mark a cell with a flag")
        lines.append("by using the righ click. Another right click")
        lines.append("marks a questionmark. If a cell is empty it")
        lines.append("doesn't have mines around it. If a cell has a")
        lines.append("number, it means that there are that many")
        lines.append("mines around the cell. Lose the game by")
        lines.append("opening a cell that contains a mine.")
        x_value = 63
        y_value = 150
        for line_text in lines:
            line = self.font_smaller.render(line_text, True, (220, 220, 220))
            self.screen.blit(line, (x_value, y_value))
            y_value+=30
