'''Game UI'''
import pygame

class GameUI:
    '''Class for the game UI of Tetris game.
    The game UI is responsible for drawing the game board and the current block on the screen.'''
    def __init__(self, tetris):
        self.tetris = tetris
        pygame.display.set_caption("Tetris")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.tetris.width * self.tetris.block_size,
             self.tetris.height * self.tetris.block_size))


    def create_grid(self):
        '''Method for creating the grid on the screen for the game of Tetris and drawing visible lines'''
        for x in range(self.tetris.width):
            for y in range(self.tetris.height):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 0),
                    (x * self.tetris.block_size, y * self.tetris.block_size,
                        self.tetris.block_size, self.tetris.block_size)
                )

            # Draw vertical lines
            for x in range(0,
                           (self.tetris.width + 1) * self.tetris.block_size,
                           self.tetris.block_size):
                pygame.draw.line(self.screen, (105, 105, 105),
                                 (x, 0), (x, self.tetris.height * self.tetris.block_size))

            # Draw horizontal lines
            for y in range(0,
                           (self.tetris.height + 1) * self.tetris.block_size,
                           self.tetris.block_size):
                pygame.draw.line(self.screen, (105, 105, 105),
                                 (0, y), (self.tetris.width * self.tetris.block_size, y))

    def draw_block(self):
        '''Method for drawing the current block on the grid.
        The block is drawn by drawing a rectangle for each block in the block shape.'''
        #Draw current block
        for y, row in enumerate(self.tetris.current_block.shape):
            for x, col in enumerate(row):
                if col == 1:
                    pygame.draw.rect(
                        self.screen,
                        self.tetris.current_block.color,
                        ((self.tetris.current_block_x + x) * self.tetris.block_size,
                            (self.tetris.current_block_y + y) * self.tetris.block_size,
                             self.tetris.block_size, self.tetris.block_size)
                        )
