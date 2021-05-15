from functions import ability
from functions import equipment
from functions import character
from functions import encounters
from functions import enemy_round
from functions import post_combat
from functions import weapon
from main import print_stuff

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
