from functions.loading import save


def part_one():
	save('chapter3_main.part_one')
	file = __import__("chapter3_jungle")
	run = getattr(file, "part_one")
	run()
