import character
import ability
import combat
import equipment
import random
import inventory

monsters = {
	"mbandit": combat.generate_enemy(*[15, 2, 6, 50, 5, random.randrange(8, 16), "human", "male", "bandit"]),
	"fbandit": combat.generate_enemy(*[12, 2, 6, 50, 10, random.randrange(8, 16), "human", "female", "bandit"]),
	"ghoul": combat.generate_enemy(*[9, 3, 5, 45, 8, random.randrange(5, 11), "monster", "it", "ghoul"])# maxhp, mindamage, maxdamage, baseskill, agility, type, gender, name
}

character.get_name()
character.get_gender()
character.get_title()
ability.get_ability()
equipment.get_equipment()
combat.intro(monsters["fbandit"])
