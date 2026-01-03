import pygame
from player import Player
from level.level import Level
from .camera import Camera
from utils.keys import getkeys
from sys import exit

def main(screen, clock):
    player = Player(400, 300, screen)
    level = Level(0, screen)
    camera = Camera()
    dt = 1 / 60
    while True:
        screen.fill((173, 216, 230))
        
        keys = getkeys()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.VIDEORESIZE:
                screen_w, screen_h = screen.get_size()
                screen = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE)
                player.screen = screen

        player.update(keys, level, dt)
        # camera.update()
        player.draw(camera.x, camera.y)
        level.draw()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    import entry