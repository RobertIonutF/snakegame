import random
from variables import CELL_SIZE, WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))

    def reset_position(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1), random.randint(0, (HEIGHT // CELL_SIZE) - 1))