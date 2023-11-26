scene_list = []
scene = 0
screen = None


def switch_scene(index):
    global scene
    global scene_list
    scene = index
    scene_list[scene].__init__(screen)
    scene_list[scene].update()
