from functions.utils import input_stuff

START_GOLD = 20

equipment = {
	"potions": 1,
	"knives": 2,
	"oils": 0,
	"smoke bombs": 1,
	"gold": START_GOLD,
	"empowering": False,
	"serrated": False,
	"fatal": False,
	"disorientating": False
}

def get_equipment():
	equipment_options = [" Potion", " Knife", "n Oil", " Smoke Bomb"]
	equipment_choice = int(input_stuff(f"""Finally, you'll get a look at your starting equipment. You have:
	1 Longsword (Sharpness 1, Finesse 0, Stability 5)
	{START_GOLD} gold
	1 Potion
	2 Knives
	1 Smoke Bomb

Your choice of a consumable item.
	1. Potion (heals 4-8 health)
	2. Knife (deals a guaranteed 2-5 damage)
	3. Oil (your next attack deals 200% damage)
	4. Smoke Bombs (your next attack makes an extra attack)

Type the number of the item you want
> """, ['1', '2', '3', '4']))

	equipment_confirm = input(f"""Are you sure you want a{equipment_options[equipment_choice - 1]}? y/n
> """)

	if equipment_confirm != "y":
		get_equipment()

	elif equipment_choice == 1:
		equipment["potions"] += 1

	elif equipment_choice == 2:
		equipment["knives"] += 1

	elif equipment_choice == 3:
		equipment["oils"] += 1

	elif equipment_choice == 4:
		equipment["smoke bombs"] += 1
