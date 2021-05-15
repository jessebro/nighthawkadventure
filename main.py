import character
import ability
import enemy_round
import equipment
import random
import inventory
import town
import rest
import encounters

gang = [encounters.monsters["fbandit"], encounters.monsters["ghoul"]]

character.get_name()
character.get_gender()
character.get_title()
ability.get_ability()
equipment.get_equipment()
town.town("Finklestein", "Pat the dog", True)
print("The dog is very happy.")
