import time
import random
from functions import character
from functions import ability
from functions import post_combat
from functions import player_turn
from functions import equipment

gang_size = 0
gang_lads = []
combat = True

def combat_flow(enemy):
	global combat
	combat = True
	while combat:
		player_turn.turn(enemy)
		if dead_check(enemy):
			continue
		enemy_turn(enemy)
		if player_defeat():
			continue


def generate_enemy(maxhp, mindamage, maxdamage, baseskill, baseagility, xp, type, gender, name):
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


def initialize(enemies):
	global gang_size
	global gang_lads
	gang_size = len(enemies)
	gang_lads = enemies
	for enemy in enemies:
		combat_flow(enemy)


def enemy_turn(enemy):
	enemy["playermod"] = 0
	if enemy["type"] == "human":
		action = random.randrange(1,6)
		if action == 1 and enemy["parry"] == False:
			enemy_parry(enemy)
		if action == 2 and enemy["distract"] == False:
			enemy_distract(enemy)
		else:
			enemy_attack(enemy)
	else:
		action = random.randrange(1,5)
		if action == 1 and enemy["parry"] == False:
			enemy_parry(enemy)
		else:
			enemy_attack(enemy)


def enemy_attack(enemy, damage_modi = 1):
	reference = enemy["reference"]
	initial_script = [f"The {reference['object']} lunges in, ready to strike.",
"You ready yourself as your adversary charges forward, teeth bared in savage fury.",
f"The {reference['object']} charges, {reference['his']} eyes gleaming."]
	success_script = [
f"You are too slow to react. The {reference['object']} strikes you a blow. You hit the ground hard but roll to your feet, panting for breath.",
f"{reference['he'].capitalize()} takes a swing at you, and the attack finds its mark. You feel blood on your skin, and jump away before further harm.",
f"Your opponent lunges forwards. Before you can avoid the attack, you are dealt a glancing blow.",
f"You are beaten down by a hail of strikes, blocking one after the other. Finally, one makes its way through your defenses and you feel a sharp pain."]
	fail_script = [
f"Though your opponent comes in with speed and ferocity, you avoid everything {reference['he']} tries to strike you with.",
f"A strike is aimed at your head, but you are too quick for the {reference['object']}. You kick {reference['him']} and {reference['he']} staggers before {reference['he']} gets another chance to attack.",
f"{reference['he'].capitalize()} lunges forwards, missing you and stumbling past you. But {reference['he']} whirls again in another attack. You duck at the last second, the hair on your head whipping with the passing attack.",
f"As the attack passes to within a hair's breadth of your face, you twist and jump away in a diving roll, coming back to your feet, staring angrily at your opponent."]
	enemy["parry"] = False
	enemy["distract"] = False
	print(random.choice(initial_script))
	enemy_roll = random.randrange(1, 101)
	time.sleep(5)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"]):
		print(random.choice(success_script))
		enemy_damage = random.randrange(enemy["mindamage"] * damage_modi, (enemy["maxdamage"] * damage_modi) + 1)
		ability.ability["health"] -= enemy_damage
		time.sleep(5)
		print(f"You are hit for {enemy_damage} damage!")
		time.sleep(5)
	else:
		print(random.choice(fail_script))
		time.sleep(5)
		print(f"Your enemy misses!")
		time.sleep(3)


def enemy_parry(enemy):
	reference = enemy["reference"]
	initial_script = [
f"The {reference['object']} braces {reference['him']}self, and glares at you, daring you to fight.",
f"The other combatant raises {reference['his']} defenses, covering {reference['him']}self.",
f"Your opponent assumes a defensive stance, flattening {reference['his']} feet and barely moving."]
	if enemy["type"] == "human":
		initial_script.append(f"""Your opponent smiles at you wickedly. "Come on, {reference["whore"]}!" {reference['he']} yells.""")
	print(random.choice(initial_script))
	enemy["playermod"] -= (10 - enemy["agility"])
	enemy["parry"] = True
	time.sleep(5)


def enemy_distract(enemy):
	reference = enemy["reference"]
	initial_script = [f"You close in, sword leading the way. But at the last second, {reference['he']} jumps away, leaving you staggering past.",
"Your adversary lunges unexpectedly, and you only recognize the feint when it's too late and have already lept to the side, leaving yourself off balance.",
f"Suddenly, the {reference['object']} jumps forward, shoving your chest with one hand. You stagger, the breath knocked from your body."]
	print(random.choice(initial_script))
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
			print("A potion was used to prevent defeat.")
			ability.ability["health"] = 0
			ability.ability["health"] += random.randrange(4, 9)
		else:
			print("You are struck by your opponent, and the next thing you know, you have fallen. Everything begins to go dark, and there is nothing you can do to stop it.")
			post_combat.victory("defeat")


def kill(enemy):
	global gang_size
	global gang_lads
	global combat
	gang_size -= 1
	reference = enemy['reference']
	human_death = [
f"As your sword bites deeply into your enemy, {reference['he']} moans in pain, then crumples to the ground, dark blood flowing onto the ground.",
f"The {reference['object']} stares at you for a moment. Then a trickle of blood comes from the corner of {reference['his']} mouth, and {reference['he']} falls, dead.",
f"You pull your sword from your adversary's chest, and {reference['he']} topples over backwards instantly, dead before {reference['he']} hits the ground.",
f"You bury your sword up to the hilt into the {reference['object']}, the blade protruding from {reference['his']} back. You kick {reference['him']} from your sword, and the body falls, blood pooling.",
f"For a moment, {reference['he']} stays standing. But then {reference['he']} crashes down to the ground, a scarlet blossom growing around {reference['his']} body.",
f"The {reference['object']} falls to {reference['his']} knees, head leaning forward. You don't hesitate, bringing your sword down like an executioner's axe, taking the head from {reference['his']} shoulders.",
f"You cut the {reference['object']}'s hand, and {reference['he']} drops {reference['his']} weapon. {reference['he'].capitalize()} tries to punch you, but you duck under the blow and cut {reference['him']} across the back. {reference['he'].capitalize()} falls without a cry.",
f"The {reference['object']} falls onto {reference['his']} back, gasping for air. You lunge forwards and plunge your sword into {reference['his']} chest, spattering your blade with blood."]
	monster_death = [f"The {reference['object']} growls one last time, then falls to the ground.",
f"With a sickening squelch, you tear your sword from the monster, and it topples like an upset statue."]
	if enemy["type"] == "human":
		print(random.choice(human_death))
		time.sleep(5)
	else:
		print(random.choice(monster_death))
		time.sleep(5)
	if gang_size <= 0:
		combat = False
		post_combat.end_combat(gang_lads)
	else:
		next_victim(gang_lads)
		return False


def next_victim(enemies):
	gang_index = 0
	gang_index += 1  # This will always equal 1, so why not just set it to 1?
	enemy = enemies[gang_index]
	reference = enemy['reference']
	friend_approach = [
f"A {reference['object']} rushes forward, {reference['pain']}ing with rage at {reference['his']} companion's death.",
f"A {reference['object']} approaches you now, more wary than your previous, now deceased opponent.",
f"You ready your sword, now stained with blood, shouting a challenge to your next opponent. {reference['he'].capitalize()} responds to the challenge and moves forwards."]
	print(random.choice(friend_approach))
	time.sleep(5)
	return False