import pygame

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



# Game Loop
while True:
    pass

pygame.quit()