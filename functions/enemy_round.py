import time
from functions import achievements
from functions import character
from functions import ability
from functions import post_combat
from functions import player_turn
from functions import equipment
from functions.player_turn import buffs
from functions.combat_scripts import *
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import print_stuff
from functions import sounds
from functions import settings

delay = 5
if settings.settings['immersion'] == "OFF":
		delay = 0

# naughty global state goes here
defaults = {
	"gang_size": 0,
	"gang_lads": [],
	"gang_index": 0,
	"assistance": False,
	"goad": "",
	"damage_dealt": 0,
	"damage_received": 0,
	"health_restored": 0,    # Put round summary
	"turns_taken": 0,
	"total_damage_dealt": 0,
	"total_damage_received": 0,
	"hits": 0,
	"attacks": 0,
	"damages": [],
	"striked": False,
	"parried": False,
	"distracted": False,
	"used_item": False,
	"knifed": False,
	"countered": False,
	"strikes_made": [],
	"deaded": 0
}

game_state = {}



def combat_flow(enemy, enemies, allies, boss):
	global game_state
	if boss:
		sounds.doom()
	else:
		sounds.play_combat(enemy['type'])
	while True:
		game_state['damage_dealt'] = 0
		game_state['damage_received'] = 0
		game_state['health_restored'] = 0
		game_state['turns_taken'] += 1
		player_turn.turn(enemy, allies)
		if dead_check(enemy, enemies, boss):
			break
		if player_defeat():
			break
		enemy_turn(enemy, enemies, allies, boss)
		if enemy['yield']:
			break
		if dead_check(enemy, enemies, boss):
			break
		if player_defeat():
			break
		for ally in allies:
			ally_turn(ally, enemy)
			if dead_check(enemy, enemies, boss):
				break
		round_summary(enemy)


def generate_actor(maxhp, mindamage, maxdamage, baseskill, baseagility, xp, type, gender, name):
	enemy = {}
	enemy["maxhp"] = maxhp * settings.settings["difficulty"]["health_mult"]
	enemy["hp"] =  enemy["maxhp"]
	enemy["mindamage"] = mindamage
	enemy["maxdamage"] = maxdamage
	enemy["baseskill"] = baseskill * settings.settings["difficulty"]["accuracy_mult"]
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
	if enemy['type'] == "human":
		enemy['yield'] = False
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


def initialize(enemies: list, allies=(), boss=False):
	global game_state
	global defaults
	game_state = copy.deepcopy(defaults)
	game_state['gang_size'] = len(enemies)
	game_state['gang_lads'] = enemies
	for enemy in enemies:
		if ability.ability['health'] <= 0:
			break
		combat_flow(enemy, enemies, allies, boss)


def enemy_turn(enemy, enemies, allies, boss):
	global game_state
	if get_enemy_status(enemy) == "Crippled" and enemy['type'] == 'human':
		save = random.randrange(1,101)
		if save <= ability.perks["bluster"]["effect"]:
			enemy['yield'] = True
			enemy_yield(enemy)
			return
	if enemy['bleeding'] > 0:
		damage = random.randrange(2,6)
		damage_script = colour_it(f"{damage} damage!", Color.YELLOW)
		print(f"Your enemy bleeds for {damage_script}")
		time.sleep(delay)
		enemy["modifier"] -= (10 * enemy['bleeding'])
		enemy["bleeding"] -= 1
		game_state['damage_dealt'] += damage
		game_state['total_damage_dealt'] += damage
		if dead_check(enemy, enemies, boss):
			if not achievements.achievements['bleed_out']['unlocked']:
				achievements.get_achievement("bleed_out")
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
	goad = game_state['goad']
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
	global game_state
	reference = enemy["reference"]
	enemy["parry"] = False
	enemy["distract"] = False
	if target == "player":
		print_script("enemy_strike", enemy, ally)
	else:
		get_scripts(enemy, ally, "ally")
		print_script("enemy_attack_ally", enemy, ally)
	enemy_roll = random.randrange(1, 101)
	time.sleep(delay)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"]):
		if target == "player":
			agility_roll = random.randrange(1, 15)
			if agility_roll <= ability.ability["agility"]:
				print(colour_it("You see the attack coming, but you will have to react quickly to avoid it.", Color.CHECK))
				time.sleep(delay)
				dodge = ability.reaction(1.25, random.randrange(2, 4))
				if dodge:
					print("You are nimble enough to avoid the blow!")
					time.sleep(delay)
					return
				else:
					print("Despite your efforts, you are too slow to avoid the blow.")
					time.sleep(delay)
			print_script("enemy_hit", enemy, ally)
		else:
			print_script("enemy_hit_ally", enemy, ally)
		enemy_damage = (random.randrange(enemy["mindamage"] * damage_modi, (enemy["maxdamage"] * damage_modi) + 1) - ability.ability["armour"] - buffs[2])
		if target == "player":
			if random.randrange(1, 101) <= ability.perks['lightning reflexes']['effect']:
				enemy_damage = 1
				print("Through your lightning reflexes, the attack only scrapes you.")
			ability.ability["health"] -= enemy_damage
		else:
			ally['hp'] -= enemy_damage
		enemy_damage_script = colour_it(f"{enemy_damage} damage!", Color.RED)
		time.sleep(delay)
		if target == "player":
			print(f"You are hit for {enemy_damage_script}")
			game_state["damage_received"] += enemy_damage
			game_state['total_damage_received'] += enemy_damage
		else:
			print(f"{ally['reference']['object']} is hit for {enemy_damage_script}")
		time.sleep(delay)
	else:
		if target == "player":
			print_script("enemy_miss", enemy, ally)
		else:
			print_script("enemy_miss_ally", enemy, ally)
		time.sleep(delay)
		print(colour_it("Your enemy misses!", Color.GREEN))
		time.sleep(delay)


