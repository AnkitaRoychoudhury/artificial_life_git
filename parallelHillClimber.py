from solution import SOLUTION
import constants as c
import numpy as np
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        if os.path.exists('brain*.nndf'):
            os.remove('brain*.nndf')
        if os.path.exists("fitness*.txt"):
            os.remove("fitness*.txt")
        
        
        #os.system('rm fitness*.txt')

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            


        #self.child = SOLUTION()
        


    def Evolve(self):

        self.Evaluate(self.parents)   

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}

        for i,key in enumerate(self.parents):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    
    def Mutate(self):
        for i,key in enumerate(self.children):
            self.children[i].Mutate()
  
    def Evaluate(self, solutions):

        for i,key in enumerate(solutions):
            solutions[i].Start_Simulation("DIRECT")

        for i,key in enumerate(solutions):
            solutions[i].Wait_For_Simulation_To_End()
        

    def Select(self):
        for i,key in enumerate(self.parents):
            if self.parents[i].fitness < self.children[i].fitness: # original >
                self.parents[i] = self.children[i]

    def Print(self):
        for i,key in enumerate(self.parents):
            print('\n', self.parents[i].fitness, self.children[i].fitness,'\n')


    def Show_Best_1(self):
        first_parent = self.parents[0]
        first_parent.Start_Simulation("GUI")

    def Show_Best(self):
  
        
        # best fitness is 0 distance from origin
        best_fitness_dist = 10
        origin = 1

        print(self.parents[0])
        for i,key in enumerate(self.parents):
            curr_fitness = self.parents[i].fitness
            # get distance from world element
            curr_fitness_distance = np.abs(curr_fitness - origin)
            if curr_fitness_distance < best_fitness_dist: # original <
                best_parent_ind = i

        best_parent = self.parents[best_parent_ind]
        best_parent.Start_Simulation("GUI")


        #pass
       #self.parent.Evaluate("GUI")



