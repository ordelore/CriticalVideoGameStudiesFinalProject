import pygame, util
class MapScreen:
	def __init__(self, surface, scale):
		self.image = util.loadImage("Classroom No Sprites.png", "Rooms", scale)
		self.position = (0,0)
		
	def blitMap(self, surface):
		surface.blit(self.image, self.position)
	
	def shiftScreen(self, offset):
		ogPosition0 = self.position[0]
		ogPosition1 = self.position[1]
		self.position = (ogPosition0 + offset[0], ogPosition1 + offset[1])
	
	def get_position(self):
		return self.position
