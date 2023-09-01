import pygame 
import random
from variables import CELL_SIZE, WIDTH, HEIGHT
from variables import WHITE, GREEN, RED
from snake import Snake
from food import Food

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
CLOCK = pygame.time.Clock()

def draw():
    SCREEN.fill(WHITE)
    for segment in snake.body:
        pygame.draw.rect(SCREEN, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(SCREEN, RED, (food.position[0]*CELL_SIZE, food.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

def main():
    global snake, food
    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        snake.move()

        if snake.get_head_position() == food.position:
            snake.grow()
            food.reset_position()

        if snake.collides_with_itself():
            snake = Snake()

        draw()
        CLOCK.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()