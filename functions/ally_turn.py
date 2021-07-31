def generate_ally(maxhp, mindamage, maxdamage, baseskill, baseagility, gender, name):
	ally = {}
	ally["maxhp"] = maxhp
	ally["hp"] =  ally["maxhp"]
	ally["mindamage"] = mindamage
	ally["maxdamage"] = maxdamage
	ally["baseskill"] = baseskill
	ally["skill"] = ally["baseskill"]
	ally["baseagility"] = baseagility
	ally["agility"] = ally["baseagility"]
	ally["gender"] = gender
	ally["modifier"] = 0
	ally["assist"] = False
	ally["distract"] = False
	ally["reference"] = ally_reference(gender, name)
	return ally


def ally_reference(gender, name):
	reference = {}
	reference["object"] = name
	if gender == "male":
		reference["his"] = "his"
		reference["him"] = "him"
		reference["he"] = "he"
	elif gender == "female":
		reference["his"] = "her"
		reference["him"] = "her"
		reference["he"] = "she"
	else:
		reference["his"] = "its"
		reference["him"] = "it"
		reference["he"] = "it"
	if type == "human":
		reference["pain"] = "scream"
		reference["curse"] = "curse"
	else:
		reference["pain"] = "howl"
		reference["curse"] = "growl"
	reference["insult"] = character.character["titles"]['insult']
	reference["whore"] = character.character["titles"]["whore"]
	return reference
