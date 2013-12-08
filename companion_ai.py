"""The companion AI is one of the more complex pieces of code to be written for this game.
the AI needs to run once for each dwarf each turn and it needs to decide based on mood and dwarf
characteristics whether or not it is going to do its designated job, whether it is going to go crazy,
or whether it is going to sit around and stuff it's face all day (there will be more things they will
do I am just trying to get my point across."""

import glob
import os

def priority():
	path = os.getcwd()
	newpath = path + "\\dwarves"
	
	os.chdir(newpath)
	
	files = glob.glob("*.txt")
	numOfLoops = len(files) - 1
	
	for i in range(0, numOfLoops):
		tempI = i + 1
		file = open("dwarf%s.txt" % (tempI), "r")
		fileContents = file.read()
		fileContents = fileContents.split("\n")
		
		dwarf = str(fileContents[0])
		mentalIllness = str(fileContents[1])
		emotion = str(fileContents[2])
		inventory = str(fileContents[3])
		
		if emotion == "happy":
			priority = "work"
		elif emotion == "sad":
			priority = "eat"
		elif emotion == "grumpy":
			priorityC = random.randint(1,2)
			if priorityC == 1: #Work
				priority = "work"
			elif priorityC == 2:
				priority = "grumpy work"
			#end if
		elif emotion == "angry":
			priority = "tantrum"
			if mentalIllness == "True":
				priority = "tantrum_x" #This is like tantrum but the dwarf can murder people
	#end for
	os.chdir(path)
	print priority