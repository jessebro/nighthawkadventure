import time
from functions import ability
from functions import inventory
from functions import equipment
from functions import enemy_round
from functions.utils import input_stuff
from functions.combat_scripts import *
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import clear
from functions import settings

delay = 5
if settings.settings['immersion'] == "OFF":
	delay = 0



buffs = [0, 0, 0]


def get_turn_choice(enemy):
	print_script("turn_start", enemy)
	action = input_stuff(f"""Do you...
	1. Strike
	2. Parry
	3. Distract       ~ {ability.ability["health"]} / {ability.ability["maxhealth"]} health ~
	4. Use Item
	5. Check Inventory
> """, ["1", "2", "3", "4", "5"])
	return action


def turn(enemy, allies):
	global buffs
	clear()
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


def strike(enemy, allies, damage_mod=1.0, smoke=False, bonus=0, critical_bonus=10, counter=False):
	global buffs
	damage_bonus = bonus
	critical = critical_bonus
	bleeding = 20
	bleed_lvl = 1
	vampiric = False
	agility_check = 30
	if not counter:
		enemy_round.game_state['striked'] = True
	attacks = [known for known in weapon.weapon["attacks"] if known['enabled']]
	prompt = ""
	counter = 0
	options = []
	if enemy_round.game_state['assistance']:
		enemy['playermod'] += 10
	for attack in attacks:
		counter += 1
		prompt = prompt + str(counter) + ". " + attack["name"] + attack["description"] + """
"""
		options.append(str(counter))
	prompt = prompt + "> "
	attack_choice = int(input_stuff(prompt, options))
	attack_choice -= 1
	if attacks[attack_choice]['name'] not in enemy_round.game_state['strikes_made']:
		enemy_round.game_state['strikes_made'].append(attacks[attack_choice]['name'])
	if attacks[attack_choice]['name'] == "Power Strike":
		enemy["playermod"] -= 10
		damage_mod += 0.5
	elif attacks[attack_choice]['name'] == "Precision Strike":
		enemy["playermod"] += 10
		damage_mod -= 0.25
	elif attacks[attack_choice]['name'] == "Rending Strike":
		enemy["playermod"] -= 10
		damage_mod += 1
		bleeding = 1000
		bleed_lvl = 2
	elif attacks[attack_choice]['name'] == "Dancing Strike":
		enemy["playermod"] -= 10
		agility_check = 1000
	elif attacks[attack_choice]['name'] == "Vampire Strike":
		damage_mod -= 0.25
		vampiric = True
	print_script("player_attack", enemy)
	time.sleep(delay)
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
		enemy_round.game_state['attacks'] += 1
		if roll <= (75 + ability.ability["strength"] + enemy["playermod"] + (ability.ability['level']) - enemy["agility"]):
			enemy_round.game_state['hits'] += 1
			print_script("player_hit", enemy)
			time.sleep(delay)
			if roll <= (critical + (weapon.weapon["finesse"] * 2) + (buffs[1] * 5)):
				print("The strike was well aimed, and scored a critical hit!")
				time.sleep(delay)
				damage_multi += 1
			if roll <= (bleeding + (weapon.weapon["sharpness"] + ability.ability["strength"])):
				enemy["bleeding"] += bleed_lvl
				print("Your attack cuts deep, and causes your enemy to bleed!")
				time.sleep(delay)
			min_damage = int((ability.ability["strength"] / 2) * damage_multi)
			max_damage = int((ability.ability["strength"]) * damage_multi)
			player_damage = random.randrange(min_damage, max_damage) + int(weapon.weapon["sharpness"] / 2) + damage_bonus + (buffs[0] * 2)
			player_damage_script = colour_it(f"{player_damage} damage!", Color.YELLOW)
			if vampiric:
				healing = random.randrange(1,101)
				if healing <= 50:
					ability.ability["health"] += player_damage
					print(f"You regained {player_damage_script} health from your vampiric attack!")
					time.sleep(delay)
					enemy_round.game_state['health_restored'] += player_damage
					if ability.ability["health"] > ability.ability["maxhealth"]:
						ability.ability["health"] = ability.ability["maxhealth"]
			enemy["hp"] -= player_damage
			print(f"You hit for {player_damage_script}")
			time.sleep(delay)
			weapon.lose_stability()
			counter += 1
			enemy_round.game_state['damage_dealt'] += player_damage
			enemy_round.game_state['total_damage_dealt'] += player_damage
			enemy_round.game_state['damages'].append(player_damage)
			if enemy['hp'] <= 0:
				return
		else:
			if enemy["parry"]:
				print_script("player_hit_parry", enemy)
				time.sleep(delay)
				print(colour_it("Your enemy parries your blow and counter attacks!", Color.REDF))
				time.sleep(delay)
				counter += 1
				enemy_round.choose_target(enemy, allies)
				if ability.ability['health'] <= 0:
					enemy_round.player_defeat()
			else:
				print_script("player_miss", enemy)
				time.sleep(delay)
				print(colour_it("You miss your attack!", Color.RED))
				time.sleep(delay)
				counter += 1
		if attacks == 3:
			attacks -= 1
			print_script("player_extra_attack", enemy)
			time.sleep(delay)
		elif attacks == 4:
			attacks -= 1
			print("You use the smoke to disappear, then emerge again suddenly.")
			time.sleep(delay)


