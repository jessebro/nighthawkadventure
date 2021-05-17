import time
import random
from functions import ability
from functions import inventory
from functions import weapon
from functions import equipment
from functions import enemy_round
from functions.utils import input_stuff

def get_turn_choice(enemy):
	reference = enemy["reference"]
	initial_script = [f"""You circle each other, sizing each other up.""",
f"""You ready your weapon and glare at your opponent.""",
f"""You feel your heart pounding, feel your chest rising with smooth, even breaths.""",
f"""{reference['object'].capitalize()} lunges. You jump aside at the last second."""]
	if enemy["type"] == "human":
		initial_script.append("""Steel meets, and you stare at each other, blades locked in a clinch.""")
	action = input(random.choice(initial_script) + f""" Do you...
	1. Strike
	2. Parry
	3. Distract       ~ {ability.ability["health"]} / {ability.ability["maxhealth"]} health ~
	4. Use Item
	5. Check Inventory
> """)
	return action


def turn(enemy):
	enemy["modifier"] = 0
	action = get_turn_choice(enemy)
	if action == "1":
		strike(enemy)
	elif action == "2":
		parry(enemy)
	elif action == "3":
		distract(enemy)
	elif action == "4":
		use_item(enemy)
	elif action == "5":
		inventory_shown = inventory.show()
		if not inventory_shown:
			turn(enemy)


def strike(enemy, damage_mod=1.0, smoke=False):
	critical = 10
	bleeding = 20
	bleed_lvl = 1
	vampiric = False
	agility_check = 30
	reference = enemy["reference"]
	attacks = [known for known in weapon.weapon["attacks"] if known['enabled']]
	prompt = ""
	counter = 0
	options = []
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


	initial_script = ["You lunge forward suddenly, sword leading the way.",
"You swiftly close the distance between you and your adversary, weapon raised high.",
f"""You rush towards {reference["object"]}, sword grasped firmly.""",
f"You approach {reference['object']}, attacking when you are only a few paces away.",
f"Your opponent jumps towards you. You parry the blow easily, spin your sword, and riposte swiftly.",
f"You charge forwards, spin on one foot, and bring your sword crashing down on {reference['object']}.",
"Your opponent moves to attack, but stumbles on some irregular terrain. You seize your chance and lunge forwards."]
	success_script = [f"You feel the tip of your sword bury in your enemy's flesh, accompanied by a {reference['pain']} of pain.",
"Your opponent tries to duck away from the blow, but you feel a bit of resistance, and see a spurt of blood.",
f"""You're too fast for your opponent. {reference['he'].capitalize()} raises {reference['his']} defenses weakly, but you easily bat away the blockage and cut into {reference["him"]} with your sword deeply.""",
f"""You twirl your sword in a silver spiral, feeling with satisfaction as the sword bites deeply into {reference["object"]}.""",
f"{reference['object'].capitalize()} readies {reference['him']}self for your attack. At the last second you duck and roll behind {reference['him']}, under {reference['his']} guard and slash {reference['him']} across the back.",
f"You enemy tries to step backwards, but {reference['his']} heel hits a raised section of ground. {reference['he'].capitalize()} staggers, and you slash {reference['him']} easily.",
f"With a deft sword movement you explode into action, striking with your whirling sword, spilling the blood of {reference['object']}."]
	fail_script = ["Your sword slices through the air, but meets nothing as your adversary sidesteps",
"You swing your sword in a cruel lateral strike, but your opponent ducks just in time, the wind chasing the blade making a whistling sound."
,f"""You swing your sword downwards, grunting with the effort. {reference["object"].capitalize()} jumps back at the last second, the tip of your sword barely a inch from {reference["his"]} body."""]
	agility_script = ["You're quick enough to strike a second time.",
"You bring your blade back quickly for a second attempt.",
"You spin with the momentum of the sword, whirling and attacking again swiftly."]
	parry_script = [f"You swing your sword, but {reference['object']} is ready, dodging sideways at the last second.",
f"As you charge forwards, {reference['object']} slams into you, pushing you back, staggering."]
	if enemy["type"] == "human":
		success_script.extend([f"{reference['he'].capitalize()} moves to block your blow, but you bring your foot up suddenly in a kick. Then you strike, {reference['his']} staggering form an easy victim to your blade.",
f"""You feel your sword find its target, and hear a scream of pain. "A pox on you!" {reference['object']} spits. """])
		fail_script.extend([f"There's the ring of steel on steel as {reference['object']} brings {reference['his']} sword up just in time.",
f"""{reference['object'].capitalize()} pushes your attack aside and grins wickedly. "What now, you {reference['insult']}?" {reference['he']} hisses. """])
	print(random.choice(initial_script))
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
			print(random.choice(success_script))
			time.sleep(5)
			if roll <= (critical + (weapon.weapon["finesse"] * 2) + ability.ability["strike_lvl"]):
				print("The strike was well aimed, and scored a critical hit!")
				time.sleep(3)
				damage_multi += 1
			if roll <= (bleeding + (weapon.weapon["sharpness"] + ability.ability["strength"])):
				enemy["bleeding"] += bleed_lvl
				print("Your attack cuts deep, and causes your enemy to bleed!")
				time.sleep(4)
			min_damage = int((ability.ability["strength"] / 2) * damage_multi)
			max_damage = int((ability.ability["strength"] + 2) * damage_multi)
			player_damage = random.randrange(min_damage, max_damage) + ability.ability["strike_lvl"] + weapon.weapon["sharpness"]
			if vampiric:
				healing = random.randrange(1,101)
				if healing <= 50:
					ability.ability["health"] += player_damage
					print(f"You regained {player_damage} health from your vampiric attack!")
					if ability.ability["health"] > ability.ability["maxhealth"]:
						ability.ability["health"] = ability.ability["maxhealth"]
			enemy["hp"] -= player_damage
			print(f"You hit for {player_damage} damage!")
			time.sleep(5)
			weapon.lose_stability()
			counter += 1
		else:
			if enemy["parry"]:
				print(random.choice(parry_script))
				time.sleep(5)
				print("Your enemy parries your blow and counter attacks!")
				time.sleep(3)
				counter += 1
				enemy_round.enemy_attack(enemy)
			else:
				print(random.choice(fail_script))
				time.sleep(5)
				print(f"You miss your attack!")
				time.sleep(5)
				counter += 1
		if attacks == 3:
			attacks -= 1
			print(random.choice(agility_script))
			time.sleep(5)
		elif attacks == 4:
			attacks -= 1
			print("You use the smoke to disappear, then emerge again suddenly.")
			time.sleep(5)


