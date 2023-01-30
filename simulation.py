import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        
        if directOrGUI == 'DIRECT':
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
        
        #physicsClient = p.connect(p.GUI)

        self.world = WORLD()
        self.robot = ROBOT()

        #if 
        #p.connect(p.DIRECT)
        #p.connect(p.GUI)
        

    def Run(self):

        for t in range(c.num_iters):
             p.stepSimulation()
             self.robot.Sense(t)
             self.robot.Think()
             self.robot.Act(t)

             time.sleep(c.sleep_time)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


