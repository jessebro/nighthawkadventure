from functions import enemy_round
from functions import ability
import random


xp_handouts = {
	"practice": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 10, " ", " ", " "]),
	"small": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 25, " ", " ", " "]),
	"medium": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 50, " ", " ", " "]),
	"large": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 85, " ", " ", " "]),
	"level": enemy_round.generate_actor(*[0, 0, 0, 0, 0, 100, " ", " ", " "]),

}

# maxhp, mindamage, maxdamage, baseskill, agility, xp, type, gender, name


def monster_access(key):
	monsters = {
		"freebee": enemy_round.generate_actor(*[1, 0, 0, 0, -1000, 100, "monster", "it", "the freebee"]),
		"mbandit": enemy_round.generate_actor(*[20, 2, 6, 50, 5, random.randrange(8, 16), "human", "male", "the male bandit"]),
		"fbandit": enemy_round.generate_actor(*[15, 2, 6, 50, 8, random.randrange(8, 16), "human", "female", "the female bandit"]),
		"cbandit": enemy_round.generate_actor(*[40, 4, 8, 65, 10, random.randrange(18, 26), "human", random.choice(['male', 'female']), "the bandit captain"]),
		"chaos_daughter": enemy_round.generate_actor(*[29, 3, 8, 65, 10, random.randrange(18, 29), "human", "female", "the Daughter of Chaos"]),
		"ghoul": enemy_round.generate_actor(*[9, 3, 5, 45, 10, random.randrange(5, 11), "monster", "it", "the ghoul"]),
		"bone_hag": enemy_round.generate_actor(*[30, 4, 7, 45, 0, random.randrange(15, 24), "monster", "it", "the bone hag"]),
		"lalikin": enemy_round.generate_actor(*[23, 3, 6, 55, 5, random.randrange(12, 21), "monster", "it", "the lalikin"]),
		"crag": enemy_round.generate_actor(*[63, 6, 15, 25, -15, random.randrange(20, 33), "monster", "it", "the crag"]),
		"moracka": enemy_round.generate_actor(*[36, 4, 8, 50, 13, random.randrange(20, 30), "monster", "it", "the moracka"]),
		"ogre": enemy_round.generate_actor(*[53, 5, 12, 20, -10, random.randrange(19, 27), "monster", "it", "the ogre"]),
		"injured ogre": enemy_round.generate_actor(*[23, 5, 12, 20, -10, random.randrange(19, 27), "monster", "it", "the ogre"]),
		"wolf": enemy_round.generate_actor(*[13, 3, 8, 65, 10, random.randrange(4, 10), "monster", "it", "the wolf"]),
		"dinosaur": enemy_round.generate_actor(*[100, 8, 16, 45, -20, 100, "monster", "it", "the jungle creature"]),
	}
	return monsters[key]


def special_access(key):
	character = {
		"garurt": enemy_round.generate_actor(*[25, 4, 9, 65, 8, 35, "human", "male", "Garurt"]),
	}
	return character[key]


def ally_access(key):
	allies = {
		"homeboy": enemy_round.generate_actor(*[15 * ability.ability['level'], 7, 15, 70, 10, 1, "human", "male", "your homeboy"]),
		"tamara": enemy_round.generate_actor(*[15 + (ability.ability['level'] * 2), 7, 15, 70, 10, 1, "human", "female", "Tamara"]),
	}
	return allies[key]
