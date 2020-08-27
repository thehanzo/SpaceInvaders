import pygame

from helpers.ScreenHelper import ScreenHelper


class Player:

    # region Class variables
    screenHelper = None
    # Set spaceship
    spaceship_obj = pygame.image.load("img/shuttle.png")
    # Set position
    posx = None
    posy = None
    # Boundaries
    boundaryUp = None
    boundaryLeft = None
    boundaryDown = None
    boundaryRight = None
    # endregion

    def __init__(self, screenHelper):
        self.screenHelper = screenHelper
        # Set position
        self.posx = self.screenHelper.getCenter("posx")
        self.posy = self.screenHelper.height - 60
        # Boundaries
        self.boundaryUp = self.screenHelper.getCenter("posy")
        self.boundaryLeft = 0
        self.boundaryDown = self.screenHelper.height - 60
        self.boundaryRight = self.screenHelper.width - 65

    def fire(self):
        pass

    def move(self, direction):
        if direction == "Up":
            # Limit Up movement to center of screen
            if self.posy > self.boundaryUp:
                self.posy -= 5
        if direction == "Left":
            if self.posx > self.boundaryLeft:
                self.posx -= 5
        if direction == "Down":
            if self.posy < self.boundaryDown:
                self.posy += 5
        if direction == "Right":
            if self.posx < self.boundaryRight:
                self.posx += 5

    def print(self):
        self.screenHelper.print(self.spaceship_obj, self.posx, self.posy)