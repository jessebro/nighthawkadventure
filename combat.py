import time
import random
import character
import ability
import equipment
import inventory
import post_combat
import weapon


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
	return reference


def intro(enemy):
	reference = enemy["reference"]
	script = f"""You come across a {reference["object"]}. {reference["he"].capitalize()} readies {reference["him"]}self for a fight and you draw your sword."""
	print(script)
	time.sleep(3)
	turn(enemy)


def get_turn_choice(enemy):
	reference = enemy["reference"]
	initial_script = [f"""You circle each other, sizing each other up. Do you...
	1. Strike
	2. Parry
	3. Distract
	4. Use Item
	5. Check Inventory
	6. Flee
> """, f"""You ready your weapon and glare at your opponent. Do you...
	1. Strike
	2. Parry
	3. Distract
	4. Use Item
	5. Check Inventory
	6. Flee
> """, f"""You feel your heart pounding, feel your chest rising with smooth, even breaths. Do you...
	1. Strike
	2. Parry
	3. Distract
	4. Use Item
	5. Check Inventory
	6. Flee
> """, f"""The {reference["object"]} lunges. You jumps aside at the last second. Do you...
	1. Strike
	2. Parry
	3. Distract
	4. Use Item
	5. Check Inventory
	6. Flee
> """]
	if enemy["type"] == "human":
		initial_script.append("""Steel meets, and you stare at each other, blades locked in a clinch. Do you...
	1. Strike
	2. Parry
	3. Distract
	4. Use Item
	5. Check Inventory
	6. Flee
> """)
	action = input(random.choice(initial_script))
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
	elif action == "6":
		flee(enemy)


def strike(enemy, damage_mod=1.0):
	reference = enemy["reference"]
	initial_script = ["You lunge forward suddenly, sword leading the way.",
"You swiftly close the distance between you and your adversary, weapon raised high.",
f"""You rush towards the {reference["object"]}, sword grasped firmly.""",
f"You approach the {reference['object']}, attacking when you are only a few paces away.",
f"Your opponent jumps towards you. You parry the blow easily, spin your sword, and riposte swiftly.",
f"You charge forwards, spin on one foot, and bring your sword crashing down on the {reference['object']}.",
"Your opponent moves to attack, but stumbles on some irregular terrain. You seize your chance and lunge forwards."]
	success_script = [f"You feel the tip of your sword bury in your enemy's flesh, accompanied by a {reference['pain']} of pain.",
"Your opponent tries to duck away from the blow, but you feel a bit of resistance, and see a spurt of blood.",
f"""You're too fast for your opponent. {reference['he'].capitalize()} raises {reference['his']} defenses weakly, but you easily bat away the blockage and cut into {reference["him"]} with your sword deeply.""",
f"""You twirl your sword in a silver spiral, feeling with satisfaction as the sword bites deeply into the {reference["object"]}.""",
f"The {reference['object']} readies {reference['him']}self for your attack. At the last second you duck and roll behind {reference['him']}, under {reference['his']} guard and slashing {reference['him']} across the back.",
f"You enemy tries to step backwards, but {reference['his']} heel hits a raised section of ground. {reference['he'].capitalize()} staggers, and you slash {reference['him']} easily.",
f"With a deft sword movement you explode into action, striking with your whirling sword, spilling the blood of the {reference['object']}."]
	fail_script = ["Your sword slices through the air, but meets nothing as your adversary sidesteps",
"You swing your sword in a cruel lateral strike, but your opponent ducks just in time, the wind chasing the blade making a whistling sound."
,f"""You swing you sword downwards, grunting with the effort. The {reference["object"]} jumps back as the last second, the tip of your sword barely a inch from {reference["his"]} body."""]
	agility_script = ["You're quick enough to strike a second time.",
"You bring your blade back quickly for a second attempt.",
"You spin with the momentum of the sword, whirling and attacking again swiftly."]
	parry_script = [f"You swing your sword, but the {reference['object']} is ready, dodging sideways at the last second.",
f"As you charge forwards, the {reference['object']} slams into you, pushing you back, staggering."]
	if enemy["type"] == "human":
		success_script.extend([f"{reference['he'].capitalize()} moves to block your blow, but you bring your foot up suddenly in a kick. Then you strike, {reference['his']} staggering form an easy victim to your blade.",
f"""You feel your sword find its target, and hear a scream of pain. "A pox on you!" the {reference['object']} spits. """])
		fail_script.extend([f"There's the ring of steel on steel as the {reference['object']} brings {reference['his']} sword up just in time.",
f"""The {reference['object']} pushes your attack aside and grins wickedly. "What now, you {character.character['titles']['insult']}?" {reference['he']} hisses. """])
	print(random.choice(initial_script))
	time.sleep(5)
	counter = 0
	roll = random.randrange(1,101)
	agility_roll = random.randrange(1, 101)
	attacks = 1
	if agility_roll <= (20 + (ability.ability["agility"])):
		attacks = 3
	while counter < attacks:
		if roll <= (70 + (ability.ability["strength"] * 1.5) + enemy["playermod"] - enemy["agility"]):
			print(random.choice(success_script))
			time.sleep(5)
			if roll <= (10 + (weapon.weapon["finesse"] * 2)):
				print("The strike was well aimed, and scored a critical hit!")
				time.sleep(3)
				damage_mod += 1
			min_damage = int((ability.ability["strength"] / 2) * damage_mod)
			max_damage = int((ability.ability["strength"] + 3) * damage_mod)
			player_damage = random.randrange(min_damage, max_damage) + ability.ability["strike_lvl"] + weapon.weapon["sharpness"]
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
				enemy_attack(enemy)
			else:
				print(random.choice(fail_script))
				time.sleep(5)
				print(f"You miss your attack!")
				time.sleep(5)
				counter += 1
		if enemy['hp'] <= 0:
			kill(enemy)
			return False
		elif attacks == 3:
			attacks -= 1
			print(random.choice(agility_script))
			time.sleep(5)
	enemy_turn(enemy)

