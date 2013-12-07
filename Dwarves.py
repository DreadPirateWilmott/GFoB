#Created by DreadPirateWilmott on November 14th 2013
#Last edited on the 4th of December
#Feel free to change, break, create, or mod anything about this game as you see fit


#Current Version 0.0.4 - 7 hours 25 minutes of recorded time (since 0.0.3)

#import essential files
import beekeeping
import generate
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
	
	file = open("locations.txt", "r")
	locations = file.read()
	locations = locations.split("\n")
	randLoc = random.randint(0, 15)
	location = locations[randLoc]
	
	os.chdir(path)
	#Loop 5 times to get each goblin a name
	nList = []
	for i in range(1, 6): #5 times
		first = random.randint(1, len(fNames)) - 1
		last = random.randint(1, len(lNames)) - 1
		
		fName = fNames[first]
		lName = lNames[last]
		name = "%s %s" % (fName, lName)
		nList.append(name)
	#end for
	fortressName = str(raw_input("Fortress name: "))
	return nList, fortressName, location

def Menu():
	print "[Start] New Game"
	print "[Load] Game"
	cMenu = str(raw_input(": ").lower())
	
	if cMenu == "start" or cMenu == "load":
		Main(cMenu)
	#end if
	
def Main(cMenu): #This is the function call
	tileList, tileNlist = generate.genW() #Tiles, tile names, world size
	nList, fortressName, location = Embark()
	tileList, tileNlist = beekeeping.Bees(tileList, tileNlist)
	if cMenu == "start":
		print "Your dwarf caravan arrives in the fields of %s" % (location)
		
		#Get a name list variable from the names of your goblins
		names = ", ".join(nList)
		print "Your party of dwarves consists of %s" % (names)
		
		pause = raw_input("PAUSE")
	#end if
Menu()
