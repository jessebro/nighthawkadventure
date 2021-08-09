import pickle
import os
from functions import ability
from functions import equipment
from functions import character
from functions import weapon
from functions.utils import print_it
from functions.utils import Color
from functions.utils import colour_it



def boot():
	start = input(f"""{colour_it("~ THE NIGHTHAWK ~", Color.RED)}
1. New Game
2. Load Game
3. Exit
> """)
	if start == "3":
		exit()
	elif start != "1":
		return load()
	return True


def save(position):
	print_it("Your game has been saved!", Color.FUNCTION)
	data = {
		"character": character.character,
		"ability": ability.ability,
		"equipment": equipment.equipment,
		"weapon": weapon.weapon,
		"story": character.story,
		"position": position
	}
	with open(f'savefiles/{character.character["fullname"]}.dat', 'wb') as f:
		pickle.dump(data, f, protocol=2)


def load():
	profiles = os.listdir("savefiles")
	counter = 0
	choices = []
	for profile in profiles:
		counter += 1
		choices.append(counter)
		print(f"{counter}. {profile.strip('.dat')}")
	while True:
		loaded = int(input("> "))
		if loaded not in choices:
			continue
		break
	loaded = profiles[loaded - 1]

	with open(f'savefiles/{loaded}', 'rb') as f:
		data = pickle.load(f)
	character.character = data['character']
	character.story = data['story']
	ability.ability = data['ability']
	equipment.equipment = data['equipment']
	weapon.weapon = data['weapon']
	return data["position"]
