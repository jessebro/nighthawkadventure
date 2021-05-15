from functions import ability
from functions import equipment
from functions import character
from functions import town
from functions import encounters
from functions import enemy_round
import time

def print_stuff(scripts):
	for script in scripts:
		print(script)
		time.sleep(5)

character.get_name()
character.get_gender()
character.get_title()
ability.get_ability()
equipment.get_equipment()

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
"You woman moves to the alley wall and picks up a sword leaning against it. She turns to you, grinning.",
f'''"It's amazing how effective that old gag is," she laughes, raising her weapon.''',
f"""The man behind you speaks up. "Kill and strip the {character.character["titles"]["insult"]}!" """])

gang = [encounters.monsters["fbandit"], encounters.monsters["mbandit"]]
enemy_round.initialize(gang)
