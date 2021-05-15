import random
import time
from functions import equipment
from functions import weapon
from functions import ability

def end_combat(enemy):
	choice = input(f"""All danger has gone. The ground has been spattered with blood, and the adrenaline has left you feeling a bit weak. Do you...
1. Loot the corpses
2. Step away
> """)
	if choice == "1":
		generate_loot(enemy)
	else:
		ability.gain_xp(enemy)
		victory("victory")
		return False


def victory(result):
	if result == "victory":
		return True
	else:
		return False

def generate_loot(enemies):
	for enemy in enemies:
		reference = enemy["reference"]
		if enemy["type"] == "human":
			gold = random.randrange(1,11)
			print(f"You find {gold} gold on the {reference['object']}'s body.")
			time.sleep(4)
			equipment.equipment['gold'] += gold
			item = random.randrange(1,11)
			if item == 6 or item == 7:
				print(f"You also find a knife.")
				time.sleep(4)
				equipment.equipment['knives'] += 1
			elif item == 8:
				print(f"You also find a knife.")
				time.sleep(4)
				equipment.equipment['knives'] += 1
			elif item == 9:
				print(f"You also find a sword oil.")
				time.sleep(4)
				equipment.equipment['oils'] += 1
			elif item == 10:
				print(f"You also find a smoke bomb.")
				time.sleep(4)
				equipment.equipment['smoke bombs'] += 1
			else:
				time.sleep(0.01)
			sword_boost = random.randrange(1,11)
			if sword_boost >= 8:
				print(f"You find a whetstone to improve your weapon.")
				time.sleep(4)
				boosted = random.choice(["sharpness", "sharpness", "max stability", "finesse"])
				weapon.weapon[boosted] += 1
				print(f"{weapon.weapon['weaponname'].capitalize()}'s {boosted} has been increased by 1!")
				time.sleep(4)
		else:
			print(f"Though the {reference['object']} does not carry equipment, you find some coins in its stomach, no doubt the remains of the {reference['object']}'s victims.")
			gold = random.randrange(1, 5)
			time.sleep(4)
			print(f"You find {gold} gold on the {reference['object']}'s body.")
			time.sleep(4)
			equipment.equipment['gold'] += gold
	ability.gain_xp(enemies)
	victory("victory")
	return False
