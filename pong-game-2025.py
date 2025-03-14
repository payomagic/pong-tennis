import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG Tennis 2025")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Ball properties
BALL_SIZE = 20
ball_speed_x = 7
ball_speed_y = 7

# Create paddles and ball (using pygame.Rect)
left_paddle = pygame.Rect(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 10 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Initialize scores
score_left = 0
score_right = 0

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key handling for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom of the screen
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Check for scoring (ball goes out of bounds)
    if ball.left <= 0:
        score_right += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1  # change direction after scoring
    if ball.right >= WIDTH:
        score_left += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1  # change direction after scoring

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display the scores
    font = pygame.font.Font(None, 74)
    text_left = font.render(str(score_left), True, WHITE)
    text_right = font.render(str(score_right), True, WHITE)
    screen.blit(text_left, (WIDTH // 4, 10))
    screen.blit(text_right, (WIDTH * 3 // 4, 10))

    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(60)