# create an enviorment for a character to move in
# initial build

# On hold for now, will experiment with Godot

import pygame

pygame.init()

#set up screen
screen = pygame.display.set_mode([1000, 1000])

# end with user prompt
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Backround color
    screen.fill((0, 0, 225))

    # character
    pygame.draw.circle(screen, (225, 0, 0), (250, 250), 75)

    # flip the display
    pygame.display.flip()

# fin
pygame.quit()