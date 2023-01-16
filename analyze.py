import numpy as np
import matplotlib.pyplot as mp 

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
#print(backLegSensorValues)


mp.plot(backLegSensorValues, label = 'back leg', linewidth=4)
mp.plot(frontLegSensorValues, label = 'front leg')
mp.legend()
mp.show()