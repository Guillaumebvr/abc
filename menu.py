import pygame.transform

import core
from pygame import Rect
from pygame.math import Vector2
#from play import restart

def menu():

    #pygame.transform.scale(image,(400,100),0)
    image = core.memory("decord", core.Texture("./logo2.png", Vector2(335,150)))
    if not core.memory("decord").ready:
        core.memory("decord").load()
    core.memory("decord").show()
    #pygame.transform.scale(image,(400,100),0)
    #print("menu")

    core.Draw.rect((103,113,121),(280,295,210,60),5)
    core.Draw.text((255,255,255),"NEW GAME ",(300,300),30)

    if core.getMouseLeftClick():
        r = Rect(280,295,210,60)
        if r.collidepoint(core.getMouseLeftClick()) == True :
            #core.GetMouseLeftClick()[1]) :
            #restart()
            core.memory('etat',1)

    core.Draw.rect((103,113,121), (230, 395, 320, 60), 5)
    core.Draw.text((255,255,255), "SETTINGS / RULES ", (245, 400), 30)

    if core.getMouseLeftClick():
        r = Rect(230, 395, 320, 60)
        if r.collidepoint(core.getMouseLeftClick()) == True :
            #core.GetMouseLeftClick()[1]) :
            core.memory('etat',2)

    core.Draw.rect((103, 113, 121), (330, 595, 110, 60), 5)
    core.Draw.text((255, 255, 255), "QUIT ", (core.WINDOW_SIZE[1] / 2 - 60, core.WINDOW_SIZE[1] / 2 + 200), 30)

    if core.getMouseLeftClick():
        r = Rect(330, 595, 110, 60)
        if r.collidepoint(core.getMouseLeftClick()) == True:
            # core.GetMouseLeftClick()[1]) :
            quit()