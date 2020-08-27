import pygame


class ScreenHelper:
    width = None
    height = None
    screen = None
    # Boundaries
    boundaryUp = 0
    boundaryLeft = 0
    boundaryDown = None
    boundaryRight = None

    def __init__(self, window):
        self.screen = window
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.boundaryDown = self.height
        self.boundaryRight = self.width

    def getCenter(self, position):
        if position == "posx":
            return self.width / 2
        if position == "posy":
            return self.height / 2

    def print(self, obj, posx, posy):
        self.screen.blit(obj, (posx, posy))

    def getWidth(self):
        return self.width