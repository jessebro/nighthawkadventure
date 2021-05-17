import pickle
from functions import ability
from functions import equipment
from functions import character
from functions import weapon


def save(position):
	print("Your game has been saved!")
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
