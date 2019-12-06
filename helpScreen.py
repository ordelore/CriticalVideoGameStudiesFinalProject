import pygame, os, util
import pygame.font
class HelpScreen:
	def __init__(self, scale):
		self.helpText = "This is currently placeholder text. Eventually, there will be instructions and controls"
		self.helpFont = util.loadFont("GraffitiPaintBrush.ttf", int(scale * 15))
		self.fontColor = util.white
	#code for multiline text rendering is adapted from
	#https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
	def drawHelp(self, surface):
		words = [word.split(' ') for word in self.helpText.splitlines()]  # 2D array where each row is a list of words.
		space = self.helpFont.size(' ')[0]  # The width of a space.
		max_width, max_height = surface.get_size()
		#start in upper left
		pos = (0,0)
		x, y = pos
		for line in words:
			for word in line:
				word_surface = self.helpFont.render(word, 0, self.fontColor)
				word_width, word_height = word_surface.get_size()
				if x + word_width >= max_width:
					x = pos[0]  # Reset the x.
					y += word_height  # Start on new row.
				surface.blit(word_surface, (x, y))
				x += word_width + space
			x = pos[0]  # Reset the x.
			y += word_height  # Start on new row.
