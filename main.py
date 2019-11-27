import player, pygame, sys, util, mainMenu, helpScreen, mapScreen, character
import pygame.time


def main(args):
	pygame.init()
	
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
	
	isMainMenu = True
	isGamePlay = False
	isHelpMenu = False
	isPlayerInitialized = False
	isMapInitialized = False
	
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
				if (not(isPlayerInitialized)):
					mainCharacter = character.Character(gameScreen, scale)
					isPlayerInitialized = True
				if (not(isMapInitialized)):
					mainMap = mapScreen.MapScreen(gameScreen, scale)
					isMapInitialized = True
				#TODO: check for collision before moving the player
				if (leftPressed):
					mainMap.shiftScreen((scale,0))
				if (rightPressed):
					mainMap.shiftScreen((-scale,0))
				if (upPressed):
					mainMap.shiftScreen((0,scale))
				if (downPressed):
					mainMap.shiftScreen((0,-scale))
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
			if (isHelpMenu):
				helpMenu.drawHelp(gameScreen)
			pygame.display.update()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
