import core
from pygame import Rect
from pygame.math import Vector2
#from play import reset

def restart ():
    core.memory("position", Vector2(400, 400))
    core.memory("vitesse", Vector2(0.00001, -1.0001))
    core.memory('score',0 )

def gameover ():
    #print('PERDU')

    core.Draw.text((255, 255, 255), "GAME OVER", (310, 250), 50)
    core.Draw.text((255, 255, 255), "SCORE : ", (310, 290), 50)
    core.Draw.text((255, 255, 255), str(core.memory('score')), (450, 290), 50)


    core.Draw.rect((103, 113, 121), (300, 675, 195, 60), 5)
    core.Draw.text((255, 255, 255), "BACK MENU", (310, 680), 30)

    if core.getMouseLeftClick():
        r = Rect(300, 645, 195, 60)
        if r.collidepoint(core.getMouseLeftClick()) == True:
            # core.GetMouseLeftClick()[1]) :
            restart()
            core.memory('etat', 0)
