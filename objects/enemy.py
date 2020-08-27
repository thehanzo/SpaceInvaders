import pygame

from helpers.ScreenHelper import ScreenHelper


class Enemy:

    # region Class variables
    screenHelper = None
    # Enemy ID
    enemyId = None
    # Set spaceship
    spaceship_obj = pygame.image.load("img/spaceship.png")
    # Position
    posx = None
    posy = None
    direction = 0
    # Boundaries
    boundaryUp = 0
    boundaryLeft = 0
    boundaryDown = None
    boundaryRight = None
    # Movement
    horizontalMovement = 40
    verticalMovement = 80
    # endregion

    def __init__(self, screenHelper, posx, posy, enemyId):
        self.screenHelper = screenHelper
        # Set position
        self.posx = posx
        self.posy = posy
        self.boundaryDown = self.screenHelper.height - 90
        self.boundaryRight = self.screenHelper.width - 90
        # Set ID
        self.enemyId = enemyId

    def move(self):
        # check for boundary
        if self.posx < 40:
            self.changeDirection()
        if self.posx > self.boundaryRight:
            self.changeDirection()
        # Move
        if self.direction == 0:
            # Move left
            self.posx -= self.horizontalMovement
        else:
            self.posx += self.horizontalMovement

    def changeDirection(self):
            # Jump down
            self.posy += self.verticalMovement
            self.direction = 1 if (self.direction == 0) else 0

    def print(self):
        self.screenHelper.print(self.spaceship_obj, self.posx, self.posy)