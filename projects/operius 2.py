from ursina import *
import random

app = Ursina()

# Spaceship made from multiple parts for better look
player = Entity()
player_body = Entity(parent=player, model='cube', color=color.azure, scale=(1, 0.5, 2))
player_nose = Entity(parent=player, model='cone', color=color.cyan, scale=(0.5, 1, 0.5), position=(0.5, 0, 0))
player_wing_left = Entity(parent=player, model='quad', color=color.blue, scale=(0.3, 1), position=(0, 0, 1), rotation_y=45)
player_wing_right = Entity(parent=player, model='quad', color=color.blue, scale=(0.3, 1), position=(0, 0, -1), rotation_y=-45)
player.position = (-5, 0, 0)

bullets = []
enemies = []

score = 0
health = 3

score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45), scale=2)
health_text = Text(text=f'Health: {health}', position=(0.65, 0.45), scale=2, color=color.red)

def spawn_enemy():
    enemy = Entity(model='cube', color=color.red, scale=(1, 0.5, 2),
                   position=(10, random.uniform(-3, 3), random.uniform(-3, 3)))
    enemies.append(enemy)

def enemy_spawner():
    spawn_enemy()
    invoke(enemy_spawner, delay=2)

enemy_spawner()

def update():
    global score, health

    # Animate spaceship nose up/down for simple breathing effect
    player_nose.y = 0.1 * (1 + sin(time.time() * 5))

    # Movement controls
    if held_keys['w']:
        player.y = min(player.y + 10 * time.dt, 4)
    if held_keys['s']:
        player.y = max(player.y - 10 * time.dt, -4)
    if held_keys['a']:
        player.z = min(player.z + 10 * time.dt, 4)
    if held_keys['d']:
        player.z = max(player.z - 10 * time.dt, -4)

    # Shooting
    if held_keys['space']:
        if len(bullets) < 5:
            bullet = Entity(model='sphere', color=color.yellow, scale=0.3, position=player.position + Vec3(1, 0, 0))
            bullets.append(bullet)

    # Move bullets
    for bullet in bullets[:]:
        bullet.x += 20 * time.dt
        if bullet.x > 15:
            bullets.remove(bullet)
            destroy(bullet)

    # Move enemies & collisions
    for enemy in enemies[:]:
        enemy.x -= 5 * time.dt
        if enemy.x < -10:
            enemies.remove(enemy)
            destroy(enemy)

        if enemy.intersects(player).hit:
            health -= 1
            health_text.text = f'Health: {health}'
            enemies.remove(enemy)
            destroy(enemy)
            if health <= 0:
                print(f'Game Over! Final score: {score}')
                Text(text='GAME OVER', origin=(0, 0), scale=5, color=color.red)
                application.pause()
                invoke(application.quit, delay=3)

        for bullet in bullets[:]:
            if bullet.intersects(enemy).hit:
                score += 1
                score_text.text = f'Score: {score}'
                bullets.remove(bullet)
                enemies.remove(enemy)
                destroy(bullet)
                destroy(enemy)
                break

app.run()
