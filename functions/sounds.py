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
	if type == "human":
		song = "music/Sworddancers.ogg"
	else:
		song = "music/Song of the Nighthawk.ogg"
	play(song)


def end_combat():
	play_combat_end("music/Combat_End.ogg")


def end_human():
	play_combat_end('music/Sworddancers end.ogg')


def dungeon():
	play("music/Forsaken Halls.ogg")


def title():
	play("music/A Blade and a Bag.ogg")


def travel():
	play("music/The Winding Road.ogg")


def town():
	play("music/City of Sails.ogg")


def night():
	play("music/A Deep Sky.ogg")


def dire():
	play("music/Dire Circumstances.ogg")


def doom():
	play("music/Approaching Doom.ogg")


def end_boss():
	play_combat_end("music/Boss_End.ogg")


def jungle():
	play("music/Jungle of Mysteries.ogg")


def fairy():
	play("music/Whispering Fairies.ogg")


def village():
	play("music/Haven of Humanity.ogg")


def level_up():
	play("music/Level Up.ogg", loop=1)


def play_combat_end(song):
	play(song, loop=1, fade=0)


def play(song, loop=-1, fade=500):
	global playing
	combat_songs = ('music/Sworddancers.ogg', 'music/Song of the Nighthawk.ogg')
	if song in combat_songs and playing in combat_songs:
		return
	if song != "music/Level Up.ogg":
		playing = song
	pygame.init()
	mixer.init()
	mixer.music.fadeout(fade)
	mixer.music.load(song)
	mixer.music.play(loop)


def play_prev():
	play(playing, fade=0)
