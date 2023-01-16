#generate from manylinks
import pyrosim.pyrosim as pyrosim


def Create_World():
	length=1
	width=1
	height=1

	x=3
	y=3
	z=0.5

	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name = "Torso", pos=[x,y,z] , size=[width, length, height])
	pyrosim.End()


def Create_Robot():
    length=1
    width=1
    height=1
    pyrosim.Start_URDF("body.urdf")
    
    pyrosim.Send_Cube(name = "Torso", pos=[1, 0, 1.5] , size=[width, length, height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, 0, 1.0])
    pyrosim.Send_Cube(name = "BackLeg", pos=[-0.5,0,-0.5] , size=[width, length, height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1.5,0,1])
    pyrosim.Send_Cube(name = "FrontLeg", pos=[0.5, 0, -0.5] , size=[width, length, height])
    pyrosim.End()
	# pyrosim.Send_Cube(name = "BackLeg", pos=[0.5,0,0.5] , size=[width, length, height])

	# pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [1, 0, 1.0])


	# pyrosim.Send_Cube(name = "Torso", pos=[0.5, 0, 0.5] , size=[width, length, height])

	# pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])

	# pyrosim.Send_Cube(name = "FrontLeg", pos=[0.5, 0, -0.5] , size=[width, length, height])

# try with no torso as root
   
    






Create_World()
Create_Robot()








#for i in range(10):
#	if i==0:
#		pyrosim.Send_Cube(name = "Box" + str(i), pos=[0,0,0.5+i] , size=[1, 1, 1])

#	else:
#		pyrosim.Send_Cube(name = "Box" + str(i), pos=[0,0,0.5+i] , size=[0.9**i, 0.9**i, #0.9**i])
	

