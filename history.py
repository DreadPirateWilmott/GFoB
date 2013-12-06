import os
import random

def GetRulersAndLocations():
	print "Getting history info..."
	path = os.getcwd()
	newpath = path + "\\history"
	os.chdir(newpath)
	
	#History lists - location
	location = [] #This is the city, town, field, or sea
	
	#History lists - rulers
	firstName = [] #Temporary first name list
	lastName = [] #Temporary last name list
	name = [] #This is the name of the rulers
	Race = [] #This is the race: elf, human, dwarf, goblin
	Gender = [] #This is the gender: male or female
	
	#Get the location first
	file = open("locations.txt", "r")
	fileContents = file.read()
	fileContents = fileContents.split("\n")
	
	for i in range(0, 19):
		fileline = fileContents[i]
		locationTypeAndName = fileline.split(".")
		locationAdd = "%s of %s" % (locationTypeAndName[0], locationTypeAndName[1])
		location.append(locationAdd)
	#end for
	file.close()
	
	#Get the ruler names
	file = open("rulers.txt", "r")
	fileContents = file.read()
	filelines = fileContents.split("\n")
	for i in range(0, 34): #Read the first names and related information
		if i < 19:
			info = filelines[i]
			infoSplit = info.split(".")
			firstname = infoSplit[0]
			race = infoSplit[1]
			gender = infoSplit[2]
		
			#Append to lists
			firstName.append(firstname)
			Race.append(race)
			Gender.append(gender)
		else: #Last names
			lastname = filelines[i]
			lastName.append(lastname)
		#end if
	#end for
	for i in range(0, 19):
		fName = firstName[i]
		backName = random.randint(0, 15)
		lName = lastName[backName]
		
		fullName = "%s the %s" % (fName, lName)
		name.append(fullName)
	#end for
	os.chdir(path)
	History(location, name, Race, Gender)
def History(location, name, Race, Gender):
	#X in location = X in name = X in race = X in gender; let X be a number
	for i in range(0, 100): #100 years
		doWar = random.randint(1, 100)
		if doWar >= 1 and doWar <= 33: #1 in 3 chance of war
			while True:
				faction1 = random.randint(0, 18)
				faction2 = random.randint(0, 18)
				
				if faction1 != faction2:
					#Two different factions are fighting
					break
				#end if
				
			raceOne = Race[faction1]
			raceTwo = Race[faction2]
			
			genderOne = str(Gender[faction1])

			if genderOne == "female":
				monarch = "Queen"
			elif genderOne == "male":
				monarch = "King"
			#end if
			genderTwo = str(Gender[faction2])
			if genderTwo == "female":
				monarch2 = "Queen"
			elif genderTwo == "male":
				monarch2 = "King"
			#end if
			
			nameOne = name[faction1]
			nameTwo = name[faction2]
			
			locationOne = location[faction1]
			locationTwo = location[faction2]
			
			chooseLocation = random.randint(1,2)
			
			if chooseLocation == 1:
				battleLocation = locationOne
				#Faction 2 attacked faction one
				print "The %s %s %s attacked the %s %s %s in the %s" % (raceOne, monarch, nameOne, raceTwo, monarch2, nameTwo, battleLocation)	
			elif chooseLocation == 2:
				battleLocation = locationTwo
				#Faction 1 attacked faction two
				print "The %s %s %s attacked the %s %s %s in the %s" % (raceTwo, monarch2, nameTwo, raceOne, monarch, nameOne, battleLocation)
			#end if
			pause = str(raw_input(":"))	