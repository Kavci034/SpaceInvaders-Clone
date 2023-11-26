import pygame
import laser
import scenes.scene_manager as scene_manager


class player(pygame.sprite.Sprite):
    def __init__(self, add_laser_to_group: callable):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.smoothscale_by(self.image, 0.75)
        self.rect = self.image.get_rect()
        self.rect.bottom = 700
        self.rect.centerx = 300
        self.speed = 10
        self.add_laser_to_group = add_laser_to_group
        self.laser_timer = 0
        self.lives = 3
        self.life_group = pygame.sprite.Group()
        for i in range(self.lives):
            self.life_group.add(life((i * 30 + 50, 750)))

    def update(self):
        keys = pygame.key.get_pressed()
        self.laser_timer += 1 / 60
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.laser_timer >= 0.5:
            self.laser_timer = 0
            self.add_laser_to_group(laser.Laser(self.rect.midtop))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 600:
            self.rect.right = 600

    def change_lives(self, lives):
        self.lives = lives
        self.life_group.empty()
        if self.lives < 0:
            self.lives = 0
        if self.lives == 0:
            self.kill()
            scene_manager.switch_scene(2)
        for i in range(lives):
            self.life_group.add(life((i * 30 + 25, 750)))


class life(pygame.sprite.Sprite):
    def __init__(self, position) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/lifeicon.png").convert_alpha()
        self.image = pygame.transform.smoothscale_by(self.image, 0.75)
        self.rect = self.image.get_rect()
        self.rect.center = position
