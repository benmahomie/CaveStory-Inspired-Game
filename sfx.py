import pygame
import os

pygame.mixer.init()

# Player Sounds
jump = pygame.mixer.Sound(os.path.join('sfx','Player','jump.wav'))
hurt = pygame.mixer.Sound(os.path.join('sfx','Player', 'hurt.wav'))
death = pygame.mixer.Sound(os.path.join('sfx','Player', 'die.wav'))

# Weapon Sounds
polar_star = pygame.mixer.Sound(os.path.join('sfx','Weapons','polar_star.wav'))
gun_click = pygame.mixer.Sound(os.path.join('sfx','Weapons','gun_click.wav'))

# NPC Sounds
enemy_hurt = pygame.mixer.Sound(os.path.join('sfx', 'NPCs', 'enemy_hurt.wav'))