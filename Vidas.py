import pygame
from pygame.sprite import Sprite


class Vida (Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load('Vida.png')
        self.rect = self.image.get_rect()
