from functions.loading import save


def part_one():
	save('chapter3_main.part_one')
	# file = character.get_crossroads("1")
	file = "ch"
	run = getattr(file, "part_one")
	run()
