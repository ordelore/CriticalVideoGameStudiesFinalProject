import pygame
import pygame.font
import util
#try to keep dialogue length no greater than 2 lines at once
class Dialogue:
	def __init__(self, surface, scale):
		screenWidth = surface.get_width()
		self.boxHeight = 2 * (15 * scale)
		self.dlgFont = util.loadFont("monof55.ttf", int(scale * 12))
		self.padding = 2 * scale
		fontWidth = self.dlgFont.render(" ", False, util.white).get_width()
		self.maxChars = screenWidth // fontWidth
		
		
		
	def initialize(self, string):
		self.i = 0
		self.maxI = len(string) - 1
		
		fullRender = self.dlgFont.render(string, False, util.white)
		
		if (len(string) > self.maxChars):
			#find the first space BEFORE the maxChar limit and break the line
			checkAt = self.maxChars
			while (string[checkAt] != ' '):
				checkAt -= 1
			self.topLine = string[:checkAt]
			self.bottomLine = string[checkAt+1:]
			self.lines = 2
		else:
			self.topLine = string
			self.bottomLine = ""
			self.lines = 1

	def iterate(self, surface, fast=False):
		
		
		#don't center the text, just left-justify it
		boxWidth = surface.get_width()
		
		background = pygame.surface.Surface((boxWidth, self.boxHeight))
		background.fill(util.black)
		if (self.lines == 1 or self.i < len(self.topLine)):
			renderedText = self.dlgFont.render(self.topLine[:self.i], True, util.white)
			background.blit(renderedText, (self.padding, self.padding))
		else:
			topText = self.dlgFont.render(self.topLine, True, util.white)
			bottomText = self.dlgFont.render(self.bottomLine[:(self.i - len(self.topLine))], True, util.white)
			textHeight = topText.get_height()
			
			background.blit(topText,(self.padding, self.padding))
			background.blit(bottomText, (self.padding, self.padding + textHeight))
		screenHeight = surface.get_height()
		surface.blit(background, (0, screenHeight - self.boxHeight))
		
		
		if (self.i <= self.maxI):
			if (fast):
				self.i += 2
			else:
				self.i += 1
		
