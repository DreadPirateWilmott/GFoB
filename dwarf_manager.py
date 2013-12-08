import os
import random
#Manage the dwarves

def createFiles(nList):
	path = os.getcwd()
	newpath = path + "\\essentials"
	os.chdir(newpath)
	
	
	#Make a file for each of the five dwarves
	for i in range(1, 6): #Five dwarves
		#Get all the necessary information
		tempI = i - 1
		name = str(nList[tempI])
		historyOfMentalIllness = random.randint(1, 8) #1 in 8 chance that they have mental illness in the family
		
		#Write the starting position of each dwarf
		file = open("wagonspace.txt", "r")
		fileContents = file.read()
		wagonSpace = fileContents.split(", ")
		
		#The first five spaces have dwarves on them
		compile = wagonSpace[tempI] #Line 16 - tempI
		compile = compile.split(".") #Splitting the compiled position back into a list
		
		dwarfX = compile[0]
		dwarfY = compile[2] #Compile 1 is the Z and we don't need that
		dwarfZ = 22
		
		recompile = "%s.%s.%s" % (dwarfX, dwarfZ, dwarfY)
		file.close()
		#Possible base emotions = angry, grumpy, sad, happy
		baseEmotion = random.randint(0, 15)
		if baseEmotion >= 0 and baseEmotion <= 1:
			baseEmotion = "angry"
		elif baseEmotion >= 2 and baseEmotion <= 3:
			baseEmotion = "grumpy"
		elif baseEmotion >= 3 and baseEmotion <= 4:
			baseEmotion = "sad"
		else:
			baseEmotion = "happy"
		#end if
		
		if historyOfMentalIllness == 1:
			historyOfMentalIllness = True
		else:
			historyOfMentalIllness = False
		#end if
		ownedEntities = [] #Axe, pickaxe, net
		
		file = open("dwarf%s.txt" % (i), "w")
		file.write(name + "\n")
		file.write(str(historyOfMentalIllness) + "\n")
		file.write(baseEmotion + "\n")
		file.write(str(recompile) + "\n")
		entities = ", ".join(ownedEntities)
		file.write(entities)
		
		file.close()
	#end for
	
	os.chdir(path)
def Manage():
	#Manage the dwarves
	print "WIP"