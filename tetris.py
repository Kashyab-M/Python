import random
import pygame

# Screen dimensions
GRID_SIZE = 30
COLUMNS = 300 // GRID_SIZE
ROWS = 600 // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1, 1]],          # I
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]]         # O
]

# Tetromino colors corresponding to shapes
SHAPE_COLORS = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, WHITE]

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(SHAPE_COLORS)
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.tetromino = self.new_tetromino()
        self.next_tetromino = self.new_tetromino()
        self.score = 0
        self.fall_time = 0
        self.fall_speed = 0.5

    def new_tetromino(self):
        return Tetromino(random.choice(SHAPES))

    def is_valid_position(self, offset_x=0, offset_y=0):
        for y, row in enumerate(self.tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.tetromino.x + x + offset_x
                    new_y = self.tetromino.y + y + offset_y
                    if new_x < 0 or new_x >= COLUMNS or new_y < 0 or new_y >= ROWS or self.grid[new_y][new_x] != BLACK:
                        return False
        return True

    def freeze_tetromino(self):
        for y, row in enumerate(self.tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.tetromino.y + y][self.tetromino.x + x] = self.tetromino.color

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        lines_cleared = ROWS - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [BLACK for _ in range(COLUMNS)])
        self.grid = new_grid
        self.score += lines_cleared * 10

    def move_left(self):
        if self.is_valid_position(-1, 0):
            self.tetromino.x -= 1

    def move_right(self):
        if self.is_valid_position(1, 0):
            self.tetromino.x += 1

    def rotate(self):
        self.tetromino.rotate()
        if not self.is_valid_position():
            self.tetromino.rotate()
            self.tetromino.rotate()
            self.tetromino.rotate()

    def move_down(self):
        if self.is_valid_position(0, 1):
            self.tetromino.y += 1
        else:
            self.freeze_tetromino()
            self.clear_lines()
            self.tetromino = self.next_tetromino
            self.next_tetromino = self.new_tetromino()
            if not self.is_valid_position():
                pygame.quit()
                sys.exit()
