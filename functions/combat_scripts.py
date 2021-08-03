import random

defaults = {
	"reference": {
		"object": "",
		"him": "",
		"his": "",
		"he": "",
		"pain": "",
		"curse": "",
		"insult": "",
		"whore": ""

	}
}

def print_script(scripts, enemy, ally=defaults):
	if ally == {}:
		ally = defaults
	reference = enemy['reference']

	ally_reference = ally['reference']

	choices = {
	"turn_start" : [f"""You circle each other, sizing each other up.""",
f"""You ready your weapon and glare at your opponent.""",
f"""You feel your heart pounding, feel your chest rising with smooth, even breaths.""",
f"""{reference['object'].capitalize()} lunges. You jump aside at the last second.""",
f"""Sword at the ready, you jeer at {reference['object']}.""",
f"""You flourish your blade, and {reference['object']} flinches at the display.""",
f"""Both you and {reference['object']} ready yourselves, ducking, weaving, feinting and striking each trying to gain an advantage."""],

	"player_attack" : ["You lunge forward suddenly, sword leading the way.",
"You swiftly close the distance between you and your adversary, weapon raised high.",
f"""You rush towards {reference["object"]}, sword grasped firmly.""",
f"You approach {reference['object']}, attacking when you are only a few paces away.",
f"Your opponent jumps towards you. You parry the blow easily, spin your sword, and riposte swiftly.",
f"You charge forwards, spin on one foot, and bring your sword crashing down on {reference['object']}.",
"Your opponent moves to attack, but stumbles on some irregular terrain. You seize your chance and lunge forwards."],

	"player_hit" : [
f"You feel the tip of your sword bury in your enemy's flesh, accompanied by a {reference['pain']} of pain.",
"Your opponent tries to duck away from the blow, but you feel a bit of resistance, and see a spurt of blood.",
f"""You're too fast for your opponent. {reference['he'].capitalize()} raises {reference['his']} defenses weakly, but you easily bat away the blockage and cut into {reference["him"]} with your sword deeply.""",
f"""You twirl your sword in a silver spiral, feeling with satisfaction as the sword bites deeply into {reference["object"]}.""",
f"{reference['object'].capitalize()} readies {reference['him']}self for your attack. At the last second you duck and roll behind {reference['him']}, under {reference['his']} guard and slash {reference['him']} across the back.",
f"You enemy tries to step backwards, but {reference['his']} heel hits a raised section of ground. {reference['he'].capitalize()} staggers, and you slash {reference['him']} easily.",
f"With a deft sword movement you explode into action, striking with your whirling sword, spilling the blood of {reference['object']}.",
f"You thrust ahead with your sword, shouting in triumph as the tip buries itself into {reference['object']}."],

	"player_miss" : ["Your sword slices through the air, but meets nothing as your adversary sidesteps",
"You swing your sword in a cruel lateral strike, but your opponent ducks just in time, the wind chasing the blade making a whistling sound.",
f"""You swing your sword downwards, grunting with the effort. {reference["object"].capitalize()} jumps back at the last second, the tip of your sword barely a inch from {reference["his"]} body.""",
f"""Despite your best efforts, {reference['object']} is too quick for you, dodging your strikes with ease.""",
f"""Your sword comes crashing down on {reference['object']}, but your target recoils from the blow just in time, your weapon slamming hard into the ground.""",
f"You swing your sword, but misjudge the distance. You blade passes harmlessly in front of your opponent.",
f"Your attempt to strike {reference['object']}, but {reference['he']} steps backwards just in time, the tip of your sword not even scratching {reference['him']}."],

	"player_extra_attack": ["You're quick enough to strike a second time.",
"You bring your blade back quickly for a second attempt.",
"You spin with the momentum of the sword, whirling and attacking again swiftly.",
"You twirl your sword in a figure of eight, carrying your impetus into an addition strike.",
"You take a swing again, determined to strike true."],

	"player_hit_parry": [
f"You swing your sword, but {reference['object']} is ready, dodging sideways at the last second.",
f"As you charge forwards, {reference['object']} slams into you, pushing you back, staggering.",
f"Just as you bring your sword to bare, {reference['object']} ducks behind you, striking at your back.",
f"Suddenly, your opponent ducks low and strikes at your legs, almost tripping you.",
f"Too late, you realize the trap. Your foot kicks a stone and you stumble forwards, at the mercy of {reference['object']}"],

	"player_parry": ["You raise your sword in a defensive position.",
"You brace yourself for your charging adversary, ready and waiting",
f"You bring your sword to bare, watching {reference['object']} closely.",
f"You shout a challenge to {reference['object']}, holding your ready.",
f"{reference['object'].capitalize()} rushes forwards. You grasp your sword firmly before you."],

	"player_success_parry": [
f"Your enemy runs forward, but at the last second you kick {reference['him']} back, knocking the breath from {reference['his']} body.",
f"{reference['he'].capitalize()} runs forward suddenly, but you are ready. {reference['his'].capitalize()} attack is caught on your sword and you twirl the blade swifty, knocking {reference['him']} off balance.",
f"As your opponent charges, you sidestep. {reference['he'].capitalize()} runs straight past you, back exposed, almost asking to be slashed.",
f"""{reference['object'].capitalize()} attacks, but you spin away from the blow, ending your twirl on your opponent's flank.""",
f"Your adversary closes in, but at the last second you lunge forwards, slamming your shoulder into {reference['him']}. {reference['he'].capitalize()} stumbles backwards, sputtering for breath.",
f"As the expected attack comes in, you duck and spin under the strike, bring your sword around to attack.",
f"With a swift movement, you cut at the legs of {reference['object']}, sending it stumbling."],

	"player_fail_parry": [
"You raise your sword against the expected attack, but it comes quicker than you thought. You feel a cut upon your face.",
"Your opponent rushes forwards. You try and duck to the side at the last second, but are too slow. Pain racks your body and you jump away, cursing.",
"You deflect the first attack, but the second comes in quicker than you can react. You manage to avoid the worst of the blow, but still, it hurts.",
f"Despite your defensive stance, {reference['object']} is too fast for you, dealing you a glancing blow.",
f"You move your sword to intercept, but only then realise the feint. Too late. You exposed flank falls easy prey to {reference['object']}."],

	"player_distract": ["Suddenly, you lean down, scoop up a handful of dirt and throw it in your enemy's face.",
f"You yell fiercely into the face of your opponent. {reference['he'].capitalize()} recoils at the sudden noise.",
f"""You feint sideways, then come back to your previous position. {reference['object'].capitalize()} staggers slightly at the sudden move.""",
f"As your enemy moves closer, you swiftly kick {reference['him']} painfully in the shin.",
f"Your opponent brings down {reference['his']} attack. You raised your blade at the last second, and with your free hand punch {reference['him']} in the face, sending {reference['him']} staggering away."],

	"player_potion": [
f"You jump away from the melee and pull a potion from your belt. You drain the liquid in a few seconds, and toss the empty bottle away. You feel strength lost return to you.",
f"You kick your opponent, sending {reference['him']} backwards. While {reference['he']} staggers, you drink a potion, and pain leaves your body."],

	"player_knife": [
f"Your foe lunges forwards. At the last moment you jump away, sliding across the ground. You twist and hurl a throwing knife with all your strength. The projectile finds its mark.",
f"As your opponent charges towards you, you pull out a throwing knife, throwing it at {reference['him']}. Your aim is true and {reference['he']} stumbles, a bloodstain on {reference['his']} leg."],

	"player_oil": [
f"You produce a vial of blade oil and quickly splash it on your sword. It will not last long, but it will make your enemy feel pain.",
f"{reference['object'].capitalize()} stops as you pull a vial of liquid from your belt. You pour it onto your blade, and attack."],

	"player_smoke": [
"Closing your eyes and mouth, you throw down a smoke bomb. Thick, grey smoke covers the battle area, making sight impossible.",
"You light the fuse of a smoke bomb and hurl it at your enemy. There's a bang and suddenly everything is covered by grey smoke."],

	"enemy_strike": [f"{reference['object'].capitalize()} lunges in, ready to strike.",
"You ready yourself as your adversary charges forward, teeth bared in savage fury.",
f"{reference['object'].capitalize()} charges, {reference['his']} eyes gleaming."],

	"enemy_hit": [
f"You are too slow to react. {reference['object'].capitalize()} strikes you a blow. You hit the ground hard but roll to your feet, panting for breath.",
f"{reference['he'].capitalize()} takes a swing at you, and the attack finds its mark. You feel blood on your skin, and jump away before further harm.",
f"Your opponent lunges forwards. Before you can avoid the attack, you are dealt a glancing blow.",
f"You are beaten down by a hail of strikes, blocking one after the other. Finally, one makes its way through your defenses and you feel a sharp pain."],

	"enemy_miss": [
f"Though your opponent comes in with speed and ferocity, you avoid everything {reference['he']} tries to strike you with.",
f"A strike is aimed at your head, but you are too quick for {reference['object']}. You kick {reference['him']} and {reference['he']} staggers before {reference['he']} gets another chance to attack.",
f"{reference['he'].capitalize()} lunges forwards, missing you and stumbling past you. But {reference['he']} whirls again in another attack. You duck at the last second, the hair on your head whipping with the passing attack.",
f"As the attack passes to within a hair's breadth of your face, you twist and jump away in a diving roll, coming back to your feet, glaring at your opponent."],

	"enemy_attack_ally": [
f"{reference['object'].capitalize()} turns towards {ally_reference['object']} and rushes towards {ally_reference['him']}.",
f"{ally_reference['object'].capitalize()} braces {ally_reference['him']}self as {reference['object']} moves to attack {ally_reference['him']}.",
f"You jump out of the way as {reference['object']} charges past you. {reference['he'].capitalize()} turns back around, this time moving to strike at {ally_reference['object']}."
	],

	"enemy_hit_ally": [
f"{ally_reference['object'].capitalize()} staggers away, {ally_reference['his']} attacker having drawn blood.",
f"{ally_reference['object'].capitalize()} curses as {ally_reference['his']} opponent's attack connects.",
f""""Alright," says {ally_reference['object']}, jumping away from the danger. "That one stung a little." """
	],

	"enemy_miss_ally": [
f""""Nice try," says {ally_reference['object']}, ducking away from {reference['object']}'s attack.""",
f"""{ally_reference['object'].capitalize()} sidesteps the blow directed at {ally_reference['him']}, slapping at it with {ally_reference['his']} weapon.""",
f"""{ally_reference['object'].capitalize()} rolls away from {reference['object']} and the danger, coming to {reference['his']}, panting for breath."""
	],

	"enemy_block": [
f"{reference['object'].capitalize()} braces {reference['him']}self, and glares at you, daring you to fight.",
f"The other combatant raises {reference['his']} defenses, covering {reference['him']}self.",
f"Your opponent assumes a defensive stance, flattening {reference['his']} feet and barely moving."],

	"enemy_divert": [
f"You close in, sword leading the way. But at the last second, {reference['he']} jumps away, leaving you staggering past.",
"Your adversary lunges unexpectedly, and you only recognize the feint when it's too late and have already lept to the side, leaving yourself off balance.",
f"Suddenly, {reference['object']} jumps forward, shoving your chest with one hand. You stagger, the breath knocked from your body."],

	"human_death": [
f"As your sword bites deeply into your enemy, {reference['he']} moans in pain, then crumples to the ground, dark blood flowing onto the ground.",
f"{reference['object'].capitalize()} stares at you for a moment. Then a trickle of blood comes from the corner of {reference['his']} mouth, and {reference['he']} falls, dead.",
f"You pull your sword from your adversary's chest, and {reference['he']} topples over backwards instantly, dead before {reference['he']} hits the ground.",
f"You bury your sword up to the hilt into {reference['object']}, the blade protruding from {reference['his']} back. You kick {reference['him']} from your sword, and the body falls, blood pooling.",
f"For a moment, {reference['he']} stays standing. But then {reference['he']} crashes down to the ground, a scarlet blossom growing around {reference['his']} body.",
f"{reference['object'].capitalize()} falls to {reference['his']} knees, head leaning forward. You don't hesitate, bringing your sword down like an executioner's axe, taking the head from {reference['his']} shoulders.",
f"You cut {reference['object']}'s hand, and {reference['he']} drops {reference['his']} weapon. {reference['he'].capitalize()} tries to punch you, but you duck under the blow and cut {reference['him']} across the back. {reference['he'].capitalize()} falls without a cry.",
f"{reference['object'].capitalize()} falls onto {reference['his']} back, gasping for air. You lunge forwards and plunge your sword into {reference['his']} chest, spattering your blade with blood.",
f"You spin on one foot, and bring your hand in a strong backhand. The attack cuts {reference['object']} clean in half.",],

	"monster_death": [f"{reference['object'].capitalize()} growls one last time, then falls to the ground.",
f"With a sickening squelch, you tear your sword from the monster, and it topples like an upset statue.",
f"You lunge forwards, pinning {reference['object']} by the throat and holding it to the ground. You draw your knife and plunge it home into the monster's snarling mouth.",
f"{reference['object'].capitalize()} stares at you, collpasped on the ground and growling softly. You walk over and finished it off with a mighty blow.",
f"You follow up your previous strike with a another one. {reference['object'].capitalize()} has no chance against the hail of blows.",
f"With a flurry of blows, you hack pieces of {reference['object']} off {reference['his']} main body.",
f"Your already injured opponent can only watch as you bring you sword down upon it in a lunging strike.",
f"{reference['object'].capitalize()} knows {reference['his']} time has come. In a last ditch attack, {reference['he']} lunges forward. You sidestep and finish {reference['him']} easily."],

	"enemy_approach": [
f"{reference['object'].capitalize()} rushes forward, {reference['pain']}ing with rage at {reference['his']} companion's death.",
f"{reference['object'].capitalize()} approaches you now, more wary than your previous, now deceased opponent.",
f"You ready your sword, now stained with blood, shouting a challenge to your next opponent. {reference['he'].capitalize()} responds to the challenge and moves forwards.",
f"You spin around to face your next enemy, raising your sword.",
f"You size up {reference['object']}, and prepare to do battle."],

	"ally_attack": [f"{ally_reference['object'].capitalize()} rushes towards your opponent, weapon raised high.",
f"""{ally_reference['object'].capitalize()} takes {ally_reference['his']} turn to strike at {reference['object']}.""",
f"With a suddenly lunge forwards, {ally_reference['object']} attacks at {reference['object']}'s flank.",
f""""Die!" {ally_reference['object']} yells, charging forwards, weapon at the ready.""",
f"""Gritting {ally_reference['his']} teeth, {ally_reference['object']} rushes forwards, weapon poised to strike."""],

	"ally_hit": [f"{ally_reference['object'].capitalize()}'s attack strikes true, scoring a hit.",
f""""{reference['he'].capitalize()} felt that one!" {ally_reference['object']} shouts gleefullt, jumping away before {reference['his']} opponent can make a counterattack.""",
f"With a swift blow, {ally_reference['object']}'s weapon meets the body of {reference['object']}."],

	"ally_miss": [f"{ally_reference['object'].capitalize()} moves to attack, but {ally_reference['his']} target evades the blow."],

	"ally_assist": [f"""{ally_reference['object'].capitalize()} maneuvers to flank. "Strike now!" {ally_reference['he']} yells."""],

	"ally_distract": [f""""Over here, ugly" {ally_reference['object']} jeers. {reference['object'].capitalize()} turns to face {ally_reference['him']} agrily."""],

	"ally_down": [f"""{ally_reference['object'].capitalize()} clutches {ally_reference['his']} wound, blood seeping through his fingers. "I'm sorry!" {ally_reference['he']} groans. "I'm out for this one." """,
f"""As {ally_reference['object']} is struck, {ally_reference['he']} falls and crawls away from the melee.""",
f"""{ally_reference['object'].capitalize()} is struck in the head. {ally_reference['his'].capitalize()} eyes roll back and {ally_reference['he']} falls, senseless.""",
f"""The damage {ally_reference['object']} sustains is great, and it is not long before {ally_reference['he']} passes out from the pain.""",
f"""{ally_reference['object'].capitalize()} tries to jump away from {reference['object']}, but trips and falls. {ally_reference['he'].capitalize()} is too weak to rise again."""]
	}

	return random.choice(choices[scripts])
