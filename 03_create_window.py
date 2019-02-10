import pygame
from dragon_sprite import *

pygame.init()

# Create Window
screen = pygame.display.set_mode((437, 720))

# draw background
# 1. upload image
bg = pygame.image.load("./image/background.png")
screen.blit(bg, (0, 0))

# pygame.display.update()


# draw dragon
dragon = pygame.image.load("./image/dragon.png")
screen.blit(dragon, (150, 500))

# update screen
pygame.display.update()



# Create Game clock
clock = pygame.time.Clock()


# 1. Define Rect for dragon init position
dragon_rect = pygame.Rect(150, 500, 50, 43)


# create enemy sprite
enemy = GameSprite("./image/enemy1.png")
enemy1 = GameSprite("./image/enemy1.png", 2)
# create enemy sprite group
enemy_group = pygame.sprite.Group(enemy, enemy1)


# Game Loop
while True:

    clock.tick(60)  # set the frame rate 60 per second

    # catch Event
    # action_list = pygame.event.get()
    # if len(action_list):  # only print when action
    #     print(action_list)

    # listen Event
    for event in pygame.event.get():

        # if the event is quit
        if event.type == pygame.QUIT:
            print("Exit The Game....")

            # quit unload all pygame module
            pygame.quit()

            #exit
            exit()


    # 2. Change dragon position
    dragon_rect.y -= 1


    # 3. use blit to draw
    screen.blit(bg, (0, 0))
    screen.blit(dragon, dragon_rect)


    # Sprint Group call update and then draw
    # update - update all enemy position
    enemy_group.update()
    #draw
    enemy_group.draw(screen)


    # 4. update frame
    pygame.display.update()

    if dragon_rect.y <= (0 - dragon_rect.height):
        dragon_rect.y = 720

pygame.quit()