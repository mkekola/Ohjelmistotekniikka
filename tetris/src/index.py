import sys
from tetris import Tetris
from game_ui import GameUI
from game_loop import run
from clock import Clock


sys.path.append('src')

if __name__ == "__main__":
    tetris = Tetris()
    game_ui = GameUI(tetris)
    clock = Clock()
    run(game_ui, clock)
