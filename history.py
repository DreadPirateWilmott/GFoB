import os
import random

def GetRulersAndLocations():
	print "Getting history info..."
	path = os.getcwd()
	newpath = path + "\\history"
	os.chdir(newpath)
	
	#History lists - location
	location = [] #This is the city, town, field, or sea
	locationN = [] #This is the name of the city, town, field, or sea
	
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
	
	for i in range(0, len(fileContents)):
		fileline = fileContents[i]
		locationTypeAndName = fileline.split(".")
		location.append(locationTypeAndName[0])
		locationN.append(locationTypeAndName[1])
	#end for
	file.close()
	
	#Get the ruler names
	file = open("rulers.txt", "r")
	fileline = file.readline() #This will be the top message so we don't need to do anything to it
	for i in range(0, 19): #Read the first names and related information
		fileline = file.readline()
		info = fileline.split(".")
		
		firstname = info[0]
		race = info[1]
		gender = info[2]
		
		#Append to lists
		firstName.append(firstname)
		Race.append(race)
		Gender.append(gender)
	#end for
	
	for i in range(0, 16):
		fileline = file.readline()
		lastName.append(fileline)
	#end for
	
	for i in range(0, 19):
		fName = firstName[i]
		backName = random.randint(0, 15)
		lName = lastName[backName]
		
		fullName = fName + " the " + lName
		name.append(fullName)
		print fullName
	#end if
	os.chdir(path)
def History():
	print "WIP"
	