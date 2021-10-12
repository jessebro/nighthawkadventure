from functions import character
from functions.loading import save


def part_one():
	save('chapter3_main.part_one')
	function = character.get_crossroads("1")
	module = __import__(function)
	run = getattr(module, "part_one")
	run()