def parry(enemy):
	reference = enemy["reference"]
	initial_script = ["You raise your sword in a defensive position.",
"You brace yourself for your charging adversary, ready and waiting", f"You bring your sword to bare, watching {reference['object']} closely."]
	success_script = [f"Your enemy runs forward, but at the last second you kick {reference['him']} back, knocking the breath from {reference['his']} body.",
f"{reference['he'].capitalize()} runs forward suddenly, but you are ready. {reference['his'].capitalize()} attack is caught on your sword and you twirl the blade swifty, knocking {reference['him']} off balance.",
f"As your opponent charges, you sidestep. {reference['he'].capitalize()} runs straight past you, back exposed, almost asking to be slashed.",
f"""{reference['object'].capitalize()} attacks, but you spin away from the blow, ending your twirl on your opponent's flank.""",
f"Your adversary closes in, but at the last second you lunge forwards, slamming your shoulder into {reference['him']}. {reference['he'].capitalize()} stumbles backwards, sputtering for breath."]
	fail_script = ["You raise your sword against the expected attack, but it comes quicker than you thought. You feel a cut upon your face.",
"Your opponent rushes forwards. You try and duck to the side at the last second, but are too slow. Pain racks your body and you jump away, cursing.",
"You deflect the first attack, but the second comes in quicker than you can react. You manage to avoid the worst of the blow, but still, it hurts."]
	print(random.choice(initial_script))
	enemy["modifier"] -= (10 + ability.ability["agility"] + ability.ability["parry_lvl"])
	enemy_roll = random.randrange(1,101)
	time.sleep(5)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"] - ability.ability['agility']):
		print(random.choice(fail_script))
		enemy_damage = random.randrange(enemy["mindamage"], enemy["maxdamage"])
		ability.ability["health"] -= enemy_damage
		time.sleep(5)
		print(f"You are hit for {enemy_damage} damage!")
		time.sleep(5)
		turn(enemy)
	else:
		print(random.choice(success_script))
		time.sleep(5)
		print("Your parry succeeds and you riposte!")
		time.sleep(3)
		strike(enemy, damage_mod=1.5)

