from pygame.math import Vector2
import core
import time

def creationProjectile():
    p = Vector2(core.memory("position"))
    v = Vector2(core.memory("vitesse"))
    v.scale_to_length(core.memory("vitesse").length() + 15)
    r = 3
    c = (255, 255, 255)
    startTime = time.time()

    proj = {"position": p, "vitesse": v, "rayon": r, 'startTime': startTime, "color": c}
    core.memory("projectiles").append(proj)
    #print(proj["position"].x)

def tirProjectile():
    if core.getKeyPressList("SPACE"):
        if len(core.memory("projectiles")) == 0:
            creationProjectile()
        else:
            if time.time() - core.memory("projectiles")[-1]["startTime"] > 0.5:
                creationProjectile()

def updateProjectile():
    for proj in core.memory('projectiles'):
        if time.time() - proj["startTime"] > 1:
            core.memory('projectiles').remove(proj)

    for proj in core.memory("projectiles"):
        proj["position"] = proj["position"]+proj["vitesse"]
    #print(proj["position"].x)
def drawProjectile():
    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["color"],proj["position"],proj["rayon"])