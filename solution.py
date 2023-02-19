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
        self.links_with_neurons = 0

        

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
        pyrosim.Send_Cube(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', name = "Torso", pos=[x,y,z] , size=[width, length, height])
        pyrosim.End()

    def Create_Body(self):

        green_code='    <color rgba="0 1.0 0.0 1.0"/>'
        green_name = '<material name="Green">'

        blue_code='    <color rgba="0 1.0 1.0 1.0"/>'
        blue_name = '<material name="Cyan">'

        # decide which ones will be sensor neurons now
        j = 0
        #neuron_list = []
        links_with_neurons = []

        for i in range(c.numMotorNeurons):
            if j == c.numSensorNeurons:
                break
            is_sensor = random.choice([True, False])
            if is_sensor == True:
                links_with_neurons.append(i)
                j+=1 
                #neuron_list.append(j)
        self.links_with_neurons = links_with_neurons
                
        length=0.5
        width=0.5
        height=0.5
        pyrosim.Start_URDF("body.urdf")

        # try to make mini worm

        # now do this for random number of randomly shaped links
        # initialize with the same block everytime
        pyrosim.Send_Cube(color_code=blue_code,color_name = blue_name, name = "0", pos=[0, 0, 0.25] , size=[length, width, height])
        pyrosim.Send_Joint( name = "0_1" , parent= "0" , child = "1" , type = "revolute", position = [0,0.25,0.25], jointAxis = '1 0 0')

        # iterate through the middle blocks
        i=1
        while i < c.numMotorNeurons:
            l = random.uniform(0,1)
            w = random.uniform(0,1)
            h = random.uniform(0,1)
            # if i == c.numMotorNeurons:
            #     print('here')
            #     pyrosim.Send_Cube(color_code = blue_code ,name = str(i), pos = [0,w/2,0], size = [l,w,h])
            #     break

            # color part
            if i in links_with_neurons:
                pyrosim.Send_Cube(color_code=green_code , color_name = green_name, name = str(i), pos = [0,w/2,0], size = [l,w,h])
            else:
                pyrosim.Send_Cube(color_code=blue_code ,color_name = blue_name, name = str(i), pos = [0,w/2,0], size = [l,w,h] )

            pyrosim.Send_Joint(name = str(i) +'_'+ str(i+1), parent = str(i), child = str(i+1), type = 'revolute', position = [0,w,0],jointAxis = '1 0 0')
            
            i += 1
    
        # the last block
        l = random.uniform(0,1)
        w = random.uniform(0,1)
        h = random.uniform(0,1)
        pyrosim.Send_Cube(color_code=blue_code, color_name = blue_name, name = str(c.numMotorNeurons), pos = [0,w/2,0], size = [l,w,h])

        pyrosim.End()


    def Create_Brain(self):

        def generate_pairs(numbers_list):
            pairs = []
            for i, num1 in enumerate(numbers_list):
                for j, num2 in enumerate(numbers_list[i+1:]):
                    pairs.append((num1, num2))
            return pairs

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        # make motor neurons
        for i in range(c.numMotorNeurons-1):
            pyrosim.Send_Motor_Neuron(name=i, jointName = str(i) +'_'+ str(i+1))
        

        # randomly place your sensors
        j = c.numMotorNeurons
        neuron_list = []
        links_with_neurons = []

        for i in range(c.numMotorNeurons):
            if j == c.numSensorNeurons:
                break
            is_sensor = random.choice([True, False])
            if is_sensor == True:
                j+=1 
                pyrosim.Send_Sensor_Neuron(name = j, linkName = str(i)) # j is sensor name, linkName is the link it correspond to
                neuron_list.append(j)
                links_with_neurons.append(i)

        
        pyrosim.End()



    def Mutate(self):
        row = rand.randint(0,c.numSensorNeurons-1)
        col = rand.randint(0, c.numMotorNeurons-1)

        self.weights[row,col] = rand.random() * 2 - 1


    


