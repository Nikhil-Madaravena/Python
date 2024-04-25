import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PADDLE_SPEED = 10
MAX_BALL_SPEED = 12
BALL_ACCELERATION = 0.1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Paddle properties
paddle_width, paddle_height = 10, 100
player_paddle = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_speed = PADDLE_SPEED
paddle_color = (0, 0, 255)

# Ball properties
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
ball_color = (255, 165, 0)

# Score variables
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font(None, 48)

# Initialize particles list
particles = []

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += paddle_speed

    # AI opponent movement
    if opponent_paddle.centery < ball.y:
        opponent_paddle.y += paddle_speed
    elif opponent_paddle.centery > ball.y:
        opponent_paddle.y -= paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        opponent_score += 1
        ball_speed_x *= -1
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
    if ball.right >= WIDTH:
        player_score += 1
        ball_speed_x *= -1
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

    # Ball collision with paddles and particle effects
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1
        # Create particles at ball's position
        for _ in range(20):  # Create 20 particles
            particles.append([ball.x, ball.y])

    # Update and draw particles
    for particle in particles:
        pygame.draw.circle(screen, ball_color, (particle[0], particle[1]), 3)
        # Optional: Implement particle motion and fading effects here

    # Optional: Remove old particles
    # particles = [particle for particle in particles if not faded_out(particle)]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, paddle_color, player_paddle)
    pygame.draw.rect(screen, paddle_color, opponent_paddle)
    pygame.draw.ellipse(screen, ball_color, ball)

    # Show scores
    player_text = basic_font.render(f"{player_score}", True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 50))

    opponent_text = basic_font.render(f"{opponent_score}", True, WHITE)
    screen.blit(opponent_text, ((WIDTH // 4) * 3 - opponent_text.get_width(), 50))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()