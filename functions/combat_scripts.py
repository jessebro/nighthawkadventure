import random
reference = {}

turn_start = [f"""You circle each other, sizing each other up.""",
f"""You ready your weapon and glare at your opponent.""",
f"""You feel your heart pounding, feel your chest rising with smooth, even breaths.""",
f"""{reference['object'].capitalize()} lunges. You jump aside at the last second."""]

player_attack = ["You lunge forward suddenly, sword leading the way.",
"You swiftly close the distance between you and your adversary, weapon raised high.",
f"""You rush towards {reference["object"]}, sword grasped firmly.""",
f"You approach {reference['object']}, attacking when you are only a few paces away.",
f"Your opponent jumps towards you. You parry the blow easily, spin your sword, and riposte swiftly.",
f"You charge forwards, spin on one foot, and bring your sword crashing down on {reference['object']}.",
"Your opponent moves to attack, but stumbles on some irregular terrain. You seize your chance and lunge forwards."]

player_hit = [f"You feel the tip of your sword bury in your enemy's flesh, accompanied by a {reference['pain']} of pain.",
"Your opponent tries to duck away from the blow, but you feel a bit of resistance, and see a spurt of blood.",
f"""You're too fast for your opponent. {reference['he'].capitalize()} raises {reference['his']} defenses weakly, but you easily bat away the blockage and cut into {reference["him"]} with your sword deeply.""",
f"""You twirl your sword in a silver spiral, feeling with satisfaction as the sword bites deeply into {reference["object"]}.""",
f"{reference['object'].capitalize()} readies {reference['him']}self for your attack. At the last second you duck and roll behind {reference['him']}, under {reference['his']} guard and slash {reference['him']} across the back.",
f"You enemy tries to step backwards, but {reference['his']} heel hits a raised section of ground. {reference['he'].capitalize()} staggers, and you slash {reference['him']} easily.",
f"With a deft sword movement you explode into action, striking with your whirling sword, spilling the blood of {reference['object']}."]

player_miss = ["Your sword slices through the air, but meets nothing as your adversary sidesteps",
"You swing your sword in a cruel lateral strike, but your opponent ducks just in time, the wind chasing the blade making a whistling sound."
,f"""You swing your sword downwards, grunting with the effort. {reference["object"].capitalize()} jumps back at the last second, the tip of your sword barely a inch from {reference["his"]} body."""]

player_extra_attack = ["You're quick enough to strike a second time.",
"You bring your blade back quickly for a second attempt.",
"You spin with the momentum of the sword, whirling and attacking again swiftly."]

player_hit_parry = [f"You swing your sword, but {reference['object']} is ready, dodging sideways at the last second.",
f"As you charge forwards, {reference['object']} slams into you, pushing you back, staggering."]

player_parry = []

player_success_parry = []

player_distract = []

player_potion = []

player_knife = []

player_oil = []

player_smoke = []

enemy_attack = []

enemy_hit = []

enemy_miss = []

enemy_attack_ally = []

enemy_hit_ally = []

enemy_miss_ally = []

enemy_parry = []

enemy_distract = []

enemy_death = []

ally_attack = []

ally_hit = []

ally_miss = []

ally_assist = []

ally_distract = []

ally_down = []


def print_script(scripts, references):
	global reference
	reference = references
	return random.choice(scripts)
