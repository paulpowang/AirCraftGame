import random
import pygame

# screen size
SCREEN_RECT = pygame.Rect(0, 0, 437, 700)
# frame rate
FRAME_PER_SEC = 60
# Timer for creating enemy
CREATE_ENEMY_EVENT = pygame.USEREVENT
# Hero shoot
HERO_FIRE_EVENT = pygame.USEREVENT + 1

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

    def __init__(self, is_alt=False):
        super().__init__("./image/background.png")

        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):

        # 1. call parent init
        super().update()

        # 2. if bg image leave screen from bottom, move bg image to top
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    '''Enemy Sprites'''

    def __init__(self):

        # 1. call parent class init, create enemy, assign image
        super().__init__("./image/enemy1.png")

        # 2. speed in random from 1 to 3
        self.speed = random.randint(1, 3)

        # 3. position in random
        self.rect.bottom = 0  # initial y position at top of screen, same as  = -rect.height
        # max x = screen width - enemy width
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1. get parent class update
        super().update()

        # 2. check if fly out of screen, then del the enemy
        if self.rect.y >= SCREEN_RECT.height:
            # print("fly out of screen and delete....")
            # kill() can remove sprite from group and destroy from memory.
            self.kill()

    def __del__(self):
        # print("enemy destroy...")
        pass


class Hero(GameSprite):
    '''Hero sprite'''


    def __init__(self):
        # 1. call parent init
        super().__init__("./image/dragon.png", 0)

        # 2. Hero initial position
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3. create bullet sprite group
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        # hero only move on x direction
        self.rect.x += self.speed

        # let hero cannot move out of screen
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("shoot...")

        for i in (0, 1, 2):


            # 1. create bullet sprite
            bullet = Bullet()
            # 2. bullet position
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. add bullet into group
            self.bullet_group.add(bullet)

class Bullet(GameSprite):
    '''Bullet Sprite'''

    def __init__(self):
        super().__init__("./image/bullet1.png", -2)

    def update(self):

        super().update()
        # if bullet out of screen
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("destroy bullet...")
