from pygame import mixer
import pygame

playing = ""

def play_combat():
	global playing
	if playing == "combat":
		return
	playing = "combat"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Song of the Nighthawk.ogg')
	song.play(-1)


def end_combat():
	global playing
	if playing == "end_combat":
		return
	playing = "end_combat"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Combat_End.ogg')
	song.play()


def dungeon():
	global playing
	if playing == "dungeon":
		return
	playing = "dungeon"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Forsaken Halls.ogg')
	song.play(-1)


def title():
	global playing
	if playing == "title":
		return
	playing = "title"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/A Blade and a Bag.ogg')
	song.play(-1)


def travel():
	global playing
	if playing == "travel":
		return
	playing = "travel"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/The Winding Road.ogg')
	song.play(-1)


def town():
	global playing
	if playing == "town":
		return
	playing = "town"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/City of Sails.ogg')
	song.play(-1)


def night():
	global playing
	if playing == "night":
		return
	playing = "night"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/A Deep Sky.ogg')
	song.play(-1)
