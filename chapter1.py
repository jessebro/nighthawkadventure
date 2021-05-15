from functions import ability
from functions import equipment
from functions import character
from functions import encounters
from functions import enemy_round
from functions import post_combat
from functions import weapon
from functions.utils import print_stuff

def ghouls_at_farm():
	print_stuff(["You make your way outside of Blackburrow. It is late morning, and the sky is a cobalt blue.",
	"Birds sing, and the long grass sways in the breeze. The air is cool, but not cold, and fluffy white clouds float in the sky.",
	"You stear off the main road and onto a dirt track leading to the Lizardtongue Mountains. About an hour into the journey you come across a farm.",
	"Wheat stalks stand golden against the pale grass. You decide to cut through the wheat field, rather than take a detour around it.",
	"That's when you hear shouting and cursing. You begin to run, and see a man standing in the front door of his house. He is swinging a pitchfork to and fro.",
	"Standing before him are four ghouls; pale, lanky, short and hairless humanoids that feed on rotting flesh. Two other ghouls lie dead and bleeding.",
	"The man sees you and screams for help. You see a little girl and a teenage boy standing behind the man, expressions of terror on their faces.",
	"You know that the man will not be able to hold the ghouls back forever."])

	choice = input("""1. Help the farmer.
	2. Continue on your way.
	> """)
	if choice == "1":
		print_stuff([f"You rush forwards, {weapon.weapon['weaponname']} in hand. The ghouls turn to face you now, but one of them continues to focus on the farmer",
	"One of the ghouls lunges forward suddenly, and you ready your sword."])
		enemies = [encounters.monster_access("ghoul"), encounters.monster_access("ghoul"), encounters.monster_access("ghoul")]
		gang = enemies
		enemy_round.initialize(gang)
		if post_combat.victory == False:
			print("There is no one to save you. The farmer cannot hold the ghouls back for much longer, and the ghouls will show no mercy to those in the way of their food.")
			exit()
		print_stuff([f"You wipe ghoul blood from your sword with a cloth. The farmer approaches you, his own pitchfork stained a dark red.",
	f'"Thank you, kind stranger," the man says. He bites his lip for a second, then pulls a money bag from his belt and holds it out to you.',
	f'''"It's not much, but you deserve a reward, {character.character['titles']['casual']}."'''])
		choice = input("""1. "Thank you. Take care."
2. "Keep the money. Your children need it."
> """)
		if choice == "1":
			print_stuff(["You take the gold bid the farmer farewell, before continuing on your way.",
"You recieved 10 gold!"])
			equipment.equipment["gold"] += 10
		else:
			print_stuff(["You push the money bag away, and you notice the man seems to relax a bit. Clearly he was hoping you would refuse.",
f'''"Thank you again. But at least let me give you a meal before you leave."''',
"You accept the man's offer and he brings you into his small house. He gives you a bowl of green soup. You eat it, and it tastes good enough.",
"The soup reenergizes you, despite its mediocre taste. Once you have finished eating, the farmer bids you farwell, and you continue towards the Lizardtongue Mountains"])
			ability.ability["health"] += 5
			ability.gain_xp(encounters.xp_handouts["small"])

def hag_lair():
	print_stuff(['You continue along the trail, and you pass by a few more farms, and sometimes the people maintaining them, nodding in greeting as you pass.',
'''Finally, the track becomes wilder, the farms become less, before disappearing altogether. Small pockets of trees and undergrowth now dot the countryside.''',
'It is late in the afternoon when the trail splits suddenly. It is clear which path will lead to the mountains. The other pass leads into a small forest.'])
	choice = input("""1. Explore the forest trail.
2. Take the path to the Lizardtongue Mountains
> """)
	if choice == "1":
		print_stuff(['You walk down the forest path. Light from the afternoon sun slants through the thin canopy of leaves, and small critters rustle in the leaflitter.',
'After following the trail for about ten minutes, it ends in a small log cabin. No lights shine through the glass windows, but you can detect some movement from inside.',])
		choice = input("""1. "Is anyone home?!"
2. Try to open the door.
3. Turn back and head for the Lizardtongue Mountains.
> """)
		if choice == "1":
			print_stuff(["You see the movement stop for a moment, then a creature comes hurtling out the door.",
'''"Dinsers!" the creature shrieks with glee. "Dinsers has comses!" The creature is a bone hag.''',
"""It takes on the form of an elderly woman with grey skin that hangs and droops in strange folds, dull black hair and dressed in nothing but a loincloth. 
They have sharp claws on their fingers and toes.""",
f"You also know that hags enjoy to the taste of living flesh, especially that of young people or elves. You draw {weapon.weapon['weaponname']} and ready yourself."])
		elif choice == "2":
			print_stuff(["You move to the door and twist the doorknob. The door swings open, and immediately the smell of rot assaults your nose.",
"Almost everything here is broken or decayed. Only two things seem solid here; a cauldron of meat soup, and a hunched form. The form turns to see, and grins toothily.",
'''"Dinsers!" the creature shrieks with glee. "Dinsers has comses!" The creature is a bone hag.''',
"""It takes on the form of an elderly woman with grey skin that hangs and droops in strange folds, dull black hair and dressed in nothing but a loincloth. 
It has sharp claws on their fingers and toes.""",
"""You also know that hags enjoy to the taste of living flesh. Before you can react, the hag lunges forwards, crashing into you. 
The two of you tumble outside of the cabin and into the forest. You roll to your feet and draw your sword, and the hag rises to its feet, snarling."""])
		else:
			print_stuff(['Deciding not to disturb the inhabitants - whoever they may be - you trace your steps back to the junction in the trail.'])
			return False
		enemy_round.initialize([encounters.monster_access("bone_hag")])



