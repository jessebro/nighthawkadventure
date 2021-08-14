from pygame import mixer
import pygame

playing = ""


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
	mixer.fadeout(1000)
	song = pygame.mixer.Sound(play)
	song.play(-1)


def end_combat():
	global playing
	if playing == "music/Combat_End.ogg":
		return
	playing = "music/Combat_End.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Combat_End.ogg')
	song.play()


def end_human():
	global playing
	if playing == "music/Sworddancers end.ogg":
		return
	playing = "music/Sworddancers end.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Sworddancers end.ogg')
	song.play()


def dungeon():
	global playing
	if playing == "music/Forsaken Halls.ogg":
		return
	playing = "music/Forsaken Halls.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Forsaken Halls.ogg')
	song.play(-1)


def title():
	global playing
	if playing == "music/A Blade and a Bag.ogg":
		return
	playing = "music/A Blade and a Bag.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/A Blade and a Bag.ogg')
	song.play(-1)


def travel():
	global playing
	if playing == "music/The Winding Road.ogg":
		return
	playing = "music/The Winding Road.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/The Winding Road.ogg')
	song.play(-1)


def town():
	global playing
	if playing == "music/City of Sails.ogg":
		return
	playing = "music/City of Sails.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/City of Sails.ogg')
	song.play(-1)


def night():
	global playing
	if playing == "music/A Deep Sky.ogg":
		return
	playing = "music/A Deep Sky.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/A Deep Sky.ogg')
	song.play(-1)


def dire():
	global playing
	if playing == "music/Dire Circumstances.ogg":
		return
	playing = "music/Dire Circumstances.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Dire Circumstances.ogg')
	song.play(-1)


def doom():
	global playing
	if playing == "music/Approaching Doom.ogg":
		return
	playing = "music/Approaching Doom.ogg"
	pygame.init()
	mixer.init()
	mixer.fadeout(1000)
	song = pygame.mixer.Sound('music/Approaching Doom.ogg')
	song.play(-1)


def end_boss():
	global playing
	if playing == "music/Boss_End.ogg":
		return
	playing = "music/Boss_End.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Boss_End.ogg')
	song.play()


def jungle():
	global playing
	if playing == "music/Jungle of Mysteries.ogg":
		return
	playing = "music/Jungle of Mysteries.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Jungle of Mysteries.ogg')
	song.play(-1)


def fairy():
	global playing
	if playing == "music/Whispering Fairies.ogg":
		return
	playing = "music/Whispering Fairies.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Whispering Fairies.ogg')
	song.play(-1)


def village():
	global playing
	if playing == "music/Haven of Humanity.ogg":
		return
	playing = "music/Haven of Humanity.ogg"
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Haven of Humanity.ogg')
	song.play(-1)


def level_up():
	global playing
	pygame.init()
	mixer.init()
	mixer.stop()
	song = pygame.mixer.Sound('music/Level Up.ogg')
	song.play()


def play_prev():
	song = pygame.mixer.Sound("music/A Blade and a Bag.ogg")
	song.play(-1)
