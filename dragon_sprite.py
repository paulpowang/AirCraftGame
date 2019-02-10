import pygame

class GameSprite(pygame.sprite.Sprite):
    '''Aircraft Game Sprite'''

    def __init__(self, image_name, speed=1):

        # call parent class __init__()
        super().__init__()

        # define object element
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # move up
        self.rect.y += self.speed