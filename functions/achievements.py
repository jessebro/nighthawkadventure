import pickle
import copy
from functions.utils import print_stuff
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import clear


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
		"completed": "You completed a combat encounter of three or more enemies without taking damage.",
		"unlocked": False
	},
	"body_count": {
		"name": "Body Count",
		"description": "Defeat a group of three or more enemies in the same amount of turns.",
		"completed": "You defeated a group of three or more enemies in the same amount of turns.",
		"unlocked": False
	},
	"knife_master": {
		"name": "Knife Master",
		"description": "Kill an enemy using only knives.",
		"completed": "You killed an enemy using only knives.",
		"unlocked": False
	},
	"counter_kill": {
		"name": "Counter Kill",
		"description": "Defeat a group of two or more enemies using only Counter Parry.",
		"completed": "You defeated a group of two or more enemies using only Counter Parry.",
		"unlocked": False
	},
	"back_for_more": {
		"name": "Back for More",
		"description": "Drop to 0 health three times in the same combat encounter... and win.",
		"completed": "You dropped to 0 health three times in the same combat encounter... and won.",
		"unlocked": False
	},
	"bleed_out": {
		"name": "Bleed Out",
		"description": "Kill an enemy with bleeding damage.",
		"completed": "You killed an enemy with bleeding damage.",
		"unlocked": False
	},
	"jack_of_all_trades": {
		"name": "Jack of all Trades",
		"description": "Complete a combat encounter with at least one strike, parry, and distract.",
		"completed": "You completed a combat encounter with at least one strike, parry, and distract.",
		"unlocked": False
	},
	"swordmaster": {
		"name": "Swordmaster",
		"description": "Complete a combat encounter while using at least three different strikes.",
		"completed": "You completed a combat encounter while using at least three different strikes.",
		"unlocked": False
	},
	"teamwork": {
		"name": "Teamwork",
		"description": "Kill an enemy while an ally has either goaded or distracted them.",
		"completed": "You killed an enemy while an ally has either goaded or distracted them",
		"unlocked": False
	},
}

backup = copy.deepcopy(achievements)

def save_achievements():
	global achievements
	data = copy.deepcopy(achievements)
	with open(f'Achievements.dat', 'wb') as f:
			pickle.dump(data, f, protocol=2)


def get_achievement(gained):
	global achievements
	if achievements[gained]['unlocked'] != True:
		achievements[gained]['unlocked'] = True
		print_stuff([f'''{colour_it(f"Achievement Unlocked: {achievements[gained]['name']}!", Color.YELLOW)}'''])
		save_achievements()
	else:
		return


def load_achievements():
	global achievements
	with open(f'Achievements.dat', 'rb') as f:
		data = pickle.load(f)
	achievements = copy.deepcopy(data)


def view_achievements():
	global achievements
	global backup
	clear()
	print(f"""{colour_it("~ THE NIGHTHAWK ~", Color.RED)}
""")
	keys = achievements.keys()
	load_achievements()
	if achievements.keys() != keys:
		for achievement in achievements:
			if achievements[achievement]['unlocked']:
				backup[achievement]['unlocked'] = True
		achievements = copy.deepcopy(backup)
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
	print(view)
	print_stuff([''])




