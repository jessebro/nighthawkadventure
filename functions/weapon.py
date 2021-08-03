import random

weapon = {
	"sharpness": 1,
	"finesse": 0,
	"stability": 5,
	"max stability": 5,
	"weaponname": "your weapon",
	"attacks": [{"name": "Dueler's Strike",
	             "description": " (basic attack)",
	             "enabled": True,
	             "damage": 0,
	             "accuracy": 0},
	            {"name": "Power Strike",
	             "description": " (higher damage, lower accuracy)",
	             "enabled": True,
	             "damage": 1.5,
	             "accuracy": -10},
				{"name": "Precision Strike",
	             "description": " (lower damage, higher accuracy)",
	             "enabled": False,
	             "damage": 0.75,
	             "accuracy": 10
	             },
	            {"name": "Rending Strike",
				 "description": " (lower accuracy, guaranteed two levels of bleeding)",
	             "enabled": False,
	             "damage": 1,
	             "accuracy": -10
	             },
	            {"name": "Dancing Strike",
				"description": " (lower accuracy, always makes two attacks)",
	             "enabled": False,
	             "damage": 1,
	             "accuracy": -10
	             },
	            {"name": "Vampire Strike",
				"description": " (lower damage, chance to heal damage dealt)",
				"enabled": False,
	            "damage": 0.75,
	            "accuracy": 0
	             }],
	"parries": [{"name": "Counter Parry",
	             "description": " (make an attack for 150% damage on a successful parry)",
	             "enabled": True},
				{"name": "Opportunist's Parry",
	             "description": " (take an extra turn after a succesful parry)",
	             "enabled": False},
				{"name": "Vengeance Parry",
	             "description": " (make an attack after parrying. If parry failed, the attack gains bonus damage equal to damage taken)",
	             "enabled": False}],
	"distracts": [{"name": "Dirty Distract",
	             "description": " (successfully distracting makes you perform a more accurate attack)",
	             "enabled": True},
				{"name": "Lacerating Distract",
	             "description": " (successfully distracting inflicts two levels of bleeding)",
	             "enabled": False},
				{"name": "Deadly Distract",
	             "description": " (successfully distracting increases your critical hit chance and damage)",
	             "enabled": False}]

}

def get_active():
	return [known for known in weapon["attacks"] if known['enabled']]

def get_inactive():
	return [known for known in weapon["attacks"] if not known['enabled']]


def attack_by_name(name):
	for next in weapon["attacks"]:
		if next['name'] == name:
			return next
	return name


def parry_by_name(name):
	for next in weapon["parries"]:
		if next['name'] == name:
			return next
	return name


def distract_by_name(name):
	for next in weapon["distracts"]:
		if next['name'] == name:
			return next
	return name


def get_weapon_name():
	name = input("""What do you want your weapon to be called?
> """)
	confirm = input(f"""Are you sure you want you weapon to be called {name}? y/n
> """)
	if confirm != "y":
		get_weapon_name()
		return False
	else:
		weapon["weaponname"] = name


def lose_stability():
	breakchance = random.randrange(1, 3)
	if breakchance == 2:
		weapon["stability"] -= 1
		if weapon["stability"] == 0:
			weapon["sharpness"] -= 1
			weapon["stability"] = weapon["max stability"]
			if weapon["sharpness"] < 1:
				weapon["sharpness"] = 1
			else:
				print(f"{weapon['weaponname'].capitalize()} lost a level of sharpness!")
