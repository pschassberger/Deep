
# snake game
import pygame
from random import randint
import random


# Constants
BLUE = (102,178,255)
GREEN = (0,255,128)
BLACK = (0,0,0)
RED = (255,51,51)

UI_WIDTH=1080
UI_HEIGHT=720



pygame.init()
ui = pygame.display.set_mode((UI_WIDTH,UI_HEIGHT))
pygame.display.update()

def game():
  
    game = True
    x, y = 200, 200
    dx, dy = 0, 0
    clock = pygame.time.Clock()
    # main game loop
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game = False
            
            print(event)

            '''if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx = 20
                    dy = 0
                elif event.key == pygame.K_LEFT:
                    dx = -20
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -20
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = 20
                    dx = 0
        x += dx
        y += dy
        ui.fill(BLACK)
        pygame.draw.rect(ui, GREEN, [x,y,20,20])'''


        nn_moves()
        
        pygame.display.update()
        clock.tick(20)

        #snake_movement()
        #target()

    pygame.quit()
    quit()

# autonoma

def nn_moves():
    outcomes = ['right', 'left', 'up', 'down']
    x,y=200,200
    choice = random.choice(outcomes)
    if choice == 'right':
        dx = 20
        dy = 0
    elif choice == 'left':
        dx = -20
        dy = 0
    elif choice == 'up':
        dx = 0
        dy = -20
    elif choice == 'down':
        dx = 0
        dy = 20

    x += dx
    y += dy
    ui.fill(BLACK)
    pygame.draw.rect(ui, GREEN, [x,y,20,20])

game()