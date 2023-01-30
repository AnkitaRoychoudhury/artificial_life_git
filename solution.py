import numpy as np
import numpy.random as rand
import pyrosim.pyrosim as pyrosim
import os
import time


class SOLUTION:

    def __init__(self, nextAvailableID):
        
        self.weights = np.random.rand(3,2) * 2 -1
        self.myID = nextAvailableID
        

    def Start_Simulation(self, directOrGUI):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " &")


    def Wait_For_Simulation_To_End(self):

        fitnessFileName = 'fitness'+str(self.myID)+'.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        print('filename',fitnessFileName)
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
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name = "Torso", pos=[1, 0, 1.5] , size=[width, length, height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, 0, 1.0])
        pyrosim.Send_Cube(name = "BackLeg", pos=[-0.5,0,-0.5] , size=[width, length, height])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1.5,0,1])
        pyrosim.Send_Cube(name = "FrontLeg", pos=[0.5, 0, -0.5] , size=[width, length, height])

        pyrosim.End()


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName = "Torso_BackLeg"),
        pyrosim.Send_Motor_Neuron(name=4, jointName = "Torso_FrontLeg")

        sensor_names = [0,1,2]
        motor_names = [0,1] # or [3,4] step 23
        weight = 1
        a = -1
        b = 1
        for currentRow in sensor_names:
            for currentColumn in motor_names:
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        row = rand.randint(0,2)
        col = rand.randint(0,1)

        self.weights[row,col] = rand.random() * 2 - 1

