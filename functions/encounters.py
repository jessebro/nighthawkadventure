from functions import enemy_round
import random

xp_handouts = {
	"practice": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 10, " ", " ", " "]),
	"small": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 25, " ", " ", " "]),
	"medium": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 50, " ", " ", " "]),
	"large": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 85, " ", " ", " "])
}

# maxhp, mindamage, maxdamage, baseskill, agility, xp, type, gender, name

def monster_access(key):
	monsters = {
		"mbandit": enemy_round.generate_actor(*[15, 2, 6, 50, 5, random.randrange(8, 16), "human", "male", "the male bandit"]),
		"fbandit": enemy_round.generate_actor(*[12, 2, 6, 50, 8, random.randrange(8, 16), "human", "female", "the female bandit"]),
		"chaos_daughter": enemy_round.generate_actor(*[18, 3, 8, 65, 10, random.randrange(18, 29), "human", "female", "the daughter of chaos"]),
		"ghoul": enemy_round.generate_actor(*[9, 3, 5, 45, 10, random.randrange(5, 11), "monster", "it", "the ghoul"]),
		"bone_hag": enemy_round.generate_actor(*[22, 4, 7, 45, 0, random.randrange(15, 24), "monster", "it", "the bone hag"]),
		"lalikin": enemy_round.generate_actor(*[17, 3, 6, 55, 5, random.randrange(12, 21), "monster", "it", "the lalikin"]),
		"crag": enemy_round.generate_actor(*[30, 6, 15, 25, -5, random.randrange(20, 33), "monster", "it", "the crag"]),
		"moracka": enemy_round.generate_actor(*[25, 4, 8, 50, 13, random.randrange(20, 30), "monster", "it", "the moracka"]),
		"ogre": enemy_round.generate_actor(*[30, 5, 12, 20, -10, random.randrange(19, 27), "monster", "it", "the ogre"]),
		"injured ogre": enemy_round.generate_actor(*[23, 5, 12, 20, -10, random.randrange(19, 27), "monster", "it", "the ogre"]),
		"wolf": enemy_round.generate_actor(*[7, 3, 8, 65, 10, random.randrange(4, 10), "monster", "it", "the wolf"]),
	}
	return monsters[key]


def special_access(key):
	character = {
		"garurt": enemy_round.generate_actor(*[21, 4, 9, 65, 8, 35, "human", "male", "Garurt"]),
	}
	return character[key]


def ally_access(key):
	allies = {
		"tamara": enemy_round.generate_actor(*[20, 3, 7, 70, 10, 0, "human", "female", "Tamara"]),
	}
	return allies[key]
