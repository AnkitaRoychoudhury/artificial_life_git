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
    
        
        os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        #os.system('python3 simulate2.py ' + directOrGUI + " " + str(self.myID) + " &")

 


    def Wait_For_Simulation_To_End(self):

        fitnessFileName = 'fitness'+str(self.myID)+'.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(1)

        f = open(fitnessFileName, "r")
        try:
            self.fitness = float(f.readlines()[0])
        except:
            print('exception occured')
            self.fitness = 0

        f.close()
        os.system('rm ' + fitnessFileName)


    def Set_ID(self, val): 
        self.myID = val

   

    def Create_World(self):
        length=0.3
        width=0.3
        height=0.3

        x=3
        y=3
        z=0.5

        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', name = "Torso", pos=[x,y,z]
         , size=[length,width,height],)

        sphere_size = 0.2
        # pyrosim.Send_Sphere(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', 
        #  name = "ball1", pos=[-3,-3,1]
        #  , size=[sphere_size],)


        for i in range(7):
            for j in range(7):
                i = i+1 
                j = j+1
                pyrosim.Send_Sphere(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', 
                    name = "ball1", pos=[-i,-j,1]
                    , size=[sphere_size],)

                pyrosim.Send_Sphere(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', 
                    name = "ball1", pos=[i,j,1]
                    , size=[sphere_size],)

                pyrosim.Send_Sphere(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', 
                    name = "ball1", pos=[i,-j,1]
                    , size=[sphere_size],)

                pyrosim.Send_Sphere(color_code ='<color rgba="0 1.0 1.0 1.0"/>',color_name = '<material name="Cyan">', 
                    name = "ball1", pos=[-i,j,1]
                    , size=[sphere_size],)


        pyrosim.End()

    def Create_Body(self):

        # define color codes
        green_code='    <color rgba="0 1.0 0.0 1.0"/>'
        green_name = '<material name="Green">'

        blue_code='    <color rgba="0 1.0 1.0 1.0"/>'
        blue_name = '<material name="Cyan">'
        
        pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")

        self.sensor_cubes = []
        self.chosen_cubes = []
        self.joint_names = []
        # get random widths btwn 0.2 and 1
        a = 0.2
        b = 1

        # get number of torsos
        #numTorso = random.randint(1,8)
        numTorso = 1
        for n_torso in range(numTorso):
        
            curr_torso_name = 'Torso'+str(n_torso)
            
            # define first torso and joint
            if n_torso == 0:
                pyrosim.Send_Cube(color_code = blue_code, color_name = blue_name, name='Torso0', pos=[1+(4*0), 0, 1.5] , size=[4, 1, 1])
                pyrosim.Send_Joint(name = curr_torso_name+"_"+curr_torso_name+"Leg1", parent = curr_torso_name, child = curr_torso_name+"Leg1", type = 'revolute', position = [0.5,0,1], jointAxis = '1 0 0')
                self.joint_names.append(curr_torso_name+"_"+curr_torso_name+"Leg1")
            else:
                # connect the torsos
                pyrosim.Send_Joint(name = curr_torso_name + '_' + 'Torso'+str(n_torso-1), parent = curr_torso_name, child = 'Torso'+str(n_torso-1), type = 'revolute', position = [0,4,0], jointAxis = '1 0 0')
                # send first torso
                pyrosim.Send_Cube(color_code = blue_code, color_name = blue_name, name = curr_torso_name, pos=[2,2, 0], size =[4,1,1])
                # connect torso to leg
                pyrosim.Send_Joint(name = curr_torso_name+"_"+curr_torso_name+"Leg1", parent = curr_torso_name, child = curr_torso_name+"Leg1", type= 'revolute', position = [0.5,0,1], jointAxis = '1 0 0')
                self.joint_names.append(curr_torso_name+"_"+curr_torso_name+"Leg1")
                
            # define first leg (relative)
            rand_len = (b-a) * random.random() + a
            #name = Torso0Leg1
            pyrosim.Send_Cube(color_code = green_code, color_name = green_name, name = curr_torso_name+'Leg1', pos = [-0.5 + (4*n_torso), 0, -0.5], size = [rand_len, 1, 1])

            # choose random number of cubes for the current torso
            all_cubes = [curr_torso_name+'Leg2', curr_torso_name+'Leg3', curr_torso_name+'Leg4', curr_torso_name+'Leg5']
            n_legs = random.randint(1,4)
            curr_chosen_cubes = random.sample(all_cubes, n_legs)
            for c in curr_chosen_cubes:
                self.chosen_cubes.append(c)

            self.sensor_cubes.append(curr_torso_name)
            self.sensor_cubes.append(curr_torso_name+"Leg1")
            self.chosen_cubes.append(curr_torso_name)
            self.chosen_cubes.append(curr_torso_name+"Leg1")

            if curr_torso_name+'Leg2' in curr_chosen_cubes:
                pyrosim.Send_Joint( name = curr_torso_name+"_"+curr_torso_name+"Leg2" , parent= curr_torso_name , child = curr_torso_name+"Leg2" , type = "revolute", position = [1.5, 0,1], jointAxis = '1 0 0')
                self.joint_names.append(curr_torso_name+"_"+curr_torso_name+"Leg2")
                rand_len = (b-a) * random.random() + a

                is_sensor = random.choice([True, False])
                if is_sensor == True:
                    color_code = green_code
                    color_name = green_name
                    self.sensor_cubes.append(curr_torso_name+"Leg2")
                else:
                    color_code = blue_code
                    color_name = blue_name

                pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = curr_torso_name+"Leg2", pos=[0.5, 0, -0.5] , size=[rand_len,1,1])


            if curr_torso_name+"Leg3" in curr_chosen_cubes:
                pyrosim.Send_Joint( name = curr_torso_name+"_"+curr_torso_name+"Leg3"  , parent= curr_torso_name , child = curr_torso_name+"Leg3" , type = "revolute", position = [0.75, 0,1], jointAxis = '1 0 0')
                self.joint_names.append(curr_torso_name+"_"+curr_torso_name+"Leg3")
                rand_len = (b-a) * random.random() + a

                is_sensor = random.choice([True, False])
                if is_sensor == True:
                    color_code = green_code
                    color_name = green_name
                    self.sensor_cubes.append(curr_torso_name+"Leg3")
                else:
                    color_code = blue_code
                    color_name = blue_name

                pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = curr_torso_name+"Leg3", pos=[0, 0, -0.5] , size=[rand_len,1,1])


            if curr_torso_name+'Leg4' in curr_chosen_cubes:
                pyrosim.Send_Joint( name = curr_torso_name+"_"+curr_torso_name+"Leg4" , parent= curr_torso_name , child = curr_torso_name+"Leg4" , type = "revolute", position = [0, 0,1], jointAxis = '1 0 0')
                self.joint_names.append(curr_torso_name+"_"+curr_torso_name+"Leg4")
                rand_len = (b-a) * random.random() + a

                is_sensor = random.choice([True, False])
                if is_sensor == True:
                    color_code = green_code
                    color_name = green_name
                    self.sensor_cubes.append(curr_torso_name+"Leg4")
                else:
                    color_code = blue_code
                    color_name = blue_name
                pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = curr_torso_name+"Leg4", pos=[-1, 0, -0.5] , size=[rand_len,1,1])


            if curr_torso_name+'Leg5' in curr_chosen_cubes:
                self.joint_names.append(curr_torso_name+"_"+curr_torso_name+"Leg5")
                pyrosim.Send_Joint( name = curr_torso_name+"_"+curr_torso_name+"Leg5" , parent= curr_torso_name, child = curr_torso_name+"Leg5" , type = "revolute", position = [2, 0,1], jointAxis = '1 0 0')
                rand_len = (b-a) * random.random() + a

                is_sensor = random.choice([True, False])
                if is_sensor == True:
                    color_code = green_code
                    color_name = green_name
                    self.sensor_cubes.append(curr_torso_name+"Leg5")
                else:
                    color_code = blue_code
                    color_name = blue_name

                pyrosim.Send_Cube(color_code = color_code, color_name = color_name,name = curr_torso_name+"Leg5", pos=[1, 0, -0.5] , size=[rand_len,1,1])

            #self.chosen_cubes.append(curr_chosen_cubes)
            #self.sensor_cubes.append(curr_sensor_cubes)


        self.numMotors = n_legs + 2
        self.numSensors = len(self.sensor_cubes)

        self.weights = np.random.rand(self.numSensors, self.numMotors) * 2 - 1
        #self.sensor_cubes = self.chosen_cubes


        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # give leg1 a sensor
        #pyrosim.Send_Sensor_Neuron(name = 0, linkName = 'Leg1')

        # give first link motor
       # pyrosim.Send_Motor_Neuron(name = 0 + self.numSensors, jointName = 'Torso_Leg1')
        #all_sensors = []
        #all_motors = []
        for i,sensor in enumerate(self.sensor_cubes):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = sensor)
            #all_sensors.append((i,sensor))

        #self.chosen_cubes.remove('Torso')
        #chosen_cubes_2 = [x for x in self.chosen_cubes if not x.startswith("Torso")]
        #chosen_cubes_2.sort()
        for j, curr_joint in enumerate(self.joint_names):
            # if motor == 'Torso':
            #     pass
            # else:
            pyrosim.Send_Motor_Neuron(name = j + self.numSensors , jointName = curr_joint)
            #all_motors.append((j+self.numSensors, 'Torso_' + motor))


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


    


