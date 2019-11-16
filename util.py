import pygame, os


def checkForQuit(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True

def loadImage(spriteName):
		sprite = pygame.image.load(os.path.join("sprites", spriteName))
		return sprite