def parry(enemy):
	reference = enemy["reference"]
	initial_script = ["You raise your sword in a defensive position.",
"You brace yourself for your charging adversary, ready and waiting", f"You bring your sword to bare, watching the {reference['object']} closely."]
	success_script = [f"Your enemy runs forward, but at the last second you kick {reference['him']} back, knocking the breath from {reference['his']} body.",
f"{reference['he'].capitalize()} runs forward suddenly, but you are ready. {reference['his'].capitalize()} attack is caught on your sword and you twirl the blade swifty, knocking {reference['him']} off balance.",
f"As your opponent charges, you sidestep. {reference['he'].capitalize()} runs straight past you, back exposed, almost asking to be slashed.",
f"""The {reference['object']} attacks, but you spin away from the blow, ending your twirl on your opponent's flank.""",
f"Your adversary closes in, but at the last second you lunge forwards, slamming your shoulder into {reference['him']}. {reference['he'].capitalize()} stumbles backwards, sputtering for breath."]
	fail_script = ["You raise your sword against the expected attack, but it comes quicker than you thought. You feel a cut upon your face.",
"Your opponent rushes forwards. You try and duck to the side as the last second, but are too slow. Pain racks your body and you jump away, cursing.",
"You deflect the first attack, but the second comes in quicker than you can react. You manage to avoid the worst of the blow, but still, it hurts."]
	print(random.choice(initial_script))
	enemy["modifier"] -= (10 + ability.ability["agility"] + ability.ability["parry_lvl"])
	enemy_roll = random.randrange(1,101)
	time.sleep(5)
	if enemy_roll <= (enemy["skill"] + enemy["modifier"]):
		print(random.choice(fail_script))
		enemy_damage = random.randrange(enemy["mindamage"], enemy["maxdamage"])
		ability.ability["health"] -= enemy_damage
		time.sleep(5)
		print(f"You are hit for {enemy_damage} damage!")
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
f"""You feint sideways, then come back to your previous position. The {reference['object']} staggers slightly at the sudden move.""",
f"As your enemy moves closer, you swiftly kick {reference['him']} painfully in the shin.",
f"Your opponent brings down {reference['his']} blade. You raised your own at the last second, and with your free hand punch {reference['him']} in the face, sending {reference['him']} staggering away."]
	print(random.choice(initial_script))
	time.sleep(5)
	enemy["playermod"] += (10 + ability.ability["agility"] + ability.ability["distract_lvl"] * 2)
	attack_chance = random.randrange(1,101)
	if attack_chance <= (50 + ability.ability['agility']):
		print("Your enemy's loss of focus allows you to make an attack!")
		strike(enemy)
	else:
		enemy_turn(enemy)


def use_item(enemy):
	reference = enemy["reference"]
	potion_script = [f"You jump away from the melee and pull a potion from your belt. You drain the liquid in a few seconds, and toss the empty bottle away. You feel strength lost return to you.",
f"You kick your opponent, sending {reference['him']} backwards. While {reference['he']} staggers, you drink a potion, and pain leaves your body."]
	knife_script = [f"Your foe lunges forwards. At the last moment you jump away, sliding across the ground. You twist and hurl a throwing knife with all your strength. The projectile finds its mark.",
f"As your opponent charges towards you, you pull out a throwing knife, throwing it at {reference['him']}. Your aim is true and {reference['he']} stumbles, a bloodstain on {reference['his']} leg."]
	oil_script = [f"You produce a vial of blade oil and quickly splash it on your sword. It will not last long, but it will make your enemy feel pain.",
f"The {reference['object']} stops as you pull a vial of liquid from your belt. You pour it onto your blade, and attack."]
	smoke_bomb_script = ["Closing your eyes and mouth, you throw down a smoke bomb. Thick, grey smoke covers the battle area, making seeing impossible.",
"You light the fuse of a smoke bomb and hurl it at your enemy. There's a bang and suddenly everything is covered by grey smoke. You use the distraction to make your escape."]
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
		else:
			print(random.choice(potion_script))
			healing = random.randrange(4,9)
			ability.ability["health"] += healing
			time.sleep(5)
			print(f"You regained {healing} health!")
			time.sleep(5)
			enemy_turn(enemy)
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
			if enemy['hp'] <= 0:
				kill(enemy)
				return False
			else:
				enemy_turn(enemy)
	if item_use == "3":
		equipment.equipment["oils"] -= 1
		if equipment.equipment["oils"] <0:
			print("You have no more oils!")
			equipment.equipment["oils"] = 0
			time.sleep(2)
			use_item(enemy)
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
		else:
			print(random.choice(smoke_bomb_script))
			time.sleep(5)
			flee(enemy, smoke=True)
	else:
		turn(enemy)


