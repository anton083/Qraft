
from .all_imports import *


"""
    
    def colored_amogus(color):
        
        # Make video with Pixies' song "Allison".
        amogus = gm.Group([gm.Group([
            gm.Cuboid((0.65, 0, 0),(0.65, 0.5, 0.55),color),
            gm.Cuboid((0.5, -0.3, 0),(0.5, 0.2, 0.4),color),
            gm.Cuboid((0.3, 0, 0.15),(0.5, 0.4, 0.25),color),
            gm.Cuboid((0.3, 0, -0.15),(0.5, 0.4, 0.25),color),
            gm.Cuboid((0.7, 0.25, 0),(0.3, 0.2, 0.4),(0.3,0.7,0.9)),
            gm.Cuboid((0.8, 0.25, -0.1),(0.05, 0.21, 0.1),(0.8,0.9,1))],
            position=[-0.5,0,0])])
        return amogus
        
    amogi = gm.Group([
        gm.Group([(colored_amogus((0.85,0.9,0.2)))], [0,0,1], UNIT_QUATERNIONS.copy().rotate(qj, math.pi/2)),
        gm.Group([(colored_amogus((0.1,0.9,0.2)))], [0,0,-1]),
        gm.Group([(colored_amogus((0.9,0.1,0.2)))], [0,0,-2]),
        gm.Group([(colored_amogus((0.1,0.1,0.9)))], [0,0,0], UNIT_QUATERNIONS.copy().rotate(qk, math.pi/2)),
        ])
    
    
    amogi2 = gm.Group([
        gm.Group([(colored_amogus((0.85,0.9,0.2)))], [0,0,1], UNIT_QUATERNIONS.copy().rotate(qj, math.pi/2)),
        gm.Group([(colored_amogus((0.1,0.9,0.2)))], [0,0,-1]),
        gm.Group([(colored_amogus((0.9,0.1,0.2)))], [0,0,-2]),
        gm.Group([(colored_amogus((0.1,0.1,0.9)))], [0,0,0], UNIT_QUATERNIONS.copy().rotate(qk, math.pi/2)),
        ], [0,2,-5])
            
        if keys[pygame.K_SPACE]:
            amogi.unit_vectors.rotate(Q([1,1,1]), 0.05)
            amogi2.unit_vectors.rotate(Q([1,1,1]), -0.05)
        
        amogi.render(light_vector=light_vector)
        amogi2.render(light_vector=light_vector)
"""