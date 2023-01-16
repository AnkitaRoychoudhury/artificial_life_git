import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        
    # do these go inside def __init__?
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        #self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot.robotId)