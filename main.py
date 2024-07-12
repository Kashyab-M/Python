import pygame
import sys
from graphics import Graphics
from tetris import Tetris

class Game:
    def __init__(self):
        pygame.init()
        self.graphics = Graphics()
        self.tetris = Tetris()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.graphics.update_display(self.tetris.grid, self.tetris.tetromino)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.tetris.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.tetris.move_right()
                    elif event.key == pygame.K_DOWN:
                        self.tetris.move_down()
                    elif event.key == pygame.K_UP:
                        self.tetris.rotate()

            self.tetris.fall_time += self.clock.get_rawtime()
            self.clock.tick()

            if self.tetris.fall_time / 1000 > self.tetris.fall_speed:
                self.tetris.fall_time = 0
                self.tetris.move_down()

if __name__ == "__main__":
    Game().run()
