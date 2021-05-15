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
	"You steer off the main road and onto a dirt track leading to the Lizardtongue Mountains. About an hour into the journey you come across a farm.",
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
"You received 10 gold!"])
			equipment.equipment["gold"] += 10
		else:
			print_stuff(["You push the money bag away, and you notice the man seems to relax a bit. Clearly he was hoping you would refuse.",
f'''"Thank you again. But at least let me give you a meal before you leave."''',
"You accept the man's offer and he brings you into his small house. He gives you a bowl of green soup. You eat it, and it tastes good enough.",
"The soup energises you, despite its mediocre taste. Once you have finished eating, the farmer bids you farewell, and you continue towards the Lizardtongue Mountains"])
			ability.ability["health"] += 5
			ability.gain_xp([encounters.xp_handouts["small"]])


def hag_lair():
	treasure = 0
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
		if post_combat.victory == False:
			print("No one knows you came here, and no one can save you now. Unfortunately, you'll probably end up in the hag's cooking pot.")
			exit()
		print_stuff(["With the bone hag dead, you enter the cabin. You look around, and you see a worn chest, the cauldron of meat soup, a table with papers on it, and a pile of bones."])
		while True:
			investigate = input("""1. Search the chest.
2. Investigate the cauldron.
3. Check the papers
4. Examine the bones.
5. Leave
> """)
			if investigate == "1":
				print_stuff(["You open the chest, and are slightly disappointed when all you find are worn clothes, riddled with moth holes."])
			elif investigate == "2":
				while True:
					option = input("""The cauldron contains some meat soup. It is still warm, and a wooden stirring spoon sticks out from its depths.
1. Taste the soup.
2. Step away.
> """)
					if option == "1":
						print_stuff(["The soup tastes fresh, and has chunks of meat in it. The meat itself tastes similar to pork."])
						continue
					else:
						break
			elif investigate == "3":
				treasure += 1
				print("""You pick up a piece of paper and read.
	____________________________________________________
		My dearest Chana,
	If I am to die prematurely, you must lift the chest 
	and take the belongings below it. That should be
	enough to keep you alive, and perhaps flourish.
		Denvar
	____________________________________________________""")
				if treasure == 1:
					option = input("""1. Search under the chest.
2. Step away.
> """)
					if option == "1":
						equipment.equipment["gold"] += 50
						print_stuff(["You obey the instructions in the note, lifting the chest and peering under it.",
"Underneath you see a reasonably large bag of money, as well as a silver ring etched with runes.",
"You take the money, counting 50 gold coins."])
						ring = input("""1. Put on the ring.
2. Leave the ring.
>""")
						if ring == "1":
							ability.ability["strength"] += 1
							print_stuff(["You feel a tingling sensation as you slip the ring on, and a sudden burst of power.",
"Your Strength has been increased by 1!"])
						else:
							continue
					else:
						treasure = 0
						continue
				else:
					print_stuff([""])
					continue
			elif investigate == "4":
				print_stuff(["You discover two things about the bones. First, it is that of a woman, due to the shape of the bones and the scraps of woman's clothing lying nearby.",
"Second, the bones have been scraped clean of all flesh, due to the knicks and scratches of something being drawn along them."])
			else:
				break
		print_stuff(["You leave the cabin, satisfied with what you achieved. You head back along the trail, and back to the junction."])
	print_stuff(["You turn onto the path to the Lizardtongue Mountains, and continue your trek."])


def campers():
	print_stuff(["The sky is growing darker. The bird song is giving way to the chirp of the crickets, and the air grows cold.",
"Even as you begin to consider a place to stop for the night, you see a flickering orange light from behind a clump of high bushes."])
	choice = input("""1. Investigate the sources of the fire.
2. Keep walking until you find somewhere to rest.
> """)
	if choice == "1":
		print_stuff(["You walk over to the source of the fire. Once you reach it, you see two men, and two large backpacks surrounding a campfire.",
"One of the men, large and muscular, jumps to his feet at the sight of you, drawing his sword. The other, who is shorter, slender and lean, also rises to his feet.",
'''"Who are you?" the large man demands. "Friend or foe?" The other man places a hand on his companion's shoulder and smiles at you.''',
f'''"I beg your pardon, {character.character["titles"]["formal"]}," he says smoothly. "We're just on guard, as we have learnt to be."''',
'''The large man continues to eye you warily and doesn't sheath his sword. The lean one gestures to the campfire.''',
'''"Share a fire?" he offers kindly.'''])
		choice = input("""1. "Yes, thank you."
2. "I'd best be on my way." 
> """)
		if choice == "1":
			print_stuff(["""The lean man's smile increases. "Excellent," he says. You take a seat by the fire, and bask in its warmth.""",
"""The lean man takes a seat beside you, but the large man grumbles something about taking a walk and leaves.""",
""""I do not believe we have been properly introduced," the lean man says kindly. He lays a hand on his chest. "I'm Eladris. And you are?"
"""])
			reply = input(f"""1. "I'm {character.character["name"]}."
2. "I'd rather not tell you."
> """)
			if reply == "1":
				print_stuff([f""""{character.character['name']}," Eladris says, testing your name on his tongue."""])
			else:
				print_stuff(["""Eladris laughs. "Keep your secrets then," he chuckles. "But you should learn to be more trusting." """])
			print_stuff(["So what brings you here? Monsters are roaming the countryside in even great numbers these days."])
			reply = input(f"""1. "I'm looking for some missing people."
2. "I do not fear monsters. It is the other way around." 
> """)
			if reply == "1":
				print_stuff([f""""I see," Eladris says. "I will not pry, though my curiosity demands me to do so." """])
			else:
				print_stuff([""""You're a confident one," he says. "Be wary it doesn't become hubris." """])
			while True:
				question = input(f"""1. "So... what's a half-elf doing out here?"
2. "Who's your cheerful friend?" 
3. "You said monsters were increasing in numbers..."
4. "I'm going to get some sleep." 
> """)
		else:
			print_stuff(["""The lean man shrugs. "Safe travels," he says. You walk away from the camp sight and back to the trail."""])


