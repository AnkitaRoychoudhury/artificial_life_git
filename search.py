import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np

np.random.seed(40)

phc = PARALLEL_HILL_CLIMBER()
for i in [2,3,4]:
    #i = 4
        #phc.Show_Best()
    phc.Evolve(i)
    phc.Show_Best()

#os.system('python3 hillclimber.py')
# os.system('python3 simulate2.py')

# for i in range(5):
#     os.system('python3 generate.py')
#     os.system('python3 simulate2.py')