def distract(enemy):
	reference = enemy["reference"]
	initial_script = ["Suddenly, you lean down, scoop up a handful of dirt and throw it in your enemy's face.",
f"You yell fiercely into the face of your opponent. {reference['he'].capitalize()} recoils at the sudden noise.",
f"""You feint sideways, then come back to your previous position. {reference['object'].capitalize()} staggers slightly at the sudden move.""",
f"As your enemy moves closer, you swiftly kick {reference['him']} painfully in the shin.",
f"Your opponent brings down {reference['his']} attack. You raised your blade at the last second, and with your free hand punch {reference['him']} in the face, sending {reference['him']} staggering away."]
	print(random.choice(initial_script))
	time.sleep(5)
	enemy["playermod"] += (10 + ability.ability["agility"] + ability.ability["distract_lvl"] * 2)
	attack_chance = random.randrange(1,101)
	if attack_chance <= (50 + ability.ability['agility'] + ability.ability["distract_lvl"]):
		print("Your enemy's loss of focus allows you to make an attack!")
		time.sleep(3)
		strike(enemy)
	else:
		return False



def use_item(enemy):
	reference = enemy["reference"]
	potion_script = [f"You jump away from the melee and pull a potion from your belt. You drain the liquid in a few seconds, and toss the empty bottle away. You feel strength lost return to you.",
f"You kick your opponent, sending {reference['him']} backwards. While {reference['he']} staggers, you drink a potion, and pain leaves your body."]
	knife_script = [f"Your foe lunges forwards. At the last moment you jump away, sliding across the ground. You twist and hurl a throwing knife with all your strength. The projectile finds its mark.",
f"As your opponent charges towards you, you pull out a throwing knife, throwing it at {reference['him']}. Your aim is true and {reference['he']} stumbles, a bloodstain on {reference['his']} leg."]
	oil_script = [f"You produce a vial of blade oil and quickly splash it on your sword. It will not last long, but it will make your enemy feel pain.",
f"{reference['object'].capitalize()} stops as you pull a vial of liquid from your belt. You pour it onto your blade, and attack."]
	smoke_bomb_script = ["Closing your eyes and mouth, you throw down a smoke bomb. Thick, grey smoke covers the battle area, making sight impossible.",
"You light the fuse of a smoke bomb and hurl it at your enemy. There's a bang and suddenly everything is covered by grey smoke."]
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
		1. {equipment.equipment["potions"]} {plurals["potions"]}
		2. {equipment.equipment["knives"]} {plurals["knives"]}
		3. {equipment.equipment["oils"]} {plurals["oils"]}
		4. {equipment.equipment["smoke bombs"]} {plurals["smoke bombs"]}

Enter 'b' to go back
> """)
	if item_use == "1":
		equipment.equipment["potions"] -= 1
		if equipment.equipment["potions"] <0:
			print("You have no more potions!")
			equipment.equipment["potions"] = 0
			time.sleep(2)
			use_item(enemy)
			return False
		elif ability.ability["health"] == ability.ability["maxhealth"]:
			print("You're on max health, and a potion would have no effect.")
			time.sleep(5)
			equipment.equipment["potions"] += 1
			use_item(enemy)
			return False
		else:
			print(random.choice(potion_script))
			healing = random.randrange(4,9)
			ability.ability["health"] += healing
			time.sleep(5)
			print(f"You regained {healing} health!")
			time.sleep(5)
			enemy_round.enemy_turn(enemy)
	if item_use == "2":
		equipment.equipment["knives"] -= 1
		if equipment.equipment["knives"] <0:
			print("You have no more knives!")
			equipment.equipment["knives"] = 0
			time.sleep(2)
			use_item(enemy)
		else:
			print(random.choice(knife_script))
			knife_damage = random.randrange(2, 6)
			enemy["hp"] -= knife_damage
			time.sleep(5)
			print(f"Your knife hits for {knife_damage} damage!")
			time.sleep(5)
	if item_use == "3":
		equipment.equipment["oils"] -= 1
		if equipment.equipment["oils"] <0:
			print("You have no more oils!")
			equipment.equipment["oils"] = 0
			time.sleep(2)
			use_item(enemy)
			return False
		else:
			print(random.choice(oil_script))
			time.sleep(5)
			strike(enemy, damage_mod=2)
			if enemy['hp'] <= 0:
				return False
	if item_use == "4":
		equipment.equipment["smoke bombs"] -= 1
		if equipment.equipment["smoke bombs"] <0:
			print("You have no more smoke bombs!")
			equipment.equipment["smoke bombs"] = 0
			time.sleep(2)
			use_item(enemy)
			return False
		else:
			print(random.choice(smoke_bomb_script))
			time.sleep(5)
			strike(enemy,smoke=True)
	if item_use == "b":
		turn(enemy)
		return False
