import os
import copy
import pickle
from functions.utils import input_stuff
from pygame import mixer
from functions.utils import clear
from functions.utils import print_stuff
from functions.utils import clear
from functions.utils import print_it
from functions.utils import Color
from functions.utils import colour_it

settings = {
	"music": 10,
	"difficulty": "Fair Fight",
	"immersion": "ON"
}


def save_settings():
	global settings
	data = copy.deepcopy(settings)
	with open(f'Settings.dat', 'wb') as f:
			pickle.dump(data, f, protocol=2)


def load_settings():
	global settings
	if os.path.isfile('Settings.dat'):
		with open(f'Settings.dat', 'rb') as f:
			data = pickle.load(f)
		settings = copy.deepcopy(data)


def get_settings():
	while True:
		music_status = settings["music"]
		difficulty = settings["difficulty"]
		immersion = settings["immersion"]
		clear()
		choice = input_stuff(f"""{colour_it("~ THE NIGHTHAWK ~", Color.RED)}
1. Music [{music_status}]
2. Difficulty [{difficulty}]
3. Immersive Scripts [{immersion}]
4. Cancel
> """, ["1", "2", "3", "4"])
		if choice:
			if choice == "1":
				settings["music"] = int(input_stuff("""Enter volume 1-10
> """, map(str, range(0,11))))
				mixer.music.set_volume(settings["music"] / 10)
			elif choice == "2":
				input_stuff("""1. Storybook. Enemies have reduced health and accuracy. Enjoy the story, and hasten the battles.
2. Fair Fight. Presents a small challenge. Balanced combat.
3. Warrior's Path. Enemies have increased health and accuracy. For those that lust after challenges.
4. The Walk of Death. Enemies have increased health and accuracy, can score critical hits, and rests are disable. For the most hardcore players.
5. Custom. Choose exactly how the difficulty functions.
6. Exit.
> """, ["1", "2", "3", "4", "5", "6"])
			elif choice == "3":
				settings[immersion] = "OFF"
			elif choice == "4":
				save_settings()
				return
			choice = False


def check_settings():
	return settings
