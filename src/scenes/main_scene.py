from . import scene

import pygame
import enemy
import player

score = 0


class main_scene(scene.Scene):
    def __init__(self, screen):
        global score
        super().__init__([], screen)
        self.background = pygame.image.load("assets/background.png").convert()
        player_group = pygame.sprite.GroupSingle()
        laser_group = pygame.sprite.Group()
        enemy_laser_group = pygame.sprite.Group()
        enemy_group = enemy.EnemyGroup(5, 3, enemy_laser_group.add)
        player_group.add(player.player(laser_group.add))
        self.spriteGroups.append(player_group)
        self.spriteGroups.append(laser_group)
        self.spriteGroups.append(enemy_group)
        self.spriteGroups.append(enemy_laser_group)
        self.spriteGroups.append(player_group.sprites()[0].life_group)
        score = 0
        self.font = pygame.font.Font("assets/Quicksand-Regular.ttf", 20)

    def update(self):
        global score
        super().update()
        self.scoretext = self.font.render(f"Score: {score}", True, (255, 255, 255))
        collidelist = pygame.sprite.groupcollide(
            self.spriteGroups[1], self.spriteGroups[2], True, True
        )
        if collidelist:
            score += len(collidelist)
        if pygame.sprite.groupcollide(
            self.spriteGroups[0], self.spriteGroups[3], False, True
        ):
            self.spriteGroups[0].sprites()[0].change_lives(
                self.spriteGroups[0].sprites()[0].lives - 1
            )
        if not self.spriteGroups[2].sprites():
            self.spriteGroups[2].__init__(5, 3, self.spriteGroups[3].add)
            self.spriteGroups[1].empty()
            self.spriteGroups[2].direction *= 1.5
            for i in self.spriteGroups[2].sprites():
                i.time_range[0] *= 0.9
                i.time_range[1] *= 0.9
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.switch_scene(0)

    def draw(self):
        for i in range(3):
            for j in range(4):
                self.screen.blit(self.background, (i * 256, j * 256))
        super().draw()
        self.screen.blit(self.scoretext, (10, 10))
