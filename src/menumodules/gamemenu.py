""" moduuli, joka sisältää Gamemenu luokan
"""
import pygame
from gamemodules.game import Game
from gamemodules.field import Field

class GameMenu:
    """ Luokka, joka vastaa pelivalikosta.
    Attributes:
        running: Boolean-arvo, joka kuvaa onko pelivalikko käynnissä.
        screen_height: Lukuarvo, joka kuvaa näytön korkeutta pikseleinä.
        screen_width: Lukuarvo, joka kuvaa näytön leveyttä pikseleinä.
        screen: kuvaa pygamen kuvaruutua.
        easy_button: pygamen rect-olio, joka kuvaa valikon easy näppäintä.
        easy: Tuple, jonka arvot ovat easy tasoisen pelin korkeus, leveys ja miinojen määrä.
        mediumhard_button: pygamen rect-olio, joka kuvaa valikon mediumhard näppäintä.
        mediumhard: Tuple, jonka arvot ovat mediumhard tasoisen pelin korkeus, leveys ja miinojen määrä.
        expert_button: pygamen rect-olio, joka kuvaa valikon expert näppäintä.
        expert: Tuple, jonka arvot ovat expert tasoisen pelin korkeus, leveys, ja miinojen määrä.
        back_button: pygamen rect-olio, joka kuvaa valikon back näppäintä.
        button_color: Tuple, joka kuvaa värikoodina valikon näppäimien väriä.
        background_color: Tuple, joka kuvaa värikoodina valikon taustan väriä.
        cell_size: Lukuarvo, joka kuvaa yksittäisen miinaharavakentän ruudun kokoa pikseleinä.
        font: pygame fontti valikon suuremmille teksteille.
        font_small: pygame fontti valikon pienemmille teksteille. 
    """
    def __init__(self):
        """ Luokan kostruktori.
        """
        self.running = False
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.easy_button = pygame.Rect(50, 125, 400, 75)
        self.easy = (9, 9, 10)
        self.mediumhard_button = pygame.Rect(50, 250, 400, 75)
        self.mediumhard = (16, 16, 40)
        self.expert_button = pygame.Rect(50, 375, 400, 75)
        self.expert = (16, 30, 99)
        self.back_button = pygame.Rect(75, 500, 350, 50)
        self.button_color = (140, 140, 150)
        self.background_color = (50, 50, 50)
        self.cell_size = 50
        self.font = None
        self.font_small = None
    def run_menu(self):
        """ Käynnistää pelivalikon
        """
        pygame.init()
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
            self.setup_game(self.easy, "easy")
            self.reset_screen_size()
            self.reset_caption()
        if self.mediumhard_button.collidepoint(position):
            self.setup_game(self.mediumhard, "mediumhard")
            self.reset_screen_size()
            self.reset_caption()
        if self.expert_button.collidepoint(position):
            self.setup_game(self.expert, "expert")
            self.reset_screen_size()
            self.reset_caption()
        if self.back_button.collidepoint(position):
            self.running = False
    def setup_game(self, difficulty, difficulty_text):
        """ Käynnistää parametreina annetun vaikeustason pelin.
        Args:
            difficulty: tuple, joka kertoo vaikeustason miinakentän
                korkeuden, leveyden ja miinojen määrän.
            difficulty_text: Merkkijonoarvo, joka kertoo vaikeustason
                nimen.
        """
        field = Field(difficulty[0], difficulty[1], difficulty[2])
        game = Game(field, self.cell_size, difficulty_text)
        game.run_game()
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
        """ Tarkastaa kaikki olennaiset tapahtumat
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.left_click(position)
    def draw_screen(self):
        """ Piirtää pelin näytön
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
        """Silmukka, joka aina valikon käynnissä ollessa tarkastaa
            vuorotellen tapahtuneet tapahtumat ja piirtää näytön
        """
        while self.running:
            self.check_events()
            self.draw_screen()
    def reset_screen_size(self):
        """ Uudelleenasettaa ruudun koon halutuksi
        """
        self.screen_height = 600
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    def reset_caption(self):
        """ Uudelleenasettaa ruudun otsikon halutuksi
        """
        pygame.display.set_caption("MINESWEEPER")
    