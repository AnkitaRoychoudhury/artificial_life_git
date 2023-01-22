import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        

    def Run(self):

        for t in range(c.num_iters):
             p.stepSimulation()
             self.robot.Sense(t)
             self.robot.Think(t)
             self.robot.Act(t)

             time.sleep(c.sleep_time)

    def __del__(self):
        p.disconnect()
