""" moduuli joka sisältää HighscoresMenu luokan.
"""
import pygame
from othermodules.highscores_page import HighscorePage
class HighscoresMenu:
    """ Luokka joka vastaa highscores-valikosta.
    Attributes:
        running:  Boolean-arvo, joka kuvaa onko highscores-valikko käynnissä.
        screen_height: Lukuarvo, joka kuvaa näytön korkeutta pikseleinä.
        screen_width: Lukuarvo, joka kuvaa näytön leveyttä pikseleinä.
        screen: kuvaa pygame kuvaruutua
        easy_button: pygamen rect-olio, joka kuvaa valikon easy näppäintä.
        mediumhard_button: pygamen rect-olio, joka kuvaa valikon mediumhard näppäintä.
        expert_button: pygamen rect-olio, joka kuvaa valikon expert näppäintä
        back_button: pygamen rect-olio, joka kuvaa valikon back näppäintä.
        button_color: tuple, joka kuvaa valikon näppäimien väriä.
        backround_color: tuple, joka kuvaa valion taustaväriä.
        font: Kuvaa fonttia. Aluksi arvona None.
        font_small: Kuvaa fonttia. Aluksi arvona None.
    """
    def __init__(self):
        """ Luokan konstruktori
        """
        self.running = False
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.easy_button = pygame.Rect(50, 125, 400, 75)
        self.mediumhard_button = pygame.Rect(50, 250, 400, 75)
        self.expert_button = pygame.Rect(50, 375, 400, 75)
        self.back_button = pygame.Rect(75, 500, 350, 50)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
        self.font = None
        self.font_small = None
    def run_menu(self):
        """ Käynnistää highscore-valikon
        """
        pygame.init()
        pygame.display.set_caption("MINESWEEPER - highscores")
        self.font = pygame.font.SysFont("Arial", 50, 1)
        self.font_small = pygame.font.SysFont("Arial", 30, 1)
        self.running = True
        self.menu_loop()
    def left_click(self, position):
        """ Käsittelee vasemman hiiren näppäimen painalluksesta seuraavat toimenpiteet.
        Args:
            position: Tuple, joka kuvaa koordinaatteja pisteeseen, jossa hiiri oli klikkaus hetkellä
        """
        if self.easy_button.collidepoint(position):
            easy_score_page = HighscorePage("easy")
            easy_score_page.run_highscore_page()
            self.reset_caption()
        if self.mediumhard_button.collidepoint(position):
            mediumhard_score_page = HighscorePage("mediumhard")
            mediumhard_score_page.run_highscore_page()
            self.reset_caption()
        if self.expert_button.collidepoint(position):
            expert_score_page = HighscorePage("expert")
            expert_score_page.run_highscore_page()
            self.reset_caption()
        if self.back_button.collidepoint(position):
            self.running = False
    def draw_button(self, button):
        """ Piirtää näytölle parametrinä annetun näppäimen
        Args:
            button: rect-olio, joka kuvastaa näppäintä
        """
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_text(self, text, font, x_value, y_value):
        """ Piirtää näytölle parametrien mukaisen tekstin.
        Args:
            text: Merkkijonoarvo, joka kuvaa piirrettävää tekstin
                sisältöä
            font: käytettävä fontti
            x_value: Lukuarvo, joka kuvastaa tekstin paikan
                x-koordinaattia
            y_value: Lukuarvo, joka kuvastaa tekstin paikan
                y-koordinaattia
        """
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def draw_instruction(self, text, x_value, y_value):
        """ Piirtää näytölle ohjeistuksen parametrien mukaisesti.
        Args:
            text: Merkkijonoarvo, joka kuvastaa ohjeistuksen sisältöä.
            x_value: Lukuarvo, joka kuvastaa ohjeistuksen paikan
                x-koordinaattia
            y_value: Lukuarvo, joka kuvastaa ohjeistuksen paikan
                y-koordinaattia
        """
        instruction = self.font_small.render(text, True, (220, 220, 220))
        self.screen.blit(instruction, (x_value, y_value))
    def check_events(self):
        """Tarkastaa kaikki olennaiset tapatumat
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
        self.draw_button(self.easy_button)
        self.draw_text("EASY", self.font, self.easy_button.left+138, self.easy_button.top+11)
        self.draw_button(self.mediumhard_button)
        x_value = self.mediumhard_button.left+28
        y_value = self.mediumhard_button.top+11
        self.draw_text("MEDIUMHARD", self.font, x_value, y_value)
        self.draw_button(self.expert_button)
        self.draw_text("EXPERT", self.font, self.expert_button.left+108, self.expert_button.top+11)
        self.draw_button(self.back_button)
        self.draw_text("BACK", self.font_small, self.back_button.left+135, self.back_button.top+9)
        self.draw_instruction("CHOOSE DIFFICULTY :", 100, 50)
        pygame.display.flip()
    def menu_loop(self):
        """ Peli silmukka, joka aina valikon käynnissä ollessa tarkastaa
            vuorotellen tapahtuneet tapahtumat ja piirtää näytön
        """
        while self.running:
            self.check_events()
            self.draw_screen()
    def reset_caption(self):
        """ Uudelleen asettaa ruudun otsikon halutuksi
        """
        pygame.display.set_caption("MINESWEEPER - highscores")
            