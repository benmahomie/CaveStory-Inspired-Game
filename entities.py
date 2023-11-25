import pygame
from sfx import *

class Entity:
    def __init__(self, x, y, width, height, speed, color, hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.color_og = color
        self.hp = hp
        self.full_hp = hp
        self.flash_timer = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        pass

    def flash(self, color=(255, 255, 255), frames=5):
        self.color = color # Color to flash
        self.flash_timer = frames # Frames to keep flashing

    def update(self):
        if self.flash_timer > 0:
            self.flash_timer -= 1
            if self.flash_timer == 0:
                self.color = self.color_og

class Player(Entity):
    def __init__(self, x, y, width, height, speed = 5, color = (0, 128, 255)):
        super().__init__(x, y, width, height, speed, color, 50)
        self.last_direction = 'right'  # Default direction
        self.squatting = False
        self.squat_height = self.height / 2
        self.invincible_timer = 0
        self.velocity = 0
        self.jump_allowed = True
        self.weapon_inventory = []
        self.inventory = []
        self.bullets = []
        self.shoot_cooldown = 0
        self.can_shoot = True
        self.shoot_key_up = True

    def take_damage(self, damage):
        if self.invincible_timer == 0:
            hurt.play()
            self.hp -= damage
            self.flash()
            self.invincible_timer = 90  # 90 frames (1.5 seconds) of invincibility

    def death(self):
        death.play()
    
    def update(self):
        # Update damage flash
        if self.flash_timer > 0:
            self.flash_timer -= 1
            if self.flash_timer == 0:
                self.color = self.color_og

        # Update invincibility frames flash
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

        # Update shoot cooldown (gives space between button presses)
        if self.shoot_cooldown > 0:
            self.can_shoot = False
            self.shoot_cooldown -= 1
        if self.shoot_cooldown == 0:
            self.can_shoot = True

        if self.squatting: # If player is squatting, update height
            self.height = self.squat_height

    def check_collision(self, enemies):
        for enemy in enemies:
            if (
                (enemy.x < self.x < enemy.x + enemy.width or enemy.x < self.x + self.width < enemy.x + enemy.width) and
                (enemy.y < self.y < enemy.y + enemy.height or enemy.y < self.y + self.height < enemy.y + enemy.height)
            ):
                return True
        return False
    
    def jump(self):
        if self.on_platform and self.jump_allowed:
            jump.play()
            self.velocity = -15
            self.jump_allowed = False
    
    def shoot(self):
        speed = 10

        if self.can_shoot and self.shoot_key_up:
            if self.last_direction == 'right':
                bullet = Bullet(self.x + self.width // 2, self.y + self.height // 2, speed = speed)
            else:
                bullet = Bullet(self.x + self.width // 2, self.y + self.height // 2, speed = -speed)

            polar_star.play()

            self.bullets.append(bullet) # Add bullet to present bullets list
            self.shoot_key_up = False # Show that shoot key is being held down
            self.shoot_cooldown = 5 # Set cooldown
        elif self.can_shoot == False and self.shoot_key_up:
            print("Gun click")
            gun_click.play()
        else:
            pass

    def move_bullets(self, window, enemies):
        bullets_to_remove = [] 
        for bullet in self.bullets:  # Create a copy of the list to safely remove items
            bullet.move()
            bullet.draw(window)

            for enemy in enemies:  # Loop through enemies list
                if bullet.check_collision([enemy]):
                    enemy.take_damage(bullet.damage)
                    bullets_to_remove.append(bullet)
                    break  # Exit loop if collision is detected

            if bullet.out_of_range():
                bullets_to_remove.append(bullet)
        
        for bullet in bullets_to_remove:
            if bullet in self.bullets:  # Check if bullet still in list
                self.bullets.remove(bullet)

    def check_on_platform(self, platforms):
        self.on_platform = False  # Reset before checking
        for plat_x, plat_y, plat_w, plat_h in platforms:
            if (self.y + self.height >= plat_y >= self.y) and (self.x + self.width > plat_x) and (self.x < plat_x + plat_w):
                if self.velocity >= 0:
                    self.on_platform = True
                    self.y = plat_y - self.height
                    self.velocity = 0
                    break

class Enemy(Entity):
    def __init__(self, x, y, width, height, color = (255, 0, 0), speed = 2, hp = 100, damage = 10):
        super().__init__(x, y, width, height, speed, color, hp)
        self.damage = damage
        self.is_dead = False
        self.explosion_radius = 0
        
    def move(self):
        self.x += self.speed
        if self.x >= 800 - self.width or self.x <= 0:
            self.speed = -self.speed

    def take_damage(self, damage):
        enemy_hurt.play()
        self.hp -= damage  # Decrease enemy hp
        self.flash()  # Make enemy flash

    def death_animation(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x + self.width // 2, self.y + self.height // 2), self.explosion_radius)
        self.explosion_radius += 1

class Bullet:
    def __init__(self, x, y, speed=10, bullet_range=200, damage=10):
        self.x = x
        self.y = y
        self.start_x = x
        self.speed = speed
        self.radius = 5 
        self.range = bullet_range
        self.damage = damage

    def move(self):
        self.x += self.speed

    def draw(self, window):
        pygame.draw.circle(window, (0, 255, 0), (self.x, self.y), self.radius)

    def check_collision(self, enemies):
        for enemy in enemies:
            if enemy.x < self.x < enemy.x + enemy.width and enemy.y < self.y < enemy.y + enemy.height:
                return True
        return False
    
    def out_of_range(self):
        return abs(self.start_x - self.x) > self.range