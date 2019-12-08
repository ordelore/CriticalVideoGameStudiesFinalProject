import pygame, util

class Character():
	def __init__(self, surface, scale):
		super().__init__()
		self.scale = scale
		scaleSize = scale * 0.05
		leftImage = util.loadImage("Avatar Left.png", "Characters", scaleSize)
		upImage = util.loadImage("Avatar Back.png", "Characters", scaleSize)
		rightImage = util.loadImage("Avatar Right.png", "Characters", scaleSize)
		downImage = util.loadImage("Avatar Front.png", "Characters", scaleSize)
		self.screenWidth, self.screenHeight = surface.get_size()
		
		self.imageArray = [leftImage, rightImage, upImage, downImage]
		
		self.changeDirection(3)
		
	def changeDirection(self, direction):
		#direction is
		#0: left
		#1: right
		#2: up
		#3: down
		if (0 <= direction <= 3):
			self.direction = direction
			self.image = self.imageArray[direction]
			playerWidth, playerHeight = self.image.get_size()
			positionX = int(self.screenWidth / 2 - playerWidth / 2)
			positionY = int(self.screenHeight / 2 - playerHeight / 2)
			self.position = (positionX, positionY)
			self.rect = pygame.Rect(self.position, (self.image.get_width(), self.image.get_height()))
			
	def drawCharacter(self, surface):
		surface.blit(self.image, self.position)

	def detectCollision(self, otherRect):
		return self.rect.colliderect(otherRect)
	
	def getCollisionDialogue(self, otherNPCs):
		#this si going to be like seeing that if the player moved forward and collided, what npc would they collide with? and then return that NPCs line of dialogue
		#otherwise, return an empty string
		if (self.direction == 0):
			mapShift = (self.scale,0)
		elif (self.direction == 1):
			mapShift = (-self.scale,0)
		elif (self.direction == 2):
			mapShift = (0,self.scale)
		elif (self.direction == 3):
			mapShift = (0,-self.scale)
		
		futurePosition = (self.position[0] - mapShift[0], self.position[1] - mapShift[1])
		futureRect = pygame.Rect(futurePosition, (self.rect.width, self.rect.height))
		for nonplayer in otherNPCs:
			if futureRect.colliderect(nonplayer.get_rect()):
				return nonplayer.get_dialogue()
		return None

		#for i in range(len(otherNPCs)):
			
	def willCollide(self, offset, rectList, direction):
		futurePosition = (self.rect.x - offset[0], self.rect.y - offset[1])
		futureImage = self.imageArray[direction]
		futureRect = pygame.Rect(futurePosition, futureImage.get_size())
		for npcRect in rectList:
			if futureRect.colliderect(npcRect):
				return False
		return True
