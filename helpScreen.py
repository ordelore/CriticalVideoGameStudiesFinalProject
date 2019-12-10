import pygame, os, util
import pygame.font
class HelpScreen:
	def __init__(self, scale):
		self.helpTextBefore = "Welcome to the Grief demo. This is a game about loss, and this demo implements a portion of this grander vision. Use the arrow keys to move around and use the \[Z\] button to interact with objects and NPCs. Press \[Z\] to return to the main menu."
		self.helpTextAfter = "Whether or not you think you won against the beast, the world pays you no attention. In fact, this demonstration of courage has taken energy away from you, but the world is not interested in helping you recover. It\'s up to you to decide how you want to approach your recovery."
		self.helpFont = util.loadFont("GraffitiPaintBrush.ttf", int(scale * 15))
		self.fontColor = util.white
	#code for multiline text rendering is adapted from
	#https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
	def drawHelp(self, surface, isAfter=True):
		if (not(isAfter)):
			text = self.helpTextBefore
		else:
			text = self.helpTextAfter
		words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
		space = self.helpFont.size(' ')[0]  # The width of a space.
		max_width, max_height = surface.get_size()
		#start in upper left
		pos = (0,0)
		x, y = pos
		for line in words:
			for word in line:
				word_surface = self.helpFont.render(word, True, self.fontColor)
				word_width, word_height = word_surface.get_size()
				if x + word_width >= max_width:
					x = pos[0]  # Reset the x.
					y += word_height  # Start on new row.
				surface.blit(word_surface, (x, y))
				x += word_width + space
			x = pos[0]  # Reset the x.
			y += word_height  # Start on new row.
