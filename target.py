import core
from pygame import Rect
import random



def targetCollision():
    for proj in core.memory("projectiles"):
        if core.memory('target').collidepoint(proj["position"].x, proj["position"].y) :
            #print("BOOM")
            core.memory("projectiles").remove(proj)
            core.memory("target", Rect(random.randint(50, 750), random.randint(50, 750), 90,90))
            core.memory('score',core.memory('score')+1)



def drawTarget():
    #core.Draw.rect((0, 0, 0), core.memory("target"))
    #while core.memory('nbrtarget') = 0 :
        core.memory("textureAsteroide", core.Texture("./asteroide.png", core.memory('target')))

        if not core.memory("textureAsteroide").ready:
            core.memory("textureAsteroide").load()
        core.memory("textureAsteroide").show()



