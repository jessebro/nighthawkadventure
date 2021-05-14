import random
import equipment
import inventory
import time
import weapon


def town(name, objective,firsttime=False):
	print(f"""{name}'s citizens are up and about. Merchant's shout their wares, guttersnipes pick the pockets of unsuspecting
townsfolk, and those more fortunate in life look down their nose at those with less luck.""")
	if firsttime:
		time.sleep(6)
	activity = input(f"""What would you like to do?
1. Look at the markets
2. Visit the blacksmith        {equipment.equipment["gold"]} gold
3. Rest at the inn
4. Check your inventory
5. {objective}

> """)
	if activity == "1":
		market(name, objective)
	elif activity == "2":
		blacksmith(name, objective)
	elif activity == "3":
		inn(name, objective)
	elif activity == "5":
		inventory_shown = inventory.show()
		if not inventory_shown:
			town(name, objective)
	elif activity == "5":
		return False

def market(name, objective):
	purchasing = True
	print("You enter the market, and immediately start browsing, looking for things you could use on your travels.")
	time.sleep(4)
	while purchasing:
		purchase = input(f"""What would you like to purchase?
	1. Potions (25 gold)
	2. Knives (20 gold)
	3. Oils (50 gold)
	4. Smoke bombs (40 gold)

Enter 'b' to leave
> """)
		if purchase == "b":
			break
		ur_stuff = [equipment.equipment["potions"], equipment.equipment["knives"], equipment.equipment["oils"], equipment.equipment["smoke bombs"]]
		word_keys = ["Potion", "Knife", "Oil", "Smoke bomb"]
		prices = [25, 20, 50, 40]
		choice = int(purchase) - 1
		if equipment.equipment["gold"] < prices[choice]:
			print("You don't have enough gold for that.")
			continue
		ur_stuff[choice] += 1
		equipment.equipment["gold"] -= prices[choice]
		print(f"""You bought a {word_keys[choice]} for {prices[choice]} gold.""")
		time.sleep(4)
	town(name, objective)


def blacksmith(name, objective):
	purchasing = True
	print("""There's the ring of hammer and anvil as you come into the blacksmith.
Weapons, tools and blades hang on racks, the place smells of sweat and fire.""")
	time.sleep(4)
	while purchasing:
		purchase = input(f"""What would you like smithed?
	1. Upgrade Sharpness (20 gold)
	2. Upgrade Finesse (30 gold)
	3. Upgrade Stability (15 gold)
	4. Repair Weapon (10 gold)

Enter 'b' to leave
> """)
		if purchase == "b":
			break
		ur_stuff = [weapon.weapon["sharpness"], weapon.weapon["finesse"], weapon.weapon["stability"], weapon.weapon["max stability"]]
		word_keys = [f"increased {weapon.weapon['weaponname']}'s Sharpness", f"increased {weapon.weapon['weaponname']}'s Finesse", f"increased {weapon.weapon['weaponname']}'s Stability", f"restored {weapon.weapon['weaponname']}'s Stability"]
		prices = [20, 30, 15, 10]
		choice = int(purchase) - 1
		if equipment.equipment["gold"] < prices[choice]:
			print("You don't have enough gold for that.")
			time.sleep(3)
			continue
		ur_stuff[choice] += 1
		equipment.equipment["gold"] -= prices[choice]
		print(f"""You {word_keys[choice]} for {prices[choice]} gold.""")
		time.sleep(4)
	town(name, objective)


def inn(name, objective):
	pass


def rest(name, objective):
	pass
