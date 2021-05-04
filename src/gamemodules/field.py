""" Moduuli, joka sisältää luokan Field.
"""
from random import randint
from gamemodules.cell import Cell
class Field:
    """ Luokka, joka kuvaa yksittäistä pelikenttää.
    Attributes:
        height: Lukuarvo, joka kuvastaa montako ruutua pelikentällä on pystysuunnassa.
        width: Lukuarvo, joka kuvastaa montako ruutua pelikentällä on vaakasuunnassa.
        how_many_mines: Lukuarvo, joka kuvastaa montako miinaa sisältävää ruutua pelikentällä on.
    """
    def __init__(self, height, width, how_many_mines):
        """ Luokan konstruktori. Luo uuden pelikentän sekä etsii ja
            merkitsee, jokaiselle pelikentän ruudulle sen vierus ruutujen koordinaatit.
        Args:
            height: Lukuarvo, joka kuvastaa montako
                    ruutua pelikentällä on pystysuunnassa (pakollinen).
            width: Lukuarvo, joka kuvastaa montako
                    ruutua pelikentällä on vaakasuunnassa. (pakollinen).
            how_many_mines: Lukuarvo, joka kuvastaa montako
                    miinaa siltävää ruutua pelikentällä on (pakollinen).
        """
        self.height = height
        self.width = width
        self.how_many_mines = how_many_mines
        self.create_a_field()
        self.find_neighbours()
    def create_a_field(self):
        """ Luo uuden pelikentän ja muttaa how_many_mines attribuutin
            mukaisen määrän ruutuja miinoja sisältäviksi.
        """
        self.field = [[Cell() for w in range(self.width)] for h in range(self.height)]
        for _ in range(self.how_many_mines):
            while True:
                x_value = randint(0, self.width-1)
                y_value = randint(0, self.height-1)
                if not self.field[y_value][x_value].mine:
                    self.field[y_value][x_value].turn_into_a_mine()
                    break
    def find_neighbours(self):
        """ Kutsuu funktiota list_neighbours, jokaiselle pelikentän ruudulle.
        """
        for y_value in range(0, self.height):
            for x_value in range(0, self.width):
                self.list_neighbours(y_value, x_value)
    def list_neighbours(self, y_value, x_value):
        """ listaa annettujen koordinaattien omaavan ruudun kaikkien viereisten ruutujen
            koordinaatit listaksi. Kutsutaan kyseiselle ruudulle funktiota mark_neighbours ja
            annetaan parametriksi luotu lista.
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        neighbours = []
        for n_y in range(y_value - 1, y_value + 2):
            for n_x in range(x_value - 1, x_value + 2):
                if n_y == y_value and n_x == x_value:
                    continue
                if n_y < 0 or n_x < 0:
                    continue
                if n_y > (self.height-1):
                    continue
                if n_x > (self.width-1):
                    continue
                else:
                    neighbours.append((n_y, n_x))
        self.field[y_value][x_value].mark_neighbours(neighbours)
        self.check_neighbours(y_value, x_value)
    def check_neighbours(self, y_value, x_value):
        """ Laskee annettujen koordinaattien omaan ruudun ympärillä olevien ruutujen
            määrän, joissa on miina.
        Args:
            y_value:Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value:Lukuarvo, joka kuvaa kyseessä olevan ruudun x_koordinaatin arvoa.
        """
        neighbour_mines_amount = 0
        for neighbour in self.field[y_value][x_value].neighbours:
            if self.is_cell_a_mine(neighbour[0], neighbour[1]):
                neighbour_mines_amount += 1
        self.field[y_value][x_value].mark_neigbour_mines(neighbour_mines_amount)
    def open_cell(self, y_value, x_value):
        """ Avaa annettujen koordinaattien omaavan ruudun, jos se ei ole merkattu
            lipulla tai kysymysmerkillä. Jos kyseisellä ruudulla ei ole yhtään miinaa
            sen viereisissä ruuduissa, kutsutaan täämän lisäksi myös funktiota
            open_empty_neighbours
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        if not self.field[y_value][x_value].is_opened():
            if not self.field[y_value][x_value].is_flagged():
                if not self.field[y_value][x_value].is_questionmark():
                    if self.field[y_value][x_value].neighbour_mines == 0:
                        self.field[y_value][x_value].open()
                        self.open_empty_neighbours(y_value, x_value)
                    else:
                        self.field[y_value][x_value].open()
    def open_empty_neighbours(self, y_value, x_value):
        """ Käy läpi annettujen koordinaattien omaavan ruudun naapurit ja
            kutsuu nille funktiota open, jos ne eivät ole miinoja.
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        for neighbour in self.field[y_value][x_value].neighbours:
            if not self.field[neighbour[0]][neighbour[1]].is_opened():
                if not self.field[neighbour[0]][neighbour[1]].is_a_mine():
                    self.open_cell(neighbour[0], neighbour[1])
    def open_all(self):
        """ Avaa kaikki pelikentän ruudut, eli kutsuu kaikille ruuduille
            funktiota open.
        """
        for y_value in range(0, self.height):
            for x_value in range(0, self.width):
                self.field[y_value][x_value].open()
    def mark_a_cell(self, y_value, x_value):
        """ Merkitsee annettujen koordinaattien mukaisen avaamattoman ruudun riippuen tämän
            nykyisestä tilasta. Jos ruudussa ei ole merkintöjä, kutsutaan sille funktiota
            mark_flag. Jos ruudussa on lippu, kutsutaan sille funktiota mark_questionmark.
            Jos ruudussa on kysymerkki, kutsutaan sille funktiota remove_markings.
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        if not self.field[y_value][x_value].is_opened():
            if self.field[y_value][x_value].is_not_marked():
                self.field[y_value][x_value].mark_flagg()
            elif self.field[y_value][x_value].is_flagged():
                self.field[y_value][x_value].mark_questionmark()
            elif self.field[y_value][x_value].is_questionmark():
                self.field[y_value][x_value].remove_markings()
    def blow_up_a_mine(self, y_value, x_value):
        """ Kutsuu annettujen koordinaattien omaavaa ruutua funktioll a blow_up eli merkitsee
            sen räjäytetyksi
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        self.field[y_value][x_value].blow_up()
    def is_cell_a_mine(self, y_value, x_value):
        """ Palauttaa arvon True jos annetut koordinaatit omaava ruutu on miina.
            Muuten palauttaa arvon False.
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        if self.field[y_value][x_value].is_a_mine():
            return True
        return False
    def is_cell_opened(self, y_value, x_value):
        """ Palauttaa arvon True, jos annetut koordinaatit omaava ruutu on avattu.
            Muuten palauttaa arvon False.
        Args:
            y_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun y-koordinaatin arvoa.
            x_value: Lukuarvo, joka kuvaa kyseessä olevan ruudun x-koordinaatin arvoa.
        """
        if self.field[y_value][x_value].is_opened():
            return True
        return False
