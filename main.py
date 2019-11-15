import pygame, sys, util


def main(args):
	pygame.init()
	
	#scaling factor of game's window'
	scale = 2
	#tuple of game's window size'
	size = (int(scale * 320),int(scale * 240))
	#intialize the game screen and fill it with black
	gameScreen = pygame.display.set_mode(size)
	gameScreen.fill([0,0,0])
	pygame.display.update()
	
	
	previousFrameTime = 0
	timeBetweenFrames = 16
	while (True):
		if (util.checkForQuit(pygame.event.get())):
			pygame.quit()
			sys.exit()
		#handle input section
		#if main menu, do main menu stuff
			#if horizontal arrows pressed
				#update which menu option is highlighted
			#if enter is pressed
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
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
