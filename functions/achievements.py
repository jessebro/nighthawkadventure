import pickle
import copy
import os
from functions.utils import print_stuff
from functions.utils import colour_it
from functions.utils import Color


achievements = {
	"resourceful": {
		"name": "Resourceful",
		"description": "Complete a combat encounter without using items.",
		"completed": "You completed a combat encounter without using items.",
		"unlocked": False
	},
	"untouchable": {
		"name": "Untouchable",
		"description": "Complete a combat encounter of three or more enemies without taking damage.",
		"completed": "You complete a combat encounter of three or more enemies without taking damage.",
		"unlocked": False
	},
	"body_count": {
		"name": "Body Count",
		"description": "Defeat a group of two or more enemies in the same amount of turns.",
		"completed": "You defeated a group of two or more enemies in the same amount of turns.",
		"unlocked": False
	}
}

def save_achievements():
	global achievements
	data = copy.deepcopy(achievements)
	with open(f'Achievements.dat', 'wb') as f:
			pickle.dump(data, f, protocol=2)


def get_achievement(gained):
	global achievements
	achievements[gained]['unlocked'] = True


def load_achievements():
	global achievements
	with open(f'Achievements.dat', 'rb') as f:
		data = pickle.load(f)
	achievements = copy.deepcopy(data)


def view_achievements():
	global achievements
	load_achievements()
	view = ""
	for achievement in achievements:
		if achievements[achievement]['unlocked']:
			view = view + f"""~{colour_it(achievements[achievement]['name'], Color.GREEN)}~
{achievements[achievement]['completed']}

"""
		else:
			view = view + f"""~{colour_it(achievements[achievement]['name'], Color.RED)}~
{achievements[achievement]['description']}

"""
	print_stuff([view])




