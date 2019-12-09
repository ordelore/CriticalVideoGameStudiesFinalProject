import pygame, os
import pygame.font
from pygame import mixer
black  	  = [0,0,0]
white  	  = [255,255,255]

red    	  = [255,0,0]
yellow 	  = [255,255,0]
green  	  = [0,255,0]
greenBlue = [0,255,255]
blue   	  = [0,0,255]
purple 	  = [255,0,255]
lightYellowGreen = [189,255,75]

rainbow = (red,yellow,green,greenBlue,blue,purple)
musicNames = ["Background Theme.ogg", "Regret Theme.ogg", "Sad Theme.ogg", "Anger Theme.ogg"]

def getRainbow(index):
	return rainbow[index % len(rainbow)]
	
def checkForQuit(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True
def loadFont(name, size):
	return pygame.font.Font(os.path.join("fonts", name), size)
def loadImage(spriteName, subFolder, scale):
		sprite = pygame.image.load(os.path.join("sprites", subFolder, spriteName))
		newSize = tuple([int(scale*x) for x in sprite.get_size()])
		return pygame.transform.scale(sprite, newSize)

def loadAudio(nameIndex):
	mixer.music.stop()
	mixer.music.load(os.path.join("audio", musicNames[nameIndex]))
	mixer.music.play(-1)
