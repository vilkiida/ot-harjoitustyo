""" Moduuli, joka sisältää luokan Highscores
"""
import sqlite3

class Highscores:
    """ Luokka, joka vastaa highscores tietokannan käsittelystä
    Attributes:
        database: luo yhteyden tietokantaann.
    """
    def __init__(self):
        """ Luokan konstructori
        """
        self.database = sqlite3.connect("highscores.db")
        self.database.isolation_level = None

    def create_table(self):
        """ Luo tietokantaan taulun highscores
        """
        sql = "CREATE TABLE highscores (id INTEGER PRIMARY KEY, date TIMESTAMP, time INTEGER, difficulty TEXT)"
        self.database.execute(sql)

    def new_score(self, date, time, difficulty):
        """ Lisää tietokannan highscores tauluun parametrien mukaisen uuden
            tuloksen
        Args:
            date: Aikaleima, joka kuvaa milloin suoritus on tehty
            time: Lukuarvo, joka kuvaa suoritusaikaa sekunteina
            difficulty: Merkkijonoarvo, joka kuvaa vaikestasoa nimeltä.
        """
        try:
            sql="INSERT INTO highscores (date, time, difficulty) VALUES (?, ?, ?)"
            self.database.execute(sql, [date, time, difficulty])
        except:
            print("Unable to add to highscores")
    
    def get_high_scores(self, difficulty):
        """ Palauttaa listassa tiedot parhaimmasta 5 suorituksesta parhausjärjestyksessä
            parametrina annetussa vaikeustasossa.
        Args:
            difficulty: Merkkijonoarvo, joka kuvaa vaikeustasoa nimeltä.
        """
        try:
            sql = "SELECT date, time FROM highscores WHERE difficulty = ? ORDER BY time, date LIMIT 5"
            highscores = self.database.execute(sql, [difficulty]).fetchall()
        except:
            return None
        return highscores
    def drop_table(self):
        """ Poistaa taulun highscores tietokannasta, jos sellainen on.
        """
        try:
            sql = "DROP TABLE if exists highscores"
            self.database.execute(sql)
        except:
            print("Unable to drop table")
    def erase_scores(self, difficulty):
        """ Poistaa tietyn parametrinä annetun vaikeustason tuloksen tietokannasta
        Args:
            difficulty: Merkkijonoarvo, joka kuvaa vaikeustasoa nimeltä.
        """
        try:
            sql = "DELETE FROM highscores WHERE difficulty = ?"
            self.database.execute(sql, [difficulty])
        except:
            print(f"Unable to delete all from {self.difficulty} scores")
