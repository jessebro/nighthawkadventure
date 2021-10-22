from functions.loading import save
from functions import character


def part_one():
	save('chapter3_main.part_one')
	file = __import__(character.get_crossroads("1"))
	run = getattr(file, "part_one")
	run()
