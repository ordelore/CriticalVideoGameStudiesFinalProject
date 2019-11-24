import pygame, util

class Player:
	def __init__(self, surface, scale):
		self.sprite = util.loadImage("redBlueSprite", scale * 0.1)
		
		width, height = surface.get_size()
		playerWidth, playerHeight = self.sprite.get_size()
		positionX = int(width / 2 - playerWidth / 2)
		positionY = int(height / 2 - playerHeight / 2)
		self.position = (positionX, positionY)
	
	def drawCharacter(self, surface):
		surface.blit(self.sprite, self.position)
		
