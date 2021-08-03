import time
from functions import character
from functions import ability
from functions import post_combat
from functions import player_turn
from functions.player_turn import buffs
from functions.combat_scripts import *

gang_size = 0
gang_lads = []
gang_index = 0
combat = True
assistance = False
goad = ""

def combat_flow(enemy, allies):
	global combat
	combat = True
	while combat:
		player_turn.turn(enemy, allies)
		if dead_check(enemy):
			break
		if player_defeat():
			break
		enemy_turn(enemy, allies)
		if dead_check(enemy):
			break
		if player_defeat():
			break
		for ally in allies:
			ally_turn(ally, enemy)
			if dead_check(enemy):
				break


def generate_actor(maxhp, mindamage, maxdamage, baseskill, baseagility, xp, type, gender, name):
	enemy = {}
	enemy["maxhp"] = maxhp
	enemy["hp"] =  enemy["maxhp"]
	enemy["mindamage"] = mindamage
	enemy["maxdamage"] = maxdamage
	enemy["baseskill"] = baseskill
	enemy["skill"] = enemy["baseskill"]
	enemy["type"] = type
	enemy["baseagility"] = baseagility
	enemy["agility"] = enemy["baseagility"]
	enemy["gender"] = gender
	enemy["modifier"] = 0
	enemy["playermod"] = 0
	enemy["parry"] = False
	enemy["distract"] = False
	enemy["bleeding"] = 0
	enemy["xp"] = xp
	enemy["reference"] = generate_reference(type, gender, name)
	return enemy


def generate_reference(type, gender, name):
	reference = {}
	reference["object"] = name
	if gender == "male":
		reference["his"] = "his"
		reference["him"] = "him"
		reference["he"] = "he"
	elif gender == "female":
		reference["his"] = "her"
		reference["him"] = "her"
		reference["he"] = "she"
	else:
		reference["his"] = "its"
		reference["him"] = "it"
		reference["he"] = "it"
	if type == "human":
		reference["pain"] = "scream"
		reference["curse"] = "curse"
	else:
		reference["pain"] = "howl"
		reference["curse"] = "growl"
	reference["insult"] = character.character["titles"]['insult']
	reference["whore"] = character.character["titles"]["whore"]
	return reference


def initialize(enemies: list, allies=()):
	global gang_size
	global gang_lads
	gang_size = len(enemies)
	gang_lads = enemies
	for enemy in enemies:
		if ability.ability['health'] <= 0:
			break
		combat_flow(enemy, allies)


def enemy_turn(enemy, allies):
	if enemy['bleeding'] > 0:
		damage = random.randrange(2,6)
		print(f"Your enemy bleeds for {damage} damage!")
		time.sleep(4)
		enemy["modifier"] -= (10 * enemy['bleeding'])
		enemy["bleeding"] -= 1
		if dead_check(enemy):
			return
	enemy["playermod"] = 0
	if enemy["type"] == "human":
		action = random.randrange(1,6)
		if action == 1 and enemy["parry"] == False:
			enemy_parry(enemy)
		if action == 2 and enemy["distract"] == False:
			enemy_distract(enemy)
		else:
			choose_target(enemy, allies=allies)
	else:
		action = random.randrange(1,5)
		if action == 1 and enemy["parry"] == False:
			enemy_parry(enemy)
		else:
			choose_target(enemy, allies=allies)


def choose_target(enemy, allies):
	targets = ['player']
	target = ""
	ally = {}
	for allied in allies:
		targets.append(allied["reference"]['object'])
	for targetable in targets:
		if random.randrange(1, 3) == 1:
			target = targetable
			break
	if goad != "":
		for allied in allies:
			if allied['reference']['object'] == goad:
				target = goad
	for allied in allies:
		if allied['reference']['object'] == target:
			ally = allied
			break
	if target == "" or target == "player":
		target = "player"
	enemy_attack(enemy, ally, target)


