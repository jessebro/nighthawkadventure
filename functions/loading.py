import pickle
import os
from functions import ability
from functions import equipment
from functions import character
from functions import weapon
from functions import achievements
from functions.utils import input_stuff
from functions.utils import print_stuff
from functions.utils import clear
from functions.utils import print_it
from functions.utils import Color
from functions.utils import colour_it


def boot():
	path = "Achievements.dat"
	exists = os.path.isfile(path)
	if not exists:
		achievements.save_achievements()
	while True:
		clear()
		start = input_stuff(f"""{colour_it("~ THE NIGHTHAWK ~", Color.RED)}
1. New Game
2. Load Game
3. View achievements
4. Exit
> """, ["1", "2", "3", "4"])
		if start == "3":
			achievements.view_achievements()
		elif start == "4":
			exit()
		elif start != "1":
			if not os.path.exists("savefiles/"):
				print_stuff(["""There are no savefiles yet."""])
				continue
			returnable = False
			while not returnable:
				returnable = load()
			if returnable != True:
				return returnable
		else:
			return True


def save(position):
	if not os.path.exists("savefiles/"):
		os.mkdir("savefiles/")
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
	while True:
		clear()
		print(colour_it("~ THE NIGHTHAWK ~", Color.RED))
		profiles = os.listdir("savefiles")
		counter = 0
		choices = []
		for profile in profiles:
			counter += 1
			choices.append(counter)
			print(f"{counter}. {profile.strip('.dat')}")

		print(f"{counter + 1}. Cancel")
		choices.append(counter + 1)
		loaded = int(input("> "))
		if loaded not in choices:
			continue
		elif loaded == counter + 1:
			return True
		loaded = profiles[loaded - 1]
		clear()
		print(colour_it("~ THE NIGHTHAWK ~", Color.RED))
		action = input_stuff(f"""1. Load {loaded.strip('.dat')}.
2. Delete {loaded.strip('.dat')}
3. Cancel
> """, ["1", "2", "3"])
		if action == "2":
			confirm = input(f"""Are you sure you want to delete {loaded.strip('.dat')}? Ths action cannot be undone. y/n
> """)
			if confirm == "y":
				os.remove(f"savefiles/{loaded}")
		elif action == "3":
			continue
		else:
				break

	with open(f'savefiles/{loaded}', 'rb') as f:
		data = pickle.load(f)
	character.character = data['character']
	character.story = data['story']
	ability.ability = data['ability']
	equipment.equipment = data['equipment']
	weapon.weapon = data['weapon']
	return data["position"]
