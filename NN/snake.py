
# snake game
import pygame
from random import randint

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
    # main game loop
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game = False
            print(event)

        snake()
        #target()

    pygame.quit()
    quit()

# snake and target
def snake():
    x1, y1 = 200, 200
    pygame.draw.rect(ui, GREEN, [x1,y1,20,20])
    pygame.display.update()

def target():
    x_pos = randint(0,1060)
    y_pos = randint(0,700)
    pygame.draw.rect(ui, RED, [x_pos,y_pos,20,20])
    pygame.display.update()

def movement(function()):
    


game()