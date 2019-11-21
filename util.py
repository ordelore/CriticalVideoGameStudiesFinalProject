import pygame, os

black = [0,0,0]
white = [255,255,255]
green = [0,255,0]
def checkForQuit(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True

def loadImage(spriteName, scale):
		sprite = pygame.image.load(os.path.join("sprites", spriteName))
		newSize = tuple([int(scale*x) for x in sprite.get_size()])
		return pygame.transform.scale(sprite, newSize)
