import pygame

class Tetris:
    def __init__(self, width=10, height=20, block_size=30):

        self.width = width
        self.height = height
        self.block_size = block_size
        self.screen = pygame.display.set_mode((width * block_size, height * block_size))
        self.clock = pygame.time.Clock()

    def create_grid(self):

        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(self.screen, (0, 0, 0), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))

        # Draw vertical lines
        for x in range(0, (self.width + 1) * self.block_size, self.block_size):
            pygame.draw.line(self.screen, (105, 105, 105), (x, 0), (x, self.height * self.block_size))

        # Draw horizontal lines
        for y in range(0, (self.height + 1) * self.block_size, self.block_size):
            pygame.draw.line(self.screen, (105, 105, 105), (0, y), (self.width * self.block_size, y))


    pygame.display.set_caption("Tetris")
    pygame.init()
    
    def run(self):            
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.create_grid()  
            pygame.display.update()
            self.clock.tick(60)
            

        pygame.quit()

if __name__ == "__main__":
    tetris = Tetris()
    tetris.run()