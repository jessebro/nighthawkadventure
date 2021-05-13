import character
import ability
import enemy_round
import equipment
import random
import post_combat

monsters = {
	"mbandit": enemy_round.generate_enemy(*[15, 2, 6, 50, 5, random.randrange(8, 16), "human", "male", "bandit"]),
	"fbandit": enemy_round.generate_enemy(*[12, 2, 6, 50, 8, random.randrange(8, 16), "human", "female", "bandit"]),
	"chaos_daughter": enemy_round.generate_enemy(*[20, 3, 8, 65, 15, random.randrange(15, 26), "human", "female", "daughter of chaos"]),
	"ghoul": enemy_round.generate_enemy(*[9, 3, 5, 45, 10, random.randrange(5, 11), "monster", "it", "ghoul"])# maxhp, mindamage, maxdamage, baseskill, agility, type, gender, name
}

gang = [monsters["fbandit"], monsters["ghoul"]]

character.get_name()
character.get_gender()
character.get_title()
ability.get_ability()
equipment.get_equipment()
enemy_round.initialize(gang)
