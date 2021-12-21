import pygame
from pygame.locals import *
from components.Player import Player
from components.PlayerController import PlayerController
# Initialize the pygame:
pygame.init()

# Create the game screen:
screen = pygame.display.set_mode([800, 600])
p = Player()
pc = PlayerController(player=p)

if __name__ == "__main__":
    running = True
    while running:

        # Did the user click the window close button?

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        p.update()
        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        p.position.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 2
        p.position.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 2
        print(p.position.x, p.position.y)
        # Draw a solid blue circle in the center

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display

        pygame.display.flip()



