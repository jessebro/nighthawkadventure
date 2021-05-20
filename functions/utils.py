from enum import Enum
import os

# System call - apparently needed for color, see
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
os.system('')


def input_stuff(prompt, options):
	while True:
		choice = input(prompt)
		if choice in options:
			return choice


class Color(Enum):
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	UNDERLINE = '\033[4m'
	RESET = '\033[0m'


# Usage: print_it('Hello', Color.RED)
def colour_it(msg, color=Color.RESET):
	if not isinstance(color, Color):
		color = Color.RESET
	return color.value + msg + Color.RESET.value


def print_it(msg, color):
	print(colour_it(msg, color))


def print_stuff(scripts):
	for script in scripts:
		print(script)
		input(f"""
{colour_it("~~", Color.YELLOW)}""")
