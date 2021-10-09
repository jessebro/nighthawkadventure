from pygame import mixer
import pygame
from functions import settings

playing = ""
settings.load_settings()

mixer.init()
mixer.music.set_volume(settings.settings["music"] / 10)

def get_volume():
	volume = settings.check_settings()
	volume = volume["music"]
	return volume

def play_combat(type):
	global playing
	if type == "human":
		play = "music/Sworddancers.ogg"
	else:
		play = "music/Song of the Nighthawk.ogg"
	if playing == "fighty":
		return
	playing = "fighty"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load(play)
	mixer.music.play(-1)


def end_combat():
	global playing
	if playing == "music/Combat_End.ogg":
		return
	playing = "music/Combat_End.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	mixer.music.load('music/Combat_End.ogg')
	mixer.music.play()


def end_human():
	global playing
	if playing == "music/Sworddancers end.ogg":
		return
	playing = "music/Sworddancers end.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	mixer.music.load('music/Sworddancers end.ogg')
	mixer.music.play()


def dungeon():
	global playing
	if playing == "music/Forsaken Halls.ogg":
		return
	playing = "music/Forsaken Halls.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/Forsaken Halls.ogg')
	mixer.music.play(-1)


def title():
	global playing
	if playing == "music/A Blade and a Bag.ogg":
		return
	playing = "music/A Blade and a Bag.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/A Blade and a Bag.ogg')
	mixer.music.play(-1)


def travel():
	global playing
	if playing == "music/The Winding Road.ogg":
		return
	playing = "music/The Winding Road.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/The Winding Road.ogg')
	mixer.music.play(-1)


def town():
	global playing
	if playing == "music/City of Sails.ogg":
		return
	playing = "music/City of Sails.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/City of Sails.ogg')
	mixer.music.play(-1)


def night():
	global playing
	if playing == "music/A Deep Sky.ogg":
		return
	playing = "music/A Deep Sky.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/A Deep Sky.ogg')
	mixer.music.play(-1)


def dire():
	global playing
	if playing == "music/Dire Circumstances.ogg":
		return
	playing = "music/Dire Circumstances.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/Dire Circumstances.ogg')
	mixer.music.play(-1)


def doom():
	global playing
	if playing == "music/Approaching Doom.ogg":
		return
	playing = "music/Approaching Doom.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/Approaching Doom.ogg')
	mixer.music.play(-1)


def end_boss():
	global playing
	if playing == "music/Boss_End.ogg":
		return
	playing = "music/Boss_End.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	mixer.music.load('music/Boss_End.ogg')
	mixer.music.play()


def jungle():
	global playing
	if playing == "music/Jungle of Mysteries.ogg":
		return
	playing = "music/Jungle of Mysteries.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/Jungle of Mysteries.ogg')
	mixer.music.play(-1)


def fairy():
	global playing
	if playing == "music/Whispering Fairies.ogg":
		return
	playing = "music/Whispering Fairies.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/Whispering Fairies.ogg')
	mixer.music.play(-1)


def village():
	global playing
	if playing == "music/Haven of Humanity.ogg":
		return
	playing = "music/Haven of Humanity.ogg"
	pygame.init()
	mixer.init()
	mixer.music.fadeout(500)
	mixer.music.load('music/Haven of Humanity.ogg')
	mixer.music.play(-1)


def level_up():
	global playing
	pygame.init()
	mixer.init()
	mixer.stop()
	mixer.music.load('music/Level Up.ogg')
	mixer.music.play()


def play_prev():
	mixer.music.load(playing)
	mixer.music.play(-1)
