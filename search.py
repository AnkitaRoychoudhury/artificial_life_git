import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
for i in range(7):
    #phc.Show_Best()
    phc.Evolve()
    phc.Show_Best()

#os.system('python3 hillclimber.py')
# os.system('python3 simulate2.py')

# for i in range(5):
#     os.system('python3 generate.py')
#     os.system('python3 simulate2.py')
