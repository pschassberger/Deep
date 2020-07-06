# create an enviorment for a character to move in
# initial build

# On hold for now, will experiment with Godot

import pygame


pygame.init()

#set up screen
screen = pygame.display.set_mode([2000, 1500])
# character
x = 200
y = 200
width = 200
height = 200
velocity = 50
# end with user prompt
running = True
while running:
    # quit game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Backround color
    screen.fill((0, 0, 0))

    # keys
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= velocity

    if key[pygame.K_RIGHT]:
        x += velocity

    if key[pygame.K_UP]:
        y -= velocity

    if key[pygame.K_DOWN]:
        y += velocity

    # draw character
    pygame.draw.rect(screen, (225, 0, 0), (x, y, width, height))
    pygame.display.update()
    # redraw old location
    screen.fill((0,0,0))
    # update display
    

# fin
pygame.quit()