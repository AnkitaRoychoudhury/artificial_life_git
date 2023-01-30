import os
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.Show_Best()
hc.Evolve()
hc.Show_Best()

#os.system('python3 hillclimber.py')
# os.system('python3 simulate2.py')

# for i in range(5):
#     os.system('python3 generate.py')
#     os.system('python3 simulate2.py')
