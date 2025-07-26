import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets
player_img = pygame.image.load("streamlit_class/player.png")  # Replace with actual player image
obstacle_img = pygame.image.load("streamlit_class/obstacle.png")  # Replace with actual obstacle image
bg_img = pygame.image.load("streamlit_class/f823d341d35e050517a1f42e8d0712a5.jpg")  # Replace with actual background image
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))  # Ensure background fits the screen

# Player class
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.rect = self.image.get_rect(midbottom=(100, HEIGHT - 10))
        self.gravity = 0
    
    def jump(self):
        if self.rect.bottom >= HEIGHT - 10:
            self.gravity = -15
    
    def update(self):
        self.gravity += 0.8
        self.rect.y += self.gravity
        if self.rect.bottom >= HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self, x, speed):
        size = random.randint(30, 60)  # Random obstacle size
        self.image = pygame.transform.scale(obstacle_img, (size, size))
        self.rect = self.image.get_rect(midbottom=(x, HEIGHT - 10))
        self.speed = speed
    
    def update(self):
        self.rect.x -= self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Main function
def main():
    clock = pygame.time.Clock()
    running = True
    player = Player()
    obstacles = []
    spawn_timer = 0
    game_time = 0
    speed = 5
    score = 0
    bg_x1 = 0
    bg_x2 = WIDTH
    font = pygame.font.Font(None, 36)
    
    while running:
        screen.fill(WHITE)
        game_time += 1
        score = game_time // 10
        
        # Increase difficulty over time
        if game_time % 500 == 0:
            speed += 1
        
        # Move background
        bg_x1 -= 2
        bg_x2 -= 2
        if bg_x1 <= -WIDTH:
            bg_x1 = WIDTH
        if bg_x2 <= -WIDTH:
            bg_x2 = WIDTH
        screen.blit(bg_img, (bg_x1, 0))
        screen.blit(bg_img, (bg_x2, 0))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()
        
        # Spawn obstacles
        spawn_timer += 1
        if spawn_timer > max(100 - speed * 5, 30):
            spawn_timer = 0
            obstacles.append(Obstacle(WIDTH, speed))
        
        # Update objects
        player.update()
        for obs in obstacles[:]:
            obs.update()
            if obs.rect.right < 0:
                obstacles.remove(obs)
            if player.rect.colliderect(obs.rect):
                running = False  # End game on collision
        
        # Draw objects
        player.draw(screen)
        for obs in obstacles:
            obs.draw(screen)
        
        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(30)
    
    # Game over screen
    screen.fill(WHITE)
    game_over_text = font.render("Game Over! Press any key to exit.", True, BLACK)
    screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.flip()
    pygame.time.delay(2000)
    
    pygame.quit()

if __name__ == "__main__":
    main()
