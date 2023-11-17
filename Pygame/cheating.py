import pygame
import unittest

def check_collision(player, enemies):
    return pygame.sprite.spritecollideany(player, enemies)

class TestCollision(unittest.TestCase):
    def test_collision_detection(self):
        player = pygame.sprite.Sprite()
        player.rect = pygame.Rect(0, 0, 10, 10)

        enemy = pygame.sprite.Sprite()
        enemy.rect = pygame.Rect(0, 0, 10, 10)

        enemies = pygame.sprite.Group()
        enemies.add(enemy)

        result = check_collision(player, enemies)

        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
