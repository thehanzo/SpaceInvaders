import pygame

from helpers.ScreenHelper import ScreenHelper
from objects.bullet import Bullet


class BulletHandler:

    # region Class variables
    screen = None
    bullets = []
    # Firing
    fireCooldown = 300
    lastShot = None
    # endregion

    def __init__(self, screenHelper):
        self.screen = screenHelper
        self.lastShot = pygame.time.get_ticks()

    def move(self):
        # Move all active bullets
        for x in self.bullets:
            x.move()

    def print(self):
        for x in self.bullets:
                x.print()

    def fireBullet(self, posx, posy):
        # fire only if cooldown has finished
        now = pygame.time.get_ticks()
        if (now - self.lastShot) >= self.fireCooldown:
            self.lastShot = now
            self.bullets.append(Bullet(self.screen, posx, posy))