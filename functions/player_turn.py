import time
from functions import ability
from functions import inventory
from functions import weapon
from functions import equipment
from functions import enemy_round
from functions.utils import input_stuff
from functions.combat_scripts import *
from functions.utils import colour_it
from functions.utils import Color



buffs = [0, 0, 0]


def get_turn_choice(enemy):
	reference = enemy["reference"]
	action = input_stuff(print_script("turn_start", enemy) + f""" Do you...
	1. Strike
	2. Parry
	3. Distract       ~ {ability.ability["health"]} / {ability.ability["maxhealth"]} health ~
	4. Use Item
	5. Check Inventory
> """, ["1", "2", "3", "4", "5"])
	return action


def turn(enemy, allies):
	global buffs
	enemy["modifier"] = 0
	for buff in buffs:
		buff -= 1
		if buff < 0:
			buff = 0
	action = get_turn_choice(enemy)
	if action == "1":
		strike(enemy, allies)
	elif action == "2":
		parry(enemy, allies)
	elif action == "3":
		distract(enemy, allies)
	elif action == "4":
		use_item(enemy, allies)
	elif action == "5":
		inventory_shown = inventory.show()
		if not inventory_shown:
			turn(enemy, allies)


def strike(enemy, allies, damage_mod=1.0, smoke=False, bonus=0, critical_bonus=10):
	global buffs
	damage_bonus = bonus
	critical = critical_bonus
	bleeding = 20
	bleed_lvl = 1
	vampiric = False
	agility_check = 30
	reference = enemy["reference"]
	attacks = [known for known in weapon.weapon["attacks"] if known['enabled']]
	prompt = ""
	counter = 0
	options = []
	if enemy_round.assistance:
		enemy['playermod'] += 10
	for attack in attacks:
		counter += 1
		prompt = prompt + str(counter) + ". " + attack["name"] + attack["description"] + """
"""
		options.append(str(counter))
	prompt = prompt + "> "
	attack = input_stuff(prompt, options)
	if attack == "2":
		enemy["playermod"] -= 10
		damage_mod += 0.5
	elif attack == "3":
		enemy["playermod"] += 10
		damage_mod -= 0.25
	elif attack == "4":
		enemy["playermod"] -= 10
		damage_mod += 1
		bleeding = 1000
		bleed_lvl = 2
	elif attack == "5":
		damage_mod -= 0.25
		agility_check = 1000
	elif attack == "6":
		damage_mod -= 0.25
		vampiric = True
	print(print_script("player_attack", enemy))
	time.sleep(5)
	counter = 0
	agility_roll = random.randrange(1, 101)
	attacks = 1
	if agility_roll <= (agility_check + (ability.ability["agility"])):
		attacks = 3
	if smoke:
		attacks = 4
		counter = -1
	while counter < attacks:
		damage_multi = damage_mod
		roll = random.randrange(1, 101)
		if roll <= (75 + (ability.ability["strength"] * 1.5) + enemy["playermod"] - enemy["agility"]):
			print(print_script("player_hit", enemy))
			time.sleep(5)
			if roll <= (critical + (weapon.weapon["finesse"] * 2) + ability.ability["strike_lvl"] + (buffs[1] * 5)):
				print("The strike was well aimed, and scored a critical hit!")
				time.sleep(3)
				damage_multi += 1
			if roll <= (bleeding + (weapon.weapon["sharpness"] + ability.ability["strength"])):
				enemy["bleeding"] += bleed_lvl
				print("Your attack cuts deep, and causes your enemy to bleed!")
				time.sleep(4)
			min_damage = int((ability.ability["strength"] / 2) * damage_multi)
			max_damage = int((ability.ability["strength"] + 2) * damage_multi)
			player_damage = random.randrange(min_damage, max_damage) + ability.ability["strike_lvl"] + weapon.weapon["sharpness"] + damage_bonus + (buffs[0] * 2)
			player_damage_script = colour_it(f"{player_damage} damage!", Color.YELLOW)
			if vampiric:
				healing = random.randrange(1,101)
				if healing <= 50:
					ability.ability["health"] += player_damage
					print(f"You regained {player_damage_script} health from your vampiric attack!")
					if ability.ability["health"] > ability.ability["maxhealth"]:
						ability.ability["health"] = ability.ability["maxhealth"]
			enemy["hp"] -= player_damage
			print(f"You hit for {player_damage_script}")
			time.sleep(5)
			weapon.lose_stability()
			counter += 1
		else:
			if enemy["parry"]:
				print(print_script("player_hit_parry", enemy))
				time.sleep(5)
				print("Your enemy parries your blow and counter attacks!")
				time.sleep(3)
				counter += 1
				enemy_round.choose_target(enemy, allies)
			else:
				print(print_script("player_miss", enemy))
				time.sleep(5)
				print(colour_it("You miss your attack!", Color.RED))
				time.sleep(5)
				counter += 1
		if attacks == 3:
			attacks -= 1
			print(print_script("player_extra_attack", enemy))
			time.sleep(5)
		elif attacks == 4:
			attacks -= 1
			print("You use the smoke to disappear, then emerge again suddenly.")
			time.sleep(5)


