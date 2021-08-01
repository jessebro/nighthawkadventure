import time
from functions import character
from functions import ability
from functions import post_combat
from functions import player_turn
from functions import equipment
from functions.player_turn import buffs
from functions.combat_scripts import *

gang_size = 0
gang_lads = []
gang_index = 0
combat = True
assistance = 0
goad = 0

def combat_flow(enemy, allies):
	global combat
	combat = True
	while combat:
		player_turn.turn(enemy)
		if dead_check(enemy):
			continue
		enemy_turn(enemy, allies)
		if player_defeat():
			continue
		for ally in allies:
			ally_turn(ally, enemy)
			if dead_check(enemy):
				continue


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
		combat_flow(enemy, allies)


def enemy_turn(enemy, allies):
	if enemy['bleeding'] > 0:
		damage = random.randrange(2,6)
		print(f"Your enemy bleeds for {damage} damage!")
		time.sleep(4)
		enemy["modifier"] -= (10 * enemy['bleeding'])
		enemy["bleeding"] -= 1
		dead_check(enemy)
	enemy["playermod"] = 0
	if enemy["type"] == "human":
		action = random.randrange(1,6)
		if action == 1 and enemy["parry"] == False:
			enemy_parry(enemy)
		if action == 2 and enemy["distract"] == False:
			enemy_distract(enemy)
		else:
			enemy_attack(enemy, allies=allies)
	else:
		action = random.randrange(1,5)
		if action == 1 and enemy["parry"] == False:
			enemy_parry(enemy)
		else:
			enemy_attack(enemy, allies=allies)


def enemy_attack(enemy, allies, damage_modi = 1):
	reference = enemy["reference"]
	target_select = random.randrange(1, len(allies) + 3)
	if target_select <= len(allies):
		target = "ally"
	else:
		target = "player"
	enemy["parry"] = False
	enemy["distract"] = False
	print(print_script(enemy_strike, reference))
	enemy_roll = random.randrange(1, 101)
	time.sleep(5)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"]):
		agility_roll = random.randrange(1, 15)
		if agility_roll <= ability.ability["agility"]:
			print("You see the attack coming, but you will have to react quickly to avoid it.")
			time.sleep(3)
			dodge = ability.reaction(1.25, random.randrange(2, 4))
			if dodge:
				return
			else:
				print("Despite your efforts, you are too slow to avoid the blow.")
		print(print_script(enemy_hit, reference))
		enemy_damage = (random.randrange(enemy["mindamage"] * damage_modi, (enemy["maxdamage"] * damage_modi) + 1) - ability.ability["armour"] - buffs[2])
		ability.ability["health"] -= enemy_damage
		time.sleep(5)
		print(f"You are hit for {enemy_damage} damage!")
		time.sleep(5)
	else:
		print(print_script(enemy_miss, reference))
		time.sleep(5)
		print(f"Your enemy misses!")
		time.sleep(3)


def enemy_parry(enemy):
	reference = enemy["reference"]
	print(print_script(enemy_block, reference))
	enemy["playermod"] -= (10 - enemy["agility"])
	enemy["parry"] = True
	time.sleep(5)


def enemy_distract(enemy):
	reference = enemy["reference"]
	print(print_script(enemy_divert, reference))
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
			ability.ability["health"] = 0
			ability.ability["health"] += random.randrange(2, 6)
		else:
			print("You are struck by your opponent, and the next thing you know, you have fallen. Everything begins to go dark, and there is nothing you can do to stop it.")
			post_combat.victory("defeat")


def kill(enemy):
	global gang_size
	global gang_lads
	global combat
	gang_size -= 1
	reference = enemy['reference']
	if enemy["type"] == "human":
		print(print_script(human_death, reference))
		time.sleep(5)
	else:
		print(print_script(monster_death, reference))
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
	time.sleep(5)
	return False

def ally_turn(ally, enemy):
	action = random.randrange(1, 6)
	if action == 1 and ally['parry'] == False:
		ally_assist(ally, enemy)
	elif action == 2 and ally['distact'] == False:
		ally_distract(ally, enemy)
	else:
		ally_strike(ally, enemy)

def ally_strike(ally, enemy):
	reference = ally["reference"]
	ally["parry"] = False
	ally["distract"] = False
	ally_roll = random.randrange(1, 101)
	time.sleep(5)
	time.sleep(3)
	if ally_roll <= (ally["skill"] + ally["modifier"]):
		ally_damage = (random.randrange(ally["mindamage"], ally["maxdamage"] + 1))
		enemy["health"] -= ally_damage
		time.sleep(5)
		print(f"{reference['name']} hits for {ally_damage} damage!")
		time.sleep(5)
	else:
		print(f"{reference['name']} misses!")
		time.sleep(3)

def ally_assist(ally, enemy):
	global assistance
	reference = ally['reference']
	assistance = 1

def ally_distract(ally, enemy):
	global goad
	reference = ally['reference']
	goad = 1
