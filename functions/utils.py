from functions import loading


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
~ ENTER TO CONTINUE ~""")


def input_stuff(prompt, options):
	while True:
		choice = input(prompt)
		if choice in options:
			return choice
