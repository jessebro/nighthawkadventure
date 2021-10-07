import os
import copy
import pickle
from functions.utils import input_stuff
from pygame import mixer
from functions.utils import clear
from functions.utils import Color
from functions.utils import colour_it

settings = {
	"music": 10,
	"difficulty": {
		"name": "Fair Fight",
		"health_mult": 1,
		"accuracy_mult": 1,
		"rests": True
	},
	"immersion": "ON"
}


def custom_difficulty():
	settings["difficulty"]["name"] = "Custom"
	settings["difficulty"]["health_mult"] = float(input("""Enter a health multiplier (e.g. entering 2 will give enemies double health)
> """))
	settings["difficulty"]["accuracy_mult"] = float(input("""Enter an accuracy multiplier (e.g. entering 2 will give enemies double accuracy)
> """))
	settings["difficulty"]["rests"] = input_stuff("""Do you want rests enabled? (y/n)
> """, ["y", "n"]) == "y"


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
2. Difficulty [{difficulty["name"]}]
3. Immersive Scripts [{immersion}]
4. Cancel
> """, ["1", "2", "3", "4"])
		if choice:
			if choice == "1":
				settings["music"] = int(input_stuff("""Enter volume 1-10
> """, map(str, range(0,11))))
				mixer.music.set_volume(settings["music"] / 10)
			elif choice == "2":
				clear()
				difficulties = ["Storybook", "Fair Fight", "Warrior's Path", "The Walk of Death", "Custom"]
				mults = [0.7, 1.0, 1.3, 1.7]
				choice = int(input_stuff(f"""{colour_it("~ THE NIGHTHAWK ~", Color.RED)}
1. Storybook. Enemies have reduced health and accuracy. Enjoy the story, and hasten the battles.
2. Fair Fight. Presents a small challenge. Balanced combat.
3. Warrior's Path. Enemies have increased health and accuracy. For those that lust after challenges.
4. The Walk of Death. Enemies have increased health and accuracy, can score critical hits, and rests are disable. For the most hardcore players.
5. Custom. Choose exactly how the difficulty functions.
6. Exit.
> """, ["1", "2", "3", "4", "5", "6"]))
				if choice == 6:
					continue
				else:
					settings["difficulty"]['name'] = difficulties[choice - 1]
					if choice == 5:
						custom_difficulty()
					else:
						settings["difficulty"]["health_mult"] = mults[choice - 1]
						settings["difficulty"]["accuracy_mult"] = mults[choice - 1]
					if choice == 4:
						settings["difficulty"]["rests"] = False
			elif choice == "3":
				if settings["immersion"] == "ON":
					settings["immersion"] = "OFF"
				else:
					settings["immersion"] = "ON"
			elif choice == "4":
				save_settings()
				return
			choice = False


def check_settings():
	return settings
