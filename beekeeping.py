def Bees(tileList, tileNlist):
	
	zLevel = int(raw_input("Z level: "))
	
	startingPoint = str(raw_input("Starting position: "))
	startingPoints = startingPoint.split(".") #X.Y
	
	Xstart = int(startingPoints[0])
	Ystart = int(startingPoints[1])
	
	endingPoint = str(raw_input("Ending position: "))
	endingPoints = endingPoint.split(".") #X.Y
	
	Xend = int(endingPoints[0])
	Yend = int(endingPoints[1])
	
		
	if Xstart >= Xend and Ystart >= Yend:
		tempX = Xstart
		tempY = Ystart
		while tempX >= Xend:
			while tempY >= Yend:
				compile = "%s.%s.%s" % (tempX, zLevel, tempY)
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
				tempY += 1
			#end while
			tempY = Ystart
			tempX += 1
		#end while
	#end if
	
	if compile in tileList:
		print "Space obstructed by existing tiles."
	else:
		print "That is a valid space for beekeeping."
		#Work on this later: This will lead to the beekeeping function"
	#end if
	
	return tileList, tileNlist