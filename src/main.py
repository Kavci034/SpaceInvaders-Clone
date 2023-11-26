import pygame
import scenes.main_scene
import scenes.title_scene
import scenes.scene_manager
import scenes.gameover_scene

pygame.init()

screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders - Pygame CE")
scenes.scene_manager.screen = screen

main_scene = scenes.main_scene.main_scene(screen)
title_scene = scenes.title_scene.title_scene(screen)
gameover_scene = scenes.gameover_scene.gameover_scene(screen)

scenes.scene_manager.scene_list.append(title_scene)
scenes.scene_manager.scene_list.append(main_scene)
scenes.scene_manager.scene_list.append(gameover_scene)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scenes.scene_manager.scene_list[scenes.scene_manager.scene].update()
    scenes.scene_manager.scene_list[scenes.scene_manager.scene].draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
