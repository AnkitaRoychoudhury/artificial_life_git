import numpy as np
import numpy.random as rand
import random
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        
        self.weights = 0
        self.myID = nextAvailableID
        self.links_with_neurons = 0
        self.numSensorNeurons = 0

        

    def Start_Simulation(self, directOrGUI):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
    
        
        os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " 2&>1 &")
       # os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " &")

 


    def Wait_For_Simulation_To_End(self):

        fitnessFileName = 'fitness'+str(self.myID)+'.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(1)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.readlines()[0])

        f.close()
        os.system('rm ' + fitnessFileName)


    def Set_ID(self, val): 
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
        links_with_neurons = []


        for i in range(c.numMotorNeurons):
            is_sensor = random.choice([True, False])
            if is_sensor == True:
                links_with_neurons.append(i)
                j+=1 

        if len(links_with_neurons) == 0:
            links_with_neurons.append(0)
        


        self.links_with_neurons = links_with_neurons
        self.numSensorNeurons = len(links_with_neurons)
        self.weights = np.random.rand(self.numSensorNeurons, c.numMotorNeurons) * 2 - 1
                
        length=0.25
        width=0.25
        height=0.25
        pyrosim.Start_URDF("body.urdf")


        # now do this for random number of randomly shaped links
        # initialize with the same block everytime
        pyrosim.Send_Cube(color_code=blue_code,color_name = blue_name, name = "0", pos=[0, 0, 0.25] , size=[length, width, height])
        pyrosim.Send_Joint( name = "0_1" , parent= "0" , child = "1" , type = "revolute", position = [0,0.25,0.25], jointAxis = '1 0 0')

        # iterate through the middle blocks
        i=1

        while i < c.numMotorNeurons:
            l = random.uniform(0.2,c.maxLen)
            w = random.uniform(0.2,c.maxLen)
            h = random.uniform(0.2,c.maxLen)
            side = random.choice([1,2,3,4])

            # color part
            if i in links_with_neurons:
                color_code = green_code
                color_name = green_name
            else:
                color_code = blue_code
                color_name = blue_name

            # pick a side
            if side == 1:
                posn_cube = [0, -w/2, 0]
                posn_joint = [0,-w,0]
                
            elif side == 2:
                posn_cube = [0, 0, w/2]
                posn_joint = [0,0,w]

            elif side == 3:
                posn_cube = [0, w/2, 0]
                posn_joint = [0,w,0]
            
            elif side == 4:
                posn_cube = [0, -w/2, 0]
                posn_joint = [0,-w,0]

            # determine if block is hitting other blocks 


            pyrosim.Send_Cube(color_code = color_code, color_name = color_name, name = str(i), pos = posn_cube, size = [l,w,h])

            i += 1

         # the last block
        l = random.uniform(0,1)
        w = random.uniform(0,1)
        h = random.uniform(0,1)
        pyrosim.Send_Cube(color_code=blue_code, color_name = blue_name, name = str(c.numMotorNeurons), pos = [0,w/2,0], size = [l,w,h])


        # send all cubes then all joints
        i = 1
        while i < c.numMotorNeurons:
            pyrosim.Send_Joint(name = str(i) +'_'+ str(i+1), parent = str(i), child = str(i+1), type = 'revolute', position = posn_joint,jointAxis = '1 0 0')
            
            i += 1
    
       
        pyrosim.End()


    def Create_Brain(self):

        def generate_pairs(numbers_list):
            pairs = []
            for i, num1 in enumerate(numbers_list):
                for j, num2 in enumerate(numbers_list[i+1:]):
                    pairs.append((num1, num2))
            return pairs

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # make motor neurons - will have name 0 to #motor neurons - 1
        motor_names = []
        for i in range(c.numMotorNeurons):
            motor_names.append(i)
            pyrosim.Send_Motor_Neuron(name=i, jointName = str(i) +'_'+ str(i+1))
        
        # make sensor neurons - will have name #motor neurons to # motor neurons + sensor neurons
        j = c.numMotorNeurons
        links_with_neurons = self.links_with_neurons

        for link in links_with_neurons:
            name = j + link
            pyrosim.Send_Sensor_Neuron(name = name, linkName = str(link))

        # send synapses
        weight = 1
        a = -1
        b = 1
   
        # all pairs of neurons must have synapses:
        for currentRow, a in enumerate(links_with_neurons):
            for currentColumn, b in enumerate(motor_names):
                pyrosim.Send_Synapse(sourceNeuronName = a + c.numMotorNeurons, targetNeuronName = b, weight = self.weights[currentRow][currentColumn])

        #try to hard code to check if this fixes

        #pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName )

        #print('NEURONS',self.links_with_neurons)
        # pyrosim.Send_Sensor_Neuron(name=0, linkName = "0")

        # sensor_names = [0,1,2]
        # motor_names = [0,1] # or [3,4] step 23
        # weight = 1
        # a = -1
        # b = 1
        # print('w',self.weights)
        # print('n',neuron_list)
        # all pairs of neurons must have synapses : SKIP FOR NOW:( 
        # if len(neuron_list)>1:
        #     pairs_list = generate_pairs(neuron_list)

        #     for i,pair in enumerate(pairs_list):
        #         a = pair[0]
        #         b = pair[1]
        #         pyrosim.Send_Synapse(sourceNeuronName = a, targetNeuronName = b, weight = self.weights[a][b])

        # for k,currentRow in enumerate(neuron_list): #from random numbers above
        #     for currentColumn in range(c.numMotorNeurons): #0,1
        #         pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numMotorNeurons, weight = self.weights[k][currentColumn])
        
        pyrosim.End()



    def Mutate(self):
        # change function to add
        # row = rand.randint(0,self.numSensorNeurons-1)
        row = rand.randint(0,self.numSensorNeurons)
        col = rand.randint(0, c.numMotorNeurons)
        #col = rand.randint(0, c.numMotorNeurons-1)
        

        self.weights[row,col] = rand.random() * 2 - 1


    


