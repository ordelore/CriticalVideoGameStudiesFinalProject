import player, pygame, sys, util, mainMenu
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
	
	isMainMenu = True
	isGamePlay = False
	isPlayerInitialized = False
	canPressLeft = True
	canPressRight = True
	
	while (True):
		if (util.checkForQuit(pygame.event.get())):
			pygame.quit()
			sys.exit()
		#handle input section
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_LEFT]):
			leftPressed = True
		else:
			leftPressed = False
		
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
		#if main menu, do main menu stuff
			#if horizontal arrows pressed
				#update which menu option is highlighted
			#if z is pressed
				#update which screen should be shown now
		#if help screen
			#if enter pressed
				#go back to main menu
		#if options screen
			#vertical arrows
				#select different options
			#horizontal arrows
				#adjust sliders/options
		#otherwise, do main game stuff
			#this will be like character movement, maybe two extra buttons for attacking/blocking
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
		if (isGamePlay):
			if (not(isPlayerInitialized)):
				mainCharacter = player.Player(gameScreen)
				
		#handle drawing things
		#draw everything onto a single surface, then blit that surface onto the screen at the end
		#the drawing should only occur at the fastest 60 times per second
			#if the loop is running faster than that, don't draw anythin
		#if main menu, do main menu stuff
				#clear the screen and draw the main menu
				#at this point, it's a basic main menu
				# [title] centered on the top
				# [Play] and [Help] and [Options] centered on the bottom
		#if help screen
			#if help has not been drawn to the screen yet
				#draw the help text
				#include that the player should press [Enter] to return to the main menu
		#otheriwse, do main game stuff
		currentTime = pygame.time.get_ticks()
		if (currentTime - previousFrame > timeBetweenFrames):
			previousFrame = currentTime
			gameScreen.fill((0,0,0))
			#time to draw a new frame
			if (isMainMenu):
				menu.drawMainMenu(gameScreen)
			if (isGamePlay):
				mainCharacter.drawCharacter(gameScreen)
			
			pygame.display.update()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
