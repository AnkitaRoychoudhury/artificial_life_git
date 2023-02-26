import numpy as np
import numpy.random as rand
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 -1
        self.myID = nextAvailableID
        

    def Start_Simulation(self, directOrGUI):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        
        os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        #os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " &")



    def Wait_For_Simulation_To_End(self):

        fitnessFileName = 'fitness'+str(self.myID)+'.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(1)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.readlines()[0])

        f.close()
        os.system('rm ' + fitnessFileName)


    def Set_ID(self, val): # NOT SURE STEP 33 PHC
        self.myID = val

   

    def Create_World(self):
        length=1
        width=1
        height=1

        x=3
        y=3
        z=0.5

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name = "Torso", pos=[x,y,z] , size=[width, length, height])
        pyrosim.End()

    def Create_Body(self):
        length=1
        width=1
        height=1

        # get random widths btwn 0.2 and 1
        a = 0.2
        b = 1
        box1 = (b-a) * random.random() + a
        box2 = (b-a) * random.random() + a

        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name = "Torso", pos=[1,0,1.5] , size=[4, 1, 1])

        pyrosim.Send_Joint( name = "Torso_Leg1" , parent= "Torso" , child = "Leg1" , type = "revolute", position = [0.5,0,1], jointAxis = '1 0 0')
        pyrosim.Send_Cube(name = "Leg1", pos=[-0.5, 0, -0.5] , size=[box1, 1, 1])

        pyrosim.Send_Joint( name = "Torso_Leg2" , parent= "Torso" , child = "Leg2" , type = "revolute", position = [1.5, 0,1], jointAxis = '1 0 0')
        pyrosim.Send_Cube(name = "Leg2", pos=[0.5, 0, -0.5] , size=[box2,1,1])

        # make more cubes
        pyrosim.Send_Joint( name = "Torso_Leg3" , parent= "Torso" , child = "Leg3" , type = "revolute", position = [0.75, 0,1], jointAxis = '1 0 0')
        pyrosim.Send_Cube(name = "Leg3", pos=[0, 0, -0.5] , size=[box2,1,1])

        pyrosim.Send_Joint( name = "Torso_Leg4" , parent= "Torso" , child = "Leg4" , type = "revolute", position = [0, 0,1], jointAxis = '1 0 0')
        pyrosim.Send_Cube(name = "Leg4", pos=[-1, 0, -0.5] , size=[box2,1,1])

        pyrosim.Send_Joint(color_code ='    <color rgba="0 1.0 1.0 1.0"/>', name = "Torso_Leg5" , parent= "Torso" , child = "Leg5" , type = "revolute", position = [2, 0,1], jointAxis = '1 0 0')
        pyrosim.Send_Cube(name = "Leg5", pos=[1, 0, -0.5] , size=[box2,1,1])

    

        pyrosim.End()




    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName = "Leg1")
        pyrosim.Send_Sensor_Neuron(name=2, linkName = "Leg2")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName = "RightLeg")
        # pyrosim.Send_Sensor_Neuron(name=5, linkName = "FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=6, linkName = "BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=7, linkName = "RightLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=8, linkName = "LeftLowerLeg")
        
        pyrosim.Send_Motor_Neuron(name=2, jointName = "Torso_Leg1"),
        # pyrosim.Send_Motor_Neuron(name=10, jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=11, jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name=12, jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name=13, jointName = "FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=14, jointName = "BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=15, jointName = "RightLeg_RightLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=16, jointName = "LeftLeg_LeftLowerLeg")

        # sensor_names = [0,1,2]
        # motor_names = [0,1] # or [3,4] step 23
        weight = 1
        a = -1
        b = 1
        for currentRow in range(c.numSensorNeurons): #0,1,2
            for currentColumn in range(c.numMotorNeurons): #0,1
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()



    def Mutate(self):
        row = rand.randint(0,c.numSensorNeurons)
        col = rand.randint(0, c.numMotorNeurons)

        self.weights[row,col] = rand.random() * 2 - 1

