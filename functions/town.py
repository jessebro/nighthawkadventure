import random
import time
from functions import equipment
from functions import inventory
from functions import weapon
from functions import ability
from functions import blackjack

def town(name, objective,firsttime=False):
	print(f"""{name}'s citizens are up and about. Merchant's shout their wares, guttersnipes pick the pockets of unsuspecting
townsfolk, and those more fortunate in life look down their nose at those with less luck.""")
	if firsttime:
		time.sleep(6)
	activity = input(f"""What would you like to do?
1. Look at the markets
2. Visit the blacksmith       ~ {equipment.equipment["gold"]} gold ~
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
	elif activity == "4":
		inventory_shown = inventory.show()
		if not inventory_shown:
			town(name, objective)
	elif activity == "5":
		return False

def market(name, objective):
	print("You enter the market, and immediately start browsing, looking for things you could use on your travels.")
	time.sleep(4)
	while True:
		purchase = input(f"""What would you like to purchase?
	1. Potions (25 gold)
	2. Knives (20 gold)
	3. Oils (50 gold)
	4. Smoke bombs (40 gold)

Enter 'b' to leave
> """)
		if purchase == "b":
			break
		word_keys = ["Potion", "Knife", "Oil", "Smoke bomb"]
		prices = [25, 20, 50, 40]
		choice = int(purchase) - 1
		if equipment.equipment["gold"] < prices[choice]:
			print("You don't have enough gold for that.")
			continue
		elif purchase == "1":
			equipment.equipment["potions"] += 1
		elif purchase == "2":
			equipment.equipment["knives"] += 1
		elif purchase == "3":
			equipment.equipment["oils"] += 1
		elif purchase == "4":
			equipment.equipment["smoke bombs"] += 1
		equipment.equipment["gold"] -= prices[choice]
		print(f"""You bought a {word_keys[choice]} for {prices[choice]} gold.""")
		time.sleep(4)
	town(name, objective)


def blacksmith(name, objective):
	print("""There's the ring of hammer and anvil as you come into the blacksmith.
Weapons, tools and blades hang on racks, and the place smells of sweat and fire.""")
	time.sleep(4)
	while True:
		purchase = input(f"""What would you like smithed?
	1. Upgrade Sharpness (20 gold)
	2. Upgrade Finesse (30 gold)
	3. Upgrade Stability (15 gold)
	4. Repair Weapon (10 gold)

Enter 'b' to leave
> """)
		if purchase == "b":
			break
		word_keys = [f"increased {weapon.weapon['weaponname']}'s Sharpness", f"increased {weapon.weapon['weaponname']}'s Finesse", f"increased {weapon.weapon['weaponname']}'s Stability", f"restored {weapon.weapon['weaponname']}'s Stability"]
		prices = [20, 30, 15, 10]
		choice = int(purchase) - 1
		if equipment.equipment["gold"] < prices[choice]:
			print("You don't have enough gold for that.")
			time.sleep(3)
			continue
		elif purchase == "1":
			weapon.weapon["sharpness"] += 1
		elif purchase == "2":
			weapon.weapon["finesse"] += 1
		elif purchase == "3":
			weapon.weapon["max stability"] += 1
			weapon.weapon["stability"] += 1
		elif purchase == "4":
			weapon.weapon["stability"] = weapon.weapon["max stability"]
		equipment.equipment["gold"] -= prices[choice]
		print(f"""You {word_keys[choice]} for {prices[choice]} gold.""")
		time.sleep(4)
	town(name, objective)


def inn(name, objective):
	print("""You enter the inn, and immediately the smell of food and drink hits you. The inn is well lit, and everywhere
people sit around tables, eating, drinking, talking or playing cards""")
	time.sleep(6)
	while True:
		purchase = input(f"""What would you like to do?
	1. Get a meal (10 gold)
	2. Join a game of cards
	3. Listen for rumours

Enter 'b' to leave
> """)
		if purchase == "b":
			break
		elif purchase == "1":
			if equipment.equipment["gold"] < 10:
				print("You don't have enough gold for that.")
				continue
			else:
				equipment.equipment["gold"] -= 10
				print("You enjoy a good meal, and feel refreshed and more energised.")
				time.sleep(4)
				print("You regain all health you've lost!")
				time.sleep(2)
				ability.ability["health"] = ability.ability["maxhealth"]
		elif purchase == "2":
			blackjack.cards()
		elif purchase == "3":
			rumours(name, objective)
	town(name, objective)


def rumours(name, objective):
	rumour_scripts = ["You hear that there's talk of a rise in an organisation known as the Daughters of Chaos. People say that more and more women join their ranks.",
"From eavesdropping on conversations, you hear a rumour that treasure hunters are becoming more and more unsuccesful, and that some have even disappeared in mysterious circumstances.",
"You hear nothing of use; only the superstitious ramblings of worried townsfolk.", "There is nothing out of the ordinary in the conversations of people at the moment.",
"There's talk of magic items being held securely being stolen by an unknown person or persons."]
	print(random.choice(rumour_scripts))
	time.sleep(6)
	return False

