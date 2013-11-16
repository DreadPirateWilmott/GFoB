#Created by DreadPirateWilmott on November 14th 2013
#Current Version 0.0.1 - Please note that I do tend to comment a lot on my code for future reference
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
	playerY = 1
	faceDir = 1 #The direction that you are facing; defaults to forward being + on the X
	compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
	blockList = [] #Format for blocklist is the X coordinate. Y coordinate. Z coordinate
	while True: #Loop forever, there will be a command to end the game
		print "Current Pirate position is %s X, %s Y, and %s Z" % (playerX, playerY, playerZ)
		instruction = str(raw_input(": ").lower())
		if "move" in instruction: #Ex move.forward
			#The player wishes to move in one of the four directions
			moveList = instruction.split(".")
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
				print "Pirate fell one space"
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
				faceDir = 1
			#end if
		#end if
		elif "turn" in instruction: #Ex turn.right
			#The player wishes to turn in one of the two directions
			#1 = X+, 2 = Z+, 3 = X-, 4 = Z-
			directionList = instruction.split(".")
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
			placeList = instruction.split(".")
			direction = placeList[1]
			
			if direction == "forward":
				if faceDir == 1:
					blockX = playerX + 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 2:
					blockZ = playerZ + 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 3:
					blockX = playerX - 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 4:
					blockZ = playerZ - 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
			elif direction == "back":
				if faceDir == 1:
					blockX = playerX - 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 2:
					blockZ = playerZ - 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 3:
					blockX = playerX + 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 4:
					blockZ = playerZ + 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
			elif direction == "left":
				if faceDir == 1:
					blockZ = playerZ - 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 2:
					blockX = playerX + 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 3:
					blockZ = playerZ + 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 4:
					blockX = playerX - 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "right":
				if faceDir == 1:
					blockZ = playerZ + 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 2:
					blockX = playerX - 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
				elif faceDir == 3:
					blockZ = playerZ - 1
					compiledBlock = "%s.%s.%s" % (playerX, playerY, blockZ)
				elif faceDir == 4:
					blockX = playerX + 1
					compiledBlock = "%s.%s.%s" % (blockX, playerY, playerZ)
			elif direction == "up":
				blockY = playerY + 1
				compiledBlock = "%s.%s.%s" % (playerX, blockY, playerZ)
			elif direction == "down" and playerY > 1:
				blockY = playerY - 1
				compiledBlock = "%s.%s.%s" % (playerX, blockY, playerZ)
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
			playerX = 1
			playerY = 1
			playerZ = 1
			blockList = []
			return
		
			#Open player info file
			file = open("player.txt", "w")
			compiledCo = "%s.%s.%s" % (playerX, playerY, playerZ)
			file.write(compiledCo)
			file.close()

			#Open world info file
			file = open("gameinfo.txt", "w")
			file.write(str(blockList))
			file.close()
		#end if
Main()
