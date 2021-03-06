from functions import ability
from functions import character
from functions import equipment
from functions import weapon
import random
from functions import settings
from functions.utils import input_stuff
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import clear
from functions.utils import int_to_roman

def show():
	clear()
	menu = input_stuff(f"""
~ {character.character["fullname"]} ~
~ Level {ability.ability["level"]} ~ [{ability.ability['xp']}/100] xp
{character.character["gender"].capitalize()}

Health: {ability.ability["health"]}/{ability.ability["maxhealth"]}
Armour: {ability.ability["armour"]}
Gold: {equipment.equipment["gold"]}
1. Character Stats
2. Weapon
3. Items
4. Perks
5. Settings
6. Exit
> """, ["1", "2", "3", "4", "5", "6"])

	if menu == "1":
		clear()
		leave1 = input_stuff(f"""
Your stats are:

{colour_it('Strength', Color.STRENGTH)} {ability.ability["strength"]}
{colour_it('Agility', Color.AGILITY)} {ability.ability["agility"]}
{colour_it('Awareness', Color.AWARENESS)} {ability.ability["awareness"]}
{colour_it('Endurance', Color.ENDURANCE)} {ability.ability["endurance"]}
{colour_it('Persona', Color.PERSONA)} {ability.ability["persona"]}

Enter 'b' to go back
> """, ["b"])
		if leave1 == "b":
			show()
	elif menu == "2":
		weapon_stats()
	elif menu == "3":
		item_list()
	elif menu == "4":
		perk_list()
	elif menu == "5":
		settings.get_settings()
		show()
	elif menu == "6":
		return False


def weapon_stats():
	clear()
	menu = input_stuff(f""" 
~ {weapon.weapon["weaponname"]} ~
	
{weapon.weapon["weaponname"]}'s stats are:

Sharpness {weapon.weapon["sharpness"]}
Finesse {weapon.weapon["finesse"]}
Stability {weapon.weapon["stability"]} / {weapon.weapon["max stability"]}
	
Enter 'n' to rename your weapon
Enter 'b' to go back
> """, ["n", "b"])
	if menu == "n":
		weapon.weapon["weaponname"] = input(f"""What do you want to call your weapon? (Previous name "{weapon.weapon["weaponname"]})
> """)
		weapon_stats()
	if menu == "b":
		show()

def item_list():
	clear()
	while True:
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

		menu = input_stuff(f"""
You have:

{equipment.equipment["potions"]} {plurals["potions"]}
{equipment.equipment["knives"]} {plurals["knives"]}
{equipment.equipment["oils"]} {plurals["oils"]}
{equipment.equipment["smoke bombs"]} {plurals["smoke bombs"]}
		
Enter 'h' to consume a healing potion.
Enter 'b' to go back
> """, ["b", "h"])
		if menu == "h":
			if equipment.equipment["potions"] <= 0:
				print("You have no more potions!")
			else:
				equipment.equipment["potions"] -= 1
				ability.heal(random.randrange(4,9))
				print()
		elif menu == "b":
			break
	show()


def perk_list():
	clear()
	keys = ability.perks.keys()
	display = ""
	for key in keys:
		if ability.perks[key]['level'] >= 1:
			display += f"""{key.title()} {int_to_roman(ability.perks[key]['level'])}: {ability.perks[key]['description']} [{ability.perks[key]['effect']}%]
"""
	display += """
Enter 'b' to go back
> """
	input_stuff(display, ['b'])
	show()
