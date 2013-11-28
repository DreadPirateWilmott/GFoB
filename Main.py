#Created by DreadPirateWilmott on November 14th 2013
#Last edited on the 24th
#Feel free to make edits and make this program your own, I only ask that you keep the DreadPirateWilmott name
#on the top of the program.
#Current Version 0.0.2 - Please note that I do tend to comment a lot on my code for future reference
"""The purpose of the main game is to give player control over an entity and have them control that entity.
One of the main purposes of the game is building a fortress and defending against enemy invasions. The main 
challenge comes from the fact that it is a text game. The entire game will take place on a 20x20 square platform with each player only being able
to move one space at a time. The main control functions of the game will include movement in 4 directions,
the ability to turn, the ability to shoot, and the ability to place an object to block shots. The controllable
character will be referred to as a pirate in the code, and the AI opponent will be referred to as a Knight."""
#import essential files
import time
import random
import math

def Menu():
	print "Start"
	print "Tutorial"
	print "Controls"
	cMenu = str(raw_input(": ").lower())
	
	if cMenu == "start":
		GFoB()
	elif cMenu == "tutorial":
		Tutorial()
	elif cMenu == "controls":
		ControlPrint()
	#end if

def ControlPrint():
	print "To understand the controls you need to understand how I refer to commands. There are three types: primary, secondary, tertiary."
	print "Primary commands are the first word and the identifier. Secondary commands are generally directions. Tertiary commands are only used for distance."
	print "In the game there are currently 5 commands that need to be listed: move, place, turn, mine, and shoot."
	print "Move - Primary command, Forward, Back, Left, Right - Secondary command, No tertiary command."
	print "Place - Primary command, Forward, Back, Left, Right - Secondary command, Tertiary command is distance (up to four spaces)."
	print "Mine - Primary command, Forward, Back, Left, Right - Secondary command, Tertiary command is distance (up to four spaces)."
	print "Turn - Primary command, Right, Left - Secondary command, No tertiary command."
	Menu()
	
def Tutorial():
	print "The purpose of the game is to build, manage, and successfully defend a fortress."
	print "See the controls menu located in the main menu for more information on key bindings."
	Menu()
	
