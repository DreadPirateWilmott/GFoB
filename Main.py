#Created by DreadPirateWilmott on November 14th 2013
#Last edited on the 4th of December
#Feel free to change, break, create, or mod anything about this game as you see fit


#Current Version 0.0.4 - 5 hours of recorded time (since change)

#import essential files
import history
import random
import glob
import os

def Embark(): #This lets you name your goblins and your fortress as well as prepare for the journey ahead
	path = os.getcwd()
	newpath = path + "\\naming"
	os.chdir(newpath)
	
	#Get the first name list
	file = open("first.txt", "r")
	fNames = file.read()
	fNames = fNames.split("\n")
	file.close()
	
	#Get the last name list
	file = open("last.txt", "r")
	lNames = file.read()
	lNames = lNames.split("\n")
	file.close()
	
	os.chdir(path)
	#Loop 5 times to get each goblin a name
	nList = []
	for i in range(1, 6): #5 times
		first = random.randint(1, len(fNames)) - 1
		last = random.randint(1, len(lNames)) - 1
		
		fName = fNames[first]
		lName = lNames[last]
		name = "%s %s" % (fName, lName)
		print name
		nList.append(name)
	os.chdir(path)
	
	fortressName = str(raw_input("Fortress name: "))
	return nList, fortressName
def genW():
	XZboundary = int(raw_input("Enter how large you want your world to be: ")) + 1
	print "Generating world..."
	tileList = []
	tileNlist = []
	for x in range(1, XZboundary):
		for z in range(1, XZboundary):
			for y in range(1, 21):
				if y < 18:
					if y >= 16:
						dirtChance = random.randint(1, 11)
						if dirtChance == 1:
							tileName = "dirt"
						else:
							tileName = "stone"
					else:
						tileName = "stone"
				elif y >= 18:
					airChance = random.randint(1,3)
					if airChance == 1:
						tileName = "air"
					else:
						tempY = y - 1
						tempCompile = "%s.%s.%s" % (x, tempY, z)
						if tempCompile not in tileList: #Air
							tileName = "air"
						else:
							treeChance = random.randint(1, 100)
							if treeChance == 1:
								tileName = "wood"
								print "Tree created"
							else:
								tileName = "dirt"
					#end if
					
				if tileName != "air":
					if tileName == "wood": #Spawn a tree
						tempY = y
						for i in range(0, 5): #Tree will be five tiles tall
							compile = "%s.%s.%s" % (x, y, z)
							y += 1
							tileList.append(compile)
							tileNlist.append(tileName)
						#end for / leaves will be added later
					else:
						compile = "%s.%s.%s" % (x, y, z)
						tileList.append(compile)
						tileNlist.append(tileName)
					#end if
				#end if
			#end for
		#end for
	#end for
	return tileList, tileNlist, XZboundary
	
def Menu():
	print "[Start] New Game"
	print "[Load] Game"
	cMenu = str(raw_input(": ").lower())
	
	if cMenu == "start" or cMenu == "load":
		Main(cMenu)
	#end if
	
def Main(cMenu): #This is the function call
	tileList, tileNlist, XZboundary = genW() #Tiles, tile names, world size
	if cMenu == "start":
		print "Your goblin caravan arrives in the hills of"
		history.GetRulersAndLocations()
	#end if
Menu()