def parry(enemy, allies):
	reference = enemy["reference"]
	parries = [known for known in weapon.weapon["parries"] if known['enabled']]
	opportunist = False
	vengeance = False
	prompt = ""
	counter = 0
	options = []
	for parry in parries:
		counter += 1
		prompt = prompt + str(counter) + ". " + parry["name"] + parry["description"] + """
"""
		options.append(str(counter))
	prompt = prompt + "> "
	parry = input_stuff(prompt, options)
	if parry == "2":
		opportunist = True
	elif parry == "3":
		vengeance = True
	print(print_script("player_parry", enemy))
	enemy["modifier"] -= (10 + ability.ability["agility"] + ability.ability["parry_lvl"])
	enemy_roll = random.randrange(1,101)
	time.sleep(5)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"] - ability.ability['agility']):
		print(print_script("player_fail_parry", enemy))
		enemy_damage = random.randrange(enemy["mindamage"], enemy["maxdamage"])
		enemy_damage_script = colour_it(str(enemy_damage), Color.YELLOW)
		ability.ability["health"] -= enemy_damage
		time.sleep(5)
		print(f"You are hit for {enemy_damage_script} damage!")
		time.sleep(5)
		if enemy_round.player_defeat():
			return
		if vengeance:
			print("You shrug off the pain and lunge forwards in an attempt to take revenge!")
			time.sleep(3)
			strike(enemy, allies, bonus=enemy_damage)
		turn(enemy, allies)
	else:
		print(print_script("player_success_parry", enemy))
		time.sleep(5)
		print(colour_it("Your parry succeeds and you riposte!", Color.GREEN))
		time.sleep(3)
		if opportunist:
			turn(enemy, allies)
			return False
		if vengeance:
			strike(enemy, allies)
		else:
			strike(enemy, allies, damage_mod=1.5)

def distract(enemy, allies):
	reference = enemy["reference"]
	distracts = [known for known in weapon.weapon["distracts"] if known['enabled']]
	lacerating = False
	deadly = False
	prompt = ""
	counter = 0
	options = []
	for distract in distracts:
		counter += 1
		prompt = prompt + str(counter) + ". " + distract["name"] + distract["description"] + """
"""
		options.append(str(counter))
	prompt = prompt + "> "
	distract = input_stuff(prompt, options)
	if distract == "2":
		lacerating = True
	elif distract == "3":
		deadly = True
	print(print_script("player_distract", enemy))
	time.sleep(5)
	attack_chance = random.randrange(1,101)
	if attack_chance <= (50 + ability.ability['agility'] + ability.ability["distract_lvl"]):
		if lacerating == True:
			enemy["bleeding"] += 2
			print(colour_it("Your enemy's loss of focus allows you to cut them, causing them to bleed!", Color.GREEN))
			time.sleep(3)
		elif deadly == True:
			buffs[0] += 2
			buffs[1] += 2
			print(colour_it("Your enemy's loss of focus opens them up to significant damage!", Color.GREEN))
			time.sleep(3)
		else:
			enemy["playermod"] += (10 + ability.ability["agility"] + ability.ability["distract_lvl"] * 2)
			print(colour_it("Your enemy's loss of focus allows you to make an attack!", Color.GREEN))
			time.sleep(3)
			strike(enemy, allies)
	else:
		return False



