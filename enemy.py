import pygame
import util
from random import randrange
from math import sqrt
from os.path import join

def calcVelocity(sourcePosition, target):
	velocity = (target[0] - sourcePosition[0], target[1] - sourcePosition[1])
	norm = sqrt(velocity[0] ** 2 + velocity[1] ** 2)
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
		self.currentImage = 0
		self.projectiles = []
		self.projectileCounter = 0
		
		
	def fireProjectile(self, velocity, onscreenPos):
		words = ["Why", "If Only", "I'm Wrong"]
		wordIndex = randrange(len(words))
		wordSurface = self.wordFont.render(words[wordIndex], True, util.lightYellowGreen)
		
		self.projectiles.append(Projectile(wordSurface, velocity, onscreenPos))
	
	def blitEnemy(self, screen, gameCharacter, offsetXY):
		
		playerPosition = gameCharacter.get_position()
		
		onscreenPosition = (self.position[0] + offsetXY[0], self.position[1] + offsetXY[1])
		velocity = calcVelocity(onscreenPosition, playerPosition)
		
		self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])
		onscreenPosition = (int(self.position[0] + offsetXY[0]), int(self.position[1] + offsetXY[1]))
		
		print("enemy position: ", onscreenPosition)
		screen.blit(self.images[self.currentImage], onscreenPosition)
		
		for projectile in self.projectiles:
			lifetime = projectile.blitProjectile(screen, onscreenPosition)
			if (lifetime == 300):
				self.projectiles.remove(projectile)
		
		self.projectileCounter += 1
		if (self.projectileCounter % 100 == 0):
			self.fireProjectile(velocity, onscreenPosition)
		
class Projectile:
	def __init__(self, image, velocity, position):
		self.image = image
		self.velocity = list(map(lambda a: a * 2, velocity))
		self.position = position
		self.lifetime = 0
	
	def blitProjectile(self, surface, offsetXY):
		self.lifetime += 1
		newX = int(self.position[0] + self.velocity[0])
		newY = int(self.position[1] + self.velocity[1])
		self.position = (newX, newY)
		print("projectile source: ", position)
		surface.blit(self.image, (self.position[0] + offsetXY[0], self.position[1] + offsetXY[1]))
		return self.lifetime
