import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

num_iters = 10000
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")


pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(num_iters)
frontLegSensorValues = np.zeros(num_iters)

a = -np.pi/2
b = np.pi/2
targPos = (b-a) * random.random() + a
#targPos = random.uniform(a,b)
force = 150

for i in range(num_iters):
	p.stepSimulation()

	#backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#print(backLegTouch)

	a = -np.pi/2
	b = np.pi/2
	targPos = (b-a) * random.random() + a		
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_BackLeg", 
	controlMode = p.POSITION_CONTROL,targetPosition = -targPos ,maxForce = force)

	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_FrontLeg", 
	controlMode = p.POSITION_CONTROL,targetPosition = targPos ,maxForce = force)

	time.sleep(1/30)
	#print(i)

print(backLegSensorValues)
np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)
p.disconnect()
