import dwarf_manager
import os
import random

def prepare(): #This lets you name get the names of your dwarves and name the fortress
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
	randLoc = random.randint(0, 14)
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
	
	dwarf_manager.createFiles(nList)
	
	packed = "TEMP"
	points = 50
	inventory = []
	possibleItems = ["stone", "meat", "dirt"] #All possible packing items must be listed here
	print "Stone = 2p\nMeat = 8p\nDirt = 2p\nType 'done' when you are finished."
	while packed != "done" and points > 1:
		packed = str(raw_input(">").lower())
		if packed != "done":
			numberItemSplit = packed.split(" ")
			amount = int(numberItemSplit[0])
			item = str(numberItemSplit[1])
		#end if
			if item not in possibleItems:
				print "Not a valid item."
			else:
				for i in range(0, amount):
					inventory.append(item)
					if item == "stone" or item == "dirt":
						points -= 2
					elif item == "meat":
						points -= 8
					#end if
				#end for
			
			print "%s points left." % (points)
			#end if
	#end while
	return nList, fortressName, location, inventory