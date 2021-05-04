""" Moduuli, joka sisältää luokan Game.
"""
import time
import pygame
class Game:
    """ Luokka, joka vastaa yksittäisen miinaharava pelin toiminnasta.
    Attributes:
        field: Field-luokan olio, joka on kyseisen pelin pelikenttä.
        cell_size: Lukuarvo, joka kuvastaa yksittäisen pelikentän ruudun kokoa.
        field_width: Lukuarvo, joka kuvastaa pelin Field-olion kentän leveyttä.
        field_height: Lukuarvo, joka kuvastaa pelin Field-olion kentän korkeutta.
        screen_width: Lukuarvo, joka kuvastaa pelin näytön leveyttä.
        screen_height: Lukuarvo, joka kuvastaa pelin näytön korkeutta.
        screen: muuttuja, johon on tallennettuna pelin näyttö.
        title: Merkkijonoarvo, joka kuvaa peli-ikkunaan merkittävää otsikkoa.
        running: Boolean-arvo, joka kuvaa onko peli sillä hetkellä käynnissä.
        game_lost: Boolean-arvo, joka kuvaa onko peli hävitty.
        game_won: Boolean-arvo, joka kuvaa onko peli voitettu.
        start_time: Lukuarvo, joka kuvaa aikaa, jolloin peli lähtee käyntiin
        end_time: Lukuarvo, joka kuvaa aikaa, jolloin peli loppuu joko voiton tai häviön ansiosta.
        time: Lukuarvo, joka kuvaa peliin käytettyä aikaa.
        font: Fontti, jota käytetään "GAME LOST" ja "GAME WON!" teksteihin.
        font_small: Fontti, jota käytetään, muihin teksteihin.
    """
    def __init__(self, field, cell_size, title):
        """ Luokan konstruktori. Asettaa pelin attribuutit argumenttien mukaisesti.
        Args:
            field: Field-luokan olio, joka on kyseisen pelin kenttänä.
            cell_size: Lukuarvo, joka kuvastaa yksittäisen pelikentän ruudun kokoa.
            title: Merkkijonoarvo, joka kuvaa peli-ikkunaan merkittävää otsikkoa.
        """
        self.field = field
        self.cell_size = cell_size
        self.field_width = field.width
        self.field_height = field.height
        self.screen_width = self.cell_size*self.field_width
        self.screen_height = self.cell_size*self.field_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.title = title
        self.running = False
        self.game_lost = False
        self.game_won = False
        self.start_time = None
        self.end_time = None
        self.time = None
        self.font = None
        self.font_small = None
    def run_game(self):
        """ Asettaa pelin käynnistämistä varten tarvittavat attribuutit oikein ja käynnistää pelin.
        """
        while True:
            pygame.init()
            self.font = pygame.font.SysFont("ARIAL", 50, 1)
            self.font_small = pygame.font.SysFont("ARIAL", 25, 1)
            pygame.display.set_caption(f"MINESWEEPER - {self.title}")
            self.running = True
            self.loop()
            break
        return
    def handle_time(self):
        """ Laskee start_timen ja end_timen avulla peliin kuluneen ajan ja
            palauttaa sen oikeassa muodossa.
        """
        difference = self.end_time - self.start_time
        hours = difference // 3600
        difference = difference - hours*3600
        minutes = difference // 60
        seconds = difference - minutes*60
        self.time = ('%d:%d:%d' %(hours, minutes, seconds))
    def game_over_lost(self, y_value, x_value):
        """ Tekee pelin häviämisen jälkeen tapahtuvat toimenpiteet.
            Näitä ovat: ajan laskeminen, kaikkien ruutujen avaaminen,
            annettujen koordinnaattien mukaisen ruudun räjäyttäminen
            sekä pelin merkitseminen hävityksi.
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        self.handle_time()
        self.field.open_all()
        self.field.blow_up_a_mine(y_value, x_value)
        self.game_lost = True
    def game_over_won(self):
        """ Tekee pelin voittamisen jälkeen tapahtuvat toimenpiteet.
            Näitä ovat: ajan laskeminen, kaikkien ruutujen avaaminen
            sekä pelin merkitseminen voitetuksi
        """
        self.handle_time()
        self.field.open_all()
        self.game_won = True
    def check_for_win(self):
        """ Tarkistaa onko peli voitettu, eli kaikki miinattomat
            ruudut avattu.
        """
        victory = True
        for y_value in range(0, self.field_height):
            for x_value in range(0, self.field_width):
                if not self.field.is_cell_a_mine(y_value, x_value):
                    if not self.field.is_cell_opened(y_value, x_value):
                        victory = False
        return victory
    def left_click(self, position):
        """ Käsittelee vasemman hiirennäppäimen klikkaamisesta seuraavat
            tapahtumat.
        Args:
            position: Tuple, joka sisältää koordinaatit pisteeseen, jossa
            hiiri on ollut klikkaamis hetkellä.
        """
        x_value = position[0] // self.cell_size
        y_value = position[1] // self.cell_size
        if self.is_first_move():
            self.start_time = time.time()
        if self.field.field[y_value][x_value].is_a_mine():
            if not self.field.field[y_value][x_value].is_flagged():
                if not self.field.field[y_value][x_value].is_questionmark():
                    self.end_time = time.time()
                    self.game_over_lost(y_value, x_value)
        else:
            self.field.open_cell(y_value, x_value)
            if self.check_for_win():
                self.end_time = time.time()
                self.game_over_won()
    def is_first_move(self):
        """ Tarkistaa onko kaikki ruudut vielä avaamattomia, eli onko
        seuraava klikkaus ensimmäinen.
        """
        all_closed = True
        for y_value in range(self.field_height):
            for x_value in range(self.field.width):
                if self.field.field[y_value][x_value].is_opened():
                    all_closed = False
        return all_closed
    def right_click(self, position):
        """ Käsittellee oikeanpuolimmaisen hiiren näppäimen painalluksesta
            seuraavat tapahtumat
        Args:
            position: Tuple, joka sisältää koordinaatit pisteeseen, jossa
            hiiri on ollut klikkaamis hetkellä.
        """
        x_value = position[0] // self.cell_size
        y_value = position[1] // self.cell_size
        self.field.mark_a_cell(y_value, x_value)
    def check_events(self):
        """ Tarkistaa kaikki pelin tapahtumat.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.game_lost:
                        self.running = False
                    elif self.game_won:
                        self.running = False
                    else:
                        position = pygame.mouse.get_pos()
                        self.left_click(position)
                if event.button == 3:
                    position = pygame.mouse.get_pos()
                    self.right_click(position)
    def draw_screen(self):
        """ Piirtää näytölle halutut asiat.
        """
        self.screen.fill((255, 0, 0))
        for y_value in range(self.field_height):
            for x_value in range(self.field_width):
                cell = self.field.field[y_value][x_value]
                self.screen.blit(cell.image, (x_value*self.cell_size, y_value*self.cell_size))
        if self.game_lost:
            self.game_lost_graphics()
        if self.game_won:
            self.game_won_graphics()
        pygame.display.flip()
    def game_lost_graphics(self):
        """ Piirtää näytölle tarvittavat tekstit, kun peli on hävitty.
        """
        game_lost = self.font.render("GAME LOST", True, (255, 255, 255), (128, 0, 0))
        self.screen.blit(game_lost, (self.screen_width//2 - 150, self.screen_height//2 - 50))
        text1 = ("YOUR TIME: " + self.time)
        game_time = self.font_small.render(text1, True, (255, 255, 255), (128, 0, 0))
        self.screen.blit(game_time, (self.screen_width // 2 - 105, self.screen_height // 2 + 10))
        text2 = "click anywhere to go back"
        back = self.font_small.render(text2, True, (255, 255, 255), (128, 0, 0))
        self.screen.blit(back, (self.screen_width//2 - 153, self.screen_height//2 + 80))
    def game_won_graphics(self):
        """ Piirtää näytölle tarvittavat tekstit, kun peli on voitettu.
        """
        game_won = self.font.render("GAME WON!", True, (255, 255, 255), (0, 150, 150))
        self.screen.blit(game_won, (self.screen_width//2 - 150, self.screen_height // 2 -50))
        text1 = ("YOUR TIME: " + self.time)
        game_time = self.font_small.render(text1, True, (255, 255, 255), (0, 150, 150))
        self.screen.blit(game_time, (self.screen_width // 2 - 105, self.screen_height // 2 + 10))
        text2 = "click anywhere to go back"
        back = self.font_small.render(text2, True, (255, 255, 255), (0, 150, 150))
        self.screen.blit(back, (self.screen_width//2 - 153, self.screen_height//2 + 80))
    def loop(self):
        """ Peli silmukka, joka tarkistaa tapahtumat ja piirtää näytön,
            aina uudelleen, niin kauan kunnes peli ei ole enää käynnissä.
        """
        while self.running:
            self.check_events()
            self.draw_screen()