def parry(enemy, allies):
	reference = enemy["reference"]
	parries = [known for known in weapon.weapon["parries"] if known['enabled']]
	opportunist = False
	vengeance = False
	prompt = ""
	counter = 0
	options = []
	enemy_round.game_state['parried'] = True
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
	print_script("player_parry", enemy)
	enemy["modifier"] -= (10 + ability.ability["agility"])
	enemy_roll = random.randrange(1,101)
	time.sleep(delay)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"] - ability.ability['agility']):
		print_script("player_fail_parry", enemy)
		enemy_damage = random.randrange(enemy["mindamage"], enemy["maxdamage"])
		enemy_damage_script = f"{colour_it(str(enemy_damage) + ' damage!', Color.YELLOW)}"
		ability.ability["health"] -= enemy_damage
		time.sleep(delay)
		print(f"You are hit for {enemy_damage_script}")
		time.sleep(delay)
		if enemy_round.player_defeat():
			return
		if vengeance:
			print("You shrug off the pain and lunge forwards in an attempt to take revenge!")
			time.sleep(delay)
			strike(enemy, allies, bonus=enemy_damage)
		turn(enemy, allies)
	else:
		print_script("player_success_parry", enemy)
		time.sleep(delay)
		print(colour_it("Your parry succeeds and you riposte!", Color.GREEN))
		time.sleep(delay)
		if opportunist:
			turn(enemy, allies)
			return False
		if vengeance:
			strike(enemy, allies)
		else:
			strike(enemy, allies, damage_mod=1.5, counter=True)

def distract(enemy, allies):
	reference = enemy["reference"]
	distracts = [known for known in weapon.weapon["distracts"] if known['enabled']]
	lacerating = False
	deadly = False
	enemy_round.game_state['distracted'] = True
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
	print_script("player_distract", enemy)
	time.sleep(delay)
	attack_chance = random.randrange(1,101)
	if attack_chance <= (50 + ability.ability['agility']):
		if lacerating == True:
			enemy["bleeding"] += 2
			print(colour_it("Your enemy's loss of focus allows you to cut them, causing them to bleed!", Color.GREEN))
			time.sleep(delay)
		elif deadly == True:
			buffs[0] += 2
			buffs[1] += 2
			print(colour_it("Your enemy's loss of focus opens them up to significant damage!", Color.GREEN))
			time.sleep(delay)
		else:
			enemy["playermod"] += (10 + ability.ability["agility"] * 2)
			print(colour_it("Your enemy's loss of focus allows you to make an attack!", Color.GREEN))
			time.sleep(delay)
			strike(enemy, allies)
	else:
		return False



def use_item(enemy, allies):
	global buffs
	reference = enemy["reference"]
	enemy_round.game_state['used_item'] = True
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
			time.sleep(delay)
			use_item(enemy, allies)
			return False
		elif ability.ability["health"] == ability.ability["maxhealth"]:
			print("You're on max health, and a potion would have no effect.")
			time.sleep(delay)
			equipment.equipment["potions"] += 1
			use_item(enemy,allies)
			return False
		else:
			print_script("player_potion", enemy)
			healing = random.randrange(4,9)
			healing_script = colour_it(f"{healing} health!", Color.GREEN)
			ability.heal(healing)
			time.sleep(delay)
			print(f"You regained {healing_script}")
			time.sleep(delay)
			if equipment.equipment["empowering"] == True:
				boost = random.choice([0, 1, 2])
				words = [colour_it("damage", Color.YELLOW), colour_it("critical chance", Color.RED), colour_it("damage resistance", Color.CYAN)]
				buffs[boost] += 3
				print(f"Your {words[boost]} has been boosted!")
				time.sleep(delay)
			enemy_round.game_state['health_restored'] += healing
	if item_use == "2":
		equipment.equipment["knives"] -= 1
		if equipment.equipment["knives"] <0:
			print("You have no more knives!")
			equipment.equipment["knives"] = 0
			time.sleep(delay)
			use_item(enemy, allies)
		else:
			enemy_round.game_state['knifed'] = True
			print_script("player_knife", enemy)
			knife_damage = random.randrange(2, 6)
			knife_damage_script = colour_it(f"{knife_damage} damage!", Color.YELLOW)
			enemy["hp"] -= knife_damage
			enemy_round.game_state['damage_dealt'] += knife_damage
			enemy_round.game_state['total_damage_dealt'] += knife_damage
			time.sleep(delay)
			print(f"Your knife hits for {knife_damage_script}")
			time.sleep(delay)
			if equipment.equipment["serrated"] == True:
				enemy["bleeding"] += 1
				print(f"Your knife causes the enemy to bleed!")
				time.sleep(delay)
	if item_use == "3":
		equipment.equipment["oils"] -= 1
		if equipment.equipment["oils"] <0:
			print("You have no more oils!")
			equipment.equipment["oils"] = 0
			time.sleep(delay)
			use_item(enemy, allies)
			return False
		else:
			print_script("player_oil", enemy)
			time.sleep(delay)
			oil = 2
			fatal = random.randrange(1,101)
			if equipment.equipment["fatal"] == True and fatal <= 15:
				enemy["hp"] = 0
				print(f"You strike home with your oil, and it burns {reference['object']} from the inside, killing {reference['him']} instantly.")
				time.sleep(delay)
			else:
				strike(enemy, allies, damage_mod=oil)
			if enemy['hp'] <= 0:
				return False
	if item_use == "4":
		equipment.equipment["smoke bombs"] -= 1
		if equipment.equipment["smoke bombs"] <0:
			print("You have no more smoke bombs!")
			equipment.equipment["smoke bombs"] = 0
			time.sleep(delay)
			use_item(enemy, allies)
			return False
		else:
			print_script("player_smoke", enemy)
			time.sleep(delay)
			if equipment.equipment["disorientating"] == True:
				enemy["modifier"] -= 10
			strike(enemy, allies, smoke=True)
	if item_use == "b":
		turn(enemy, allies)
		return False
