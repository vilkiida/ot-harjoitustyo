""" moduuli, joka sisältää luokan MainMenu
"""
import pygame
from menumodules.gamemenu import GameMenu
from menumodules.highscores_menu import HighscoresMenu
from othermodules.instructions import Instruction
class MainMenu:
    """ Luokka, joka vastaa päävalikosta.
    Attributes:
        screen_height: Lukuarvo, joka kuvaa ruudun korkeutta pikseleinä.
        screen_width: Lukuarvo, joka kuvaa ruudun leveyttä pikseleinä.
        screen: kuvaa pygamen kuvaruutua.
        gamemenu_button: rect-olio, joka kuvaa pelivalikkoon ohjaavaa näppäintä.
        highscores_button: rect-olio, joka kuvaa highscores-valikkoon
            ohjaavaa näppäintä.
        instructions_button: rect-olio, joka kuvaa ohjesivulle ohjaavaa näppäintä.
        button_color: tuple, joka kuvaa valikon näppäimien väriä
        background_color: tuple, joka kuvaa valikon taustaväriä.
        font: kuvaa fonttia, aluksi arvo None.
    """
    def __init__(self):
        """ Luokan konstruktori.
        """
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.gamemenu_button = pygame.Rect(50, 75, 400, 100)
        self.highscores_button = pygame.Rect(50, 250, 400, 100)
        self.instructions_button = pygame.Rect(50, 425, 400, 100)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
        self.font = None
    def run_mainmenu(self):
        """ Käynnistää Päävalikon
        """
        pygame.init()
        pygame.display.set_caption("MINESWEEPER")
        self.font = pygame.font.SysFont("Arial", 50, 1)
        self.menu_loop()
    def draw_button(self, button):
        """ piirtää näytölle parametrinä annetun näppäimen
        """
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_text(self, text, x_value, y_value):
        """ Piirtää näytölle parametrien mukaisen tekstin.
        Args:
            text: Merkkijonoarvo, joka kuvaa piirrettävää tekstin
                sisältöä
            x_value: Lukuarvo, joka kuvastaa tekstin paikan
                x-koordinaattia
            y_value: Lukuarvo, joka kuvastaa tekstin paikan
                y-koordinaattia
        """
        button_text = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def left_click(self, position):
        """ Käsittelee vasemman hiiren näppäimen painalluksesta seuraavat toimenpiteet.
        Args:
            position: Tuple, joka kuvaa koordinaatteja pisteeseen, jossa hiiri oli klikkaus hetkellä
        """
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
        """Tarkastaa kaikki oleelliset tapahtumat
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
        self.draw_button(self.gamemenu_button)
        self.draw_text("PLAY", self.gamemenu_button.left+140, self.gamemenu_button.top+25)
        self.draw_button(self.highscores_button)
        self.draw_text("HIGHSCORES", self.highscores_button.left+33, self.highscores_button.top+25)
        self.draw_button(self.instructions_button)
        self.draw_text("HELP", self.instructions_button.left+140, self.instructions_button.top+25)
        pygame.display.flip()
    def menu_loop(self):
        """Silmukka, joka aina valikon käynnissä ollessa tarkastaa
            vuorotellen tapahtuneet tapahtumat ja piirtää näytön
        """
        while True:
            self.check_events()
            self.draw_screen()
    def reset_caption(self):
        """ Uudelleenasettaa ruudun otsikon
        """
        pygame.display.set_caption("MINESWEEPER")
