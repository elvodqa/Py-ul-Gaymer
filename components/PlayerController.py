import pygame

from components.Component import Component
from components.Player import Player

class PlayerController(Component):
    def __init__(self, player: Player):
        super(PlayerController, self).__init__(player)

    def update(self, event):
        keys = pygame.key.get_pressed()
        self.player.position.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 2
        self.player.position.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 2
        print(self.player.position.x, self.player.position.y)