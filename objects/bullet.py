import pygame


class Bullet:

    # Class variables
    screenHelper = None
    white = (255, 255, 255)
    bulletShape = pygame.image.load("img/bullet.png")
    # Position
    posx = None
    posy = None
    screen = None

    def __init__(self, screenHelper, posx, posy):
        self.screenHelper = screenHelper
        self.posx = posx
        self.posy = posy

    def move(self):
        self.posy -= 5

    def print(self):
        self.screenHelper.print(self.bulletShape, self.posx, self.posy)