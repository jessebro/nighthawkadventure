import sys
from enum import Enum
import os
import time

# System call - apparently needed for color, see
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
os.system('')

default_actions = {}


def clear():
	if sys.platform.startswith("win"):
		os.system('cls')
	else:
		os.system('clear')


def input_stuff(prompt, options, actions=None):
	if not actions:
		actions = default_actions
	while True:
		choice = input(prompt)
		if choice in actions:
			actions[choice]()
		if options == "*":
			break
		elif choice in options:
			return choice
		clear()


class Color(Enum):
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[34m'
	PURPLE = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	UNDERLINE = '\033[4m'
	RESET = '\033[0m'
	BOLD = '\33[1m'

	STRENGTH = '\033[31m'
	AGILITY = '\033[93m'
	AWARENESS = '\033[34m'
	ENDURANCE = '\033[92m'
	PERSONA = '\033[35m'

	QUEST = '\033[93m'     # YELLOW
	ENEMY = '\033[31m'     # RED
	NPC = '\033[92m'       # GREEN2
	CHECK = '\033[34m'     # BLUE
	PLACE = '\033[35m'     # PURPLE
	FUNCTION = '\033[36m'  # CYAN
	LOOT = '\33[1m'        # BOLD


# Usage: print_it('Hello', Color.RED)
def colour_it(msg, color=Color.RESET):
	if not isinstance(color, Color):
		color = Color.RESET
	return color.value + msg + Color.RESET.value


def print_it(msg, color):
	print(colour_it(msg, color))


def print_stuff(scripts):
	for script in scripts:
		for letter in script:
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(0.02)
		print("")
		leave = input_stuff(f"""{colour_it("~~", Color.YELLOW)}""", "*")
		if leave == "exit":
			exit()
		clear()
