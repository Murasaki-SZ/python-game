import pygame
class PlayerMovement: 
    player_speed = 5

    @classmethod
    def move_player(cls, player):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.y -= cls.player_speed
            return True, 1
        if keys[pygame.K_s]:
            player.y += cls.player_speed
            return True, 1
        if keys[pygame.K_a]:
            player.x -= cls.player_speed
            return True, 1
        if keys[pygame.K_d]:
            player.x += cls.player_speed
            return True, 1
        
        if keys[pygame.K_ESCAPE]:
            return False
        


        return True, 0