import pygame
import math
import random
import time

# Initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("space_invader/icon.png")
pygame.display.set_icon(icon)

# Load images
player_img = pygame.image.load("space_invader/spaceship.png")
bullet_img = pygame.image.load("space_invader/bullet.png")
enemy_imgs = [
    pygame.image.load("space_invader/ufo.png"),
    pygame.image.load("space_invader/ufo2.png"),
    pygame.image.load("space_invader/ufo3.png")
]
powerup_imgs = {
    "life": pygame.image.load("space_invader/powerup_life.png"),
    "rapid": pygame.image.load("space_invader/powerup_rapid.png")
}

# Fonts
score_font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 36)

# Player variables
player_x = 225
player_y = 430
player_speed = 4
player_x_change = 0
lives = 3
max_lives = 5
score = 0

# Bullet variables
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
is_fired = False
rapid_fire = False
rapid_fire_end = 0

# Enemy and powerup variables
enemies = []
powerups = []
POWERUP_TYPES = ["life", "rapid"]
powerup_timer = 0

# Level variables
level = 1
max_level = 5
in_level_screen = False
game_over = False
game_won = False

clock = pygame.time.Clock()


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def show_hud():
    draw_text(f"Score: {score}", score_font, (255, 255, 255), 10, 10)
    draw_text(f"Level: {level}", score_font, (255, 255, 255), 10, 30)
    draw_text(f"Lives: {lives}", score_font, (255, 255, 255), 400, 10)


def show_player(x, y):
    screen.blit(player_img, (x, y))


def fire_bullet(x, y):
    screen.blit(bullet_img, (x + 16, y))


def is_hit(ex, ey, bx, by):
    return math.hypot(ex - bx, ey - by) < 30


def check_collision(ex, ey, px, py):
    return math.hypot(ex - px, ey - py) < 40


def spawn_powerup():
    ptype = random.choice(POWERUP_TYPES)
    powerups.append({
        "type": ptype,
        "x": random.randint(20, 460),
        "y": 0,
        "speed": 2
    })


def draw_powerup(p):
    img = powerup_imgs[p["type"]]
    screen.blit(img, (p["x"], p["y"]))


def collect_powerup(p):
    global lives, rapid_fire, rapid_fire_end
    if p["type"] == "life" and lives < max_lives:
        lives += 1
    elif p["type"] == "rapid":
        rapid_fire = True
        rapid_fire_end = time.time() + 5  # 5 seconds rapid fire


def generate_enemies(level):
    enemies.clear()
    count = 4 + level * 2  # number of enemies grows per level
    speed_min = max(1, 1 + level // 2)  # speed grows slowly with level
    speed_max = speed_min + 2
    for _ in range(count):
        enemies.append({
            "img": random.choice(enemy_imgs),
            "x": random.randint(0, 440),
            "y": random.randint(20, 150),
            "x_change": random.choice([-1, 1]) * random.randint(speed_min, speed_max)
        })


# Initialize enemies for first level
generate_enemies(level)

while True:
    screen.fill("#290916")
    show_hud()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not in_level_screen and not game_over and not game_won:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -player_speed
                elif event.key == pygame.K_RIGHT:
                    player_x_change = player_speed
                elif event.key == pygame.K_SPACE:
                    if not is_fired or rapid_fire:
                        bullet_x = player_x
                        bullet_y = player_y
                        is_fired = True

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    player_x_change = 0

        elif in_level_screen:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                level += 1
                if level > max_level:
                    game_won = True
                else:
                    generate_enemies(level)
                    in_level_screen = False

        elif game_over or game_won:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Restart game after game over or win
                level = 1
                lives = 3
                score = 0
                rapid_fire = False
                is_fired = False
                player_x = 225
                generate_enemies(level)
                game_over = False
                game_won = False
                in_level_screen = False

    if game_over:
        draw_text("GAME OVER", big_font, (255, 50, 50), 140, 220)
        draw_text("Press ENTER to Restart", score_font, (255, 255, 255), 135, 270)
        pygame.display.update()
        clock.tick(60)
        continue

    if game_won:
        draw_text("YOU WIN!", big_font, (0, 255, 100), 160, 220)
        draw_text("Press ENTER to Restart", score_font, (255, 255, 255), 135, 270)
        pygame.display.update()
        clock.tick(60)
        continue

    if in_level_screen:
        # Show level complete screen
        draw_text(f"Level {level} Complete!", big_font, (0, 255, 255), 110, 200)
        draw_text("Press ENTER to Continue", score_font, (255, 255, 255), 140, 250)
        pygame.display.update()
        clock.tick(60)
        continue

    # Move player
    player_x += player_x_change
    player_x = max(0, min(player_x, 436))
    show_player(player_x, player_y)

    # Update bullet
    if is_fired:
        bullet_y -= bullet_speed
        fire_bullet(bullet_x, bullet_y)
        if bullet_y <= 0:
            is_fired = False

    # Disable rapid fire after duration
    if rapid_fire and time.time() > rapid_fire_end:
        rapid_fire = False

    # Move and draw enemies
    enemies_alive = 0
    for enemy in enemies:
        # Skip enemies that moved off screen (dead)
        if enemy["y"] < 0:
            continue

        enemies_alive += 1
        enemy["x"] += enemy["x_change"]

        # Bounce off screen edges
        if enemy["x"] <= 0:
            enemy["x_change"] = abs(enemy["x_change"])
            enemy["y"] += 20
        elif enemy["x"] >= 440:
            enemy["x_change"] = -abs(enemy["x_change"])
            enemy["y"] += 20

        # Collision with player - lose life and "kill" enemy
        if check_collision(enemy["x"], enemy["y"], player_x, player_y):
            lives -= 1
            enemy["y"] = -100  # Remove enemy from screen
            if lives <= 0:
                game_over = True

        # Bullet hits enemy
        if is_fired and is_hit(enemy["x"], enemy["y"], bullet_x, bullet_y):
            enemy["y"] = -100  # Remove enemy
            score += 1
            is_fired = False

        screen.blit(enemy["img"], (enemy["x"], enemy["y"]))

    # Spawn powerups periodically
    if pygame.time.get_ticks() - powerup_timer > 7000:
        spawn_powerup()
        powerup_timer = pygame.time.get_ticks()

    # Move and draw powerups
    for p in powerups[:]:
        p["y"] += p["speed"]
        draw_powerup(p)
        if check_collision(p["x"], p["y"], player_x, player_y):
            collect_powerup(p)
            powerups.remove(p)
        elif p["y"] > 500:
            powerups.remove(p)

    # Check if level cleared
    if enemies_alive == 0 and not in_level_screen:
        if level < max_level:
            in_level_screen = True
        else:
            game_won = True

    pygame.display.update()
    clock.tick(60)
