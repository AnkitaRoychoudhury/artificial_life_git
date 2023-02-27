import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np

np.random.seed(1)

phc = PARALLEL_HILL_CLIMBER()
for i in range(1):
    #phc.Show_Best()
    phc.Evolve()
    print('here')
    phc.Show_Best()

#os.system('python3 hillclimber.py')
# os.system('python3 simulate2.py')

# for i in range(5):
#     os.system('python3 generate.py')
#     os.system('python3 simulate2.py')
