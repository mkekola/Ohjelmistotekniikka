'''Tetris game class'''
import random
from block import Blocks

class Tetris:
    '''Class for the game of Tetris.
    The game board is represented by a grid of 0s and 1s. 0 represents an empty space and 1 represents a block.
    The blocks are represented by a list of lists of 0s and 1s. 0 represents an empty space and 1 represents a block.'''
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

    def spawn_block(self):
        '''Method for spawning a new block.
        The block is spawned at the top center of the game board.
        The block is chosen randomly from the list of blocks.'''
        #Spawn random block top center
        shape_rand = random.randint(0, len(Blocks) - 1)
        self.current_block = Blocks[shape_rand]
        self.current_block_x = self.width // 2 - len(self.current_block.shape[0]) // 2
        self.current_block_y = 0

    def move_block_left(self):
        '''Mehod for moving block left.
        The block can only be moved left if there is no collision with another block or the left edge of the game board.'''
        if self.current_block_x > 0 and not self.check_collision():
            self.current_block_x -= 1

    def move_block_right(self):
        '''Method for moving block right.
        The block can only be moved right if there is no collision with another block or the right edge of the game board.'''
        if self.current_block_x < self.width - len(self.current_block.shape[0]) and not self.check_collision():
            self.current_block_x += 1

    def move_block_down(self):
        '''Method for moving block down.
        The block can only be moved down if there is no collision with another block or the bottom edge of the game board.'''
        if not self.check_collision():
            self.current_block_y += 1
        else:
            self.lock_block()
            self.spawn_block()


#tämä koodi on generoitu ChatGBT:llä
    def check_collision(self):
        '''Method for checking collision.
        The block can only be moved if there is no collision with another block or the bottom edge of the game board.'''
        for y, row in enumerate(self.current_block.shape):
            for x, col in enumerate(row):
                if col == 1:
                    if (
                        self.current_block_y + y >= self.height
                        or self.grid[self.current_block_y + y][self.current_block_x + x] == 1
                    ):
                        return True

        # Check collision with blocks at the bottom
        for x in range(len(self.current_block.shape[0])):
            if (
                self.current_block_x + x < self.width
                and self.grid[self.current_block_y + len(self.current_block.shape)]
                [self.current_block_x + x] == 1
            ):
                return True

        return False
#genroitu koodi päättyy

    def lock_block(self):
        '''Methdo for locking the block in place when it collides with another block or the bottom edge of the game board.
        The block is locked in place by changing the 0s in the grid to 1s.'''
        for y, row in enumerate(self.current_block.shape):
            for x, col in enumerate(row):
                if col == 1:
                    self.grid[self.current_block_y + y][self.current_block_x + x] = 1
