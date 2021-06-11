import random
import time
from functions.utils import print_stuff
from functions.utils import input_stuff
from functions.utils import Color
from functions.utils import colour_it

MAX_ABILITY_SCORE = 27

ability = {
	"strength": 0,
	"agility": 0,
	"awareness": 0,
	"endurance": 0,
	"persona": 0,
	"maxhealth": 0,
	"health": 0,
	"armour": 0,
	"level": 1,
	"xp": 0,
	"strike_lvl": 0,
	"parry_lvl": 0,
	"distract_lvl": 0
}


def get_ability():
	ability_samples = [0, 0, 0, 0, 0]
	random_assign = [7, 6, 5, 5, 4]
	print(f"""Next, determine your statistics. There are five abilities.
	{colour_it("Strength", Color.RED)} determines your ability to fight, lift things and break things
	{colour_it("Agility", Color.GREEN)} determines your ability to run away, dodge and your chance to make an extra attack
	{colour_it("Awareness", Color.BLUE)} determines your ability to detect lies, notice things and identify things
	{colour_it("Endurance", Color.YELLOW)} determines your ability to withstand pain, hold your breath and determines your health points.
	{colour_it("Persona", Color.PURPLE)} determines your ability to persuade and interact with people to get what you want.
One by one, type in a number for each stat.
The total must not exceed 27, and no individual stat can be less than 1 or greater than 10.""")
	decide = input("""1. Select abilities manually.
2. Leave it to chance
> """)
	if decide == "1":
		ability_choice = " "
		ability_samples[0] = int(input(f"{colour_it('Strength', Color.STRENGTH)}: "))
		ability_samples[1] = int(input(f"{colour_it('Agility', Color.AGILITY)}: "))
		ability_samples[2] = int(input(f"{colour_it('Awareness', Color.AWARENESS)}: "))
		ability_samples[3] = int(input(f"{colour_it('Endurance', Color.ENDURANCE)}: "))
		ability_samples[4] = 27 - (ability_samples[0] + ability_samples[1] + ability_samples[2] + ability_samples[3])

		powercheck = True in (ele > 10 for ele in ability_samples)
		weakcheck = True in (ele < 1 for ele in ability_samples)

		if powercheck is True:
			print("One of your abilities was greater than 10. Try again.")
			time.sleep(3)
			get_ability()

		elif weakcheck is True:
			print("One of your abilities was less than 1. Try again.")
			time.sleep(3)
			get_ability()

		elif sum(ability_samples) > MAX_ABILITY_SCORE:
			print(f"The sum of your ability points was greater than {MAX_ABILITY_SCORE}. Try again.")
			time.sleep(3)
			get_ability()

		else:
			ability_choice = input(f"""Your ability scores are:
	{colour_it("Strength", Color.STRENGTH)}: {ability_samples[0]}
	{colour_it("Agility", Color.AGILITY)}: {ability_samples[1]}
	{colour_it("Awareness", Color.AWARENESS)}: {ability_samples[2]}
	{colour_it("Endurance", Color.ENDURANCE)}: {ability_samples[3]}
	{colour_it("Persona", Color.PERSONA)}: {ability_samples[4]}
			
Do you want these to be your ability scores? y/n
> """)

		if ability_choice != "y":
			get_ability()

		else:
			ability["strength"] = ability_samples[0]
			ability["agility"] = ability_samples[1]
			ability["awareness"] = ability_samples[2]
			ability["endurance"] = ability_samples[3]
			ability["persona"] = ability_samples[4]

	else:
		random.shuffle(random_assign)
		ability_choice = input(f"""Your ability scores are:
	{colour_it("Strength", Color.STRENGTH)}: {random_assign[0]}
	{colour_it("Agility", Color.AGILITY)}: {random_assign[1]}
	{colour_it("Awareness", Color.AWARENESS)}: {random_assign[2]}
	{colour_it("Endurance", Color.ENDURANCE)}: {random_assign[3]}
	{colour_it("Persona", Color.PERSONA)}: {random_assign[4]}

Do you want these to be your ability scores? y/n
> """)

		if ability_choice != "y":
			get_ability()

		else:
			ability["strength"] = random_assign[0]
			ability["agility"] = random_assign[1]
			ability["awareness"] = random_assign[2]
			ability["endurance"] = random_assign[3]
			ability["persona"] = random_assign[4]

	ability["maxhealth"] = ability["endurance"] + 15
	ability["health"] = ability["maxhealth"]


def heal(healing):
	ability["health"] += healing
	if ability["health"] >= ability["maxhealth"]:
		ability["health"] = ability["maxhealth"]


def gain_xp(enemies):
	gained_exp = 0
	for enemy in enemies:
		exp = enemy['xp']
		gained_exp += exp
	ability['xp'] += gained_exp
	print_stuff([colour_it(f'You gained {gained_exp} xp!', Color.FUNCTION)])
	levels = int(ability['xp'] / 100)
	if levels > 0:
		level_up(levels)
	return False


def level_up(levels):
	if levels == 1:
		plurals = "time"
	else:
		plurals = "times"
	print_stuff([colour_it(f"You've leveled up {int(levels)} {plurals}!", Color.FUNCTION)])
	time.sleep(3)
	ability['level'] += levels
	ability['xp'] %= 100
	counter = 0
	while counter < levels:
		print(f"""Which ability do you want to increase?
1. {colour_it("Strength", Color.STRENGTH)}
2. {colour_it("Agility", Color.AGILITY)}
3. {colour_it("Awareness", Color.AWARENESS)}
4. {colour_it("Endurance", Color.ENDURANCE)}
5. {colour_it("Persona", Color.PERSONA)}""")
		ability_boost = int(input_stuff('> ', ["1", "2", "3", "4", "5"]))
		choices = ["strength", "agility", "awareness", "endurance", "persona"]
		choice = choices[(ability_boost - 1)]
		ability[choice] += 1
		print(f"Your {choice.capitalize()} increased by 1!")
		time.sleep(3)

		print("""Which action do you want to improve?
1. Strike
2. Parry
3. Distract""")
		action_boost = int(input_stuff('> ', ["1", "2", "3"]))
		action_choices = ["strike", "parry", "distract"]
		action_choice = action_choices[(action_boost - 1)]
		ability[f"{action_choice}_lvl"] += 1
		print(f"{action_choice.capitalize()} has been upgraded!")
		time.sleep(3)

		ability["maxhealth"] = ability["endurance"] + 10
		ability["maxhealth"] += (5 * (ability["level"] - 1))
		ability["maxhealth"] = int(ability["maxhealth"])
		ability["health"] = ability["maxhealth"]
		counter += 1


def reaction(difficulty, cycles):
	cycle = 0
	while cycle < cycles:
		choice = None
		inputs = ["q", "w", "e", "r", "t", "y"]
		selection = random.choice(inputs)
		time.sleep(random.randrange(2, 6))
		if choice != None:
			return True
		while choice == None:
			countdown = time.time()
			choice = input(selection)
			print(time.time() - countdown - 0.4)
			if (time.time() - countdown - 0.4) >= difficulty:
				return False
		if choice != selection:
			return False
		else:
			cycle += 1
	return True
