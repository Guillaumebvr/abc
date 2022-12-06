import core
from pygame.math import Vector2

from Vaisseau import drawPlayer,controleVaisseau
from Projectiles import creationProjectile,tirProjectile,updateProjectile,drawProjectile
from target import targetCollision, drawTarget
from menu import menu
from gameover import gameover

def score():
    core.Draw.text((255, 255, 255), "score : " + str(core.memory("score")), (10, 10), 10, '')

def traverser():
    if core.memory("position").y < 0:
        core.memory("position").y = core.WINDOW_SIZE[1]
    if core.memory("position").x < 0:
        core.memory("position").x = core.WINDOW_SIZE[1]
    if core.memory("position").y > core.WINDOW_SIZE[1]:
        core.memory("position").y = 0
    if core.memory("position").x > core.WINDOW_SIZE[1]:
        core.memory("position").x = 0

def background():
    core.memory("background", core.Texture( "./background.jpg", (1, 1), 0, (1440, 800)))
    if not core.memory("background").ready:
        core.memory("background").load()
    core.memory("background").show()


def play():
    #print('play')
    background()

    if core.getKeyPressList("SPACE"):
        tirProjectile()
    if core.getKeyPressList('ESCAPE'):
        reset()
        core.memory('etat',0)

    if core.memory("target").collidepoint(core.memory("position")):
        core.memory("etat",3)

    drawPlayer()
    controleVaisseau()
    traverser()

    updateProjectile()
    drawProjectile()

    #collisionVaisseau()
    targetCollision()
    drawTarget()
    #targetmovement()
    if core.getKeyPressList('p'):
        core.memory('etat',3)

    score()
