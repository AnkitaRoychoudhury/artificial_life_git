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

        self.numMotors = 0
        self.numSensors = 0

        self.chosen_cubes = 0
        self.sensor_cubes = 0

        

    def Start_Simulation(self, directOrGUI):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
    
        
       # os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " &")

 


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
        pyrosim.Send_Cube(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', name = "Torso", pos=[x,y,z]
         , size=[width, length, height],)

        pyrosim.Send_Sphere(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', 
         name = "ball1", pos=[-3,-3,1]
         , size=[0.5],)


        pyrosim.End()

    def Create_Body(self):

        # define color codes
        green_code='    <color rgba="0 1.0 0.0 1.0"/>'
        green_name = '<material name="Green">'

        blue_code='    <color rgba="0 1.0 1.0 1.0"/>'
        blue_name = '<material name="Cyan">'
        
        


        # get random widths btwn 0.2 and 1
        a = 0.2
        b = 1

        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        #pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        
        pyrosim.Send_Cube(color_code = blue_code, color_name = blue_name, name = "Torso", pos=[1,0,1.5] , size=[4, 1, 1])

        pyrosim.Send_Joint(name = "Torso_Leg1" , parent= "Torso" , child = "Leg1" , type = "revolute", position = [0.5,0,1], jointAxis = '1 0 0')
        rand_len = (b-a) * random.random() + a
        pyrosim.Send_Cube(color_code = green_code, color_name = green_name,name = "Leg1", pos=[-0.5, 0, -0.5] , size=[rand_len, 1, 1])

        # random number of cubes
        all_cubes = ['Leg2', 'Leg3', 'Leg4', 'Leg5']
        n = random.randint(1,4)
        self.chosen_cubes = random.sample(all_cubes, n)
        self.sensor_cubes = ['Torso','Leg1']
        self.chosen_cubes.append('Torso')
        self.chosen_cubes.append('Leg1')

        if 'Leg2' in self.chosen_cubes:
            pyrosim.Send_Joint( name = "Torso_Leg2" , parent= "Torso" , child = "Leg2" , type = "revolute", position = [1.5, 0,1], jointAxis = '1 0 0')
            rand_len = (b-a) * random.random() + a

            is_sensor = random.choice([True, False])
            if is_sensor == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append("Leg2")
            else:
                color_code = blue_code
                color_name = blue_name


            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "Leg2", pos=[0.5, 0, -0.5] , size=[rand_len,1,1])

        if 'Leg3' in self.chosen_cubes:
            pyrosim.Send_Joint( name = "Torso_Leg3" , parent= "Torso" , child = "Leg3" , type = "revolute", position = [0.75, 0,1], jointAxis = '1 0 0')
            rand_len = (b-a) * random.random() + a

            is_sensor = random.choice([True, False])
            if is_sensor == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append("Leg3")
            else:
                color_code = blue_code
                color_name = blue_name

            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "Leg3", pos=[0, 0, -0.5] , size=[rand_len,1,1])

        if 'Leg4' in self.chosen_cubes:
            pyrosim.Send_Joint( name = "Torso_Leg4" , parent= "Torso" , child = "Leg4" , type = "revolute", position = [0, 0,1], jointAxis = '1 0 0')
            rand_len = (b-a) * random.random() + a

            is_sensor = random.choice([True, False])
            if is_sensor == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append("Leg4")
            else:
                color_code = blue_code
                color_name = blue_name


            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "Leg4", pos=[-1, 0, -0.5] , size=[rand_len,1,1])

        if 'Leg5' in self.chosen_cubes:
            pyrosim.Send_Joint( name = "Torso_Leg5" , parent= "Torso" , child = "Leg5" , type = "revolute", position = [2, 0,1], jointAxis = '1 0 0')
            rand_len = (b-a) * random.random() + a

            is_sensor = random.choice([True, False])
            if is_sensor == True:
                color_code = green_code
                color_name = green_name
                self.sensor_cubes.append("Leg5")
            else:
                color_code = blue_code
                color_name = blue_name

            pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = "Leg5", pos=[1, 0, -0.5] , size=[rand_len,1,1])

        self.numMotors = n + 2
        self.numSensors = len(self.sensor_cubes)

        self.weights = np.random.rand(self.numSensors, self.numMotors) * 2 - 1
        self.sensor_cubes = self.chosen_cubes

        #print(self.sensor_cubes, 'd', self.chosen_cubes)

        pyrosim.End()

    def Create_Brain(self):


        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # give leg1 a sensor
        #pyrosim.Send_Sensor_Neuron(name = 0, linkName = 'Leg1')

        # give first link motor
       # pyrosim.Send_Motor_Neuron(name = 0 + self.numSensors, jointName = 'Torso_Leg1')
        all_sensors = []
        all_motors = []
        
        for i,sensor in enumerate(self.sensor_cubes):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = sensor)
            all_sensors.append((i,sensor))

        self.chosen_cubes.remove('Torso')
        self.chosen_cubes.sort()
        for j, motor in enumerate(self.chosen_cubes):
            # if motor == 'Torso':
            #     pass
            # else:
            pyrosim.Send_Motor_Neuron(name = j + self.numSensors , jointName = 'Torso_' + motor)
            all_motors.append((j+self.numSensors, 'Torso_' + motor))

        #print('sm', all_sensors, all_motors)

        # all pairs of neurons must have synapses:
        for currentRow in range(self.numSensors):
            for currentColumn in range(self.numMotors):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + self.numSensors, weight = self.weights[currentRow][currentColumn])


        pyrosim.End()


        



    def Mutate(self):
      
        col = rand.randint(0,self.numMotors) - 1
        row = rand.randint(0,self.numSensors) - 1
        #print('nummo', self.numMotors, 'numse', self.numSensors,'row', row, 'col', col, 'weights', self.weights)
        self.weights[row][col] = rand.random() * 2 - 1


    


