import pygame


def event_handler(game_ui):
    '''Method for handling user key presses.
    The user can move the block left, right and down using the arrow keys.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
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
    '''Mehod for running the game loop.
    The game loop is responsible for updating the game state and drawing the game board and the current block on the screen.'''
    #Main loop
    running = True
    game_ui.tetris.spawn_block()


    while running:
        running = event_handler(game_ui)

        if game_ui.tetris.move_left:
            game_ui.tetris.move_block_left()
        if game_ui.tetris.move_right:
            game_ui.tetris.move_block_right()
        game_ui.tetris.move_block_down()

        game_ui.create_grid()
        game_ui.draw_block()
        pygame.display.update()
        clock.tick()

    pygame.quit()
