from functions import ability
from functions import equipment
from functions import character
from functions import town
from functions import encounters
from functions import enemy_round
from functions import post_combat
from functions import weapon



def print_stuff(scripts):
	for script in scripts:
		print(script)
		input(">>> ")

character.get_name()
character.get_gender()
character.get_title()
ability.get_ability()
equipment.get_equipment()
gang = [encounters.monsters["fbandit"], encounters.monsters["mbandit"]]
enemy_round.initialize(gang)

print_stuff([f"""In this text based adventure, you will be taking on the role of a Nighthawk, an elite monster hunter, a sword
for hire when the ordinary folk can't handle the danger.""",
"""The adventure begins in the town of Blackburrow, a bustling place just East of the Lizardtongue Mountains, and South of 
the vast jungles of Corocana.""", """Your current task is to look for the missing son and daughter of the very worried, very rich
baron. If there is a threat to the town that was the cause of their disappearing, then you must eliminate it.""",
"""You know the following things:
- The son and daughter were aspiring adventurers, and were seeking adventure in the Lizardtongue Mountains, where a treasure
hoard lay in a cave on the largest mountain.
- The son is called Micha and the daughter is called Elfa. The baron himself is Bertholt Omar.""",
"""Before setting off on your task, you have the chance to prepare."""])

town.town("Blackburrow", "Leave to look for the Omar children", True)
print_stuff(["Your preparations complete, you head towards the main gates of Blackburrow.",
"You stop when you hear the sound of a woman crying in an alley, and the harsh voice of a man."])
choice = input("""1. Investigate the sounds.
2. Continue on your way.
> """)

if choice == "1":
	print_stuff(["You move into the dark alley. Ahead, you can see a trembling, feminine form and a man holding a sword.",
"The man turns as you approaches and shoves the woman into you. You push the woman away, and only then realise that you don't need to.",
"The woman moves to the alley wall and picks up a sword leaning against it. She turns to you, grinning.",
f'''"It's amazing how effective that old gag is," she laughes, raising her weapon.''',
f"""The man behind you speaks up. "Strip the {character.character["titles"]["insult"]} of {character.character['titles']['his']} loot!" """])
	gang = [encounters.monsters["fbandit"], encounters.monsters["mbandit"]]
	enemy_round.initialize(gang)
	if post_combat.victory == False:
		print_stuff(["You wake up lying in the alley. You hurt where you were hit, and you feel that your money was stripped from you.",
"You lost all gold!"])
		equipment.equipment["gold"] = 0
		ability.ability["health"] = int(ability.ability["maxhealth"] / 2)
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
	gang = [encounters.monsters["ghoul"], encounters.monsters["ghoul"], encounters.monsters["ghoul"]]
	enemy_round.initialize(gang)
	if post_combat.victory == False:
		print("There is no one to save you. The farmer cannot hold the ghouls back for much longer, and the ghouls will show no mercy to those in the way of their food.")
		exit()

