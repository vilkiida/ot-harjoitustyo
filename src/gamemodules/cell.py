""" Moduuli, joka sisältää luokan Cell.
"""
import pygame
from load_image import load_image
class Cell:
    """ Luokka, joka kuvaa yksittäistä ruutua miinaharavakentässä.

    Attributes:
        mine: Boolean-arvo, joka kuvastaa onko kyseinen ruutu miina.
        opened: Boolean-arvo, joka kuvastaa onko kyseinen ruutu avattu.
        flagged: Boolean-arvo, joka kuvastaa onko kyseinen ruutu merkitty lipulla.
        questionmark: Boolean-arvo, joka kuvastaa onko kyseinen ruutu merkitty kysymysmerkillä.
        neighbours: Lista, johon merkitään kaikkien ruudun ympärillä olevien
                    ruutujen y- ja x-koordinaatit.
        neighbour_mines: Lukuarvo, joka kertoo kuinka monessa ruudun viereisistä ruuduista on miina.
        image: Ruudun png-muotoinen kuva.
    """
    def __init__(self):
        """ Luokan konstruktori. Luo uuden ruudun. Konstruktorille ei anneta argumentteja.
        """
        self.mine = False
        self.opened = False
        self.flagged = False
        self.questionmark = False
        self.neighbours = []
        self.neighbour_mines = None
        self.image = load_image("ms-unopened.png")
    def is_a_mine(self):
        """ Palauttaa arvon True, jos kyseisessä ruudussa on miina,. Muuten funktio palauttaa False.
        """
        return self.mine
    def is_opened(self):
        """ Palauttaa arvon True, jos kyseinen ruutu on avattu. Muuten funktio palauttaa False.
        """
        return self.opened
    def is_flagged(self):
        """ Palauttaa arvon True, jos kyseinen ruutu on merkattu lipulla.
            Muuten funktio palauttaa False.
        """
        if not self.questionmark:
            if self.flagged:
                return True
        return False
    def is_not_marked(self):
        """ Palauttaa arvon True, jos kyseinen ruutu ei ole merkattu kysymysmerkillä eikä lipulla.
            Muussa tapauksessa palauttaa arvon False.
        """
        if not self.flagged:
            if not self.questionmark:
                return True
        return False
    def is_questionmark(self):
        """ Palauttaa arvon True, jos kyseinen ruutu on merkatty kysymysmerkillä.
            Muuten funktio palauttaa False.
        """
        if not self.flagged:
            if self.questionmark:
                return True
        return False
    def turn_into_a_mine(self):
        """ Muuttaa kyseisen ruudun miinaksi, eli merkitsee mine boolean arvon arvoksi True.
        """
        self.mine = True
    def mark_neighbours(self, neighbours):
        """ Muuttaa parametrinä saamansa listan attribuutin neighbours arvoksi.
        Args:
            neighbours: Lista koordinaateista, jotka kuuluvat ruudun ympärillä oleville ruuduille.
        """
        self.neighbours = neighbours
    def mark_neigbour_mines(self, neighbour_mines):
        """ Muuttaa parametrinä saamansa lukuarvon attribuutin neighbour_mines arvoksi.
        Args:
            neighbour_mines: Lukumäärä ruudun ympärillä olevista ruuduista, joissa on miina.
        """
        self.neighbour_mines = neighbour_mines
    def open(self):
        """ Avaa kyseisen ruudun. Muuttaa image attribuutin kuvan,
            riippuuen neighbour_mines attribuutin arvosta.
        """
        if self.opened:
            pass
        else:
            self.opened = True
            if not self.mine:
                if self.neighbour_mines == 0:
                    self.image = load_image("ms-opened.png")
                elif self.neighbour_mines == 1:
                    self.image = load_image("ms-1.png")
                elif self.neighbour_mines == 2:
                    self.image = load_image("ms-2.png")
                elif self.neighbour_mines == 3:
                    self.image = load_image("ms-3.png")
                elif self.neighbour_mines == 4:
                    self.image = load_image("ms-4.png")
                elif self.neighbour_mines == 5:
                    self.image = load_image("ms-5.png")
                elif self.neighbour_mines == 6:
                    self.image = load_image("ms-6.png")
                elif self.neighbour_mines == 7:
                    self.image = load_image("ms-7.png")
                elif self.neighbour_mines == 8:
                    self.image = load_image("ms-8.png")
            else:
                self.image = load_image("ms-mine.png")
    def mark_flagg(self):
        """ Merkitsee kyseisen ruudun lipulla, eli muuttaa flagged attribuutin arvoksi True.
        """
        self.flagged = True
        self.image = load_image("ms-flag.png")
    def mark_questionmark(self):
        """ Merkitsee kyseisen ruudun kysymysmerkiksi,
            eli muuttaa flagged attribuutin arvon arvoksi False ja
            questionmark attribuutin arvoksi True.
        """
        self.flagged = False
        self.questionmark = True
        self.image = load_image("ms-qm.png")
    def remove_markings(self):
        """ Poistaa kyseisestä ruudusta sekä lippu, että kysymysmerkki merkinnät.
            Se siis muuttaa sekä flagged, että questionmark attribuuttien arvot arvoksi False
        """
        self.flagged = False
        self.questionmark = False
        self.image = load_image("ms-unopened.png")
    def blow_up(self):
        """ Merkitsee erinäköisellä kuvalla miinan, jonka pelaaja on avaamalla räjäyttänyt.
            Se muttaa siis attribuutin image arvoa.
        """
        self.image = load_image("ms-red-mine.png")
