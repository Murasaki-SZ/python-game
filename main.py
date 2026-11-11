import pygame
import controls,graphics
pygame.init()

clock = pygame.time.Clock()
player = pygame.Rect(100,100,50,50)
speed = 5
running = True
sprite = graphics.Sprites
game_screen = graphics.Screen(600,400)
screen = game_screen.initialize_screen()
colored_background = (150,150,150)
scan_toggle = False
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
    running,moving = controls.PlayerMovement.move_player(player)

    game_screen.basic_background(colored_background)
    sprite.player_sprite(screen,moving,player)
    
    if keys[pygame.K_e]:
        scan_toggle = not scan_toggle
    if scan_toggle:
        game_screen.scan_lines()
    game_screen.flip()

    

pygame.quit()