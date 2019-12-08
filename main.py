import character
import pygame, sys
import util
import mainMenu
import helpScreen
import mapScreen
import pygame.time
import pygame.mixer
import dialogue
import npc

def main(args):
	pygame.init()
	pygame.mixer.init()
	#scaling factor of the game's window'
	scale = 2
	#tuple of game's window size'
	size = (int(scale * 320),int(scale * 240))
	#intialize the game screen and fill it with black
	gameScreen = pygame.display.set_mode(size)
	gameScreen.fill(util.black)
	pygame.display.update()
	
	previousFrame = 0
	timeBetweenFrames = 16
	
	menu = mainMenu.Menu(gameScreen, "Grief", scale)
	helpMenu = helpScreen.HelpScreen(scale)
	dialogueHandler = dialogue.Dialogue(gameScreen, scale)
	util.loadAudio("Background Sound.ogg")
	mainCharacter = character.Character(gameScreen, scale)
	mainMap = mapScreen.MapScreen(gameScreen, scale)
	
	NPCStoLoad = npc.get_npcs(0)
	npcList = []
	for notPlayer in NPCStoLoad:
		npcList.append(npc.NPC(scale, notPlayer))
	#dialogueHandler.initialize("Lorem ipsum and all that jazz. We know this is placeholder text")
	
	
	isMainMenu = True
	isGamePlay = False
	isHelpMenu = False
	isDialogue = False
	movementAllowed = True
	
	canPressLeft = True
	canPressRight = True
	canPressZ = True
	canPressX = True
	
	while (True):
		if (util.checkForQuit(pygame.event.get())):
			pygame.quit()
			sys.exit()
			
		currentTime = pygame.time.get_ticks()
		if (currentTime - previousFrame > timeBetweenFrames):
			previousFrame = currentTime
			
			#handle input section
			keys = pygame.key.get_pressed()
			if (keys[pygame.K_LEFT]):
				leftPressed = True
			else:
				leftPressed = False
			if (keys[pygame.K_ESCAPE]):
				#exit the game, also handle other stuff if necessary
				pygame.quit()
				sys.exit()
			if (keys[pygame.K_RIGHT]):
				rightPressed = True
			else:
				rightPressed = False
				
			if (keys[pygame.K_UP]):
				upPressed = True
			else:
				upPressed = False
			
			if (keys[pygame.K_DOWN]):
				downPressed = True
			else:
				downPressed = False
				
			if (keys[pygame.K_z]):
				zPressed = True
			else:
				zPressed = False
				
			if (keys[pygame.K_x]):
				xPressed = True
			else:
				xPressed = False
			#if options screen
				#vertical arrows
					#select different options
				#horizontal arrows
					#adjust sliders/options
			#otherwise, do main game stuff
				#this will be like character movement, maybe two extra buttons for doing things
					#z for interacting with objects
					#x for nothing in the overworld, or for canceling selections
						#might not even need x
				#if an option is presented
					#handle selection
			if (isMainMenu):
				if (leftPressed and canPressLeft):
					menu.decreaseHighlightIndex()
					canPressLeft = False
				elif (not(leftPressed or canPressLeft)):
					canPressLeft = True
					
				if (rightPressed and canPressRight):
					menu.increaseHighlightIndex()
					canPressRight = False
				elif (not(rightPressed or canPressRight)):
					canPressRight = True
				
				if (zPressed and canPressZ):
					positionIndex = menu.getPosition()
					if (positionIndex == 0): #help
						isMainMenu = False
						isHelpMenu = True
						canPressZ = False
					elif (positionIndex == 1): #start game
						isMainMenu = False
						canPressZ = False
						isGamePlay = True
				elif (not(zPressed or canPressZ)):
					canPressZ = True
					
			if (isHelpMenu):
				if (zPressed and canPressZ):
					isMainMenu = True
					isHelpMenu = False
					canPressZ = False
				elif (not(zPressed or canPressZ)):
					canPressZ = True
					
			if (isGamePlay):
				if (movementAllowed):
					if (leftPressed or rightPressed or upPressed or downPressed):
						npcRects = list(map(lambda a : a.get_rect(), npcList))
						if (leftPressed):
							mapShift = (scale,0)
							newDirection = 0
						if (rightPressed):
							mapShift = (-scale,0)
							newDirection = 1
						if (upPressed):
							mapShift = (0,scale)
							newDirection = 2
						if (downPressed):
							mapShift = (0,-scale)
							newDirection = 3
						#TODO: Set up bounds on the screen
						if (mainCharacter.willCollide(mapShift, npcRects, newDirection)):
							mainMap.shiftScreen(mapShift)
							mainCharacter.changeDirection(newDirection)
					if (zPressed and canPressZ): #maybe dialogue
						potentialDialogue = mainCharacter.getCollisionDialogue(npcList)
						if (potentialDialogue != None):
							dialogueHandler.initialize(potentialDialogue)
							done = False
							isDialogue = True
							movementAllowed = False
					elif (not(zPressed)):
						canPressZ = True
			#if z is pressed, check for collision IN FRONT of where the player is
			#handle drawing things
			#draw everything onto a single surface, then blit that surface onto the screen at the end
			#the drawing should only occur at the fastest 60 times per second
				#if the loop is running faster than that, don't draw anythin
			#otheriwse, do main game stuff
		
			gameScreen.fill(util.black)
			#time to draw a new frame
			if (isMainMenu):
				menu.drawMainMenu(gameScreen)
			if (isGamePlay):
				mainMap.blitMap(gameScreen)
				mainCharacter.drawCharacter(gameScreen)
				if (isDialogue):
					if (zPressed and not(done)):
						done = dialogueHandler.iterate(gameScreen, True)
					else:
						done = dialogueHandler.iterate(gameScreen, False)
					if (done and zPressed and canPressZ):
						print("dialogue done")
						isDialogue = False
						movementAllowed = True
						canPressZ = False
				mapOffset = mainMap.get_position()
				for notPlayer in npcList:
					notPlayer.drawNPC(gameScreen, mapOffset)
			if (isHelpMenu):
				helpMenu.drawHelp(gameScreen)
			pygame.display.update()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
