#Created by DreadPirateWilmott on November 14th 2013


#Current Version 0.0.4 - 8 hours 35 minutes of recorded time (since 0.0.3)

#import python files
import dwarf_manager
import beekeeping
import generate
import embark

#import built-in functiona
import random
import glob
import os



def Menu():
	print "[Start] New Game"
	print "[Load] Game"
	cMenu = str(raw_input(": ").lower())
	
	if cMenu == "start" or cMenu == "load":
		Main(cMenu)
	#end if
	
def Main(cMenu): #This is the function call
	tileList, tileNlist = generate.genW() #Tiles, tile names, world size
	nList, fortressName, location, inventory = embark.prepare()
	tileList, tileNlist = beekeeping.Bees(tileList, tileNlist)
	if cMenu == "start":
		print "Your dwarf caravan arrives in the fields of %s" % (location)
		
		#Get a name list variable from the names of your goblins
		names = ", ".join(nList)
		print "Your party of dwarves consists of %s" % (names)
	elif cMenu == "load":
		print "Hasn't been worked on yet"
	#end if
	
	instMenu = "Instruction Menu\n================\nManage Dwarves\nCrafting\nNature\nMining\nBuilding\nMenu"
	print instMenu
	while True:
		run = str(raw_input(">").lower()) #run is the main game command
		
		if run == "menu":
			print instMenu
		#end if
	#end while
Menu()
