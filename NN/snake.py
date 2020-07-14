
# snake game
import pygame

# Constants
BLUE = (102,178,255)
GREEN = (0,255,128)
BLACK = (0,0,0)
RED = (255,51,51)

def game():


    pygame.init()
    ui = pygame.display.set_mode((1080,720))
    pygame.display.update()
    game = True
    # main game loop
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game = False
            print(event)

        snake()

    pygame.quit()
    quit()

# snake and target
'''def snake():
    pygame.draw.rect(ui, GREEN, [200,150,10,10])
    pygame.display.update()'''

game()