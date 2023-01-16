import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}

        physicsClient = p.connect(p.GUI)
        self.robotId = p.loadURDF("body.urdf")

        