def use_item(enemy, allies):
	global buffs
	reference = enemy["reference"]
	plurals = {
		"potions": "Potions",
		"knives": "Knives",
		"oils": "Oils",
		"smoke bombs": "Smoke Bombs"
	}
	if equipment.equipment["potions"] == 1:
		plurals["potions"] = "Potion"
	if equipment.equipment["knives"] == 1:
		plurals["knives"] = "Knife"
	if equipment.equipment["oils"] == 1:
		plurals["oils"] = "Oil"
	if equipment.equipment["smoke bombs"] == 1:
		plurals["smoke bombs"] = "Smoke Bomb"

	item_use = input(f"""
		1. {plurals["potions"]} x{equipment.equipment["potions"]} 
		2. {plurals["knives"]} x{equipment.equipment["knives"]} 
		3. {plurals["oils"]} x{equipment.equipment["oils"]}
		4. {plurals["smoke bombs"]} x{equipment.equipment["smoke bombs"]}

Enter 'b' to go back
> """)
	if item_use == "1":
		equipment.equipment["potions"] -= 1
		if equipment.equipment["potions"] <0:
			print("You have no more potions!")
			equipment.equipment["potions"] = 0
			time.sleep(2)
			use_item(enemy, allies)
			return False
		elif ability.ability["health"] == ability.ability["maxhealth"]:
			print("You're on max health, and a potion would have no effect.")
			time.sleep(5)
			equipment.equipment["potions"] += 1
			use_item(enemy,allies)
			return False
		else:
			print(print_script("player_potion", enemy))
			healing = random.randrange(4,9)
			healing_script = colour_it(f"{healing} health!", Color.GREEN)
			ability.heal(healing)
			time.sleep(5)
			print(f"You regained {healing_script}")
			time.sleep(5)
			if equipment.equipment["empowering"] == True:
				boost = random.choice([0, 1, 2])
				words = [colour_it("damage", Color.YELLOW), colour_it("critical chance", Color.RED), colour_it("damage resistance", Color.CYAN)]
				buffs[boost] += 3
				print(f"Your {words[boost]} has been boosted!")
				time.sleep(3)
	if item_use == "2":
		equipment.equipment["knives"] -= 1
		if equipment.equipment["knives"] <0:
			print("You have no more knives!")
			equipment.equipment["knives"] = 0
			time.sleep(2)
			use_item(enemy, allies)
		else:
			print(print_script("player_knife", enemy))
			knife_damage = random.randrange(2, 6)
			knife_damage_script = colour_it(f"{knife_damage} damage!", Color.YELLOW)
			enemy["hp"] -= knife_damage
			time.sleep(5)
			print(f"Your knife hits for {knife_damage_script}")
			time.sleep(5)
			if equipment.equipment["serrated"] == True:
				enemy["bleeding"] += 1
				print(f"Your knife causes the enemy to bleed!")
				time.sleep(3)
	if item_use == "3":
		equipment.equipment["oils"] -= 1
		if equipment.equipment["oils"] <0:
			print("You have no more oils!")
			equipment.equipment["oils"] = 0
			time.sleep(2)
			use_item(enemy, allies)
			return False
		else:
			print(print_script("player_oil", enemy))
			time.sleep(5)
			oil = 2
			fatal = random.randrange(1,101)
			if equipment.equipment["fatal"] == True and fatal <= 15:
				enemy["hp"] = 0
				print(f"You strike home with your oil, and it burns {reference['object']} from the inside, killing {reference['him']} instantly.")
				time.sleep(5)
			else:
				strike(enemy, allies, damage_mod=oil)
			if enemy['hp'] <= 0:
				return False
	if item_use == "4":
		equipment.equipment["smoke bombs"] -= 1
		if equipment.equipment["smoke bombs"] <0:
			print("You have no more smoke bombs!")
			equipment.equipment["smoke bombs"] = 0
			time.sleep(2)
			use_item(enemy, allies)
			return False
		else:
			print(print_script("player_smoke", enemy))
			time.sleep(5)
			if equipment.equipment["disorientating"] == True:
				enemy["modifier"] -= 10
			strike(enemy, allies, smoke=True)
	if item_use == "b":
		turn(enemy, allies)
		return False
