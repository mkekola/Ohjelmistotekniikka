'''Tetris game class'''
import random
from block import Blocks

class Tetris:
    '''Tetris game class'''
    def __init__(self, width=10, height=20, block_size=30):

        self.width = width
        self.height = height
        self.block_size = block_size
        self.grid = [[0] * width for _ in range(height)]

        self.current_block = None
        self.current_block_x = 0
        self.current_block_y = 0

        self.move_left = False
        self.move_right = False
        self.move_down = False

        self.current_block = None


    def spawn_block(self):
        '''Spawn block'''
        #Spawn random block top center
        shape_rand = random.randint(0, len(Blocks) - 1)
        self.current_block = Blocks[shape_rand]
        self.current_block_x = self.width // 2 - len(self.current_block.shape[0]) // 2
        self.current_block_y = 0

    def move_block_left(self):
        '''Move block left'''
        self.current_block_x -= 1
        if self.check_collision():
            self.current_block_x += 1

    def move_block_right(self):
        '''Move block right'''
        self.current_block_x += 1
        if self.check_collision():
            self.current_block_x -= 1

    def move_block_down(self):
        '''Move block down'''
        self.current_block_y += 1
        if self.check_collision():
            self.current_block_y -= 1
        else:
            self.lock_block()
            self.spawn_block()

    def check_collision(self):
        '''Check collision'''
        for y, row in enumerate(self.current_block.shape):
            for x, col in enumerate(row):
                if col == 1:
                    try:
                        if self.grid[self.current_block_y + y][self.current_block_x + x] == 1:
                            return True
                    except IndexError:
                        return True
        return False

    def lock_block(self):
        '''Lock block'''
        for y, row in enumerate(self.current_block.shape):
            for x, col in enumerate(row):
                if col == 1:
                    self.grid[self.current_block_y + y][self.current_block_x + x] = 1
