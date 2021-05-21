from functions.utils import print_stuff
from functions.utils import input_stuff
from functions.utils import colour_it
from functions.utils import Color

character_entries = {

}

monster_entries = {

}


def show_characters(characters):
	for character in characters:
		print_stuff(character_entries[character])


def show_monsters(monsters):
	pass
