"""
Author: Eymen Küçükçakır
Date  : 11.01.2023

Notes : This snake game was mostly coded with the help of ChatGPT. 
        I forgot to document the things that I wrote to the AI but it started with this sentence;

        "Code me a completely playable and functional snake game using python"

        After that the AI gave me a very basic snake game and I modified it by asking the AI to
        change and add things to the code. Only at the end I had to modify some of the code 
        (mostly restart and pause parts).

        All of the comments are writen by the AI
"""

import pygame
import random
import sys

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

# Set up the font for rendering the score
font = pygame.font.Font(None, 36)

paused = False

def start_game():
    # Set up the initial score
    score = 0

    # Set up the initial score text
    score_text = font.render("", True, WHITE)

    # Set up the initial snake position and direction
    snake_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
    snake_dir = RIGHT

    # Set up the initial food position
    food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

    # Set up the snake's body
    snake_body = [snake_pos[:]]

    restart = False


    def score_screen(score):
        global restart
        screen.fill(BLACK)
        score_text = font.render(f"Your score was: {score}", True, WHITE)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2)
        screen.blit(score_text, score_text_rect)
        
        # Add retry button
        retry_text = font.render("Retry", True, WHITE)
        retry_text_rect = retry_text.get_rect()
        retry_text_rect.center = (GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2 + 50)
        screen.blit(retry_text, retry_text_rect)

        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r: # added key to retry game
                        return  # added return statement to restart game


    key_pressed = False
    score_text = font.render(f"Score: {score}", True, WHITE)

    # Set up the game loop
    running = True
    while running:
        if restart:
            restart = False
            score = 0
            snake_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
            snake_dir = RIGHT
            snake_body = [snake_pos[:]]
            food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not key_pressed:
                key_pressed = True
                if event.key == pygame.K_UP and snake_dir != DOWN:
                    snake_dir = UP
                elif event.key == pygame.K_DOWN and snake_dir != UP:
                    snake_dir = DOWN
                elif event.key == pygame.K_LEFT and snake_dir != RIGHT:
                    snake_dir = LEFT
                elif event.key == pygame.K_RIGHT and snake_dir != LEFT:
                    snake_dir = RIGHT
                elif event.key == pygame.K_SPACE:
                    print("PAUSE")
                    global paused
                    paused = not paused
                elif event.key == pygame.K_p:
                    print("PAUSE")
                    paused = not paused
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        key_pressed = False

        if paused:
            pause_text = font.render("Paused", True, WHITE)
            pause_text_rect = pause_text.get_rect()
            pause_text_rect.center = (GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2)
            screen.blit(pause_text, pause_text_rect)
            pygame.display.flip()
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and not key_pressed:
                        key_pressed = True
                        if event.key == pygame.K_SPACE: # I separated K_SPACE and K_p since for some reason they 
                            print("PAUSE")              # didn't work when I put them together with an 'or' operator. 
                            paused = not paused         # I have no idea why that is the case
                        elif event.key == pygame.K_p:
                            print("PAUSE")
                            paused = not paused
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        key_pressed = False

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
            score_screen(score)


        # Add the new position to the snake's body
        snake_body.append(snake_pos[:])

        # Check for collision with food
        if snake_pos == food_pos:

            # Generate a new food position
            while True:
                food_pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
                if food_pos not in snake_body:
                    break

            # Increment the score
            score += 1
            
            # Render the score text
            score_text = font.render(f"Score: {score}", True, WHITE)
        else:
            # Remove the snake's tail
            del snake_body[0]

        # Draw the screen
        screen.fill(BLACK)

        # Draw the snake
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE // 1.1, CELL_SIZE // 1.1))

        # Draw the food
        pygame.draw.rect(screen, WHITE, (food_pos[0] * CELL_SIZE, food_pos[1] * CELL_SIZE, CELL_SIZE // 1.1, CELL_SIZE // 1.1))

        # Blit the score text onto the screen
        screen.blit(score_text, (10, 10))  # (10, 10) is the top-left position of the text

        # Update the display
        pygame.display.update()

        # Delay to get the desired frame rate
        clock.tick(7)

        if restart:
            restart = False
            break
    

while True:
    start_game()

