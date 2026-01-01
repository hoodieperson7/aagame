import pygame
import game

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()

game.main(screen, clock)