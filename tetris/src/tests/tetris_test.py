import unittest
from index import Tetris

class TestTetris(unittest.TestCase):
    def setUp(self):
        self.tetris = Tetris()

    def test_width(self):
        self.assertEqual(self.tetris.width, 10)

    def test_height(self):
        self.assertEqual(self.tetris.height, 20)
    
    def test_block_size(self):  
        self.assertEqual(self.tetris.block_size, 30)
    
    def test_create_grid(self):        
        self.assertEqual(self.tetris.create_grid(), None)

