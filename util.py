import pygame, os

black  	  = [0,0,0]
white  	  = [255,255,255]

red    	  = [255,0,0]
yellow 	  = [255,255,0]
green  	  = [0,255,0]
greenBlue = [0,255,255]
blue   	  = [0,0,255]
purple 	  = [255,0,255]

rainbow = (red,yellow,green,greenBlue,blue,purple)

def getRainbow(index):
	return rainbow[index % len(rainbow)]
	
def checkForQuit(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True

def loadImage(spriteName, scale):
		sprite = pygame.image.load(os.path.join("sprites", spriteName))
		newSize = tuple([int(scale*x) for x in sprite.get_size()])
		return pygame.transform.scale(sprite, newSize)
