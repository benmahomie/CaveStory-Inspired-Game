import pygame
from entities import Player, Enemy
from game_logic import game_over_screen

def main():
    pygame.init()
    pygame.mixer.init()
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    running = True
    font = pygame.font.SysFont(None, 36)

    # Entities
    player = Player(100, 300, 48, 64)
    red_square1 = Enemy(300, 500, 64, 64, color=(255, 0, 0), hp=30)
    red_square2 = Enemy(100, 500, 64, 64, color=(128, 0, 0), hp=50)
    enemies = [red_square1, red_square2]

    gravity = 0.7

    platforms = [(0, 550, 800, 50), (200, 450, 200, 20), (600, 350, 200, 20)]

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    player.jump_allowed = True
                if event.key == pygame.K_x:
                    player.shoot_key_up = True
                if event.key == pygame.K_DOWN:
                    player.squatting = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= player.speed
            player.last_direction = "left"
        if keys[pygame.K_RIGHT]:
            player.x += player.speed
            player.last_direction = "right"
        if keys[pygame.K_DOWN]:
            player.squatting = True
            player.squat()
        if keys[pygame.K_z]:
            player.jump()
        if keys[pygame.K_x]:
            player.shoot()

        # Step 1: Update player's position based on current velocity
        player.y += player.velocity
        
        # Step 2: Check for platform collisions and adjust accordingly
        player.check_on_platform(platforms)

        # Step 3: Apply gravity if not on a platform
        if not player.on_platform:
            player.velocity += gravity

        # Window edge collisions for Player
        player.x = max(0, min(800 - player.width, player.x))

        # Drawing platforms
        window.fill((0, 0, 0))
        for plat_x, plat_y, plat_w, plat_h in platforms:
            pygame.draw.rect(window, (0, 255, 0), (plat_x, plat_y, plat_w, plat_h))  

        # Draw entities
        player.draw(window)

        for enemy in enemies:
            if enemy.hp <= 0:
                enemy.is_dead = True

        # Collision logic
        for enemy in enemies:
            if enemy.is_dead:
                if enemy.explosion_radius < 50:  # Set the limit for the explosion size
                    enemy.death_animation(window)
                else:
                    enemies.remove(enemy)  # Remove the enemy after reaching maximum explosion size
            else:
                if player.check_collision([enemy]):
                    player.take_damage(enemy.damage)
                enemy.draw(window)
                enemy.move()
                enemy.update()

        player.update()
        
        # Move bullets and check for collision with enemies
        player.move_bullets(window, enemies)  

        # Remove dead enemies and play any necessary animations or sounds
        enemies = [enemy for enemy in enemies if not enemy.is_dead]

        if player.hp <= 0:
            player.death()
            running = False

        # Draw the health bar background (grey bar)
        pygame.draw.rect(window, (128, 128, 128), (10, 10, player.full_hp, 20))

        # Draw the health bar (green bar)
        pygame.draw.rect(window, (0, 255, 0), (10, 10, player.hp, 20))

        # Draw the HP text
        hp_text = font.render(f"HP: {player.hp}/{player.full_hp}", True, (255, 255, 255))
        window.blit(hp_text, (115, 10))

        pygame.display.update()

    if game_over_screen(window):
        main()

if __name__ == "__main__":
    main()