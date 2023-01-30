import numpy as np
import random

num_iters = 2000
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
force = 100

numberOfGenerations = 1
populationSize = 1

numSensorNeurons = 9
numMotorNeurons = 8