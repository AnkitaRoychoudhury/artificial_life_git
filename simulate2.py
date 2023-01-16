import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

num_iters = 1000

amplitude_BackLeg = np.pi/4
frequency_BackLeg = 10
phaseOffset_BackLeg = -np.pi/4

amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 10
phaseOffset_FrontLeg = np.pi/4

# motor command vector
angle_range = np.linspace(0, 2*np.pi, num_iters)
targetAngles_BackLeg = amplitude_BackLeg * np.sin(frequency_BackLeg * angle_range + phaseOffset_BackLeg)
targetAngles_FrontLeg = amplitude_FrontLeg * np.sin(frequency_FrontLeg * angle_range + phaseOffset_FrontLeg)
#np.save('data/targetAngles_BackLeg.npy', targetAngles_BackLeg)
#np.save('data/targetAngles_FrontLeg.npy', targetAngles_FrontLeg)


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(num_iters)
frontLegSensorValues = np.zeros(num_iters)

# target position
a = -np.pi/2
b = np.pi/2
targPos = (b-a) * random.random() + a
#targPos = random.uniform(a,b)
force = 100


for i in range(num_iters):
	p.stepSimulation()

	#backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#print(backLegTouch)

	#a = -np.pi/2
	#b = np.pi/2
	#targPos = (b-a) * random.random() + a	
	#targetAngles2 = amplitude * np.sin(frequency * targetAngles[i] + phaseOffset)	
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_BackLeg", 
	controlMode = p.POSITION_CONTROL,targetPosition = targetAngles_BackLeg[i] ,maxForce = force)

	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_FrontLeg", 
	controlMode = p.POSITION_CONTROL,targetPosition = targetAngles_FrontLeg[i] ,maxForce = force)

	time.sleep(1/240)
	#print(i)

print(backLegSensorValues)
np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)
p.disconnect()
