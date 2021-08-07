from pygame import mixer
import pygame


def play_combat():
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Song of the Nighthawk.ogg')
	song.play(-1)


def end_combat():
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Combat_End.ogg')
	song.play()


def dungeon():
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Forsaken Halls.ogg')
	song.play(-1)


def title():
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/A Blade and a Bag.ogg')
	song.play(-1)


def travel():
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/The Winding Road.ogg')
	song.play(-1)




