import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 600
WHITE = (255, 255, 255)
GROUND_COLOR = (150, 150, 150)
FPS = 60
BIRD_WIDTH, BIRD_HEIGHT = 50, 40
GRAVITY = 0.25
FLAP_SPEED = -6.5

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load assets
bird_image = pygame.image.load("bird.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))
pipe_image = pygame.image.load("pipe.png").convert_alpha()
ground_image = pygame.Surface((WIDTH, 100))
ground_image.fill(GROUND_COLOR)

# Bird class
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.gravity = GRAVITY
        self.bird_rect = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

    def move(self):
        self.vel_y += self.gravity
        self.y += self.vel_y

    def jump(self):
        self.vel_y = FLAP_SPEED

    def draw(self):
        win.blit(bird_image, (self.x, self.y))
        self.bird_rect = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.top = 0
        self.bottom = 0
        self.pipe_top = pygame.transform.flip(pipe_image, False, True)
        self.pipe_bottom = pipe_image
        self.PIPE_GAP = 150
        self.PIPE_SPEED = 3
        self.passed = False
        self.set_height()

    def set_height(self):
        self.top = random.randint(50, HEIGHT - 300)
        self.bottom = self.top + self.PIPE_GAP

    def move(self):
        self.x -= self.PIPE_SPEED

    def draw(self):
        win.blit(self.pipe_top, (self.x, self.top - self.pipe_top.get_height()))
        win.blit(self.pipe_bottom, (self.x, self.bottom))

    def collision(self, bird_rect):
        bird_mask = pygame.mask.from_surface(bird_image)
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)

        top_offset = (self.x - bird_rect.x, self.top - round(bird_rect.y))
        bottom_offset = (self.x - bird_rect.x, self.bottom - round(bird_rect.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point or t_point:
            return True
        return False

# Game variables
bird = Bird(50, HEIGHT // 2 - BIRD_HEIGHT // 2)
pipes = [Pipe(WIDTH)] 
clock = pygame.time.Clock()
score = 0
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump() 

    # Bird actions and movements
    bird.move()
    if bird.y > HEIGHT - 100 - BIRD_HEIGHT:
        running = False

    # Pipe movements and collisions
    for pipe in pipes:
        pipe.move()
        if pipe.x < -pipe.pipe_top.get_width():
            pipes.remove(pipe)
            pipes.append(Pipe(WIDTH))
            score += 1
        if pipe.collision(bird.bird_rect):
            running = False  # End the game if there's a collision with any pipe

    # Draw everything
    win.fill(WHITE) 
    for pipe in pipes:
        pipe.draw()
    win.blit(ground_image, (0, HEIGHT - 100))
    bird.draw()

    # Display score
    font = pygame.font.SysFont(None, 40)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
