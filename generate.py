import random

def genW(): #Generate the world and the base wagon position
	print "Generating world..."
	tileList = []
	tileNlist = []
	for x in range(1, 51): #Forward, backward
		for z in range(1, 21): #Up, down
			for y in range(1, 51):#Left, right
				tileName = "stone"

				compile = "%s.%s.%s" % (x, z, y)
				tileList.append(compile)
				tileNlist.append(tileName)
			#end for
		#end for
	#end for
	
	wagonSX = random.randint(10, 40) #Starting X
	wagonSY = random.randint(10, 40) #Starting Y
	
	wagonEX = wagonSX + 3
	wagonEY = wagonSY + 2
	
	tileName = "wagon"
	wagonSpace = []
	z = 21 #Higher up than the rest of the map; the wagon is sitting on the ground
	for x in range(wagonSX, wagonEX):
		for y in range(wagonSY, wagonEY):
			compile = "%s.%s.%s" % (x, z, y)
			print "created wagon piece at %s" % (compile) #This is just a testing statement: NOTICE: REMOVE LATER
			tileList.append(compile)
			wagonSpace.append(compile)
			tileNlist.append(tileName)
		#end for
	#end for
	
	import os
	path = os.getcwd()
	newpath = path + "\\essentials"
	os.chdir(newpath)
	
	#Save the wagon information
	file = open("wagonspace.txt", "w")
	wagonSpace = ", ".join(wagonSpace)
	file.write(wagonSpace)
	file.close()
	os.chdir(path)
	
	return tileList, tileNlist
