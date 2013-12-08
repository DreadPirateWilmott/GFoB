import os
import random
#Manage the dwarves

def createFiles(nList):
	path = os.getcwd()
	d = path + "/dwarves"
	if not os.path.exists(d): #If dwarves does not exsist create it
		os.makedirs(d)
	#end if
	newpath = path + "/dwarves"
	os.chdir(newpath)
	
	
	#Make a file for each of the five dwarves
	for i in range(1, 6): #Five dwarves
		file = open("dwarf%s.txt" % (i), "w")
		
		#Get all the necessary information
		tempI = i - 1
		name = str(nList[tempI])
		historyOfMentalIllness = random.randint(1, 8) #1 in 8 chance that they have mental illness in the family
		if historyOfMentalIllness == 1:
			historyOfMentalIllness = True
		else:
			historyOfMentalIllness = False
		#end if
		ownedEntities = [] #Axe, pickaxe, net
		
		file.write(name + "\n")
		file.write(str(historyOfMentalIllness) + "\n")
		
		entities = ", ".join(ownedEntities)
		file.write(entities)
		
		file.close()
	#end for
