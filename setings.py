import core
from pygame import Rect

def setings ():
    print('settings')
    core.Draw.rect((103, 113, 121), (340, 645, 110, 60), 5)
    core.Draw.text((255, 255, 255), "MENU", (350, 650), 30)

    if core.getMouseLeftClick():
        r = Rect(340, 645, 110, 60)
        if r.collidepoint(core.getMouseLeftClick()) == True :
            #core.GetMouseLeftClick()[1]) :
            core.memory('etat',0)

    core.Draw.text((255, 255, 255), "RULES", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 - 300))
    core.Draw.text((255, 255, 255), "Destroy the asteroids without it touching you ", (core.WINDOW_SIZE[1] / 2 - 320, core.WINDOW_SIZE[1] / 2 - 260))
    core.Draw.text((255, 255, 255), "GOOD LUCK :) ", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 180))

    core.Draw.text((255, 255, 255), "SETTINGS" , (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 -100 ))
    core.Draw.text((255, 255, 255), "Z = Move forward", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 -40 ))
    core.Draw.text((255, 255, 255), "Q = Steer left", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 ))
    core.Draw.text((255, 255, 255), "D = Steer right", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 40))
    core.Draw.text((255, 255, 255), "SPACE = Shot", (core.WINDOW_SIZE[1] / 2 - 140, core.WINDOW_SIZE[1] / 2 + 80))
    print(core.WINDOW_SIZE[1])