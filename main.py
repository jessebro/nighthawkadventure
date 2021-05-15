from functions import ability
from functions import equipment
from functions import character
from functions import town
from functions import encounters

gang = [encounters.monsters["fbandit"], encounters.monsters["ghoul"]]

character.get_name()
character.get_gender()
character.get_title()
ability.get_ability()
equipment.get_equipment()

print(f"""In this text based adventure, you will be taking on the role of a Nighthawk, an elite monster hunter, a sword
for hire when the ordinary folk can't handle the danger.

The adventure begins in the town of Blackburrow, a bustling place just East of the Lizardtongue Mountains, and South of 
the vast jungles of Corocana. Your current task is to look for the missing son and daughter of the very worried, very rich
baron. If there is a threat to the town that was the cause of their disappearing, then you must eliminate it. 
You know the following things:
- The son and daughter were aspiring adventurers, and were seeking adventure in the Lizardtongue Mountains, where a treasure
hoard lay in a cave on the largest mountain.
- The son is called Micha and the daughter is called Elfa. The baron himself is Bertholt Omar.

Before setting off on your task, you have the chance to prepare.""")
town.town("Blackburrow", "Leave to look for the Omar children", True)
