import pygame, util
def get_npcs(sceneIndex):
	npcs = [[0]]
	return npcs[sceneIndex]
class NPC():
	
	def __init__(self, scale, npcIndex):
		npcs = ["Teacher"]
		npcDialogueBefore = ["I'm sorry to hear about what happened to Scott. You loved to play music together"]
		npcDialogueAfter  = ["You were going to be in a concert together. It's a shame we'll never hear it. I'll see you tomorrow"]
		npcPositions = [(160 * scale, 150 * scale)]
		angles = [2]
		scalings = [0.1]
		
		self.name = npcs[npcIndex]
		self.dialogueBefore = npcDialogueBefore[npcIndex]
		self.dialogueAfter = npcDialogueAfter[npcIndex]
		self.position = npcPositions[npcIndex]
		scaling = scalings[npcIndex] * scale
		self.images = []
		if (angles[npcIndex] != 2):
			leftImage = util.loadImage(self.name + " Left.png", "Characters", scaling)
			rightImage = util.loadImage(self.name + " Right.png", "Characters", scaling)
			self.images = [leftImage, rightImage]
		upImage = util.loadImage(self.name + " Back.png", "Characters", scaling)
		downImage = util.loadImage(self.name + " Front.png", "Characters", scaling)
		self.images.append(upImage)
		self.images.append(downImage)
		self.changeDirection(0)
	
	def changeDirection(self, direction):
		if (0 <= direction < len(self.images)):
			self.direction = direction
			self.image = self.images[direction]
			self.imageSize = (self.image.get_width(), self.image.get_height())
	def drawNPC(self, surface, offsetXY):
		self.onscreenPosition = (self.position[0] + offsetXY[0], self.position[1] + offsetXY[1])
		surface.blit(self.image, self.onscreenPosition)
	def get_rect(self):
		self.rect = pygame.Rect(self.onscreenPosition, self.imageSize)
		return self.rect
		
	def get_dialogue(self, isBeforeDungeon):
		return (self.dialogueAfter, self.dialogueBefore)[isBeforeDungeon]
	#functions we need: a collision detection, or something
	#return dialogue
