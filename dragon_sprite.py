import pygame

# screen size
SCREEN_RECT = pygame.Rect(0, 0, 437, 700)

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


class Background(GameSprite):
    '''Game Background Sprite'''

    def update(self):

        # 1. call parent init
        super().update()

        # 2. if bg image leave screen from bottom, move bg image to top
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


