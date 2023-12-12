'''Clock'''
import pygame


class Clock:
    '''Clock class'''
    def __init__(self, fps=2):
        self.fps = fps
        self.clock = pygame.time.Clock()

    def tick(self):
        '''Tick'''
        self.clock.tick(self.fps)
