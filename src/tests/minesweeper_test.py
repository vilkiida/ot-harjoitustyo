import unittest
from minesweeper import Main

easy=(9,9,10)
mediumhard=(16,16,40)
expert=(16,30,99)

class TestMinesweeper(unittest.TestCase):
    def test_game_height_right_when_easy(self):
        self.minesweeper = Main(easy)
        self.assertEqual(9, self.minesweeper.height)
    
    def test_game_width_right_when_easy(self):
        self.minesweeper = Main(easy)
        self.assertEqual(9, self.minesweeper.width)
    
    def test_game_mine_amount_right_when_easy(self):
        self.minesweeper = Main(easy)
        self.assertEqual(10,self.minesweeper.mine_amount)
    
    def test_game_height_right_when_mediumhard(self):
        self.minesweeper = Main(mediumhard)
        self.assertEqual(16, self.minesweeper.height)

    def test_game_width_right_when_easy(self):
        self.minesweeper = Main(mediumhard)
        self.assertEqual(16, self.minesweeper.width)
    
    def test_game_mine_amount_right_when_mediumhard(self):
        self.minesweeper = Main(mediumhard)
        self.assertEqual(40, self.minesweeper.mine_amount)
    
    def test_game_height_right_when_expert(self):
        self.minesweeper = Main(expert)
        self.assertEqual(16, self.minesweeper.height)
    
    def test_game_width_right_when_expert(self):
        self.minesweeper = Main(expert)
        self.assertEqual(30, self.minesweeper.width)
    
    def test_game_mine_amount_right_when_expert(self):
        self.minesweeper = Main(expert)
        self.assertEqual(99, self.minesweeper.mine_amount)