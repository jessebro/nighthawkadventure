from functions import ability
from functions import equipment
from functions import character
from functions import town
from functions import encounters
from functions import enemy_round
from functions import post_combat
from functions import weapon
from functions.utils import print_stuff
from functions.utils import boot
from functions.utils import input_stuff


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
	enemy_1 = encounters.monster_access("fbandit")
	enemy_2 = encounters.monster_access("mbandit")
	gang = [enemy_1, enemy_2]
	enemy_round.initialize(gang)


def prologue():
	print_stuff([f"""In this text based adventure, you will be taking on the role of a Nighthawk, an elite monster hunter, a sword
for hire when the ordinary folk can't handle the danger.""",
"""The adventure begins in the town of Blackburrow, a bustling place just East of the Lizardtongue Mountains, and South of 
the vast jungles of Corocana.""", """Your current task is to look for the missing son and daughter of the very worried, very rich
baron. If there is a threat to the town that was the cause of their disappearing, then you must eliminate it.""",
"""You know the following things:
- The son and daughter were aspiring adventurers, and were seeking adventure in the Lizardtongue Mountains, where a treasure
hoard was said to lie in a cave at the top of the largest mountain.
- The son is called Micha and the daughter is called Elfa. The baron himself is Bertholt Omar.""",
	"""Before setting off on your task, you have the chance to prepare."""])

	town.town("Blackburrow", "Leave to look for the Omar children", True)
	print_stuff(["Your preparations complete, you head towards the main gates of Blackburrow.",
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
		if post_combat.victory == False:
			print_stuff(["You wake up lying in the alley. You hurt where you were hit, and you feel that your money was stripped from you.",
"You lost all gold!"])
			equipment.equipment["gold"] = 0
			ability.ability["health"] = int(ability.ability["maxhealth"] / 2)

story = ["chapter1.ghouls_at_farm", "chapter1.hag_lair", "chapter1.campers", "chapter1.thief", "chapter1.ascent"]
position = boot()
if position in story:
	idx = story.index(position)
	story = story[idx:]
	print_stuff(["Your game loaded successfully!"])
elif not position:
	print_stuff(["Your save file could not be accessed, or has been corrupted."])
	new_game()
	prologue()
else:
	new_game()
	prologue()

run_adventure(story)
