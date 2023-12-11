import pygame
from tetris import Tetris
from game_ui import GameUI
from clock import Clock


def event_handler(game_ui):
    '''Event handler'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Quit on Escape key
                return False
            #Move block left
            if event.key == pygame.K_LEFT:
                game_ui.tetris.move_left = True
            #Move block right
            if event.key == pygame.K_RIGHT:
                game_ui.tetris.move_right = True
            #Move block down
            if event.key == pygame.K_DOWN:
                game_ui.tetris.move_down = True
        if event.type == pygame.KEYUP:
            #Stop moving block left
            if event.key == pygame.K_LEFT:
                game_ui.tetris.move_left = False
            #Stop moving block right
            if event.key == pygame.K_RIGHT:
                game_ui.tetris.move_right = False
            #Stop moving block down
            if event.key == pygame.K_DOWN:
                game_ui.tetris.move_down = False
    return True

def run(game_ui, clock):
    '''Run game'''
    #Main loop
    running = True
    while running:
        running = event_handler(game_ui)

        if game_ui.tetris.move_left:
            game_ui.tetris.move_block_left()
        if game_ui.tetris.move_right:
            game_ui.tetris.move_block_right()
        if game_ui.tetris.move_down:
            game_ui.tetris.move_block_down()

        game_ui.tetris.spawn_block()
        game_ui.create_grid()
        game_ui.draw_block()
        pygame.display.update()
        clock.tick()

    pygame.quit()
