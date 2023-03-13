# artificial_life_git
## Evolution and Environment

### Inspiration
Welcome to my evolution and environment github repository! In this branch (final), I explore the effect of the environment on evolution of simulated creatures. Imagine a world with only water, or only snow, or pebbles everywhere – would the evolved creatures walking the planet look anything like what we see today?

![Alt text](images/img0.png?raw=true "Image 0")

I was curious to study how morphologies and fitness may change as a function of evolution in a pebble world versus a flat world. My two hypotheses: (1) morphologies in pebble world may have less legs than one in a flat world because the main mechanism of travel would be rolling instead of walking with legs and, (2) creatures in pebble world would travel farther than in a flat world because they will be able to move by rolling on the pebbles.

### Body, Brain, and Selection

In order to test this, I’ve simulated evolution in silico. I instantiate a random morphology with certain constraints. The 3D creature always starts with a torso of size (4,1,1).

![Alt text](images/img1_8.png?raw=true "Image 1_8")

It has a random number (between 1 and 5) of legs with a random number of sensors (between 1 and # of legs) for each torso. It is important to have the bodies, so we can test the effect of legs on fitness in varying world environments. Legs are programmed such that they will not go through the ground or intersect. Their widths are chosen by selecting a random value between 0.2 and 1. The possible options for legs are:

![Alt text](images/img2_8.png?raw=true "Image 2_8")

Some of the legs will have sensors. These sensors allow me to detect how far the creature has travelled from the starting point. The legs that have sensors are randomly chosen and are colored green. I always guarantee that there is at least one leg with a sensor. An example of a potential morphology is shown below:

![Alt text](images/img3_8.png?raw=true "Image 3_8")

The genotype to phenotype map of this creature is shown below:

![Alt text](images/img4.png?raw=true "Image 4")

Next, we give the creature a brain. The brain is created by sending sensor neurons to only the legs that have sensors. Every leg receives a motor neuron to help it move. Every pair of motor and sensors will receive a synapse that allows us to read in the function of the motor and change the weight, thereby changing the movement. This is where evolution happens. For each generation, I will change the weights of a synapse randomly which will affect the motor function of the morphology. 

![Alt text](images/img4_8.png?raw=true "Image 4_8")

Selection for evolution was performed using a parallel hill climber algorithm. This is an algorithm by which we can compare the fitness of each parent to its child, and we only allow the one creature with the higher fitness to continue to survive and create offspring. We can have multiple parent-child competitions occurring at the same time, thereby the name ‘parallel.’ It is a hill climber because we are locally searching for the optimal fitness value by making small changes at each step.

### Testing

I tested this hypothesis by performing evolution for a number of generations and population size in a flat environment and in a pebble environment. The flat environment evolution represented my control experiments. The code necessary to change this in located in solution.py. There, in Create_World(), I determine whether the world has pebbles. The difference is represented in the schematic below:

![Alt text](images/img5.png?raw=true "Image 5")

Specifically, I performed evolution 5 times for a population size of 10. Each run had 250-500 generations. For the pebble world, I also performed evolution 5 times for a population size of 10. Each run had 100-270 generations. At the end of each generation, I calculate and save the best fitness value of the entire population. 

Unfortunately, I was not able to simulate 500 generations for the pebble world because generating a world with pebbles took a long time. I ran the pebble simulation overnight and was able to get data for only 250 generations. 

### Results

Fitness of a creature was measured by determining how far from the starting point it travelled. A creature that travelled farther was deemed ‘more fit’ than one that did not.

Interestingly, I found that creatures in the pebble world did not go farther than creatures in the flat world. Instead, the pebbles were a hindrance rather than a benefit. They functioned to block the creature instead of causing it to move. As we can see in the fitness plot below, the simulations from the flat world had higher fitness values at the last generation than the simulations in the pebble world.

![Alt text](images/fitness_plots.png?raw=true "fitness plots")

I noticed that the successful creatures that moved the farthest in the pebble world did indeed have fewer legs than the best creatures in the flat world, as shown below. This may be because legs don’t necessarily help in the pebble world, they only function to impede movement.

Flat world creature with 4 legs:
![Alt text](images/img7_b.png?raw=true "Image 7_b")

Pebble world creature with 2 legs:
![Alt text](images/img7_a.png?raw=true "Image 7_a")

If we look at the fitness curves plotted above, there was one simulation for the pebble world that I was able to run until generation 500. In this run, we see that the evolution got stuck around generation 50. After that, it was not able to improve. I believe this occurred because changing the motor weights was not enough to overcome the hurdles the pebbles posed. Instead, I may need to include the option for changing morphologies as evolution proceeds to see if the protrusion of new limbs will help the creature travel farther. 

The robots lacked many features. During evolution, they did not have the option to change their morphologies. The only degree of freedom was changing the motor weights. Perhaps allowing for spherical body shapes would have also allowed for more interesting dynamics. Due to lack of computational power, I was also not able to evolve the creatures in the pebble world for a long time. It would be interesting to determine if the creatures defined above could overcome hurdles given more evolutionary time.

### Additional Analysis
During the above experiments, I noticed that the size and location of the pebbles mattered significantly. For example, when there were more spheres in the middle, the robot had to push against the spheres more to move it out of the way, and they did not move as far. A setup is shown below:

![Alt text](images/img8.png?raw=true "Image 8")

Also, when the spheres were bigger, the robot was launched into the air immediately.

![Alt text](images/img9.png?raw=true "Image 9")

### Discussion

Given more time, I would generate a creature that did not have such a constrained body plan. It would also be interesting to see what would happen if mutations were defined as a change in the body plan and motor weights. To continue, I would run the simulation for longer with more generations and higher population size. It would also be interesting to note the effect of pebble size on creature morphology and fitness. 

## Recreate
You can run this code by cloning this branch (final) and running 'python search.py' in your command line. For now, the setting is such that there will be a population of 2 and 1 generation. You can change these values in constants.py.
![Alt text](images/img4_8.png?raw=true "Image 3")

## Citation
This is material from a course taught at Northwestern University (ChE 396 Winter 2022) by Professor Sam Kriegman and TA Donna Hooshmand. Material from ludobots by Dr. Josh Bongard (www.reddit.com/r/ludobots) is used. Pyrosim, a python package for simulation, is also used to display the morphologies and movements.
