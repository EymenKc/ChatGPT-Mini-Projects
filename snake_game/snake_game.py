import pygame
import random

# Constants
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Snake")

# Set up the clock
clock = pygame.time.Clock()

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up the initial snake position and direction
snake_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
snake_dir = RIGHT

# Set up the initial food position
food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

# Set up the snake's body
snake_body = [snake_pos[:]]

# Set up the game loop
running = True
while running:
 # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != DOWN:
                snake_dir = UP
            elif event.key == pygame.K_DOWN and snake_dir != UP:
                snake_dir = DOWN
            elif event.key == pygame.K_LEFT and snake_dir != RIGHT:
                snake_dir = LEFT
            elif event.key == pygame.K_RIGHT and snake_dir != LEFT:
                snake_dir = RIGHT
    # Update the snake position
    snake_pos[0] += snake_dir[0]
    snake_pos[1] += snake_dir[1]

    # Check for collision with walls
    if snake_pos[0] < 0:
        snake_pos[0] = GRID_WIDTH - 1
    elif snake_pos[0] >= GRID_WIDTH:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = GRID_HEIGHT - 1
    elif snake_pos[1] >= GRID_HEIGHT:
        snake_pos[1] = 0


    # Check for collision with snake's body
    if snake_pos in snake_body:
        running = False

    # Add the new position to the snake's body
    snake_body.append(snake_pos[:])

    # Check for collision with food
    if snake_pos == food_pos:
        # Generate a new food position
        food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
    else:
        # Remove the snake's tail
        del snake_body[0]

    # Draw the screen
    screen.fill(BLACK)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the food
    pygame.draw.rect(screen, WHITE, (food_pos[0] * CELL_SIZE, food_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.update()

    # Delay to get the desired frame rate
    clock.tick(10)

# Quit pygame
pygame.quit()