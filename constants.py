import numpy as np
import random

num_iters = 5000
sleep_time = 1/500

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

#100

numberOfGenerations = 100
populationSize = 10

numMotorNeurons = random.randint(1,7)
maxLen = 0.5

motorJointRange = 1
force = 100