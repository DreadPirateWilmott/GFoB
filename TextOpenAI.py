#Created by DreadPirateWilmott on November 14th 2013
#Current Version 0.0.1 - Please note that I do tend to comment alot on my code for future reference
"""The purpose of the main game is to give player control over an entity and have them fight with the
enemy AI. The entire game will take place on a 100x100 square platform with each player only being able
to move one space at a time. The main control functions of the game will include movement in 4 directions,
the ability to turn, the ability to shoot, and the ability to place an object to block shots."""
#import essential files
import time
import random
import math

def Main():
    playerX = 1
    playerZ = 1
    blockList = []
    while True: #Loop forever, there will be a command to end the game
        instruction = str(raw_input(": ").lower())
        if "move" in instruction: #Ex move.forward
            #The player wishes to move in one of the four directions
            print "Work in progress"
        #end if
        elif "turn" in instruction: #Ex turn.right
            #The player wishes to turn in one of the two directions
            print "Work in progress"
        #end if
        elif "place" in instruction: #Ex place.forward
            #The player wishes to place an object in one of the four directions
            print "Work in progress"
        #end if
        elif instruction == "shoot": #Ex shoot
            #The player wishes to shoot forward
            print "Work in progress"
        #end if
        elif instruction == "end.game":
            #Prompt for save - not yet functional
            savePrompt = str(raw_input("Would you like to save (Y or N): ").lower())
            if(savePrompt == 'n'):
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
