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
		self.attackImage = util.loadImage("Avatar Attack.png", "Characters", scaleSize)
		
		hurtLeftImage = util.loadImage("Avatar Left Damaged.png", "Characters", scaleSize)
		hurtUpImage = util.loadImage("Avatar Back Damaged.png", "Characters", scaleSize)
		hurtRightImage = util.loadImage("Avatar Right Damaged.png", "Characters", scaleSize)
		hurtDownImage = util.loadImage("Avatar Front Damaged.png", "Characters", scaleSize)
		
		self.attackImage = util.loadImage("Avatar Attack.png", "Characters", scaleSize)
		self.screenWidth, self.screenHeight = surface.get_size()
		self.attacking = False
		self.imageArray = [leftImage, rightImage, upImage, downImage]
		self.burnedArray = [hurtLeftImage, hurtRightImage, hurtUpImage, hurtDownImage]
		self.cooldownCounter = -1
		self.isBurned = False
		self.changeDirection(3)
		self.lives = 3
		self.dead = False
		self.burnedCounter = 0
	#need to rework how attacking works
	def attack(self):
		if (self.cooldownCounter <= 0):
			self.cooldownCounter = 30
			self.attacking = True
		
	def isAttacking(self):
		return self.attacking
	def get_attackRect(self):
		attackRect = self.attackImage.get_rect()
		return pygame.Rect(self.attackPosition, (attackRect.width, attackRect.height))
	def setCoolDown(self):
		self.attacking = False
		self.cooldownCounter = 30
	def get_rect(self):
		size = self.image.get_size()
		return pygame.Rect(self.position, size)
	def changeDirection(self, direction):
		#direction is
		#0: left
		#1: right
		#2: up
		#3: down
		if (0 <= direction <= 3):
			self.direction = direction
			if (not(self.isBurned)):
				self.image = self.imageArray[direction]
			else:
				self.burnedCounter -= 1
				self.image = self.burnedArray[direction]
				if (self.burnedCounter <= 0):
					self.isBurned = False
			playerWidth, playerHeight = self.image.get_size()
			positionX = int(self.screenWidth / 2 - playerWidth / 2)
			positionY = int(self.screenHeight / 2 - playerHeight / 2)
			
			attackPositionX = positionX + playerWidth
			attackPositionY = positionY + playerHeight // 2
			
			self.attackPosition = (attackPositionX, attackPositionY)
			self.position = (positionX, positionY)
			self.rect = pygame.Rect(self.position, (self.image.get_width(), self.image.get_height()))
	def get_position(self):
		return self.position
	def damage(self):
		if (not(self.isBurned)):
			self.lives -= 1
			self.isBurned = True
			self.burnedCounter = 30
		if (self.lives == 0):
			self.dead = True
	def isDead(self):
		return self.dead
	def drawCharacter(self, surface):
		if (self.attacking):
			surface.blit(self.attackImage, self.attackPosition)
		if (self.cooldownCounter > 0):
			self.cooldownCounter -= 0.5
		elif (self.attacking):
			self.setCoolDown()
				
		surface.blit(self.image, self.position)

	def detectCollision(self, otherRect):
		return self.rect.colliderect(otherRect)
	
	def getCollisionDialogue(self, otherNPCs, isBeforeDialogue):
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
				return nonplayer.get_dialogue(isBeforeDialogue)
		return None

		#for i in range(len(otherNPCs)):
			
	def willCollide(self, offset, rectList, direction):
		futureImage = self.imageArray[direction]
		
		positionX = int(self.screenWidth / 2 - futureImage.get_width() / 2)
		positionY = int(self.screenHeight / 2 - futureImage.get_height() / 2)
		
		futurePosition = (positionX - offset[0], positionY - offset[1])
		playerWidth, playerHeight = futureImage.get_size()
		futureRect = pygame.Rect(futurePosition, futureImage.get_size())
		for npcRect in rectList:
			if futureRect.colliderect(npcRect):
				return False
		return True
