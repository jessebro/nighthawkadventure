from functions import enemy_round
import random

xp_handouts = {
	"practice": enemy_round.generate_enemy(*[0, 0, 0, 0, 0, 10, " ", " ", " "]),
	"small": enemy_round.generate_enemy(*[0, 0, 0, 0, 0, random.randrange(15,26), " ", " ", " "]),
	"medium": enemy_round.generate_enemy(*[0, 0, 0, 0, 0, random.randrange(40,51), " ", " ", " "]),
	"large": enemy_round.generate_enemy(*[0, 0, 0, 0, 0, random.randrange(75,100), " ", " ", " "])
}

# maxhp, mindamage, maxdamage, baseskill, agility, xp, type, gender, name

def monster_access(key):
	monsters = {
		"mbandit": enemy_round.generate_enemy(*[15, 2, 6, 50, 5, random.randrange(8, 16), "human", "male", " male bandit"]),
		"fbandit": enemy_round.generate_enemy(*[12, 2, 6, 50, 8, random.randrange(8, 16), "human", "female", "female bandit"]),
		"chaos_daughter": enemy_round.generate_enemy(*[20, 3, 8, 65, 15, random.randrange(18, 29), "human", "female", "daughter of chaos"]),
		"ghoul": enemy_round.generate_enemy(*[9, 3, 5, 45, 10, random.randrange(5, 11), "monster", "it", "ghoul"]),
		"bone_hag": enemy_round.generate_enemy(*[18, 4, 7, 35, 0, random.randrange(15, 24), "monster", "it", "bone hag"])
	}
	return monsters[key]
