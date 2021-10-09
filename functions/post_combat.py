import random
import time
from functions import equipment
from functions import weapon
from functions import ability
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import print_stuff
from functions import settings

delay = 5
if settings.settings['immersion'] == "OFF":
		delay = 0


def end_combat(enemy):
	if len(enemy) == 1:
		loot = "corpse"
	else:
		loot = "corpses"
	choice = input(f"""All danger has gone. The ground has been spattered with blood, and the adrenaline has left you feeling a bit weak. Do you...
1. Loot the {loot}
2. Step away
> """)
	if choice == "1":
		generate_loot(enemy)
	else:
		ability.gain_xp(enemy)
		return False


def generate_loot(enemies):
	for enemy in enemies:
		reference = enemy["reference"]
		if enemy["type"] != "human":
			print(f"Though {reference['object']} does not carry equipment, you find some coins in its stomach, no doubt the remains of {reference['object']}'s victims.")
			gold = random.randrange(1, 5)
			time.sleep(delay)
			print(f"You find {gold} gold on {reference['object']}'s body.")
			time.sleep(delay)
			equipment.equipment['gold'] += gold
		elif not enemy["yield"]:
			gold = random.randrange(1,11)
			print(f"You find {gold} gold on {reference['object']}'s body.")
			time.sleep(delay)
			equipment.equipment['gold'] += gold
			item = random.randrange(1,11)
			if item == 6 or item == 7:
				knife = colour_it("knife", Color.LOOT)
				print(f"You also find a {knife}.")
				time.sleep(delay)
				equipment.equipment['knives'] += 1
			elif item == 8:
				potion = colour_it("potion", Color.LOOT)
				print(f"You also find a {potion}.")
				time.sleep(delay)
				equipment.equipment['potions'] += 1
			elif item == 9:
				oil = colour_it("oil", Color.LOOT)
				print(f"You also find a sword {oil}.")
				time.sleep(delay)
				equipment.equipment['oils'] += 1
			elif item == 10:
				smoke_bomb = colour_it("smoke bomb", Color.LOOT)
				print(f"You also find a {smoke_bomb}.")
				time.sleep(delay)
				equipment.equipment['smoke bombs'] += 1
			sword_boost = random.randrange(1,11)
			if sword_boost >= 8:
				print(f"You find a whetstone to improve your weapon.")
				time.sleep(delay)
				boosted = random.choice(["sharpness", "sharpness", "max stability", "finesse"])
				weapon.weapon[boosted] += 1
				print(f"{weapon.weapon['weaponname'].capitalize()}'s {boosted} has been increased by 1!")
				time.sleep(delay)
	ability.gain_xp(enemies)
	return False
