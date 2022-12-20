import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Pong")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the dimensions of the game objects
paddle_width = 15
paddle_height = 60
paddle_offset = 0  # Add an offset to the paddle position
ball_size = 15

# Set the initial position of the ball
ball_pos = [300, 200]

# Set the initial speed of the ball
ball_speed = [4, 2]

# Set the initial position of the paddles
left_paddle_pos = [10 + paddle_offset, (400 - paddle_height) // 2]
right_paddle_pos = [575, (400 - paddle_height) // 2]

# Set the initial score
score = [0, 0]

# Set the font for displaying the score
font = pygame.font.Font(None, 36)

# Set the game speed in frames per second
fps = 60

# Set the clock to control the game speed
clock = pygame.time.Clock()

# Set the game to run
running = True

# Set up variables to track the state of the keys
w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w_pressed = True
            elif event.key == pygame.K_s:
                s_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w_pressed = False
            elif event.key == pygame.K_s:
                s_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    # Update the paddle positions based on the state of the keys
    if w_pressed:
        left_paddle_pos[1] -= 5
    if s_pressed:
        left_paddle_pos[1] += 5
    if up_pressed:
        right_paddle_pos[1] -= 5
    if down_pressed:
        right_paddle_pos[1] += 5
    # Update the ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check for ball collision with top and bottom walls
    if ball_pos[1] < 0 or ball_pos[1] > 400 - ball_size:
        ball_speed[1] *= -1

    # Check for ball collision with paddles
    if ball_pos[0] < paddle_width + paddle_offset and left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + paddle_height:
        ball_speed[0] *= -1
    elif ball_pos[0] > 600 - paddle_width - ball_size and right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + paddle_height:
        ball_speed[0] *= -1

    # Check for ball going off the left or right side of the screen
    if ball_pos[0] < 0:
        score[1] += 1
        ball_pos = [300, 200]
        ball_speed = [4, 2]
    elif ball_pos[0] > 600:
        score[0] += 1
        ball_pos = [300, 200]
        ball_speed = [-4, 2]

    # Clear the screen
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, white, ball_pos, ball_size)
    # Draw the paddles
    pygame.draw.rect(screen, white, (left_paddle_pos[0] + paddle_offset, left_paddle_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (right_paddle_pos[0], right_paddle_pos[1], paddle_width, paddle_height))
    # Draw the score
    score_text = font.render(str(score[0]) + "-" + str(score[1]), True, white)
    screen.blit(score_text, (250, 10))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
