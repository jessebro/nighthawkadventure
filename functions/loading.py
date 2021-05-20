import pickle
from functions import ability
from functions import equipment
from functions import character
from functions import weapon
from functions.utils import print_it
from functions.utils import Color


def boot():
	start = input("""Do you want to start a new game, or load your previous save?
1. New Game
2. Load Game
> """)
	if start != "1":
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
	with open('savefile.dat', 'wb') as f:
		pickle.dump(data, f, protocol=2)


def load():
	with open('savefile.dat', 'rb') as f:
		data = pickle.load(f)
	character.character = data['character']
	character.story = data['story']
	ability.ability = data['ability']
	equipment.equipment = data['equipment']
	weapon.weapon = data['weapon']
	return data["position"]
