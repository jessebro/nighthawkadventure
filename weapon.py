import random

weapon = {
	"sharpness": 1,
	"finesse": 0,
	"stability": 5,
	"max stability": 5,
	"weaponname": "your weapon"
}

def lose_stability():
	breakchance = random.randrange(1,3)
	if breakchance == 2:
		weapon["stability"] -= 1
		if weapon["stability"] == 0:
			weapon["sharpness"] -= 1
			weapon["stability"] = weapon["max stability"]
			if weapon["sharpness"] < 1:
				weapon["sharpness"] = 1
			else:
				print(f"{weapon['weaponname'].capitalize()} lost a level of sharpness!")
