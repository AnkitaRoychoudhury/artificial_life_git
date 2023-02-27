# artificial_life_git
## Assignment 8
In branch a8, I create a 3D morphology that has a random number (between 1 and 5) of legs with a random number of sensors (between 1 and # of legs) in a chain. Links will not go through the ground or intersect. Link length, width, and height are chosen by selecting a random float between 0.2 and 1. The first link is always a box of size (5,1,1). Sensors are randomly selected and the links with sensors are colored green. Links without sensors are blue.

The body will always start with a torso:

![Alt text](img1_8.png?raw=true "Image 1")

There are 5 potential options for legs:

![Alt text](img2_8.png?raw=true "Image 2")

A random number, n, between 1 and 5 is chosen. Then, n randomly selected legs are chosen to be included in the body plan. Each leg will have a random width between 0.2 and 1. Each leg will be randomly selected to have a sensor and it is guaranteed that there is at least one sensor. 

An example of a morphology is:

![Alt text](img3_8.png?raw=true "Image 3")

The brain is created by sending sensor neurons to only those links that are chosen to have sensors. Every link receives a motor neuron. Every pair of motor and sensors will receive a synapse.

## Recreate
You can run this code by cloning branch a8 and running 'python search.py' in your command line.


## Citation
This is material from a course taught at Northwestern University (ChE 396 Winter 2022) by Professor Sam Kriegman and TA Donna Hooshmand. Material from ludobots by Dr. Josh Bongard (www.reddit.com/r/ludobots) is used. Pyrosim, a python package for simulation, is also used to display the morphologies and movements.
