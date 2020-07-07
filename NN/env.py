# create an enviorment for a character to move in
# initial build

# On hold for now, will experiment with Godot
#import pygame
import agent


pygame.init()

#set up screen
screen_width = 2000
screen_height = 1500
screen = pygame.display.set_mode([screen_width, screen_height])
# character
agent = Agent(200, 200, 100, 100)
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
    if key[pygame.K_LEFT] and agent.x > 0:
        agent.x -= agent.velocity

    if key[pygame.K_RIGHT] and agent.x < screen_width - agent.width:
        agent.x += agent.velocity

    if key[pygame.K_UP] and agent.y > 0:
        agent.y -= agent.velocity

    if key[pygame.K_DOWN] and agent.y < screen_height - agent.height:
        agent.y += agent.velocity

    # draw character
    pygame.draw.rect(screen, (225, 0, 0), (agent.x, agent.y, agent.width, agent.height))
    pygame.display.update()
    # redraw old location
    screen.fill((0,0,0))
    # update display
    

# fin
pygame.quit()