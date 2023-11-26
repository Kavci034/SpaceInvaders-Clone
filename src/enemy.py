import pygame
import random
import enemy_laser


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, add_laser_to_group: callable):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.smoothscale_by(self.image, 0.6)
        self.rect = self.image.get_rect(center=position)
        self.time_range = [120, 360]
        self.timer = random.randint(*self.time_range)
        self.time = 0
        self.add_l = add_laser_to_group

    def update(self, direction):
        self.rect.move_ip(direction)
        self.time += 1
        if self.time >= self.timer:
            self.time = 0
            self.timer = (
                random.randint(
                    int(self.time_range[0]) * 100, int(self.time_range[1] * 100)
                )
                / 100
            )
            self.add_l(enemy_laser.enemy_laser(self.rect.midbottom))


class EnemyGroup(pygame.sprite.Group):
    def __init__(self, size_x, size_y, add_laser_to_group: callable):
        super().__init__()
        for i in range(size_x):
            for j in range(size_y):
                self.add(Enemy((100 + i * 75, 100 + j * 75), add_laser_to_group))
        self.direction = 1
        self.rect = pygame.Rect(100, 100, size_x * 75, size_y * 75)

    def update(self):
        if self.rect.left < 40 or self.rect.right > 630:
            self.direction *= -1
            super().update((0, 25))
            self.rect.move_ip((0, 25))
        super().update((self.direction, 0))
        self.rect.move_ip((self.direction, 0))
