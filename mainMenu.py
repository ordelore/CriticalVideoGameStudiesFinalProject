import pygame, pygame.font, os, util
class Menu:
	def __init__(self, surface, titleName, scale):
		self.Title = titleName
		#highlight is the index of which icon is being highlighted
		self.highlighted = 0
		self.screenWidth = surface.get_width()
		
		self.mainFont = pygame.font.Font(os.path.join("fonts", "BLKCHCRY.TTF"), int(20 * scale))
		self.subFont = pygame.font.Font(os.path.join("fonts", "BLKCHCRY.TTF"), int(12 * scale))
		
		self.mainTitle = self.mainFont.render("Grief", True, util.white)
		self.startText = self.subFont.render("Start", True, util.white)
		self.helpText = self.subFont.render("Help", True, util.white, util.green)
		self.optionsText = self.subFont.render("Options", True, util.white)
		
		screenWidth, screenHeight = surface.get_size()
		
		titleWidth = self.mainTitle.get_width()
		self.titlePosition = (screenWidth / 2 - titleWidth / 2, 0)
		
		startW, startH = self.helpText.get_size()
		self.helpPosition = (int(screenWidth / 4 - startW / 2), screenHeight - startH)
		
		startW, startH = self.startText.get_size()
		self.startPosition = (int(screenWidth / 2 - startW / 2), screenHeight - startH)
		
		startW, startH = self.optionsText.get_size()
		self.optionsPosition = (int(3 * screenWidth / 4 - startW / 2), screenHeight - startH)
	
	def drawMainMenu(self, surface):
		surface.blit(self.mainTitle, self.titlePosition)
		surface.blit(self.helpText, self.helpPosition)
		surface.blit(self.startText, self.startPosition)
		surface.blit(self.optionsText, self.optionsPosition)
	
	def increaseHighlightIndex(self):
		self.unhighlight()
		if (self.highlighted < 2):
			self.highlighted += 1
		self.highlight()
			
	def decreaseHighlightIndex(self):
		self.unhighlight()
		if (self.highlighted > 0):
			self.highlighted -= 1
		self.highlight()
	
	def unhighlight(self):
		text = ("Help", "Start", "Options")[self.highlighted]
		textBox = self.subFont.render(text, True, util.white)
		if (self.highlighted == 0):
			self.helpText = textBox
		elif (self.highlighted == 1):
			self.startText = textBox
		else:
			self.optionsText = textBox

	def highlight(self):
		text = ("Help", "Start", "Options")[self.highlighted]
		textBox = self.subFont.render(text, True, util.white, util.green)
		if (self.highlighted == 0):
			self.helpText = textBox
		elif (self.highlighted == 1):
			self.startText = textBox
		else:
			self.optionsText = textBox
		
		
