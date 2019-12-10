import pygame
import util
from random import randrange
from math import sqrt
from os.path import join

def calcVelocity(sourcePosition, target):
	velocity = (target[0] - sourcePosition[0], target[1] - sourcePosition[1])
	norm = sqrt((velocity[0] ** 2 + velocity[1] ** 2) / 2)
	velocity = list(map(lambda a : a / norm, velocity))
	#print(velocity)
	return velocity
		
class Enemy:
	def __init__(self, scale):
		self.position = (300 * scale,300 * scale)
		scaling = 0.05 * scale
		openImage = util.loadImage("Piano_OpenMouth.png", join("Monsters", "Piano"), scaling)
		closedImage = util.loadImage("Piano_ClosedMouth.png", join("Monsters", "Piano"), scaling)
		damagedImage = util.loadImage("Piano_PainAnimation.png", join("Monsters", "Piano"), scaling)
		self.wordFont = util.loadFont("Remix Regular.ttf", 20 * scale)
		self.images = [openImage, closedImage, damagedImage]
		self.currentImage = closedImage
		self.projectiles = []
		self.projectileCounter = 0
		self.lives = 3
		self.dead = False
	def isDead(self):
		return self.dead
	def fireProjectile(self, velocity, onscreenPos):
		words = ["Why", "If Only", "I'm Wrong", "What If", "I'm Sorry"]
		wordIndex = randrange(len(words))
		wordSurface = self.wordFont.render(words[wordIndex], True, util.lightYellowGreen)
		
		self.projectiles.append(Projectile(wordSurface, velocity, onscreenPos))
	
	def blitEnemy(self, screen, gameCharacter, offsetXY):
		
		playerPosition = gameCharacter.get_position()
		
		onscreenPosition = (self.position[0] + offsetXY[0], self.position[1] + offsetXY[1])
		velocity = calcVelocity(onscreenPosition, playerPosition)
		
		self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])
		onscreenPosition = (int(self.position[0] + offsetXY[0]), int(self.position[1] + offsetXY[1]))
		
		if (gameCharacter.isAttacking()):
			enemySize = self.currentImage.get_size()
			enemyPosition = onscreenPosition
			enemyRect = pygame.Rect(enemyPosition, enemySize)
			attackRect = gameCharacter.get_attackRect()
			if (enemyRect.colliderect(attackRect)):
				self.currentImage = self.images[2]
				
				self.lives -= 1
				gameCharacter.setCoolDown()
				if (self.lives == 0):
					self.dead = True
		screen.blit(self.currentImage, onscreenPosition)
		
		charRect = gameCharacter.get_rect()
		for projectile in self.projectiles:
			lifetime = projectile.blitProjectile(screen, offsetXY)
			projRect = projectile.get_rect()
			if (projRect.colliderect(charRect)):
				self.projectiles.remove(projectile)
				gameCharacter.damage()
			if (lifetime == 500):
				self.projectiles.remove(projectile)
		
		self.projectileCounter += 1
		if (self.projectileCounter % 50 == 10):
			self.fireProjectile(velocity, self.position)
		elif (self.projectileCounter % 50 == 0):
			self.currentImage = self.images[0]
		elif (self.projectileCounter % 50 == 20):
			self.currentImage = self.images[1]
		
class Projectile:
	def __init__(self, image, velocity, position):
		self.image = image
		self.velocity = velocity
		self.position = position
		self.lifetime = 0
	def get_rect(self):
		size = self.image.get_size()
		return pygame.Rect(self.previousOnscreen, size)
	def blitProjectile(self, surface, offsetXY):
		self.lifetime += 1
		newX = self.position[0] + self.velocity[0]
		newY = self.position[1] + self.velocity[1]
		self.position = (newX, newY)
		self.previousOnscreen = (int(self.position[0] + offsetXY[0]), int(self.position[1] + offsetXY[1]))
		surface.blit(self.image, self.previousOnscreen)
		return self.lifetime
