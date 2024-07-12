import pygame

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
COLUMNS = SCREEN_WIDTH // GRID_SIZE
ROWS = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Graphics:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")

    def draw_grid(self, grid):
        for y in range(ROWS):
            for x in range(COLUMNS):
                pygame.draw.rect(self.screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(self.screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def draw_tetromino(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, tetromino.color,
                                     ((tetromino.x + x) * GRID_SIZE, (tetromino.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    def update_display(self, grid, tetromino):
        self.screen.fill(BLACK)
        self.draw_grid(grid)
        self.draw_tetromino(tetromino)
        pygame.display.flip()
