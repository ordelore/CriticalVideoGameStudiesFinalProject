import pygame, util

class Player:
	def __init__(self, surface):
		self.sprite = util.loadImage("redBlueSprite")
		
		width, height = surface.get_size()
		playerWidth, playerHeight = self.sprite.get_size()
		positionX = int(width / 2 - playerWidth / 2)
		positionY = int(height / 2 - playerHeight / 2)
		self.position = (positionX, positionY)
	
	def drawCharacter(self, surface):
		surface.blit(self.sprite, self.position)
		
