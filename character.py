import pygame, util

class Character(pygame.sprite.Sprite):
    def __init__(self, surface, scale):
        super().__init__()
        self.image = util.loadImage("redBlueSprite", scale * 0.1)
        width, height = surface.get_size()
        playerWidth, playerHeight = self.image.get_size()
        positionX = int(width / 2 - playerWidth / 2)
        positionY = int(height / 2 - playerHeight / 2)
        self.position = (positionX, positionY)
        self.rect = self.image.get_rect() 

    def drawCharacter(self, surface):
        surface.blit(self.sprite, self.position)

    def detectCollision(self, otherSprite):
        return self.rect.colliderect(otherSprite.rect)
        