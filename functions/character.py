character = {
	"firstname": "",
	"lastname": "",
	"fullname": "",
	"gender": "",
	"titles": {
			"he": "",
			"his": "",
			"him": "",
			"casual": "",
			"formal": "",
			"insult": "",
			"whore": "",
			"contempt": ""
	}
}

story = {
	"hag_lair": False,
	"eladris": True

}

def get_name():
	firstname = input("""What is your name?
> """)
	firstname = firstname.title()
	surname = input("""What is your surname?
> """)
	surname = surname.title()
	namechoice = input(f"""Are you sure you want your name to be "{firstname} {surname}"? y/n
> """)
	if namechoice != "y":
		get_name()

	else:
		character["firstname"] = firstname
		character["lastname"] = surname
		character["fullname"] = f"{firstname} {surname}"


def get_gender():
	genderlist = ["male", "female"]
	gender = input(f"""What is your gender? ({" / ".join(genderlist)})
> """)
	gender = gender.lower()
	if gender == "m":
		gender = "male"
	if gender == "f":
		gender = "female"
	while gender not in genderlist:
		print(f""" The gender {gender} does not exist, or you entered a typo. Try again.""")
		gender = input(f"""What is your gender? ({" / ".join(genderlist)}.)
> """)
		if gender == "m":
			gender = "male"
		if gender == "f":
			gender = "female"
	genderchoice = input(f"""Are you sure you want to be {gender}? y/n
> """)
	if genderchoice != "y":
		get_gender()
	character["gender"] = gender


def get_title():
	global character
	if character["gender"] == "male":
		character["titles"] = {
			"he": "he",
			"his": "his",
			"him": "him",
			"casual": "mister",
			"formal": "sir",
			"insult": "bastard",
			"whore": "whoreson",
			"contempt": "boy"
		}

	elif character["gender"] == "female":
		character["titles"] = {
			"he": "she",
			"his": "her",
			"him": "her",
			"casual": "miss",
			"formal": "m'lady",
			"insult": "bitch",
			"whore": "you whore",
			"contempt": "girlie"
		}
