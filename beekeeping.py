def Bees(tileList, tileNlist):
	
	zLevel = int(raw_input("Z level: "))
	
	startingPoint = str(raw_input("Starting position: "))
	startingPoints = startingPoint.split(".") #X.Y
	
	startingX = int(startingPoints[0])
	startingY = int(startingPoints[1])
	
	endingPoint = str(raw_input("Ending position: "))
	endingPoints = endingPoint.split(".") #X.Y
	
	endingX = int(endingPoints[0])
	endingY = int(endingPoints[1])
	
	if endingX > startingX:
		Xdisplaced = endingX - startingX + 1
	elif endingX < startingX:
		Xdisplaced = startingX - endingX + 1
	else:
		Xdisplaced = 1
	#end if
	
	if endingY > startingY:
		Ydisplaced = endingY - startingY + 1
	elif endingY < startingY:
		Ydisplaced = startingY - endingY + 1
	else:
		Ydisplaced = 1
	#end if
	
	#Testing
	print Xdisplaced
	print Ydisplaced
	beeArea = Xdisplaced * Ydisplaced
	print beeArea
	
	removedBlocks = []
	if beeArea >= 9 and Xdisplaced > 1 and Ydisplaced > 1:
		print "That is a valid space for beekeeping."
		for x in range(0, Xdisplaced):
			for y in range(0, Ydisplaced):
				compile = "%s.%s.%s" % (x, zLevel, y)
				if compile in tileList:
					indexV = tileList.index(compile)
					tile = tileNlist[indexV]
					
					if tile not in removedBlocks:
						print tile + " removed during construction."
						removedBlocks.append(tile)
					#Remove value
					tileList.pop(indexV)
					tileNlist.pop(indexV)
				#end if
			#end for
		#end for
	else:
		print "That is not a valid space for beekeeping."
	#end if
	
	return tileList, tileNlist