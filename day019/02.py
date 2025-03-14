import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class MainGame:
    window = None

    def __init__(self):
        pass

    def start_game(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("坦克大战")
        while True:
            pygame.display.update()

    def end_game(self):
        pass


class Tank:

    def __init__(self):
        pass

    def move(self):
        pass

    def shot(self):
        pass

    def display_tank(self):
        pass


class MyTank(Tank):

    def __init__(self):
        super().__init__()


class EnemyTank(Tank):

    def __init__(self):
        super().__init__()


class Bullet:

    def __init__(self):
        pass

    def move(self):
        pass

    def display_bullet(self):
        pass


class Wall:

    def __init__(self):
        pass

    def display_wall(self):
        pass


class Explode:

    def __init__(self):
        pass

    def display_explode(self):
        pass


class Music:

    def __init__(self):
        pass

    def play(self):
        pass


if __name__ == "__main__":
    MainGame().start_game()
