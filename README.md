Goblins: Fortress of Blood
==========

Testing AI systems in a text based game coded by me, written in python.
The first few version released onto github will be barebones, no AI programs, but in around a week I plan on releasing the
final version before the AI will begin being developed.

Please note that I am new to python, and programming in general, I am young and prone to mistakes which I hope you will forgive.

Part of this project is to see how many consecutive days I can contribute to the project with my goal being one month. 

New as of 11/16/2013
====================
Alot of the movement functionality has been added though the AI has not been added at all. Most recent is the ability to
turn and climb. The climbing ability to is activated if there is a block infront of you, and you will not fall as long as long
as their is a block forward and down one block, or below you.

Commands
========
Primary command = move

Seconday commands = .forward
                  = .back
                  = .left
                  = .right
                  
++++++++++++++++++++++++    
Primary command = place

Secondary commands = .forward
                   = .back
                   = .left
                   = .right
				   = .up
				   = .down
				   
Tertiary command = .(distance), this can be up to four blocks

++++++++++++++++++++++++
Primary command = turn

Secondary command = .right
                  = .left

++++++++++++++++++++++++
Primary command = dig

Secondary command = .forward
							= .back
							= .right
							= .left
							= .up
							= .down
							
Tertiary command = .(distance), this can be up to four blocks

++++++++++++++++++++++++
Primary command = shoot

#There are no secondary commands, the command makes you shoot forward, where you aim depends on the direction
#you are facing.
