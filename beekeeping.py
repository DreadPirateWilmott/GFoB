def Bees(tileList, tileNlist):
	
	zLevel = int(raw_input("Z level: "))
	
	
	#Get the difference in position
	Xdisplaced = None
	Ydisplaced = None
	t = False

	while Xdisplaced is None or Ydisplaced is None:
		if t == False:
			startingPoint = str(raw_input("Starting Position: "))
		else:
			startingPoint = str(raw_input("Invalid Starting Pos, Enter new Starting Position: "))
		#end if
		startingPoints = startingPoint.split(".") #X.Y
	
		startingX = int(startingPoints[0])
		startingY = int(startingPoints[1])
		if t == False:
			endingPoint = str(raw_input("Ending pPsition: "))
			t = True
		else:
			endingPoint = str(raw_input("Invalid Ending Pos, Enter new Ending Position: "))
		#end if
		endingPoints = endingPoint.split(".") #X.Y
	
		endingX = int(endingPoints[0])
		endingY = int(endingPoints[1])
	
		if endingX > startingX:
			Xdisplaced = endingX - startingX
		elif endingX < startingX:
			Xdisplaced = startingX - endingX
		#end if
	
		if endingY > startingY:
			Ydisplaced = endingY - startingY
		elif endingY < startingY:
			Ydisplaced = startingY - endingY
		#end if
	#end while
	if Xdisplaced is None:
		print "Dang"
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
	#end if
	
	return tileList, tileNlist
