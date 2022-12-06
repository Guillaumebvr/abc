from pygame.math import Vector2

import core

def move():
    #if core.memory('vitesse').length() >= - 0.1 :
     #   core.memory('vitesse').scale_to_length(core.memory('vitesse').length() + 0.1)
    core.memory('position', core.memory('position') + core.memory('vitesse'))

def drawPlayer():

    move()

    vectP1 = core.memory("vitesse")
    vectP1 = vectP1.rotate(90)
    vectP1.scale_to_length(5)
    P1 = core.memory("position") + vectP1

    vectP2 = Vector2(core.memory("vitesse"))
    vectP2.scale_to_length(40)
    P2 = core.memory("position") + vectP2

    vectP3 = core.memory("vitesse")
    vectP3 = vectP3.rotate(-90)
    vectP3.scale_to_length(5)
    P3 = core.memory("position") + vectP3
    #print(P1,P2,P3)
    core.Draw.polygon((255, 255, 255), (P1, P2, P3))
    V = {"P1" : P1, "P2": P2 , "P3" : P3 }
    #print(V)


def controleVaisseau ():
    #print(core.memory('vitesse'))

    if core.getKeyPressList("z"):
        if core.memory('vitesse')[1] > -15 :
            core.memory('vitesse').scale_to_length(core.memory('vitesse').length() + 1)
            flamme()
        else :
            core.memory('vitesse').scale_to_length(core.memory('vitesse').length() - 1)
            #flamme()
    if core.getKeyPressList('d'):
        core.memory("vitesse", core.memory('vitesse').rotate(5))
    if core.getKeyPressList('q'):
        core.memory("vitesse", core.memory('vitesse').rotate(-5))
    if core.getKeyPressList('s'):
        #core.memory('vitesse').scale_to_length(core.memory('vitesse').length() - 1)
        if core.memory('vitesse')[1] < -1 :
            core.memory('vitesse').scale_to_length(core.memory('vitesse').length() - 1)
        #else :
        #   core.memory('vitesse').scale_to_length(core.memory('vitesse').length() + 1)

def flamme():
    move()

    vectP6 = core.memory("vitesse")
    vectP6 = vectP6.rotate(-90)
    vectP6.scale_to_length(-5)
    P6 = core.memory("position") + vectP6
    core.memory("P6", P6)

    vectP4 = core.memory("vitesse")
    vectP4 = vectP4.rotate(90)
    vectP4.scale_to_length(-5)
    P4 = core.memory("position") + vectP4
    core.memory("P4", P4)

    vectP5 = Vector2(core.memory("vitesse"))
    vectP5.scale_to_length(-20)
    P5 = core.memory("position") + vectP5
    core.memory("P5", P5)

    core.Draw.polygon((255, 163, 0), (P4, P5, P6), 0)


#def collisionVaisseau():
     #if core.memory('target').dist
      # print('AIE')
    #print(V)