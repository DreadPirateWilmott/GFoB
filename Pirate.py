#Created by DreadPirateWilmott on November 14th 2013
#Current Version 0.0.1 - Please note that I do tend to comment alot on my code for future reference
"""The purpose of the main game is to give player control over an entity and have them fight with the
enemy AI. The entire game will take place on a 100x100 square platform with each player only being able
to move one space at a time. The main control functions of the game will include movement in 4 directions,
the ability to turn, the ability to shoot, and the ability to place an object to block shots. The controllable
character will be referred to as a pirate in the code, and the AI opponent will be referred to as a Knight."""
#import essential files
import time
import random
import math

def Main():
	playerX = 1
	playerZ = 1
	playerY = 5
	compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
	blockList = [] #Format for blocklist is the X coordinate. Y coordinate. Z coordinate
	while True: #Loop forever, there will be a command to end the game
		print "Current player position is %s X, %s Y, and %s Z" % (playerX, playerY, playerZ)
		instruction = str(raw_input(": ").lower())
		if "move" in instruction: #Ex move.forward
			#The player wishes to move in one of the four directions
			moveList = instruction.split(".")
			moveDirection = moveList[1]
			#The move direction will determine which way the pirate moves
			if moveDirection == "forward":
				playerX += 1
				compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
				if compiledCo in blockList:
					playerX -= 1
					print "Blocked path"
			elif moveDirection == "back":
				playerX -= 1
				compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
				if compiledCo in blockList:
					playerX += 1
					print "Blocked path"
			elif moveDirection == "right":
				playerZ += 1
				compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
				if compiledCo in blockList:
					playerZ -= 1
					print "Blocked path"
			elif moveDirection == "left":
				playerZ -= 1
				compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
				if compiledCo in blockList:
					playerZ += 1
					print "Blocked path"
			elif moveDirection == "up": #To move upwards the block you wish to climb needs to be in front of you
				tempX = playerX + 1 #This is a temporary, unimportant value that is used for testing location conditions
				tempCompile = "%s.%s.%s" % (tempX, playerY, playerZ)
				if(tempCompile in blockList):
					playerY += 1
				else:
					print "Climb unsuccessful"
				compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
				if compiledCo in blockList:
					playerY -= 1
					print "Blocked path"
			#Moving down will be done automatically by the game
			tempX = playerX + 1
			tempY = playerY - 1
			tempCompile = "%s.%s.%s" % (tempX, tempY, playerZ)
			tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			while tempCompile not in blockList and tempCompile2 not in blockList and playerY > 1:
				playerY -= 1
				tempY = playerY - 1
				tempCompile = "%s.%s.%s"  % (tempX, tempY, playerZ)
				tempCompile2 = "%s.%s.%s" % (playerX, tempY, playerZ)
			#end if
			#If the player moves off of the platform then reset their position
			if playerX > 100 or playerX < 1 or playerZ > 100 or playerZ < 1:
				print "Player position reset"
				playerX = 1
				playerZ = 1
				playerY = 1
			#end if
		#end if
		elif "turn" in instruction: #Ex turn.right
			#The player wishes to turn in one of the two directions
			print "Work in progress"
		#end if
		elif "place" in instruction: #Ex place.forward
			#The player wishes to place an object in one of the four directions
			placeList = instruction.split(".")
			direction = placeList[1]
			
			if direction == "forward":
				blockX = playerX + 1
				compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "back":
				blockX = playerX - 1
				compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "left":
				blockZ = playerZ - 1
				compiledBlock = "%s.%s.%s" % (playerZ, playerY, blockZ)
			elif direction == "right":
				blockZ = playerZ + 1
				compiledBlock = "%s.%s.%s" % (playerZ, playerY, blockZ)
			#end if
			
			#Add compiledBlock to the total blocklist
			if compiledBlock not in blockList:
				blockList.append(compiledBlock)
			else:
				print "Block already in that location"
		#end if
		elif instruction == "shoot": #Ex shoot
			#The player wishes to shoot forward
			print "Work in progress"
		#end if
		elif instruction == "end.game":
			#Prompt for save - not yet functional
			savePrompt = str(raw_input("Would you like to save (Y or N): ").lower())
			if savePrompt == 'n':
				return
			else:
				Save(playerX, playerZ, blockList)

def Save(playerX, playerZ, blockList):
    #Open player info file
    file = open("player.txt", "w")
    file.write(str(playerX) + "\n") #Newline will be stripped later
    file.write(str(playerZ))
    file.close()

    #Open world info file
    file = open("gameinfo.txt", "w")
    file.write(str(blockList))
    file.close()
Main()
