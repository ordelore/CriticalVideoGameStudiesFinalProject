import pygame


def checkForQuit(events):
	for event in events:
		if event.type == pygame.QUIT:
			return True
