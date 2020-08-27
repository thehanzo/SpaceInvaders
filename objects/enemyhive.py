import pygame

from helpers.ScreenHelper import ScreenHelper
from objects.enemy import Enemy


class EnemyHive:

    # region Class variables

    screen = None
    hive = []
    movementCooldown = 500
    lastMovement = None

    # endregion

    def __init__(self, screenHelper):
        self.screen = screenHelper
        center = self.screen.getCenter("posx")
        startPositionHiveBuilder = center + (center / 2)
        posx = startPositionHiveBuilder
        self.lastMovement = pygame.time.get_ticks()
        for x in range(7):
            if x < 3:
                self.hive.append(Enemy(self.screen, posx, 0, x))
            if x > 3:
                self.hive.append(Enemy(self.screen, posx, 80, x))
            if x == 3:
                # Reset posx
                posx = startPositionHiveBuilder
            # Shift left
            if x != 3:
                posx -= 80

    def move(self):
        # move only if cooldown has finishes
        now = pygame.time.get_ticks()
        if (now - self.lastMovement) >= self.movementCooldown:
            self.lastMovement = now
            for x in self.hive:
                x.move()

    def print(self):
        for x in self.hive:
                x.print()