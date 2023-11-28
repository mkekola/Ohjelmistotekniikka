import random
import pygame



class Block:
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

class Tetris:
    def __init__(self, width=10, height=20, block_size=30):

        self.width = width
        self.height = height
        self.block_size = block_size
        self.screen = pygame.display.set_mode(
            (width * block_size, height * block_size))
        self.grid = [[0] * width for _ in range(height)]
        self.clock = pygame.time.Clock()

        self.current_block = None
        self.current_block_x = 0
        self.current_block_y = 0

    def create_grid(self):

        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 0),
                    (x * self.block_size, y * self.block_size,
                     self.block_size, self.block_size)
                )

        # Draw vertical lines
        for x in range(0, (self.width + 1) * self.block_size, self.block_size):
            pygame.draw.line(self.screen, (105, 105, 105),
                             (x, 0), (x, self.height * self.block_size))

        # Draw horizontal lines
        for y in range(0, (self.height + 1) * self.block_size, self.block_size):
            pygame.draw.line(self.screen, (105, 105, 105),
                             (0, y), (self.width * self.block_size, y))

    def draw_block(self):
        for y, row in enumerate(self.current_block.shape):
            for x, col in enumerate(row):
                if col == 1:
                    pygame.draw.rect(
                        self.screen,
                        self.current_block.color,
                        ((self.current_block_x + x) * self.block_size,
                         (self.current_block_y + y) * self.block_size,
                         self.block_size, self.block_size)
                    )

    def spawn_block(self):
        shape_rand = random.randint(0, len(Blocks) - 1)
        self.current_block = Blocks[shape_rand]
        self.current_block_x = self.width // 2 - len(self.current_block.shape[0]) // 2
        self.current_block_y = 0

    pygame.display.set_caption("Tetris")
    pygame.init()

    def run(self):
        running = True
        self.spawn_block()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.create_grid()
            self.draw_block()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.run()
