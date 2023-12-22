import unittest
from tetris import Tetris


class TestTetris(unittest.TestCase):
    def setUp(self):
        self.tetris = Tetris()

    def test_width(self):
        self.assertEqual(self.tetris.width, 10)

    def test_height(self):
        self.assertEqual(self.tetris.height, 20)

    def test_block_size(self):
        self.assertEqual(self.tetris.block_size, 30)

    def test_grid(self):
        self.assertEqual(self.tetris.grid, [[0] * 10 for _ in range(20)])


class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.tetris = Tetris()

    def test_current_block(self):
        self.assertEqual(self.tetris.current_block, None)

    def test_current_block_x(self):
        self.assertEqual(self.tetris.current_block_x, 0)

    def test_current_block_y(self):
        self.assertEqual(self.tetris.current_block_y, 0)

    def test_move_block_left(self):
        self.tetris.spawn_block()
        self.tetris.move_block_left()
        self.assertEqual(self.tetris.current_block_x, 3)

    def test_move_block_right(self):
        self.tetris.spawn_block()
        self.tetris.move_block_right()
        self.assertEqual(self.tetris.current_block_x, 5)

    def test_move_block_down(self):
        self.tetris.spawn_block()
        self.tetris.move_block_down()
        self.assertEqual(self.tetris.current_block_y, 1)

    def test_spawn_block(self):
        self.tetris.spawn_block()
        self.assertEqual(self.tetris.current_block_x, 4)
        self.assertEqual(self.tetris.current_block_y, 0)

    def test_check_collision(self):
        self.tetris.spawn_block()
        self.assertEqual(self.tetris.check_collision(), False)

