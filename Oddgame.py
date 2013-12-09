#Created by DreadPirateWilmott on November 14th 2013


#Current Version 0.0.5 - 3 hours 5 minutes for 0.0.6 release

#import python files
import dwarf_manager
import beekeeping
import generate
import embark
import zoning

#import AI
import companion_ai

#import built-in functions
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
		print "Your dwarf caravan arrives in the fields of %s." % (location)
		
		#Get a name list variable from the names of your goblins
		names = ", ".join(nList)
		print "Your party of dwarves consists of %s." % (names)
	elif cMenu == "load":
		print "Hasn't been worked on yet"
	#end if
	
	instMenu = "\nInstruction Menu\n================\nManage Dwarves\nCrafting\nJobs\nZoning\nMenu"
	print instMenu
	while True:
		run = str(raw_input(">").lower()) #run is the main game command
		
		if run == "menu":
			print instMenu
		#end if
		
		elif run == "manage dwarves":
			dwarf_manager.Manage()
		#end if
		
		elif run == "crafting":
			print "WORK IN PROGRESS"
		#end if
		
		elif run == "jobs":
			print "WORK IN PROGRESS"
		#end if
		
		elif run == "zoning":
			zoning.set(tileList)
		#end if
		
		companion_ai.priority()
	#end while
Menu()
