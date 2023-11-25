import pygame

def game_over_screen(window):
    font = pygame.font.SysFont(None, 74)
    text = font.render('Game Over', True, (255, 0, 0))
    window.blit(text, (200, 200))
    restart_text = font.render('Press R to Restart', True, (255, 255, 255))
    quit_text = font.render('Press Q to Quit', True, (255, 255, 255))
    window.blit(restart_text, (200, 270))
    window.blit(quit_text, (200, 340))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit(0)
