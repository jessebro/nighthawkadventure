import ability
import weapon
import inventory
import time
import encounters

def rest():
	activity = input(f"""What would you like to do?
1. Eat food and get some downtime
2. Sharpen {weapon.weapon["weaponname"]}
3. Practice your swordplay
4. Check your inventory

> """)
	if activity == "1":
		print("You rest and eat food, restoring your energy.")
		time.sleep(3)
		print("All lost health as been restored!")
		time.sleep(3)
		ability.ability["health"] = ability.ability["maxhealth"]

	elif activity == "2":
		sharpen()
	elif activity == "3":
		train()
	elif activity == "4":
		inventory_shown = inventory.show()
		if not inventory_shown:
			rest()

def sharpen():
	print(f"You pull out a whetstone and sharpen {weapon.weapon['weaponname']}, cleaning off the rust and filing down the nicks and chips.")
	time.sleep(4)
	print(f"{weapon.weapon['weaponname'].capitalize()}'s Sharpness increased by 1!")
	weapon.weapon["sharpness"] += 1
	time.sleep(3)

def train():
	print(f"You draw {weapon.weapon['weaponname']} and practice attack routines, honing your skills.")
	time.sleep(3)
	training_xp = [encounters.xp_handouts["practice"]]
	ability.gain_xp(training_xp)

