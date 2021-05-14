import ability
import character
import equipment
import weapon


def show():
	menu = input(f"""

		~ {character.character["fullname"]} ~
		~ Level {ability.ability["level"]} ~ [{ability.ability['xp']}/100] xp
		{character.character["gender"].capitalize()}

		Health: {ability.ability["health"]}/{ability.ability["maxhealth"]}
		Gold: {equipment.equipment["gold"]}
		1. Character Stats
		2. Weapon
		3. Items
		4. Combat notes
		5. Exit
> """)

	if menu == "1":
		leave1 = input(f"""
Your stats are:
		Strength {ability.ability["strength"]}
		Agility {ability.ability["agility"]}
		Awareness {ability.ability["awareness"]}
		Endurance {ability.ability["endurance"]}
		Persona {ability.ability["persona"]}

	Enter 'b' to go back
> """)
		if leave1 == "b":
			show()

	elif menu == "2":
		weapon_stats()

	elif menu == "3":
		item_list()

	elif menu == "4":
		combat_tutorial()

	elif menu == "5":
		return False


def weapon_stats():
	menu = input(f""" ~ {weapon.weapon["weaponname"]} ~
	
{weapon.weapon["weaponname"]}'s stats are:
		Sharpness {weapon.weapon["sharpness"]}
		Finesse {weapon.weapon["finesse"]}
		Stability {weapon.weapon["stability"]} / {weapon.weapon["max stability"]}
	
	Enter 'n' to rename your weapon
	Enter 'b' to go back
> """)
	if menu == "n":
		weapon.weapon["weaponname"] = input(f"""What do you want to call your weapon? (Previous name "{weapon.weapon["weaponname"]})
> """)
		weapon_stats()
	if menu == "b":
		show()

def item_list():
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

	menu = input(f"""You have:
		{equipment.equipment["potions"]} {plurals["potions"]}
		{equipment.equipment["knives"]} {plurals["knives"]}
		{equipment.equipment["oils"]} {plurals["oils"]}
		{equipment.equipment["smoke bombs"]} {plurals["smoke bombs"]}
	
	Enter 'b' to go back
> """)
	if menu == "b":
		show()


def combat_tutorial():
	leave = input("""~ Combat notes ~
	
ACTIONS
Strike: Strike will cause you to attack your enemy. Accuracy and damage is effected by the Strength skill, and the enemy's agility.
You have a chance to make a second attack based on your agility.

Parry: You cause the enemy to attack you, but with a penalty to their accuracy. If they miss the attack, you strike with increased damage.

Distract: You have a chance to make an attack with significantly increased accuracy. If the distract fails, it does nothing.

Use item: You expend one of your items. Potions restore some health, knives deal guaranteed damage, oils cause you to make an attack 
with increased damage, and smoke bombs cause you to instantly flee.

Flee: You try to escape combat, the chance of success based on your agility. Fleeing combat is only an option for non-story encounters.

WEAPON STATS
Sharpness: A flat bonus to damage. Each level of sharpness increases damage by 1.

Finesse: Increases the chance to land a critical hit. Each level of finesse increases the chance by 2%.

Stability: Each time you land a hit, there is a 50% chance your weapon will lose a level of stability. If stability reaches 0, 
the weapon loses a level of sharpness and stability is reset. A weapon cannot have sharpness less than 1, however.

DEATH
You do not die outright when you reach 0 hp. Instead, you can either use a potion to heal yourself, but for half of its normal effects,
or you can make an attempt to flee. If the attempt to flee fails, you die. Sometimes, the scenario will prevent you from dying, but 
will have different negative consequences. If you have no potions and cannot flee, then you will die instantly.

Enter 'b' to go back.
> """)
	if leave == "b":
		show()
