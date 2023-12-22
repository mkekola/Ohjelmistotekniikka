class Block:
    '''Represents a block in the game of Tetris. A block is defined by its color and shape.'''
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

I_Block = Block((0, 255, 255), [[1, 1, 1, 1]])  # Cyan
O_Block = Block((255, 255, 0), [[1, 1], [1, 1]])  # Yellow
T_Block = Block((128, 0, 128), [[1, 1, 1], [0, 1, 0]])  # Purple
S_Block = Block((0, 255, 0), [[0, 1, 1], [1, 1, 0]])  # Green
Z_Block = Block((255, 0, 0), [[1, 1, 0], [0, 1, 1]])  # Red
J_Block = Block((0, 0, 255), [[1, 1, 1], [0, 0, 1]])  # Blue
L_Block = Block((255, 165, 0), [[1, 1, 1], [1, 0, 0]])  # Orange

Blocks = [I_Block, O_Block, T_Block, S_Block, Z_Block, J_Block, L_Block]