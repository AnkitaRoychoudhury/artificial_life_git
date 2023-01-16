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
        # motor command vector
        # angle_range = np.linspace(0, 2*np.pi, c.num_iters)
        # targetAngles_BackLeg = c.amplitude_BackLeg * np.sin(c.frequency_BackLeg * angle_range + c.phaseOffset_BackLeg)
        # targetAngles_FrontLeg = c.amplitude_FrontLeg * np.sin(c.frequency_FrontLeg * angle_range + c.phaseOffset_FrontLeg)
       
        # backLegSensorValues = np.zeros(c.num_iters)
        # frontLegSensorValues = np.zeros(c.num_iters)

        for t in range(c.num_iters):
             p.stepSimulation()
             self.robot.Sense(t)
             self.robot.Act(t)

            # #backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

            
            # pyrosim.Set_Motor_For_Joint(bodyIndex = self.robot.robotId,jointName = "Torso_BackLeg", 
            # controlMode = p.POSITION_CONTROL,targetPosition = targetAngles_BackLeg[i] ,maxForce = c.force)

            # pyrosim.Set_Motor_For_Joint(bodyIndex = self.robot.robotId,jointName = "Torso_FrontLeg", 
            # controlMode = p.POSITION_CONTROL,targetPosition = targetAngles_FrontLeg[i] ,maxForce = c.force)

             time.sleep(c.sleep_time)

    def __del__(self):
        p.disconnect()

