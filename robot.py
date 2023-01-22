import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c

class ROBOT:
    def __init__(self):
        
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
            for i,curr_sensor in enumerate(self.sensors):

                # call the ith sensor instance's get_value() method
                SENSOR.Get_Value(self.sensors[curr_sensor],t)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

        self.amplitude = np.pi/4
        self.frequency = 5
        self.offset = 0
        
        angle_range = np.linspace(0, 2*np.pi, c.num_iters)
        self.targetAngles = self.amplitude * np.sin(self.frequency * angle_range + self.offset)
        self.targetAngles2 = self.amplitude * np.sin(self.frequency/2 * angle_range + self.offset)

    def Act(self, t):
        for i, curr_motor in enumerate(self.motors):

            MOTOR.Set_Value(self.motors[curr_motor],self,t)

            
        
