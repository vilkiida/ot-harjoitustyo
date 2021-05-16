""" moduuli, joka sisältää luokan HighscorePage
"""
from datetime import datetime
import pygame
from databasemodules.highscore_handling import Highscores

class HighscorePage:
    """ Luokka, joka vastaa highscore-sivusta
    Attributes:
        database: Highscores-olio, jonka avulla käsitellään tietokantaa.
        difficulty: Merkkijonoarvo, joka kuvaa vaikeustasoa nimeltä.
        screen_height: Lukuarvo, joka kuvaa ruudun korkeutta pikseleinä.
        screen_width: Lukuarvo, joka kuvaa ruudun leveyttä pikseleinä.
        screen: kuvaa pygamen kuvaruutua.
        back_button: rect-olio, joka kuvaa back näppäintä.
        erase_button: rect-olio, joka kuvaa erase scores näppäintä.
        button_color: tuple, joka kuvaa sivun näppäimien väriä.
        background-color: tuple, joka kuva sivun taustaväriä.
        font: kuvaa fonttia, jonka arvo on aluksi None.
        font_smaller: kuvaa fonttia, jonka arvo on aluksi None.
    """
    def __init__(self, difficulty:str):
        """ Luokan konstruktori
        Args:
            difficulty: Merkkijonoarvo, joka kuvaa vaikeustasoa
                nimeltä
        """
        self.database = Highscores()
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
        """ Käynnistää highscore-sivun
        """
        pygame.init()
        pygame.display.set_caption("MINESWEEPER - highscores-" + self.difficulty)
        self.font = pygame.font.SysFont("Arial", 30, True)
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
        if self.erase_button.collidepoint(position):
            self.erase_scores()
    def check_events(self):
        """ Tarkistaa kaikki oleelliset tapahtumat
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
        """Silmukka, joka aina valikon käynnissä ollessa tarkastaa
            vuorotellen tapahtuneet tapahtumat ja piirtää näytön
        """
        while self.running:
            self.check_events()
            self.draw_screen()
    def draw_title(self, x_value, y_value):
        """ Piirtää otsikon parametreinä annettuun kohtaan.
        Args:
            x_value: Lukuarvo, joka kuvaa otsikon paikan
                x-koordinaattia
            y-value: Lukuarvo, joka kuvaa otsikon paikan
                y-koordinaattia
        """
        title_text="Highscores for " + self.difficulty+ " :"
        title = self.font.render(title_text, True, (220, 220, 220))
        self.screen.blit(title, (x_value, y_value))
    def draw_button(self, button, button_color):
        """ Piirtää parametreinä annetun näppäimen annetulla värillä
        Args:
            button: rect-olio, joka kuvaa näppäintä
            button-color: tuple, joka kuvaa näppäimen väriä
        """
        pygame.draw.rect(self.screen, button_color, button)
    def draw_button_text(self, text, font, x_value, y_value):
        """ Piirtää tekstin_näppäimiin
        Args:
            text: Merkkojonoarvo, joka kuvaa tekstin sisältöä.
            font: kuvaa käytettävää fonttia.
            x_value: Lukuarvo, joka kuvaa tekstin paikan
                x-koordinaattia.
            y-value: Lukuarvo, joka kuvaa tekstin paikan
                y-koordinaattia.
        """
        button_text = font.render(text, True, (0, 0, 0))
        self.screen.blit(button_text, (x_value, y_value))
    def get_highscores(self):
        """ Palauttaa highscore-tietokannasta tiedot 5 parhaasta
            tuloksesta
        """
        return self.database.get_high_scores(self.difficulty)
    def erase_scores(self):
        """ Poistaa kyseisen vaikeustason tulokset tietokannasta
        """
        self.database.erase_scores(self.difficulty)
    def format_time(self, time):
        """ Muotoilee pelin suoritusajan oikeaan muotoon
        Args: Lukuarvo, joka kuvaa suoritusajan sekunteina.
        """
        hours = time // 3600
        time = time - hours*3600
        minutes = time // 60
        seconds = time - minutes*60
        return ('%d:%d:%d' %(hours, minutes, seconds))
    def format_date(self, date):
        """ Muotoilee merkkijonona olevan aikaleiman oikeaan
            muotoon
        Args:
            date: Merkkijonoarvo ,joka kuva aikaleimaa voitetun pelin
                päättymisestä
        """
        date = date[:16]
        datetime_object = datetime.strptime(date, "%Y-%m-%d %H:%M")
        return datetime_object.strftime("%H:%M %d.%m.%y")
    def draw_scoreboard(self):
        """ Piirtää highscore taulukon
        """
        scores = self.get_highscores()
        x_value=63
        y_value=150
        text_date = "DATE"
        text_score = "SCORE"
        titles_text = f"{text_date:>30}                {text_score}"
        titles = self.font_smaller.render(titles_text, True, (220, 220, 220))
        self.screen.blit(titles, (x_value, y_value))
        y_value+=40
        for i in range(0, 5):
            try:
                time = scores[i][1]
                score_time = self.format_time(time)
                rank = f"{i+1}."
                formatted_date = self.format_date(scores[i][0])
                score_text = f"{rank:17}{formatted_date}            {score_time}"
            except:
                rank = f"{i+1}."
                score_text = f"{rank}   ----------------- NO SCORE -----------------"
            score = self.font_smaller.render(score_text, True, (220, 220, 220))
            self.screen.blit(score, (x_value, y_value))
            y_value += 40
