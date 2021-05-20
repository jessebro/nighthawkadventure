from functions import loading
import os

# System call - apparently needed for color, see
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
os.system('')


def boot():
	start = input("""Do you want to start a new game, or load your previous save?
1. New Game
2. Load Game
> """)
	if start != "1":
		return loading.load()
	return True


def print_stuff(scripts):
	for script in scripts:
		print(script)
		input("""
~~""")


def input_stuff(prompt, options):
	while True:
		choice = input(prompt)
		if choice in options:
			return choice


# Usage: print_it('Hello', 'RED')
def print_it(msg, color='RESET'):
	color = color.upper()
	if color not in style:
		color = 'RESET'
	print(style[color] + msg + style['RESET'])


style = {
	'BLACK': '\033[30m',
	'RED': '\033[31m',
	'GREEN': '\033[32m',
	'YELLOW': '\033[33m',
	'BLUE': '\033[34m',
	'MAGENTA': '\033[35m',
	'CYAN': '\033[36m',
	'WHITE': '\033[37m',
	'UNDERLINE': '\033[4m',
	'RESET': '\033[0m',
}
