import random
import time

from pygame import Rect
from pygame.math import Vector2

import core
from Vaisseau import drawPlayer,controleVaisseau
from Projectiles import creationProjectile,tirProjectile,updateProjectile
from play import traverser,score,background, play
from target import targetCollision,drawTarget
from menu import menu
from setings import setings
from gameover import gameover

def setup():
    core.fps = 60
    core.WINDOW_SIZE = [800, 800]

    core.memory("position", Vector2(400,400))
    core.memory('vitesse' , Vector2(0,-1))

    core.memory('projectiles', [])
    core.memory("target",Rect(random.randint(50,750),random.randint(50,750),90,90))
    #core.memory("target", [])
    #core.memory("target",[])

    #core.memory('background',0)
    core.memory('score', 0)
    core.memory('etat',0)
    core.memory('P1',0)
    core.memory('P2',0)
    core.memory('P3',0)

    core.memory('nbrtarget',0)


def run():
    #print(core.getMouseLeftClick())
    if core.memory('etat') == 0 :
        menu()
    if core.memory("etat") == 1 :
        play()
    if core.memory('etat') == 2:
        setings()
    if core.memory('etat') == 3 :
        gameover()

    core.cleanScreen()

    #background()
    #traverser()

    #print("nb projectiles : ", len(core.memory("projectiles")))

    #CLEAN
    #updateProjectile()

    #Control
    #controleVaisseau()

    #TIR
    #if core.getKeyPressList("SPACE"):
     #   tirProjectile()

    #DEPLACEMENT
    #core.memory('position',  core.memory('position')+core.memory('vitesse') )

    #DESSIN TIR
    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["color"],proj["position"],proj["rayon"])

    #Dessin Target
    #core.Draw.rect((255,0,0),core.memory("target"))
    #drawTarget()
    #Collision
    #targetCollision()

    #score
    #score()

    #dessin Vaisseau
    #drawPlayer()








core.main(setup, run)