def enemy_parry(enemy):
	reference = enemy["reference"]
	print_script("enemy_block", enemy)
	enemy["playermod"] -= (10 - enemy["agility"])
	enemy["parry"] = True
	time.sleep(delay)


def enemy_distract(enemy):
	reference = enemy["reference"]
	print_script("enemy_divert", enemy)
	enemy["modifier"] += (10 + enemy["agility"])
	enemy["distract"] = True
	time.sleep(delay)


def dead_check(enemy, enemies, boss):
	global game_state
	if enemy['hp'] <= 0:
		kill(enemy, enemies, boss)
		return True
	else:
		return False


def player_defeat():
	global game_state
	if ability.ability["health"] <= 0:
		game_state['deaded'] += 1
		if equipment.equipment["potions"] > 0:
			equipment.equipment["potions"] -= 1
			print("Your enemy deals you a blow, and suddenly everything swirls before your eyes. Quickly, you drink a potion, and the light returns. You continue to fight,")
			time.sleep(delay)
			print("A potion was used to prevent defeat, but only at half it's potency.")
			time.sleep(delay)
			ability.ability["health"] = 0
			healing = random.randrange(2, 6)
			ability.ability["health"] += healing
			game_state['health_restored'] += healing
		else:
			print("You are struck by your opponent, and the next thing you know, you have fallen. Everything begins to go dark, and there is nothing you can do to stop it.")
			return True


def kill(enemy, enemies, boss):
	global game_state
	game_state['gang_size'] -= 1
	reference = enemy['reference']
	if enemy["type"] == "human":
		print_script("human_death", enemy)
		time.sleep(delay)
	else:
		print_script("monster_death", enemy)
		time.sleep(delay)
	print(colour_it(f"{reference['object'].capitalize()} was killed!", Color.BLUE))
	time.sleep(delay)
	if game_state['knifed'] and not game_state['striked'] and not achievements.achievements['knife_master']['unlocked']:
		achievements.get_achievement('knife_master')
	if game_state['assistance'] or game_state['goad'] and not achievements.achievements['teamwork']['unlocked']:
		achievements.get_achievement("teamwork")
	if game_state['gang_size'] <= 0:
		if boss:
			sounds.end_boss()
		elif enemy['type'] == "human":
			sounds.end_human()
		else:
			sounds.end_combat()
		summary(enemies)
		post_combat.end_combat(game_state['gang_lads'])
	else:
		next_victim(game_state['gang_lads'])
		return False


def next_victim(enemies):
	global game_state
	game_state['gang_index'] += 1
	if game_state['gang_index'] >= len(enemies):
		return
	enemy = enemies[game_state['gang_index']]
	reference = enemy['reference']
	print_script("enemy_approach", enemy)
	time.sleep(delay)
	return False


