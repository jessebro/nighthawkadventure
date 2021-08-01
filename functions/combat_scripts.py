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

player_parry = ["You raise your sword in a defensive position.",
"You brace yourself for your charging adversary, ready and waiting", f"You bring your sword to bare, watching {reference['object']} closely."]

player_success_parry = [f"Your enemy runs forward, but at the last second you kick {reference['him']} back, knocking the breath from {reference['his']} body.",
f"{reference['he'].capitalize()} runs forward suddenly, but you are ready. {reference['his'].capitalize()} attack is caught on your sword and you twirl the blade swifty, knocking {reference['him']} off balance.",
f"As your opponent charges, you sidestep. {reference['he'].capitalize()} runs straight past you, back exposed, almost asking to be slashed.",
f"""{reference['object'].capitalize()} attacks, but you spin away from the blow, ending your twirl on your opponent's flank.""",
f"Your adversary closes in, but at the last second you lunge forwards, slamming your shoulder into {reference['him']}. {reference['he'].capitalize()} stumbles backwards, sputtering for breath."]

player_fail_parry = ["You raise your sword against the expected attack, but it comes quicker than you thought. You feel a cut upon your face.",
"Your opponent rushes forwards. You try and duck to the side at the last second, but are too slow. Pain racks your body and you jump away, cursing.",
"You deflect the first attack, but the second comes in quicker than you can react. You manage to avoid the worst of the blow, but still, it hurts."]

player_distract = ["Suddenly, you lean down, scoop up a handful of dirt and throw it in your enemy's face.",
f"You yell fiercely into the face of your opponent. {reference['he'].capitalize()} recoils at the sudden noise.",
f"""You feint sideways, then come back to your previous position. {reference['object'].capitalize()} staggers slightly at the sudden move.""",
f"As your enemy moves closer, you swiftly kick {reference['him']} painfully in the shin.",
f"Your opponent brings down {reference['his']} attack. You raised your blade at the last second, and with your free hand punch {reference['him']} in the face, sending {reference['him']} staggering away."]

player_potion = [f"You jump away from the melee and pull a potion from your belt. You drain the liquid in a few seconds, and toss the empty bottle away. You feel strength lost return to you.",
f"You kick your opponent, sending {reference['him']} backwards. While {reference['he']} staggers, you drink a potion, and pain leaves your body."]

player_knife = [f"Your foe lunges forwards. At the last moment you jump away, sliding across the ground. You twist and hurl a throwing knife with all your strength. The projectile finds its mark.",
f"As your opponent charges towards you, you pull out a throwing knife, throwing it at {reference['him']}. Your aim is true and {reference['he']} stumbles, a bloodstain on {reference['his']} leg."]

player_oil = [f"You produce a vial of blade oil and quickly splash it on your sword. It will not last long, but it will make your enemy feel pain.",
f"{reference['object'].capitalize()} stops as you pull a vial of liquid from your belt. You pour it onto your blade, and attack."]

player_smoke = ["Closing your eyes and mouth, you throw down a smoke bomb. Thick, grey smoke covers the battle area, making sight impossible.",
"You light the fuse of a smoke bomb and hurl it at your enemy. There's a bang and suddenly everything is covered by grey smoke."]

enemy_strike = [f"{reference['object'].capitalize()} lunges in, ready to strike.",
"You ready yourself as your adversary charges forward, teeth bared in savage fury.",
f"{reference['object'].capitalize()} charges, {reference['his']} eyes gleaming."]

enemy_hit = [f"You are too slow to react. {reference['object'].capitalize()} strikes you a blow. You hit the ground hard but roll to your feet, panting for breath.",
f"{reference['he'].capitalize()} takes a swing at you, and the attack finds its mark. You feel blood on your skin, and jump away before further harm.",
f"Your opponent lunges forwards. Before you can avoid the attack, you are dealt a glancing blow.",
f"You are beaten down by a hail of strikes, blocking one after the other. Finally, one makes its way through your defenses and you feel a sharp pain."]

enemy_miss = [f"Though your opponent comes in with speed and ferocity, you avoid everything {reference['he']} tries to strike you with.",
f"A strike is aimed at your head, but you are too quick for {reference['object']}. You kick {reference['him']} and {reference['he']} staggers before {reference['he']} gets another chance to attack.",
f"{reference['he'].capitalize()} lunges forwards, missing you and stumbling past you. But {reference['he']} whirls again in another attack. You duck at the last second, the hair on your head whipping with the passing attack.",
f"As the attack passes to within a hair's breadth of your face, you twist and jump away in a diving roll, coming back to your feet, glaring at your opponent."]

enemy_attack_ally = []

enemy_hit_ally = []

enemy_miss_ally = []

enemy_block = [f"{reference['object'].capitalize()} braces {reference['him']}self, and glares at you, daring you to fight.",
f"The other combatant raises {reference['his']} defenses, covering {reference['him']}self.",
f"Your opponent assumes a defensive stance, flattening {reference['his']} feet and barely moving."]

enemy_divert = [f"You close in, sword leading the way. But at the last second, {reference['he']} jumps away, leaving you staggering past.",
"Your adversary lunges unexpectedly, and you only recognize the feint when it's too late and have already lept to the side, leaving yourself off balance.",
f"Suddenly, {reference['object']} jumps forward, shoving your chest with one hand. You stagger, the breath knocked from your body."]

human_death = [f"As your sword bites deeply into your enemy, {reference['he']} moans in pain, then crumples to the ground, dark blood flowing onto the ground.",
f"{reference['object'].capitalize()} stares at you for a moment. Then a trickle of blood comes from the corner of {reference['his']} mouth, and {reference['he']} falls, dead.",
f"You pull your sword from your adversary's chest, and {reference['he']} topples over backwards instantly, dead before {reference['he']} hits the ground.",
f"You bury your sword up to the hilt into {reference['object']}, the blade protruding from {reference['his']} back. You kick {reference['him']} from your sword, and the body falls, blood pooling.",
f"For a moment, {reference['he']} stays standing. But then {reference['he']} crashes down to the ground, a scarlet blossom growing around {reference['his']} body.",
f"{reference['object'].capitalize()} falls to {reference['his']} knees, head leaning forward. You don't hesitate, bringing your sword down like an executioner's axe, taking the head from {reference['his']} shoulders.",
f"You cut {reference['object']}'s hand, and {reference['he']} drops {reference['his']} weapon. {reference['he'].capitalize()} tries to punch you, but you duck under the blow and cut {reference['him']} across the back. {reference['he'].capitalize()} falls without a cry.",
f"{reference['object'].capitalize()} falls onto {reference['his']} back, gasping for air. You lunge forwards and plunge your sword into {reference['his']} chest, spattering your blade with blood."]

monster_death = [f"{reference['object'].capitalize()} growls one last time, then falls to the ground.",
f"With a sickening squelch, you tear your sword from the monster, and it topples like an upset statue.",
f"You lunge forwards, pinning {reference['object']} by the throat and holding it to the ground. You draw your knife and plunge it home into the monster's snarling mouth."]

enemy_approach = [
f"{reference['object'].capitalize()} rushes forward, {reference['pain']}ing with rage at {reference['his']} companion's death.",
f"{reference['object'].capitalize()} approaches you now, more wary than your previous, now deceased opponent.",
f"You ready your sword, now stained with blood, shouting a challenge to your next opponent. {reference['he'].capitalize()} responds to the challenge and moves forwards."]

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