def GFoB():
	charN = str(raw_input("Enter character name: "))
	playerX = 1
	playerZ = 1
	playerY = 1
	faceDir = 1 #The direction that you are facing; defaults to forward being + on the X
	compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
	blockList = [] #Format for blocklist is the X coordinate. Y coordinate. Z coordinate
	emptyList = [] #A list that stores values such as the co-ordinates for the crefor block
	while True: #Loop forever, there will be a command to end the game
		print "%s's current position is %s X, %s Y, and %s Z" % (charN, playerX, playerY, playerZ)
		if faceDir == 1:
			tempX = playerX + 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block forward"
			tempZ = playerZ + 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block right"
			tempX = playerX - 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block back"
			tempZ = playerZ - 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block left"
			#end if
		elif faceDir == 2:
			tempZ = playerZ + 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block forward"
			tempX = playerX - 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block right"
			tempZ = playerZ - 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block back"
			tempX = playerX + 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block left"
			#end if
		elif faceDir == 3:
			tempX = playerX - 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block forward"
			tempZ = playerZ - 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block right"
			tempX = playerX + 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block back"
			tempZ = playerZ + 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block left"
			#end if
		elif faceDir == 4:
			tempZ = playerZ - 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block forward"
			tempX = playerX + 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block right"
			tempZ = playerZ + 1
			tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
			if tempCompile in blockList:
				print "Block back"
			tempX = playerX - 1
			tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
			if tempCompile in blockList:
				print "Block left"
			#end if
		#end if
		instruction = str(raw_input(": ").lower())
		if "move" in instruction: #Ex move.forward
			#The player wishes to move in one of the four directions
			moveList = instruction.split(" ")
			moveDirection = moveList[1]
			#The move direction will determine which way the pirate moves; the direction is relative to the direction
			#that the pirate is facing.
			if moveDirection == "forward": 
				if faceDir == 1:
					playerX += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX -= 1
						print "Blocked path"
				elif faceDir == 2:
					playerZ += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ -= 1
						print "Blocked path"
				elif faceDir == 3:
					playerX -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX += 1
						print "Blocked path"
				elif faceDir == 4:
					playerZ -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ += 1
						print "Blocked path"
			elif moveDirection == "back":
				if faceDir == 1:
					playerX -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX += 1
						print "Blocked path"
				elif faceDir == 2:
					playerZ  -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ += 1
						print "Blocked path"
				elif faceDir == 3:
					playerX += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX -= 1
						print "Blocked path"
				elif faceDir == 4:
					playerZ += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ -= 1
						print "Blocked path"
			elif moveDirection == "right":
				if faceDir == 1:
					playerZ += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ -= 1
						print "Blocked path"
				elif faceDir == 2:
					playerX -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX += 1
						print "Blocked path"
				elif faceDir == 3:
					playerZ -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ += 1
						print "Blocked path"
				elif faceDir == 4:
					playerX += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX -= 1
						print "Blocked path"
			elif moveDirection == "left":
				if faceDir == 1:
					playerZ -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ += 1
						print "Blocked path"
				elif faceDir == 2:
					playerX += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX -= 1
						print "Blocked path"
				elif faceDir == 3:
					playerZ += 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerZ -= 1
						print "Blocked path"
				elif faceDir == 4:
					playerX -= 1
					compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
					if compiledCo in blockList:
						playerX += 1
						print "Blocked path"
			elif moveDirection == "climb": #To move upwards the block you wish to climb needs to be in front of you
				if faceDir == 1:
					tempX = playerX + 1 #This is a temporary, unimportant value that is used for testing location conditions
					tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
				elif faceDir == 2:
					tempZ = playerZ + 1
					tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
				elif faceDir == 3:
					tempX = playerX - 1
					tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
				elif faceDir == 4:
					tempZ = playerZ - 1
					tempCompile = "%s.%s.%s" % (playerX, playerY, tempZ)
				if(tempCompile in blockList):
					playerY += 1
					print "Climb succesful"
				else:
					print "Climb unsuccessful"
				compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
				if compiledCo in blockList:
					playerY -= 1
					print "Blocked path"
			#Moving down will be done automatically by the game
			tempX = playerX + 1
			tempY = playerY - 1
			if faceDir == 1:
				tempCompile = "%s.%s.%s" % (tempX, tempY, playerZ)
				tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			elif faceDir == 2:
				tempZ = playerZ + 1
				tempY = playerY - 1
				tempCompile = "%s.%s.%s" % (playerX, tempY, tempZ)
				tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			elif faceDir == 3:
				tempX = playerX - 1
				tempY = playerY - 1
				tempCompile = "%s.%s.%s" % (tempX, tempY, playerZ)
				tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			elif faceDir == 4:
				tempZ = playerZ - 1
				tempY = playerY - 1
				tempCompile = "%s.%s.%s" % (playerX, tempY, tempZ)
				tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			#end if
			while tempCompile not in blockList and tempCompile2 not in blockList and playerY > 1:
				playerY -= 1
				print "%s fell one space" % (charN)
				tempY = playerY - 1
				tempCompile = "%s.%s.%s"  % (tempX, tempY, playerZ)
				tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			#end if
			#If the player moves off of the platform then reset their position
			if playerX > forXplusBound or playerX < forXminusBound or playerZ > forZplusBound or playerZ < forZminusBound:
				print charN + " has travelled out of the fortress."
			if playerX > 20 or playerX < 1 or playerZ > 20 or playerZ < 1:
				print "Player position reset"
				playerX = 1
				playerZ = 1
				playerY = 1
				faceDir = 1
			#end if
		#end if
		elif "turn" in instruction: #Ex turn.right
			#The player wishes to turn in one of the two directions
			#1 = X+, 2 = Z+, 3 = X-, 4 = Z-
			directionList = instruction.split(" ")
			direction = directionList[1]
			if direction == "right":
				faceDir += 1
				if faceDir == 5:
					faceDir = 1
			elif direction == "left":
				faceDir -= 1
				if faceDir == 0:
					faceDir = 4
		#end if
		elif "place" in instruction: #Ex place.forward
			#The player wishes to place an object in one of the four directions
			placeList = instruction.split(" ")
			direction = placeList[1]
			
			if len(placeList) == 3:
				placeDis = str(placeList[2])
				if placeDis == "crefor" and len(emptyList) == 0:
					placeDis = 1
					emptyListTrig = True
					
					#Determine the boundaries for the fortress
					forXplusBound = playerX + int(raw_input("X Positive boundary distance: "))
					forXminusBound = playerX - int(raw_input("X Negative boundary distance: "))
					forZplusBound = playerZ + int(raw_input("Z Positive boundary distance: "))
					forZminusBound = playerZ - int(raw_input("Z Negative boundary distance: "))
				
				else:
					placeDis = int(placeDis)
					emptyListTrig = False
			else:
				placeDis = 1
			
			#Make sure the place distance doesn't exceed 4
			if placeDis > 4:
				placeDis = 4
				print "Distance too great, block will be placed 4 blocks away."
				
			if direction == "forward":
				if faceDir == 1:
					blockX = playerX + placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 2:
					blockZ = playerZ + placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 3:
					blockX = playerX - placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 4:
					blockZ = playerZ - placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
			elif direction == "back":
				if faceDir == 1:
					blockX = playerX - placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 2:
					blockZ = playerZ - placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 3:
					blockX = playerX + placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 4:
					blockZ = playerZ + placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
			elif direction == "left":
				if faceDir == 1:
					blockZ = playerZ - placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 2:
					blockX = playerX + placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 3:
					blockZ = playerZ + placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 4:
					blockX = playerX - placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "right":
				if faceDir == 1:
					blockZ = playerZ + placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 2:
					blockX = playerX - placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 3:
					blockZ = playerZ - placeDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 4:
					blockX = playerX + placeDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "up":
				blockY = playerY + placeDis
				compiledBlock = "%s.%s.%s" % (playerX, blockY, playerZ)
			elif direction == "down" and playerY > 1:
				blockY = playerY - placeDis
				compiledBlock = "%s.%s.%s" % (playerX, blockY, playerZ)
			#end if
			
			#Add compiledBlock to the total blocklist
			if emptyListTrig == True:
				emptyList.append(compiledBlock)
			if compiledBlock not in blockList:
				blockList.append(compiledBlock)
			else:
				print "Block already in that location"
		#end if
		elif "mine" in instruction:
			mineList = instruction.split(" ")
			direction = mineList[1]
			if len(mineList) == 3:
				mineDis = int(mineList[2])
			else:
				mineDis = 1
			#If the mining distance is greater than 4 than reduce the distance to 4
			if mineDis > 4:
				mineDis = 4
				print "Too far away, block will be mined 4 blocks away."
				
			#Determine the direction and facing direction in an attempt to remove the block
			if direction == "forward":
				if faceDir == 1:
					blockX = playerX + mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 2:
					blockZ = playerZ + mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 3:
					blockX = playerX - mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 4:
					blockZ = playerZ - mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
			elif direction == "back":
				if faceDir == 1:
					blockX = playerX - mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 2:
					blockZ = playerZ - mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 3:
					blockX = playerX + mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 4:
					blockZ = playerZ + mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
			elif direction == "left":
				if faceDir == 1:
					blockZ = playerZ - mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 2:
					blockX = playerX + mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 3:
					blockZ = playerZ + mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 4:
					blockX = playerX - mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "right":
				if faceDir == 1:
					blockZ = playerZ + mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 2:
					blockX = playerX - mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 3:
					blockZ = playerZ - mineDis
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 4:
					blockX = playerX + mineDis
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "up":
				blockY = playerY + mineDis
				compiledBlock = "%s.%s.%s" % (playerX, blockY, playerZ)
			elif direction == "down" and playerY > 1:
				blockY = playerY - mineDis
				compiledBlock = "%s.%s.%s" % (playerX, blockY, playerZ)
			#end if
			
			#Remove the block
			if compiledBlock in blockList:
				blockList.remove(compiledBlock)
				print "Block mined"
			else:
				print "No block to mine"
			#end if
			
			if direction == "down" and playerY > 1:
				tempY = playerY - 1
				compiledCo = "%s.%s.%s" % (playerX, tempY, playerZ)
				while compiledCo not in blockList and playerY > 1:
					playerY -= 1
				#end while
			#end if
		elif instruction == "shoot": #Ex shoot
			#The player wishes to shoot
			if faceDir == 1:
				for i in range(1, 21):
					tempX = playerX + i
					compiledValue = "%s.%s.%s" % (tempX, playerY, playerZ)
					if compiledValue in blockList:
						print "Blocked by object"
						break
			elif faceDir == 2:
				for i in range(1, 21):
					tempZ = playerZ + i
					compiledValue = "%s.%s.%s" % (playerX, playerY, tempZ)
					if compiledValue in blockList: 
						print "Blocked by object"
						break
			elif faceDir == 3:
				for i in range(1, 21):
					tempX = playerX - i
					compiledValue = "%s.%s.%s" % (tempX, playerY, playerZ)
					if compiledValue in blockList:
						print "Blocked by object"
						break
			elif faceDir == 4:
				for i in range(1, 21):
					tempZ = playerZ - i
					compiledValue = "%s.%s.%s" % (playerX, playerY, tempZ)
					if compiledValue in blockList:
						print "Blocked by object"
						break
			#end if
		#end if
		elif instruction == "end.game":
			return
		
def NPC():
	#This is the computer player in GFoB
	print "Not functional"

Menu()