def flee(enemy, smoke = False):
	reference = enemy["reference"]
	flee_script = ["You backpedal swiftly, before turning and breaking into a full run."]
	success_script = ["You stumble away from the combat, your enemy's jeers at your back."]
	fail_script = [f"You try to run, but your opponent won't let you escape that easily. {reference['he'].capitalize()} gives chase and catches you, once again engaging you in combat."]
	print(random.choice(flee_script))
	time.sleep(5)
	if smoke == False:
		escape_chance = random.randrange(1,101)
		if escape_chance <= (75 + (ability.ability["agility"] * 2)):
			print(random.choice(success_script))
			return False
		else:
			print(random.choice(fail_script))
			enemy["modifier"] = 10
			enemy_attack(enemy)
	else:
		print(random.choice(success_script))
		return False



def enemy_turn(enemy):
	reference = enemy["reference"]
	enemy["playermod"] = 0
	if enemy['hp'] <= 0:
		kill(enemy)
		return False
	elif enemy["type"] == "human":
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


def enemy_attack(enemy,damage_modi = 1):
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
		turn(enemy)
	else:
		print(random.choice(fail_script))
		time.sleep(5)
		print(f"Your enemy misses!")
		time.sleep(3)
		turn(enemy)


def enemy_parry(enemy):
	reference = enemy["reference"]
	initial_script = [
f"The {reference['object']} braces {reference['him']}self, and glares at you, daring you to fight.",
f"The other combatant raises {reference['his']} weapon, covering {reference['him']}self.",
f"Your opponent assumes a defensive stance, flattening {reference['his']} feet and barely moving."]
	if enemy["type"] == "human":
		initial_script.append(f"""Your opponent smiles at you wickedly. "Come on, {character.character["titles"]["whore"]}!" {reference['he']} yells.""")
	print(random.choice(initial_script))
	enemy["playermod"] -= (10 - enemy["agility"])
	enemy["parry"] = True
	time.sleep(5)
	turn(enemy)


def enemy_distract(enemy):
	reference = enemy["reference"]
	initial_script = [f"You close in, sword leading the way. But at the last second, {reference['he']} jumps away, leaving you staggering past.",
"Your adversary lunges unexpectedly, and you only recognize the feint when it's too late and have already lept to the side, leaving yourself off balance.",
f"Suddenly, the {reference['object']} jumps forward, shoving your chest with one hand. You stagger, the breath knocked from your body."]
	print(random.choice(initial_script))
	enemy["modifier"] += (10 + enemy["agility"])
	enemy["distract"] = True
	time.sleep(5)
	turn(enemy)


def kill(enemy):
	reference = enemy['reference']
	human_death = [
f"As your sword bites deeply into your enemy, {reference['he']} moans in pain, then crumples to the ground, dark blood flowing onto the ground.",
f"The {reference['object']} stares at you for a moment. Then a trickle of blood comes from the corner of {reference['his']} mouth, and {reference['he']} falls, dead.",
f"You pull your sword from your adversary's chest, and {reference['he']} topples over backwards instantly, dead before {reference['he']} hits the ground.",
f"You bury your sword up to the hilt into the {reference['object']}, the blade protruding from {reference['his']} back. You kick {reference['him']} from your sword, and the body falls, blood pooling.",
f"For a moment, {reference['he']} stays standing. But then {reference['he']} crashes down to the ground, a scarlet blossom growing around {reference['his']} body.",
f"The {reference['object']} falls to {reference['his']} knees, head leaning forward. You don't hesitate, bring your sword down like an executioners axe, taking the head from {reference['his']} shoulders.",
f"You cut the {reference['object']}'s hand, and {reference['he']} drops {reference['his']} weapon. {reference['he'].capitalize()} tries to punch you, but you duck under the blow and cut {reference['him']} across the back. {reference['he'].capitalize()} falls without a cry."]
	monster_death = [f"The {reference['object']} growls one last time, then falls to the ground.",
f"With a sickening squelch, you tear your sword from the monster, and it topples like an upset statue."]
	if enemy["type"] == "human":
		print(random.choice(human_death))
		time.sleep(5)
	else:
		print(random.choice(monster_death))
		time.sleep(5)
	post_combat.end_combat(enemy)
