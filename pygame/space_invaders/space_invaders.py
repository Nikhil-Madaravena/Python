import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SHIP_WIDTH, SHIP_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 50
BULLET_WIDTH, BULLET_HEIGHT = 5, 15
ENEMY_ROWS = 4
ENEMY_COLS = 8
ENEMY_SPEED = 3
SHIP_SPEED = 7
BULLET_SPEED = 10
ENEMY_SHOOT_FREQ = 50
SCORE_FONT_SIZE = 24

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

# Load images
ship_img = pygame.image.load('ship.png')  
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
enemy_img = pygame.image.load('enemies.webp')  
enemy_img = pygame.transform.scale(enemy_img, (ENEMY_WIDTH, ENEMY_HEIGHT))

# Fonts
font = pygame.font.Font(None, SCORE_FONT_SIZE)

# Ship properties
ship_x = WIDTH // 2 - SHIP_WIDTH // 2
ship_y = HEIGHT - SHIP_HEIGHT - 20

# Bullet properties
bullets = []
enemy_bullets = []
enemy_shoot_counter = 0

# Enemy properties
enemies = []
for row in range(ENEMY_ROWS):
    for col in range(ENEMY_COLS):
        enemy_x = col * (ENEMY_WIDTH + 10)
        enemy_y = row * (ENEMY_HEIGHT + 10)
        enemies.append(pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT))

# Game over and score variables
game_over = False
score = 0
enemies_killed = 0  # Track the number of enemies killed

# Function to draw everything
def draw():
    screen.fill(BLACK)
    screen.blit(ship_img, (ship_x, ship_y))
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet)
    for bullet in enemy_bullets:
        pygame.draw.rect(screen, RED, bullet)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Function to create new enemies
def create_new_enemies():
    enemies.clear()  # Clear existing enemies
    for row in range(ENEMY_ROWS):
        for col in range(ENEMY_COLS):
            enemy_x = col * (ENEMY_WIDTH + 10)
            enemy_y = row * (ENEMY_HEIGHT + 10)
            enemies.append(pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT))

# Main game loop
FPS = 60  # Frames per second
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)  # Set the frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship_x > 0:
            ship_x -= SHIP_SPEED
        if keys[pygame.K_RIGHT] and ship_x < WIDTH - SHIP_WIDTH:
            ship_x += SHIP_SPEED
        if keys[pygame.K_SPACE]:
            bullet_x = ship_x + SHIP_WIDTH // 2 - BULLET_WIDTH // 2
            bullet_y = ship_y
            bullets.append(pygame.Rect(bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT))

        # Enemy movement and shooting
        enemy_shoot_counter += 1
        if enemy_shoot_counter >= ENEMY_SHOOT_FREQ:
            enemy_shoot_counter = 0
            random_enemy = random.choice(enemies)
            enemy_bullet_x = random_enemy.x + ENEMY_WIDTH // 2 - BULLET_WIDTH // 2
            enemy_bullet_y = random_enemy.y + ENEMY_HEIGHT
            enemy_bullets.append(pygame.Rect(enemy_bullet_x, enemy_bullet_y, BULLET_WIDTH, BULLET_HEIGHT))

        for enemy in enemies:
            enemy.x += ENEMY_SPEED
            if enemy.x <= 0 or enemy.x >= WIDTH - ENEMY_WIDTH:
                ENEMY_SPEED *= -1
                for e in enemies:
                    e.y += 10
                break

        # Update bullets
        for bullet in bullets:
            bullet.y -= BULLET_SPEED
        for bullet in enemy_bullets:
            bullet.y += BULLET_SPEED

        # Remove bullets when they go off-screen
        bullets = [bullet for bullet in bullets if bullet.y > 0]
        enemy_bullets = [bullet for bullet in enemy_bullets if bullet.y < HEIGHT]

        # Check collision between player bullets and enemies
        for bullet in bullets:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    enemies_killed += 1  # Increment the killed count

        # Check collision between enemy bullets and player
        for bullet in enemy_bullets:
            if bullet.colliderect(pygame.Rect(ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT)):
                game_over = True

        # Check if it's time to create new enemies
        if enemies_killed > 0 and enemies_killed % 20 == 0:
            create_new_enemies()

    draw()
    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Display for 2 seconds before quitting
        pygame.quit()
