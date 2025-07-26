import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Operius - No Internet Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SKY = (135, 206, 235)

# Clock for FPS control
clock = pygame.time.Clock()
FPS = 60

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))  # Blue block as player
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - 100
        self.vel_y = 0
        self.jump_power = -15
        self.gravity = 0.8
        self.is_jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.vel_y = self.jump_power
            self.is_jumping = True

        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Ground collision
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.is_jumping = False
            self.vel_y = 0

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = random.randint(20, 50)
        self.height = random.randint(40, 70)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(0, 300)
        self.rect.bottom = HEIGHT - 50
        self.speed = 7

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

# Function to display score
def display_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def main():
    player = Player()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    spawn_timer = 0
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(SKY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spawn obstacles periodically
        spawn_timer += 1
        if spawn_timer > 90:  # every 1.5 seconds approx
            obstacle = Obstacle()
            obstacles.add(obstacle)
            all_sprites.add(obstacle)
            spawn_timer = 0

        all_sprites.update()

        # Collision check
        if pygame.sprite.spritecollideany(player, obstacles):
            font = pygame.font.SysFont(None, 72)
            game_over_text = font.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 36))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
            continue

        all_sprites.draw(screen)

        # Update score
        score += 1
        display_score(score // 10)

        # Draw ground
        pygame.draw.rect(screen, (50, 205, 50), (0, HEIGHT - 50, WIDTH, 50))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
