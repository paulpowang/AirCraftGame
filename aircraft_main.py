import pygame
from dragon_sprite import *


class AirCraftGame(object):
    '''Main game class'''

    def __init__(self):
        print("initial game")

        # 1. Create Game Screen
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. Create Game Clock
        self.clock = pygame.time.Clock()
        # 3. create sprit and sprite group
        self.__create_sprites()
        # 4. Set timer for Event Create enemy
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):

        # create background sprite and group
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # create enemy sprite and group
        self.enemy_group = pygame.sprite.Group()

        # create hero sprite and group
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Game Start")

        while True:
            # 1. set frame rate
            self.clock.tick(FRAME_PER_SEC)
            # 2. event listener
            self.__event_handler()
            # 3. collision detect
            self.__check_collide()
            # 4. update position, draw sprite group
            self.__update_sprites()
            # 5. update screen
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # see if exit the game
            if event.type == pygame.QUIT:
                AirCraftGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("Enemy showup....")
                # create enemy sprite
                enemy = Enemy()
                # add enemy sprite into group.
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("move right")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            # print("move right")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game Over")

        pygame.quit()
        exit()


if __name__ == "__main__":

    # create game object
    game = AirCraftGame()

    # start game
    game.start_game()