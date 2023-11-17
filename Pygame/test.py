from examplepygame import rungame
from examplepygame import Player
from examplepygame import Enemy
from examplepygame import Cloud

import pygame
import unittest

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def check_collision(player, enemies):
    return pygame.sprite.spritecollideany(player, enemies)

class TestCollision(unittest.TestCase):
    def test_collision_detection(self):
        self.assertFalse(rungame())

if __name__ == '__main__':
    unittest.main()


    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
