import numpy as np
import random

num_iters = 10
sleep_time = 1/10000

amplitude_BackLeg = np.pi/4
frequency_BackLeg = 10
phaseOffset_BackLeg = -np.pi/4

amplitude_FrontLeg = np.pi/4
frequency_FrontLeg = 10
phaseOffset_FrontLeg = np.pi/4

# target position
a = -np.pi/2
b = np.pi/2
targPos = (b-a) * random.random() + a
#targPos = random.uniform(a,b)
force = 1
#100

numberOfGenerations = 8
populationSize = 3

numSensorNeurons = 3
#random.randint(1,5)
#numMotorNeurons = 3
numMotorNeurons = random.randint(1,7)
numSensorNeurons = random.randint(1,numMotorNeurons)
maxLen = 0.5

motorJointRange = 1