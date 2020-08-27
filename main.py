import pygame, sys, objects
from pygame.locals import *

from helpers.ScreenHelper import ScreenHelper
from objects import player
from objects import enemyhive
from objects import bulletHandler

"""
Game loop :
* handle event
* update game state
* draw screen
"""

# initialize pygame
pygame.init()
# Clock object for FPS management
fps_clock = pygame.time.Clock()

# region Assets
# Window
screen = pygame.display.set_mode((1280, 800))
screenHelper = ScreenHelper(screen)
player = player.Player(screenHelper)
hive = enemyhive.EnemyHive(screenHelper)
bulletHandler = bulletHandler.BulletHandler(screenHelper)
# endregion

# region Game loop

while True:
    # Events
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player.move("Up")
    if keys[K_LEFT]:
        player.move("Left")
    if keys[K_DOWN]:
        player.move("Down")
    if keys[K_RIGHT]:
        player.move("Right")
    if keys[K_ESCAPE]:
        pygame.event.post(pygame.event.Event(QUIT))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bulletHandler.fireBullet(player.posx + 20, player.posy)

        if event.type == QUIT:
            # quit() is the opposite of init()
            pygame.quit()
            sys.exit()

    # Update Screen
    screen.fill((0, 0, 0))
    player.print()
    hive.move()
    hive.print()
    bulletHandler.move()
    bulletHandler.print()
    pygame.display.update()
    # wait long enough to run at 30 frame per second.
    fps_clock.tick(30)
# endregion