def enemy_attack(enemy, ally, target, damage_modi = 1):
	reference = enemy["reference"]
	enemy["parry"] = False
	enemy["distract"] = False
	if target == "player":
		print(print_script("enemy_strike", enemy, ally))
	else:
		print(print_script("enemy_attack_ally", enemy, ally))
	enemy_roll = random.randrange(1, 101)
	time.sleep(5)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"]):
		if target == "player":
			agility_roll = random.randrange(1, 15)
			if agility_roll <= ability.ability["agility"]:
				print("You see the attack coming, but you will have to react quickly to avoid it.")
				time.sleep(3)
				dodge = ability.reaction(1.25, random.randrange(2, 4))
				if dodge:
					return
				else:
					print("Despite your efforts, you are too slow to avoid the blow.")
			print(print_script("enemy_hit", enemy, ally))
		else:
			print(print_script("enemy_hit_ally", enemy, ally))
		enemy_damage = (random.randrange(enemy["mindamage"] * damage_modi, (enemy["maxdamage"] * damage_modi) + 1) - ability.ability["armour"] - buffs[2])
		if target == "player":
			ability.ability["health"] -= enemy_damage
		else:
			ally['hp'] -= enemy_damage
		time.sleep(5)
		if target == "player":
			print(f"You are hit for {enemy_damage} damage!")
		else:
			print(f"{ally['reference']['object']} is hit for {enemy_damage} damage!")
		time.sleep(5)
	else:
		if target == "player":
			print(print_script("enemy_miss", enemy, ally))
		else:
			print(print_script("enemy_miss_ally", enemy, ally))
		time.sleep(5)
		print(f"Your enemy misses!")
		time.sleep(3)


def enemy_parry(enemy):
	reference = enemy["reference"]
	print(print_script("enemy_block", enemy))
	enemy["playermod"] -= (10 - enemy["agility"])
	enemy["parry"] = True
	time.sleep(5)


def enemy_distract(enemy):
	reference = enemy["reference"]
	print(print_script("enemy_divert", enemy))
	enemy["modifier"] += (10 + enemy["agility"])
	enemy["distract"] = True
	time.sleep(5)


def dead_check(enemy):
	global combat
	if enemy['hp'] <= 0:
		kill(enemy)
		combat = False
		return True
	else:
		return False


def player_defeat():
	global combat
	if ability.ability["health"] <= 0:
		combat = False
		if equipment.equipment["potions"] > 0:
			equipment.equipment["potions"] -= 1
			print("Your enemy deals you a blow, and suddenly everything swirls before your eyes. Quickly, you drink a potion, and the light returns. You continue to fight,")
			time.sleep(5)
			print("A potion was used to prevent defeat, but only at half it's potency.")
			time.sleep(3)
			ability.ability["health"] = 0
			ability.ability["health"] += random.randrange(2, 6)
			combat = True
		else:
			print("You are struck by your opponent, and the next thing you know, you have fallen. Everything begins to go dark, and there is nothing you can do to stop it.")
			return True


def kill(enemy):
	global gang_size
	global gang_lads
	global combat
	gang_size -= 1
	reference = enemy['reference']
	if enemy["type"] == "human":
		print(print_script("human_death", enemy))
		time.sleep(5)
	else:
		print(print_script("monster_death", enemy))
		time.sleep(5)
	if gang_size <= 0:
		combat = False
		post_combat.end_combat(gang_lads)
	else:
		next_victim(gang_lads)
		return False


def next_victim(enemies):
	global gang_index
	gang_index += 1
	enemy = enemies[gang_index]
	reference = enemy['reference']
	print(print_script("enemy_approach", enemy))
	time.sleep(5)
	return False


def ally_turn(ally, enemy):
	assistance = False
	goad = ""
	if ally['hp'] <= 0 and ally['xp'] != 0:
		print(print_script('ally_down', enemy, ally))
		time.sleep(5)
		ally['xp'] = 0
	action = random.randrange(1, 6)
	if ally['xp'] == 0:
		return
	elif action == 1 and ally['parry'] == False:
		ally_assist(ally, enemy)
	elif action == 2 and ally['distract'] == False:
		ally_distract(ally, enemy)
	else:
		ally_strike(ally, enemy)

def ally_strike(ally, enemy):
	reference = ally["reference"]
	ally["parry"] = False
	ally["distract"] = False
	ally_roll = random.randrange(1, 101)
	print(print_script("ally_attack", enemy, ally))
	time.sleep(5)
	if ally_roll <= (ally["skill"] + ally["modifier"]):
		ally_damage = (random.randrange(ally["mindamage"], ally["maxdamage"] + 1))
		enemy["hp"] -= ally_damage
		print(print_script("ally_hit", enemy, ally))
		time.sleep(5)
		print(f"{reference['object']} hits for {ally_damage} damage!")
		time.sleep(5)
	else:
		print(print_script("ally_miss", enemy, ally))
		time.sleep(5)
		print(f"{reference['object']} misses!")
		time.sleep(3)

def ally_assist(ally, enemy):
	global assistance
	reference = ally['reference']
	print(print_script("ally_assist", enemy, ally))
	time.sleep(5)
	assistance = True


def ally_distract(ally, enemy):
	global goad
	reference = ally['reference']
	print(print_script("ally_assist", enemy, ally))
	time.sleep(5)
	goad = reference['object']
