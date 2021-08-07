import pickle
from functions import ability
from functions import equipment
from functions import character
from functions import weapon
from functions import enemy_round
from functions.utils import print_it
from functions.utils import Color
from functions.utils import colour_it

defaults = {
	"gang_size": 0,
	"gang_lads": [],
	"gang_index": 0,
	"combat": True,
	"assistance": False,
	"goad": "",
	"damage_dealt": 0,
	"damage_received": 0,
	"health_restored": 0,
	"enemy_status": "Untouched",
	"turns_taken": 1,
	"total_damage_dealt": 0,
	"total_damage_received": 0,
	"accuracy": 0,
	"damage_prhit": 0,
	"hits": 0,
	"attacks": 0,
	"damages": []
}


def boot():
	start = input(f"""{colour_it("~ THE NIGHTHAWK ~", Color.RED)}
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
	enemy_round.game_state = defaults
	return data["position"]
