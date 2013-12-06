import random

def genW():
	print "Generating world..."
	tileList = []
	tileNlist = []
	for x in range(1, 51):
		for z in range(1, 51):
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
				elif y >= 18 and x >= 35 or x <= 15 and z >= 35 or z <= 15:
					airChance = random.randint(1,3)
					if airChance == 1:
						tileName = "air"
					else:
						tempY = y - 1
						tempCompile = "%s.%s.%s" % (x, tempY, z)
						if tempCompile not in tileList: #Air
							tileName = "air"
						else:
							tileName = "dirt"
						#end if
					#end if
					
				if tileName != "air":
					compile = "%s.%s.%s" % (x, y, z)
					tileList.append(compile)
					tileNlist.append(tileName)
				#end if
			#end for
		#end for
	#end for
	return tileList, tileNlist
