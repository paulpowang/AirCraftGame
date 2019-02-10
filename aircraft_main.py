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


    def __create_sprites(self):

        # create background sprite and group
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # create enemy sprite and group
        self.enemy_group = pygame.sprite.Group()

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

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

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