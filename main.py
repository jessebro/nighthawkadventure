from functions import ability
from functions import equipment
from functions import character
from functions import town
from functions import encounters
from functions import enemy_round
from functions import weapon
from functions import inventory
from functions.utils import print_stuff
from functions.loading import boot
from functions.utils import input_stuff
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import print_it
from functions import utils
import chapter2
from functions import sounds

sounds.title()

def set_default_actions():
	utils.default_actions = {
		"e": inventory.show,
		"i": inventory.show
	}


def run_adventure(steps):
	# Each step looks like this "module.function", e.g. "chapter1.hag_lair"
	for step in steps:
		# split on '.' give us a list, like this: ['chapter1', 'hag_lair']
		step_parts = step.split('.')
		# dynamically load the module in step_parts[0], e.g. 'chapter1' (step_module would now be chapter1 module)
		step_module = __import__(step_parts[0])
		# getattr loads a member of a module by name, e.g. get_attr(chapter1, 'hag_lair') - note the module is not a string, it is the actual module
		step_func = getattr(step_module, step_parts[1])
		step_func()


def new_game():
	character.get_name()
	character.get_gender()
	character.get_title()
	weapon.get_weapon_name()
	ability.get_ability()
	equipment.get_equipment()


def prologue():
	elfa = colour_it("Elfa", Color.NPC)
	micha = colour_it("Micha", Color.NPC)
	bertholt = colour_it("Bertholt Omar", Color.NPC)
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	lizardtongue = colour_it("Lizardtongue Mountains", Color.PLACE)
	corocana = colour_it("Corocana", Color.PLACE)

	print_stuff([f"""In this text based adventure, you will be taking on the role of a Nighthawk, an elite monster hunter, a sword
for hire when the ordinary folk can't handle the danger.""",
f"""The adventure begins in the town of {blackburrow}, a bustling place just East of the {lizardtongue}, and South of 
the vast jungles of {corocana}.""", """Your current task is to look for the missing son and daughter of the very worried, very rich
baron. If there is a threat to the town that was the cause of their disappearing, then you must eliminate it.""",
f"""You know the following things:
- The son and daughter were aspiring adventurers, and were seeking adventure in the {lizardtongue}, where a treasure
hoard was said to lie in a cave at the top of the largest mountain.
- The son is called {micha} and the daughter is called {elfa}. The baron himself is {bertholt}.""",
"""Before setting off on your task, you have the chance to prepare."""])

	town.town("Blackburrow", "Leave to look for the Omar children", True, False)
	print_stuff([f"Your preparations complete, you head towards the main gates of {blackburrow}.",
"You stop when you hear the sound of a woman crying in an alley, and the harsh voice of a man."])
	choice = input_stuff("""1. Investigate the sounds.
2. Continue on your way.
> """, ["1", '2'])

	if choice == "1":
		print_stuff(["You move into the dark alley. Ahead, you can see a trembling, feminine form and a man holding a sword.",
"The man turns as you approach and shoves the woman into you. You push the woman away, and only then realise that you don't need to.",
"The woman moves to the alley wall and picks up a sword leaning against it. She turns to you, grinning.",
f'''"It's amazing how effective that old gag is," she laughes, raising her weapon.''',
f"""The man behind you speaks up. "Strip the {character.character["titles"]["insult"]} of {character.character['titles']['his']} loot!" """])
		enemy_1 = encounters.monster_access("fbandit")
		enemy_2 = encounters.monster_access("mbandit")
		gang = [enemy_1, enemy_2]
		enemy_round.initialize(gang)
		if ability.ability['health'] <= 0:
			print_stuff(["You wake up lying in the alley. You hurt where you were hit, and you feel that your money was stripped from you.",
"You lost all gold!"])
			equipment.equipment["gold"] = 0
			ability.ability["health"] = int(ability.ability["maxhealth"] / 2)

story = ["chapter1.ghouls_at_farm", "chapter1.hag_lair", "chapter1.campers", "chapter1.thief", "chapter1.ascent", "chapter1.cave", "chapter2.beginning", chapter2.descent,
"chapter2.reeturn", "chapter2.answers",
]
position = boot()
if position in story:
	idx = story.index(position)
	story = story[idx:]
	print_it("Your game loaded successfully!", Color.FUNCTION)
elif not position:
	print_stuff(["Your save file could not be accessed, or has been corrupted."])
	new_game()
	prologue()
else:
	new_game()
	prologue()

set_default_actions()
run_adventure(story)
