import unittest
from level import Level

LEVEL_MAP= [[0,0,0,0,1,0,0,0],
            [0,1,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,1,0,0,1,0,0,0],
            [0,1,0,0,0,1,0,0],
            [0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0]]

CELL_SIZE = 50

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE)

        
