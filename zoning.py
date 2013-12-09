import os
import glob

def set(tileList): #The zone has to be free of tiles
	path = os.getcwd()
	newpath = path + "\\essentials\\zones"
	os.chdir(newpath)
	#This lets you set the parameters of a zone
	instMenu = "\nZone Types\n===========\nSocial\nStockpile"

	zone = str(raw_input("%s\n>" % (instMenu)).lower())
	zLevel = int(raw_input("Z Level >"))
	zonedArea = []
	
	if zone == "social":
		#Designated meeting area; the dwarf AI will automatically path here if they have
		#no work to do.
		coordinates = []
		
		zoneStart = raw_input("Starting Position >") #X.Y
		coordinates = zoneStart.split(".")
		zoneEnd = raw_input("Ending Position >") #X.Y
		coordinates = coordinates + zoneEnd.split(".")
		
		Xstart = int(coordinates[0])
		Xend = int(coordinates[2])
		
		Ystart = int(coordinates[1])
		Yend = int(coordinates[3])
		
		if Xstart >= Xend and Ystart >= Yend:
			tempX = Xstart
			tempY = Ystart
			while tempX >= Xend:
				while tempY >= Yend:
					compile = "%s.%s.%s" % (tempX, zLevel, tempY)
					zonedArea.append(compile)
					tempY -= 1
				#end while
				tempY = Ystart
				tempX -= 1
			#end while
		elif Xstart >= Xend and Ystart <= Yend:
			tempX = Xstart
			tempY = Ystart
			while tempX >= Xend:
				while tempY <= Yend:
					compile = "%s.%s.%s" % (tempX, zLevel, tempY)
					zonedArea.append(compile)
					tempY += 1
				#end while
				tempY = Ystart
				tempX -= 1
			#end while
		elif Xstart <= Xend and Ystart >= Yend:
			tempX = Xstart
			tempY = Ystart
			while tempX <= Xend:
				while tempY >= Yend:
					compile = "%s.%s.%s" % (tempX, zLevel, tempY)
					zonedArea.append(compile)
					tempY -= 1
				#end while
				tempY = Ystart
				tempX += 1
			#end while
		elif Xstart <= Xend and Ystart <= Yend:
			tempX = Xstart
			tempY = Ystart
			while tempX <= Xend:
				while tempY <= Yend:
					compile = "%s.%s.%s" % (tempX, zLevel, tempY)
					zonedArea.append(compile)
					tempY += 1
				#end while
				tempY = Ystart
				tempX += 1
			#end while
		#end if
		
		#Save the zone
		lenZonedArea = len(zonedArea) - 1
		for i in range(0, lenZonedArea):
			compile = zonedArea[i]
			if compile in tileList:
				print "Zone obstructed."
				return
			else:
				print "Zone created."
				#end if
				
		zoneFiles = glob.glob("*.txt")
		if "socialzone.txt" in zoneFiles:
			print "Existing zone already in place."
			file = open("socialzone.txt", "r")
			existingZone = file.read()
			existingZone = existingZone.split(", ")
			limit = len(zonedArea)
			print len(zonedArea)
			print zonedArea
			for i in range(0, limit):
				print zonedArea[i]
				if zonedArea[i] in existingZone:
					zonedArea.pop(i)
				#end if
			#end for
			file.close()
			
			file = open("socialzone.txt", "a")
			zonedArea = ", ".join(zonedArea)
			file.write(", %s" % (zonedArea))
			file.close()
		elif "socialzone.txt" not in zoneFiles:
			file = open("socialzone.txt", "w")
			zonedArea = ", ".join(zonedArea)
			file.write(zonedArea)
			file.close()
		#end if
		#end for
	#end if
	os.chdir(path)