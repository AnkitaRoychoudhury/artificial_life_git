import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):

        physicsClient = p.connect(p.GUI)
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
    
    
    #p.loadSDF("world.sdf")