def ally_turn(ally, enemy):
	assistance = False
	goad = ""
	get_scripts(enemy, ally, "ally")
	if ally['hp'] <= 0 and ally['xp'] != 0:
		print_script('ally_down', enemy, ally)
		time.sleep(delay)
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
	global game_state
	reference = ally["reference"]
	ally["parry"] = False
	ally["distract"] = False
	ally_roll = random.randrange(1, 101)
	print_script("ally_attack", enemy, ally)
	time.sleep(delay)
	if ally_roll <= (ally["skill"] + ally["modifier"]):
		ally_damage = (random.randrange(ally["mindamage"], ally["maxdamage"] + 1))
		ally_damage_script = colour_it(f"{ally_damage} damage!", Color.YELLOW)
		enemy["hp"] -= ally_damage
		print_script("ally_hit", enemy, ally)
		time.sleep(delay)
		print(f"{reference['object'].capitalize()} hits for {ally_damage_script}")
		time.sleep(delay)
		game_state['damage_dealt'] += ally_damage
		game_state['total_damage_dealt'] += ally_damage
	else:
		print_script("ally_miss", enemy, ally)
		time.sleep(delay)
		print(colour_it(f"{reference['object'].capitalize()} misses!", Color.RED))
		time.sleep(delay)

def ally_assist(ally, enemy):
	global game_state
	print_script("ally_assist", enemy, ally)
	time.sleep(delay)
	game_state['assistance'] = True


def ally_distract(ally, enemy):
	global game_state
	reference = ally['reference']
	print_script("ally_assist", enemy, ally)
	time.sleep(delay)
	game_state['goad'] = reference['object']


def round_summary(enemy):
	global game_state
	status = get_enemy_status(enemy)
	print_stuff([f"""{colour_it("ROUND SUMMARY", Color.UNDERLINE)}
{colour_it("Damage dealt: ", Color.YELLOW)} {game_state['damage_dealt']}
{colour_it("Damage received: ", Color.RED)} {game_state['damage_received']}
{colour_it("Health restored: ", Color.GREEN)} {game_state['health_restored']}
{colour_it("Enemy Status: ", Color.BLUE)} {status}"""])


def get_enemy_status(enemy):
	if enemy['hp'] == enemy['maxhp']:
		status = "Untouched"
	elif enemy['hp'] >= enemy['maxhp'] / 1.333333333:
		status = "Good"
	elif enemy['hp'] >= enemy['maxhp'] / 2:
		status = "Bloodied"
	elif enemy['hp'] >= enemy['maxhp'] / 4:
		status = "Injured"
	else:
		status = "Crippled"
	return status


def enemy_yield(enemy):
	reference = enemy["reference"]
	money = random.randrange(1,11)
	print(f"""{reference['object'].capitalize()} throws down {reference['his']} weapon. "Enough! I yield!" {reference['he']} says, dropping {money} onto the ground.""")



def summary(enemy):
	global game_state
	accuracy = game_state['hits'] / game_state['attacks'] * 100
	damage_prhit = sum(game_state['damages']) / len(game_state['damages'])
	print_stuff([f"""{colour_it("COMBAT SUMMARY", Color.UNDERLINE)}
Turns Taken: {game_state['turns_taken']}
{colour_it("Total Damage Dealt:",Color.YELLOW)} {game_state['total_damage_dealt']}    
{colour_it("Total Damage Received:",Color.RED)} {game_state['total_damage_received']}
{colour_it("Weapon Accuracy:",Color.GREEN)} {round(accuracy, 2)}%
{colour_it("Average Damage per Hit:",Color.CYAN)} {round(damage_prhit, 2)}
{colour_it("Enemies Defeated:",Color.PURPLE)} {len(enemy)}"""])
	game_state['accuracy'] = accuracy
	game_state['damage_prhit'] = damage_prhit
	if game_state['total_damage_received'] <= 0 and len(enemy) >= 3:
		achievements.get_achievement("untouchable")
	if game_state['turns_taken'] <= len(enemy) and len(enemy) >= 3:
		achievements.get_achievement("body_count")
	if game_state['striked'] and game_state['parried'] and game_state['distracted']:
		achievements.get_achievement("jack_of_all_trades")
	if not game_state['striked'] and game_state['countered'] and not game_state['distracted'] and not game_state['knifed'] and len(enemy) >= 2:
		achievements.get_achievement("counter_kill")
	if not game_state['used_item']:
		achievements.get_achievement("resourceful")
	if len(game_state['strikes_made']) >= 3:
		achievements.get_achievement('swordmaster')
	if game_state['deaded'] >= 3:
		achievements.get_achievement('back_for_more')

