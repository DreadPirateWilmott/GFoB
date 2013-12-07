import random

def genW():
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
	return tileList, tileNlist
