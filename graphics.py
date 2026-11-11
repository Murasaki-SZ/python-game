import pygame
class Sprites:

    @staticmethod
    def player_sprite(screen,mode,player):  
        center = player.center
        end = player.bottomright
        start = player.topleft
        topR = player.topright
        bottomL = player.bottomleft

        match(mode):
            case(0):
                pygame.draw.rect(screen, (180, 0, 200), player)
            case(1):
                pygame.draw.rect(screen, (220, 0, 230), player)
                pygame.draw.line(screen, (0, 0, 0), center, end, width=5)
                pygame.draw.line(screen, (0, 0, 0), center, start, width=5)
                pygame.draw.line(screen, (0, 0, 0), center, topR, width=5)
                pygame.draw.line(screen, (0, 0, 0), center, bottomL, width=5)


class Screen: 

    def __init__(self, width=600, height=400):
        self.screen_size = (width,height)
        self.surface = None

    def initialize_screen(self):
        self.surface = pygame.display.set_mode(self.screen_size)
        return self.surface

    def flip(self):
        pygame.display.flip()


    def basic_background(self, color=(0,0,0)):
        self.surface.fill(color)

    def scan_lines(self):
        for x in range(0, self.screen_size[0], 20):
            black = (0,0,0)
            pygame.draw.line(self.surface,black,(0,x),(self.screen_size[0],x),1)