import random
from functions import ability
from functions import equipment
from functions import character
from functions import encounters
from functions import enemy_round
from functions import post_combat
from functions import weapon
from functions import rest
from functions.utils import print_stuff
from functions.utils import input_stuff
from functions.utils import colour_it
from functions.utils import Color
from functions.loading import save

lizardtongue = colour_it("Lizardtongue Mountains", Color.PLACE)
blackburrow = colour_it("Blackburrow", Color.PLACE)

def ghouls_at_farm():
	global lizardtongue
	global blackburrow
	ghouls = colour_it("ghouls", Color.ENEMY)
	save("chapter1.ghouls_at_farm")
	print_stuff([f"You make your way outside of {blackburrow}. It is late morning, and the sky is a cobalt blue.",
"Birds sing, and the long grass sways in the breeze. The air is cool, but not cold, and fluffy white clouds float in the sky.",
f"You steer off the main road and onto a dirt track leading to the {lizardtongue}. About an hour into the journey you come across a farm.",
"Wheat stalks stand golden against the pale grass. You decide to cut through the wheat field, rather than take a detour around it.",
"That's when you hear shouting and cursing. You begin to run, and see a man standing in the front door of his house. He is swinging a pitchfork to and fro.",
f"Standing before him are four {ghouls}; pale, lanky, short and hairless humanoids that feed on rotting flesh. Two other {ghouls} lie dead and bleeding.",
"The man sees you and screams for help. You see a little girl and a teenage boy standing behind the man, expressions of terror on their faces.",
f"You know that the man will not be able to hold the {ghouls} back forever."])

	choice = input_stuff("""1. Help the farmer.
2. Continue on your way.
> """, ['1', "2"])
	if choice == "1":
		print_stuff([f"You rush forwards, {weapon.weapon['weaponname']} in hand. The {ghouls} turn to face you now, but one of them continues to focus on the farmer",
f"One of the {ghouls} lunges forward suddenly, and you ready your sword."])
		enemies = [encounters.monster_access("ghoul"), encounters.monster_access("ghoul"), encounters.monster_access("ghoul")]
		enemy_round.initialize(enemies)
		if post_combat.victory == False:
			print(f"There is no one to save you. The farmer cannot hold the {ghouls} back for much longer, and the {ghouls} will show no mercy to those in the way of their food.")
			exit()
		print_stuff([f"You wipe ghoul blood from your sword with a cloth. The farmer approaches you, his own pitchfork stained a dark red.",
f'"Thank you, kind stranger," the man says. He bites his lip for a second, then pulls a money bag from his belt and holds it out to you.',
f'''"It's not much, but you deserve a reward, {character.character['titles']['casual']}."'''])
		choice = input_stuff("""1. "Thank you. Take care."
2. "Keep the money. Your children need it."
> """, ['1', "2"])
		if choice == "1":
			print_stuff(["You take the gold bid the farmer farewell, before continuing on your way.",
"You received 10 gold!"])
			equipment.equipment["gold"] += 10
		else:
			print_stuff(["You push the money bag away, and you notice the man seems to relax a bit. Clearly he was hoping you would refuse.",
f'''"Thank you again. But at least let me give you a meal before you leave."''',
"You accept the man's offer and he brings you into his small house. He gives you a bowl of green soup. You eat it, and it tastes good enough.",
"The soup energises you, despite its mediocre taste. Once you have finished eating, the farmer bids you farewell, and you continue towards the Lizardtongue Mountains"])
			ability.ability["health"] += 5
			ability.gain_xp([encounters.xp_handouts["small"]])


def hag_lair():
	global lizardtongue
	global blackburrow
	save("chapter1.hag_lair")
	treasure = 0
	bone_hag = colour_it("bone hag", Color.ENEMY)
	print_stuff(['You continue along the trail, and you pass by a few more farms, and sometimes the people maintaining them, nodding in greeting as you pass.',
'''Finally, the track becomes wilder, the farms become less, before disappearing altogether. Small pockets of trees and undergrowth now dot the countryside.''',
'It is late in the afternoon when the trail splits suddenly. It is clear which path will lead to the mountains. The other pass leads into a small forest.'])
	choice = input_stuff(f"""1. Explore the forest trail.
2. Take the path to the {lizardtongue}.
> """, ['1', "2"])
	if choice == "1":
		print_stuff(['You walk down the forest path. Light from the afternoon sun slants through the thin canopy of leaves, and small critters rustle in the leaflitter.',
'After following the trail for about ten minutes, it ends in a small log cabin. No lights shine through the glass windows, but you can detect some movement from inside.',])
		choice = input_stuff(f"""1. "Is anyone home?!"
2. Try to open the door.
3. Turn back and head for the {lizardtongue}.
> """, ['1', "2", "3"])
		if choice == "1":
			print_stuff(["You see the movement stop for a moment, then a creature comes hurtling out the door.",
f'''"Dinsers!" the creature shrieks with glee. "Dinsers has comses!" The creature is a {bone_hag}.''',
"""It takes on the form of an elderly woman with grey skin that hangs and droops in strange folds, dull black hair and dressed in nothing but a loincloth. 
They have sharp claws on their fingers and toes.""",
f"You also know that hags enjoy to the taste of living flesh, especially that of young people or elves. You draw {weapon.weapon['weaponname']} and ready yourself."])
		elif choice == "2":
			print_stuff(["You move to the door and twist the doorknob. The door swings open, and immediately the smell of rot assaults your nose.",
"Almost everything here is broken or decayed. Only two things seem solid here; a cauldron of meat soup, and a hunched form. The form turns to see, and grins toothily.",
f'''"Dinsers!" the creature shrieks with glee. "Dinsers has comses!" The creature is a {bone_hag}.''',
"""It takes on the form of an elderly woman with grey skin that hangs and droops in strange folds, dull black hair and dressed in nothing but a loincloth. 
It has sharp claws on their fingers and toes.""",
f"""You also know that hags enjoy to the taste of living flesh. Before you can react, the {bone_hag} lunges forwards, crashing into you. 
The two of you tumble outside of the cabin and into the forest. You roll to your feet and draw your sword, and the hag rises to its feet, snarling."""])
		else:
			print_stuff(['Deciding not to disturb the inhabitants - whoever they may be - you trace your steps back to the junction in the trail.'])
			return False
		enemy_round.initialize([encounters.monster_access("bone_hag")])
		if post_combat.victory == False:
			print("No one knows you came here, and no one can save you now. Unfortunately, you'll probably end up in the hag's cooking pot.")
			exit()
		print_stuff([f"With the {bone_hag} dead, you enter the cabin. You look around, and you see a worn chest, the cauldron of meat soup, a table with papers on it, and a pile of bones."])
		while True:
			quest = colour_it(""""Leave""", Color.QUEST)
			investigate = input_stuff(f"""1. Search the chest.
2. Investigate the cauldron.
3. Check the papers
4. Examine the bones.
5. {quest}
> """, ['1', "2", '3', '4', '5'])
			if investigate == "1":
				print_stuff(["You open the chest, and are slightly disappointed when all you find are worn clothes, riddled with moth holes."])
			elif investigate == "2":
				while True:
					option = input_stuff("""The cauldron contains some meat soup. It is still warm, and a wooden stirring spoon sticks out from its depths.
1. Taste the soup.
2. Step away.
> """, ['1', "2"])
					if option == "1":
						print_stuff(["The soup tastes fresh, and has chunks of meat in it. The meat itself tastes similar to pork."])
						continue
					else:
						break
			elif investigate == "3":
				character.story["hag_lair"] = True
				treasure += 1
				print_stuff(["""You pick up a piece of paper and read.
	______________________________________________________
	|	My dearest Chana,                                |
	| If I am to die prematurely, you must lift the chest| 
	| and take the belongings below it. That should be   |
	| enough to keep you alive, and perhaps flourish.    |
	|	Denvar                                           |
	|____________________________________________________|"""])
				if treasure == 1:
					option = input_stuff("""1. Search under the chest.
2. Step away.
> """, ['1', "2"])
					if option == "1":
						equipment.equipment["gold"] += 50
						print_stuff(["You obey the instructions in the note, lifting the chest and peering under it.",
"Underneath you see a reasonably large bag of money, as well as a silver ring etched with runes.",
"You take the money, counting 50 gold coins."])
						ring = input_stuff("""1. Put on the ring.
2. Leave the ring.
> """, ['1', "2"])
						if ring == "1":
							boost = colour_it("Your Strength has been increased by 1!", Color.FUNCTION)
							ability.ability["strength"] += 1
							print_stuff(["You feel a tingling sensation as you slip the ring on, and a sudden burst of power.",
{boost}])
						else:
							continue
					else:
						treasure = 0
						continue
				else:
					print_stuff([""])
					continue
			elif investigate == "4":
				print_stuff(["You discover two things about the bones. First, it is that of a woman, due to the shape of the bones and the scraps of woman's clothing lying nearby.",
"Second, the bones have been scraped clean of all flesh, due to the nicks and scratches of something being drawn along them."])
			else:
				break
		print_stuff(["You leave the cabin, satisfied with what you achieved. You head back along the trail, and back to the junction."])
	print_stuff([f"You turn onto the path to the {lizardtongue}, and continue your trek."])


def campers():
	save("chapter1.campers")
	man_name = "the large man"
	eladris = colour_it("Eladris", Color.NPC)
	garurt = colour_it("Garurt", Color.NPC)
	print_stuff(["The sky is growing darker. The bird song is giving way to the chirp of the crickets, and the air grows cold.",
"Even as you begin to consider a place to stop for the night, you see a flickering orange light from behind a clump of high bushes."])
	choice = input_stuff("""1. Investigate the source of the fire.
2. Keep walking until you find somewhere to rest.
> """, ['1', "2"])
	if choice == "1":
		print_stuff(["You walk over to the source of the fire. Once you reach it, you see two men, and two large backpacks surrounding a campfire.",
"One of the men, large and muscular, jumps to his feet at the sight of you, drawing his sword. The other, who is shorter, slender and lean, also rises to his feet.",
'''"Who are you?" the large man demands. "Friend or foe?" The other man places a hand on his companion's shoulder and smiles at you.''',
f'''"I beg your pardon, {character.character["titles"]["formal"]}," he says smoothly. "We're just on guard, as we have learnt to be."''',
'''The large man continues to eye you warily and doesn't sheath his sword. The lean one gestures to the campfire.''',
'''"Share a fire?" he offers kindly.'''])
		choice = input_stuff("""1. "Yes, thank you."
2. "I'd best be on my way." 
> """, ['1', "2"])
		if choice == "1":
			print_stuff(["""The lean man's smile increases. "Excellent," he says. You take a seat by the fire, and bask in its warmth.""",
"""The lean man takes a seat beside you, but the large man grumbles something about taking a walk and leaves.""",
f""""I do not believe we have been properly introduced," the lean man says kindly. He lays a hand on his chest. "I'm {eladris}. And you are?"
"""])
			reply = input_stuff(f"""1. "I'm {character.character["firstname"]}."
2. "I'd rather not tell you."
> """, ['1', "2"])
			if reply == "1":
				print_stuff([f""""{character.character['firstname']}," {eladris} says, testing your name on his tongue."""])
			else:
				print_stuff([f"""{eladris} laughs. "Keep your secrets then," he chuckles. "But you should learn to be more trusting." """])
			print_stuff([""""So what brings you here? Monsters are roaming the countryside in even greater numbers these days." """])
			reply = input_stuff(f"""1. "I'm looking for some missing people."
2. "I do not fear monsters. It is the other way around." 
> """, ['1', "2"])
			if reply == "1":
				print_stuff([f""""I see," {eladris} says. "I will not pry, though my curiosity demands me to do so." """])
			else:
				print_stuff([f""""You're a confident one," {eladris} says. "Be wary it doesn't become hubris." """])
			while True:
				question = input_stuff(f"""1. "So... what's a half-elf doing out here?"
2. "Who's your cheerful friend?" 
3. "You said monsters were increasing in numbers..."
4. "I'm going to get some sleep." (leave dialogue) 
> """, ['1', "2", '3', '4'])
				if question == "1":
					print_stuff([f"""{eladris} grins at you. "You noticed?" he says. "Was it the name, or my appearance?" """,
"""He shrugs. "Honestly, it's reason enough to escape the racists. But you are a 'doyana', so you wouldn't understand." """,
""""Travelling has always calmed my nerves. I do it for the simple purpose of enjoyment." """])
					continue
				elif question == "2":
					print_stuff([f""""And good looking too!" he adds, chuckling to himself. "His name is {garurt}. Don't mind him; a more distrustful man was never born." """,
""""I keep him around because he's a good fighter. My escort, so to speak." """])
					man_name = garurt
					continue
				elif question == "3":
					print_stuff([""""So I did," he sighs. "There's talk of magical fluctuations, and that's what attracting them." """,
""""The source of the disturbances remains unknown, but I'm sure someone will figure it out eventually." """,
f""""They are merely rumours, of course," {eladris} adds quickly. "But rumours can be built on truth." """])
					continue
				else:
					print_stuff([f"""{eladris} nods. "Sweet dreams," he says. Just as you are beginning to pull out your blankets, {man_name} returns from his walk.""",
"He remains silent, until Eladris is fast asleep, at which point he approaches you.",
""""I know what you are," he says. "You're a fighter; that much is clear to see. But I'm warning you that if you pull a fast one, we'll soon see who's the better fighter." """,])
					break
			reply = input_stuff("""1. "Big words for a man with a small prick."
2. "You need not worry."
3. "Get out of my face before I smash yours in." 
> """, ['1', "2", '3'])
			if reply == "1":
				print_stuff([f"""{man_name.capitalize()} glares at you. "Watch your words, {character.character['titles']['contempt']}," he spits."""])
			elif reply == "2":
				print_stuff([f"""{man_name.capitalize()} smiles wickedly. "Good. Then there's no need for trouble," he says. """])
			else:
				print_stuff([f"""{man_name.capitalize()} spits in your face. "You want to go here and now?," he says. "Because I'll fight you anytime." """])
			print_stuff([f"""{man_name.capitalize()} then stalks off, pulling out his own bedroll. It is not long before you fall asleep, staring up at the stars.""",
"""You wake up in the middle of the night, tormented by a full bladder. Silently, you move away to find somewhere to relieve yourself.""",
f"""Once you return, you notice that both {eladris} and {man_name} are speaking to each other."""])
			if ability.ability['awareness'] > 5:
				print_stuff(["You able to hear what they are saying.",
f""""I say we kill {character.character["titles"]['him']}, grab the loot and run," {man_name} says. """,
f""""Not this one," {eladris} protests. "I've talked with {character.character["titles"]['him']}, and {character.character["titles"]['he']}'s a kind person. {character.character["titles"]['he'].capitalize()} doesn't deserve that." """,
""""It's not about what they deserve. It's about what we need!" """])
			else:
				print_stuff(["You are unable to hear what they are saying. You move closer to try and listen."])
				agility_roll = random.randrange(1,101)
				if agility_roll <= (75 + ability.ability['agility']):
					print_stuff(["You enter earshot of them without being noticed.",
f""""I say we kill {character.character["titles"]['him']}, grab the loot and run," {man_name} says. """,
f""""Not this one," {eladris} says. "I've talked with {character.character["titles"]['him']}, and {character.character["titles"]['he']}'s a kind person. {character.character["titles"]['he'].capitalize()} doesn't deserve that." """,
""""It's not about what they deserve. It's about what we need!" """])
			speech = input_stuff("""1. "Greetings, gentlemen."
2. Escape to the main trail.
> """, ['1', "2"])
			if speech == "2":
				print_stuff(["""You use their chatter to make your escape, silently thanking yourself for taking your equipment with you to the lavatory.""",
"""You follow the trail a bit longer. You manage to find a small glade, which seems like a good spot to rest for the night.""",
"""You light a small fire and shrug off your backpack, sighing with relief at the break from walking."""])
				return False
			print_stuff([f"The two men turn to you. {man_name.capitalize()} jumps to his feet, drawing his sword.",
f""""The ploughing {character.character['titles']['insult']} is spying on us!" he yells, running forward, sword raised."""])
			choice = input_stuff(f"""1. Use a smoke bomb to incapacitate {man_name}.
2. Draw {weapon.weapon['weaponname']} and do battle.
> """, ['1', "2"])
			if choice == "1" and equipment.equipment['smoke bombs'] > 0:
				equipment.equipment["smoke bombs"] -= 1
				print_stuff([f"""You hurl a smoke bomb at {man_name}. He coughs and splutters and you seize your chance.""",
"""Lunging forwards, you hook your leg behind his, throwing him to the ground. His cry of rage is cut short as he lands on his back and the breath is knocked from him.""",
"""To make sure he causes no more trouble, you kick him in the side of the head, and his body goes still, apart from his chest rising and falling."""])
			else:
				enemy_round.initialize([encounters.special_access("garurt")])
				if post_combat.victory == False:
					print_stuff(["You wake up, bruised and scratched. You look around and realise that you are in the remains of the camp sight.",
"You also realise that almost all your belongings are gone. Your sword, your food, and your items remain. However, you money and knives are gone.",
"You pick yourself up and gather your equipment. It is day time, and despite being knocked unconscious, you feel slightly refreshed.",
"You continue on your journey, despite the sour defeat."])
					equipment.equipment['gold'] = 0
					equipment.equipment['knives'] = 0
					return False
				else:
					print_stuff([f"""You stand over {man_name}'s corpse. You stop when you here the sound of clapping.""",
f""""That was quite a show you put on," {eladris} says. "Where did you learn that?" """])
					reply = input_stuff("""1. "Don't look so cocky. You're next."
2. "Why did he attack me?" 
> """, ['1', "2"])
					if reply == "1":
						print_stuff([f"""At this, {eladris} chuckles. "Kill me then. I do not fear death. At least let me explain." """])
				print_stuff([f""""Please forgive Garurt," Eladris says coolly, not a hint of worry in his voice. "We were just discussing robbing you when you burst in." """,
""""We're bandits. We were thrown out of society because of my half-blood status and his friendship with me. We've had to live robbing and hiding for many years.""",
f"""{eladris} looks up at you. "Kill me if you will," he says. "My existence can only get sadder." """])
				action = input_stuff(f"""1. Kill {eladris}.
2. Walk away.
> """, ['1', "2"])
				if action == "1":
					print_stuff([f"""You step forward, sword in hand. {eladris} closes his eyes, and you impale his heart. His death is painless, and he doesn't even flinch.""",
f"""You search {eladris}' bags and come away with 27 gold coins, a healing potion, and two throwing knives."""])
					equipment.equipment["gold"] += 27
					equipment.equipment["potions"] += 1
					equipment.equipment["knives"] += 2
					character.story["eladris"] = False
				print_stuff(["""You walk away from the camp, and return to the trail."""])
		else:
			print_stuff(["""The lean man shrugs. "Safe travels," he says. You walk away from the camp sight and back to the trail."""])
	print_stuff(["""You follow the trail a bit longer. You manage to find a small glade, which seems like a good spot to rest for the night.""",
"""You light a small fire and shrug off your backpack, sighing with relief at the break from walking."""])
	rest.rest()


def thief():
	lalikins = colour_it("lalikins", Color.ENEMY)
	save("chapter1.thief")
	equipment.equipment["gold"] -= 15
	if equipment.equipment["gold"] < 0:
		equipment.equipment["gold"] = 0
	print_stuff(["You wake up the following morning. You sling on your backpack and strap on your belt.",
"It is then that you realise that some of your gold has vanished.",
"You look around to see if you dropped it. Quickly, you notice something else. Footprints."])
	direction = input_stuff(f"""1. Follow the footprints.
2. Accept the loss and continue to the {lizardtongue}.
> """, ['1', "2"])
	if direction == "1":
		print_stuff(["You begin to follow the footsteps. The thief, whoever they are, is not an expert and has not covered their tracks well.",
"The trail moves off the main path, and into a valley between two large hills. At the base of the valley, you see a young woman hunched over a campfire.",
"Her clothes are ragged, and she has no weapon to speak of. She doesn't look older than twenty.",
"As if alerted by your mere presence, the woman turns, gives a start and runs over the hill opposite and into some trees.",
"Before you can react, you here a scream and a growl."])
		choice = input_stuff("""1. Give chase to the thief.
2. Let her go and return to the trail.
> """, ['1', "2"])
		if choice == "1":
			print_stuff(["You run after the woman, and stop after cresting the next hill. What you see makes you draw your sword.",
"The woman is lying dead in a pool of blood, staring blankly at the sky. Gnawing on her leg is are two strange creature.",
"Each lanky, and uses both its arms and legs to move, unless it is grabbing something. They are covered in brown fur, and have yellow, reptilian eyes.",
f"Two pointy ears like those of a wolf adorn each head, as well as a long snout. You recognise the monsters as {lalikins}."
f"The {lalikins} turn to you and growl, showing off white, pointy teeth. They flex their claws and begin to approach you.",
f"You hold {weapon.weapon['weaponname']} at the ready, and the {lalikins} charge."])
			enemy_round.initialize([encounters.monster_access("lalikin"), encounters.monster_access("lalikin")])
			if post_combat.victory == False:
				print_stuff([f"The {lalikins} were already feeding on the woman. They will not complain about extra food."])
				exit()
			print_stuff(["You search the body of the woman and find the money she stole from you."])
			equipment.equipment["gold"] += 15
			action = input_stuff("""1. "Rest in piece." 
2. Walk away.
3. Spit on her body.
> """, ['1', "2", '3'])
			if action == "1":
				print_stuff(["You kneel down and close the woman's eyes with two fingers, before turning and walking back to the trial."])
			elif action == "3":
				print_stuff(["You hawk and spit on the woman's corpse, and you feel like you've gotten some revenge for the trouble she caused.",
"With your meager payback complete, you return to the trail."])
	print_stuff([f"You continue along the trail to the {lizardtongue}, wondering when you'll get a day of piece and quiet."])

def ascent():
	crag = colour_it("crag", Color.ENEMY)
	denvar = colour_it("Denvar", Color.NPC)
	chana = colour_it("Chana", Color.NPC)
	save("chapter1.ascent")
	print_stuff([f"It's the middle of the day when you finally reach the base of the {lizardtongue}.",
"As you climb the largest mountain, the terrain gets steeper and rockier. Many times you stumble on loose gravel.",
"The wind becomes stronger as you climb, and the air becomes cooler. You know the cave that is your objective is close to the summit.",
"Finally, after an hour of scrambling over boulders, you have had enough. You throw down your pack and take out some of your supplies.",
"Your intention is to take a quick rest before continuing."])
	rest.rest()
	print_stuff(["As your making your way up the mountain, your foot finds a patch of loose gravel. You feet the ground slide out from under you.",
"Desperately, you try to jump to safety."])
	agility_roll = random.randrange(1,9)
	if agility_roll <= ability.ability["agility"]:
		print_stuff(["You fall, but hit the ground in a roll. You are agile enough to roll to you feet and avoid the tumbling gravel."])
	else:
		print_stuff(["You slip and fall. You try to roll back to your feet, but you are not agile enough.",
"You tumble down the side of the mountain, but somehow avoid serious harm. Suddenly, you find yourself lying on the ground.",
"Dazed, you rise to your feet. You look around, and that's when you see it; a hulking mass of rock approaching you.",
"The creature appears to be a large, bald humanoid, ten feet tall at least. It is made completely of boulders at least the size of your head."
f"Every step it takes send vibrations in the ground. You know this monster to be a {crag}.",
f"A beast of animated rock, a {crag} will attack all living creatures it encounters.", "Sword in hand you run forwards.",
f"The {crag} swings at you, but you drop and slid between it's legs. The {crag}'s fist hits the ground, blasting rocks to pieces.",
"You realise that the creature may be slow, but if you get hit, your situation will be grave indeed."])
		enemy_round.initialize([encounters.monster_access("crag")])
		if post_combat.victory == False:
			print_stuff([f"The {crag} cares nothing for food, but it does enjoy killing. Unconscious, you do not see the {crag} raise it's mighty fists."])
			exit()
		print_stuff([f"Panting for breath, you watch the {crag}'s body crumble into a pile of boulders and dust.",
"You continue your climb, and soon reach the place where you fell, careful not to step in any more gravel patches."])
	print_stuff(["You continue to climb up the mountain, the final remains of sleepiness gone from you, due to the intense events.",
"Once more, you find yourself out of breath and in need of rest. You turn and look out over the nearby countryside.",
"The view is spectacular. Everything is tiny, as if you were staring at an embroidered tapestry. Blackburrow is a dark cluster in the distance.",
"When the sun begins to set, you begin to search for a place to rest. Climbing higher, you find a small mountain trail.",
"You follow it along for a short distance, and find yourself beside a large cabin. There is no sign of movement inside.",
"Firewood stands stacked against the side of the cabin. A hunting bow and a quiver of arrows lean against the side.",
"The cabin seems fresh and looked after; it is clear that someone lives or lived here recently."])
	while True:
		choice = input_stuff("""1. Try to open the cabin door.
2. Knock on the door.
3. Find somewhere else to rest.
> """, ["1","2", '3'])

		if choice == "2":
			print_stuff(["You knock on the door, but nothing stirs inside."])
			continue
		elif choice == "1":
			print_stuff(["To move for the cabin door and test the doorknob. It twists full and you hear a click. You open the door and step inside.",
"The interior is simple. A single table, a small kitchen area, a bed with a box of clothes next to it and two chairs.",
"An unlit lantern hangs from the ceiling."])
			choice = input_stuff("""1. Light the lantern.
2. Leave the lantern unlit.
> """, ["1", "2"])
			if choice == "1":
				print_stuff(["You pull out a match and light the lantern. Warm light flows over the cabin.",
"You are settling down to sleep when suddenly a rough looking man with prominent muscles, tangled beard, and a bow enters the cabin.",
"""He stares at you for a second, then speaks. His voice is deep and carrying, but somewhat fatherly.""",
""""Who are you?" he demands. "Why are you here?" He does not sound angry, only curious, and a bit wary. """])
			else:
				print_stuff(["You leave the lantern unlit and settle down to sleep. You pull out your bedroll and lay it down.",
"You are woken from your slumber by a boot tapping your ribs. The sky is black and an owl is hooting.",
"You look up and see a rough looking man with prominent muscles, tangled beard, and a bow enters the cabin.",
"""He stares at you for a second, then speaks. His voice is deep and carrying, but somewhat fatherly.""",
""""Who are you?" he demands. "Why are you here?" He does not sound angry, only curious, and a bit wary. """])
			reply = input_stuff("""1. "I came for rest."
2. "I came to loot the place."
3. "I got lost."
> """, ["1", "2", "3"])
			if reply == "1":
				print_stuff(["""The man smiles. "Then rest and be welcome," he says. """])
			elif reply == "2":
				print_stuff(["""The man raises an eyebrow. "This is my home," he says. "And I will not let you take anything." """])
			elif reply == "3":
				print_stuff([""""In that case, I'll help you as best as I can." """])
			print_stuff([""""In any case, you have entered my home without my permission. All I ask in return is answers." """,
""""First of all, where are you going on this cold evening." Before you can even begin to answer, he raises a hand and chuckles. """,
f""""Before you answer, allow me to introduce myself. I'm {denvar}. Who are you?" """])
			reply = input_stuff(f"""1. "I'm {character.character['firstname']}."
2. "..."
> """, ["1", "2"])
			if reply == "1":
				print_stuff([f"""{denvar} smiles. "So, {character.character['firstname']}, I have some questions for you." """])
			elif reply == "2":
				print_stuff([f"""{denvar} shrugs. "Fine, suit yourself. But I still have some questions for you. Answer them at least." """])
			print_stuff([""""First of all, who are you? I don't mean your name; I mean your profession. Your sword indicates you're a warrior." """])
			reply = input_stuff(f"""1. "I'm a Nighthawk."
2. "I'm a mercenary."
3. "I'm an adventurer."
> """, ["1", "2", "3"])
			if reply == "1":
				print_stuff([f""""A Nighthawk? Fascinating. I've heard many tales of your kind's exploits." """])
			elif reply == "2":
				print_stuff([f""""I see. I won't comment... but I don't approve of your method of employment." """])
			elif reply == "3":
				print_stuff([f""""Ah... The toughest and most unpredictable occupation." """])
			print_stuff([""""Second, what are you doing climbing the mountain? I hardly get people visiting." """])
			reply = input_stuff(f"""1. "I'm looking for missing people."
2. "I'm just enjoying the mountain air."
3. "I'm searching for treasure."
> """, ["1", "2", "3"])
			if reply == "1":
				print_stuff([f""""Well I wish you the best of luck on your search." """])
			elif reply == "2":
				print_stuff([f""""Of course!" {denvar} laughs. "That's why everyone traverses this treacherous landscape." """])
			elif reply == "3":
				print_stuff([f""""Be wary. The pursuit of gold has led many to their deaths." """])
			print_stuff([f"""{denvar} thinks for a bit, then nods his head. """,
""""I think that's all the questions I have," he says. "Now I'll let you ask me some." """])
			while True:
				quest = colour_it(""""I'm going to get some rest. Can I stay here?" """, Color.QUEST)
				if character.story["hag_lair"] == True:
					question = input_stuff(f"""1. "Who are you exactly?" 
2. "Have you seen a young man and woman pass this way?" 
3. {quest}
4. "Do you know someone who lives in a forest cabin near here?" 
> """, ["1", "2", "3", "4"])
				else:
					question = input_stuff(f"""1. "Who are you exactly?" 
2. "Have you seen a young man and woman pass this way?" 
3. {quest}
> """, ["1", "2", "3"])
				if question == "1":
					print_stuff([""""I'm a simple mountain man. I hunt and forage for food, but sometimes I go down to the lower plains." """,
""""However, I have a wife down there; she lives in a cabin not unlike this one. The mountain did not call to her as it called to me, though." """])
					continue
				elif question == "2":
					print_stuff([""""Hm... Ah, yes. A few days ago, a young man and woman came by. They were armed and laden with bags." """,
""""They seemed to be about sixteen years old each, and they looked related. I didn't meet them in person, though." """,
f"""Suddenly, {denvar} leans over to you. "But then there were these other people, heading the same way as those two travellers," he murmurs. """,
""""All of them were female, and they were dressed strangely. Thigh length tights, a midriff top... scantily clad for hikers. They were also all armed with curved swords." """,
""""They looked like trouble, so I didn't go to meet them. Still, I'm curious about their intentions." """])
					continue
				elif question == "3":
					print_stuff([""""Of course you can stay. Rest, eat, I've plenty to share. I have extra space for my wife." """])
					break
				elif question == "4":
					print_stuff([f""""Yes, she's my wife. {chana} is her name. Why do you ask?" """])
					reply = input_stuff("""1. "I'm afraid she's dead." 
2. "Met her on the way here. Seems well enough." (Persona roll for lying) 
> """, ["1", "2"])
					while True:
						if reply == "1":
							death = True
							break
						elif reply == "2":
							persona_roll = random.randrange(1, 101)
							if persona_roll <= (60 + ability.ability["persona"]):
								print_stuff(f"""{denvar} smiles. "That is good to know," he says.""")
								death = False
								break
							else:
								print_stuff(f"""{denvar} examines you for a moment. "You're lying," he says. He closes his eyes. "{chana}'s dead, isn't she?" """)
								death = True
								break
					if death:
						print_stuff([f"""You see {denvar} stare at you for a moment, then he turns away. You see his shoulders tremble.""",
""""How did she die?" he says. "Do not soften the blow for me." """])
						reply = input_stuff("""1. "A bone hag scraped the flesh from her bones and consumed her. Her death was avenged." 
2. "Details do not matter. But know her death was avenged."
> """, ["1", "2"])
						if reply == "1":
							print_stuff([f"""{denvar} closes his eyes for a moment. "Forgive me," he says, and he seems to compose himself. """,
""""Do you have more questions? Do not hesitate to ask." """])
						elif reply == "2":
							print_stuff([f"""{denvar} shrugs sadly. "Perhaps I do not want to know. But forgive me, do you have more questions?" """])
			ability.ability["health"] = ability.ability["maxhealth"]
			print_stuff([f"""{denvar} nods. "Before you fall asleep, let me give you some food." He moves to the kitchen area and produces a basket of various foods.""",
"""He lays the food down beside you. You see the basket contains bread, a small bottle of wine, and a various fruits.""",
f""""The bounty from my last trip to market," {denvar} says. "Eat and rest, my friend." """,
"""You eat the food and drink the wine, and it is delicious and refreshing.""",
"""You regained all lost health!""",
"""The following morning, you wake up and look around. Denvar has gone, but a piece of paper is lying next to you. You pick it up and read it.""",
"""
	____________________________________
	| I've left to go hunting,         |
	| You may leave whenever you wish. |
	|	Denvar                         |
	|__________________________________|"""])
			action = input_stuff("""1. Write your thanks on the paper.
2. Leave the cabin.
> """, ["1", "2"])
			if action == "1":
				print_stuff("You quickly scribble down your thanks to Denvar for his hospitality, then step outside the cabin.")
			print_stuff(["Today, the sky is overcast, the wind colder and stronger than before. Rain is coming.",
"Wanting to be off the mountain before the rain starts, you make haste up the side of the mountain."])
			break
		else:
			print_stuff(["You walk away from the cabin. It doesn't take you long to realise that night is falling fast. You begin to get desperate.",
"You come across a cave. It seems like it will make a good shelter, so you enter. You hold your sword ready, just in case.",
"However, nothing jumps out at you, and you manage to make camp peacefully.",
"The light of the fire illuminates the stone walls, but is sheltered by the cave's entrance. You see strange carvings on the walls.",
"Though age has worn away most of the carvings, you see depictions of swordsmen and women, large monsters, and huge battles.",
"While looking around, you see a pedestal at the far end of the cave. Runes are carved into the side of it, and it sits flush with the ground.",
"There's a thin hole in the middle that you think you could fit your sword into."])
			choice = input_stuff("""1. Push your sword into the pedestal.
2. Rest straight away.
> """, ["1", "2"])
			if choice == "1":
				boost = colour_it(f"""{weapon.weapon["weaponname"]}'s Sharpness and Finesse increased by 1 and all lost Stability has been restored!""", Color.FUNCTION)
				weapon.weapon["sharpness"] += 1
				weapon.weapon["finesse"] += 1
				weapon.weapon["stability"] = weapon.weapon["max stability"]
				print_stuff(["You slid your sword neatly into the hole, and there's the hiss of steel on stone. Then the runes begin to glow.",
"You feel a surging energy travel up the sword and into the grip. You try to pull away, but cannot.",
"Just as quickly as the sensation starts, it stops. You pull your sword from the hole, and it feels easier the manage.",
"The edge of the blade seems to shine more, and you realise that your sword has been improved and repaired.",
f"""{boost}"""])
			rest.rest()
			print_stuff(["You settle down to sleep, watching the dancing flames of the fire. Then you drift off into blackness.",
"Today, the sky is overcast, the wind colder and stronger than before. Rain is coming.",
"Wanting to be off the mountain before the rain starts, you make haste up the side of the mountain."])


def cave():
	moracka = colour_it("moracka", Color.ENEMY)
	wolves = colour_it("wolves", Color.ENEMY)
	ogre = colour_it("ogre", Color.ENEMY)
	alvyn = colour_it("Alvyn", Color.NPC)
	loot = False
	save("chapter1.cave")
	print_stuff(["After another half hour of trekking, clambering over boulders and glancing at the cloudy sky, you reach your goal.",
"The summit of the mountain is not far away now, but looming before you is a dark cave. Next to the round, stony entrance is a tablet with words on it.",
"You walk over and read the tablet.", """
	____________________________________________
	| A cave of wonders stands ahead           |
	| But heed these words, or you'll be dead  |
	| Left then right then left again          |
	| Stars below will light your way          |
	| Friend is foe and foe is friend          |
	| But if you wish to reach the end         |
	| Turn with time, or yours will cease      |
	| And the reward you seek will be released |
	|__________________________________________|""", """After reading the words carefully, you enter the cave.""",
"From somewhere deep inside the cave, you hear the dripping of water, and what you think may be human footsteps.",
"After less than a minute, you reach a junction. One path leads left, the other leads right."])
	choice = input_stuff("""1. Turn right
2. Turn left.
> """, ["1", "2"])
	if choice == "1":
		print_stuff(["""You take the right turn and walk down it for a while. Suddenly, you realise something's wrong.""",
"The voices and footsteps have gotten quieter, not louder. You take another step, and suddenly you are unable to move.",
"You notice you have walked into a huge spiderweb. Your sword is out of reach, and you know there is no hope of escape.",
"A giant spider could already be on its way to feast. Struggling will not help you. Nothing will."])
		exit()
	print_stuff(["You take the left turn and found yourself walking through a relatively straight tunnel. The air is warmer and the human sounds are getting louder.",
"You continue along the tunnel, and then another junction stands before you."])
	choice = input_stuff("""1. Turn right
2. Turn left.
> """, ["1", "2"])
	if choice == "2":
		ability.ability["health"] -= 3
		print_stuff(["""You take the left path again. Suddenly, the air seems to become denser. You peer ahead and see a pair of glowing yellow eyes.""",
"Suddenly, a monster jumps out at you, cutting you painfully across the arm with its claws. You jump away and draw your sword.",
f"The monster is tall and appears to be a wolf-like bipedal creature. You know it to be a {moracka}.",
f"It has razor sharp teeth, claws, and for its size is extremely fast. The {moracka} bares down on you, teeth bared."])
		enemy_round.initialize([encounters.monster_access("moracka")])
		if post_combat.victory == False:
			print_stuff([f"The {moracka} is a carnivore, and is not picky about what it eats. It will drag you into some dark corner to enjoy its meal undisturbed."])
			exit()
		print_stuff(["You continue along the tunnel, and find yourself at a dead end. However, sitting before you is a skeleton wearing a necklace with a black gem."])
		choice = input_stuff("""1. Try on the necklace.
2. Go back the way you came.
> """, ["1", "2"])
		if choice == "1":
			ability.ability["agility"] -= 1
			print_stuff(["You wrap the necklace around you neck. Suddenly, you feel a strange heaviness in your legs.",
"Your agility has been decreased by 1!",
"Unaware that the effect is due to the necklace, you turn around and go back the way you came."])
		print_stuff(["You go down the right tunnel. Along the way, you come across the corpse of a woman. You frown at her strange garments.",
"She has an exposed cleavage, thigh length leggings and a shirt with sleeves that barely reach her elbows.",
"Her clothes remind you somewhat of Zecherian dancers, but her skin is not sun browned. Lying still clutched in her hand is a curved sword."])
		while True:
			choice = input_stuff("""1. Loot the corpse.
2. Examine her wounds.
3. Step away.
> """, ["1", "2", "3"])
			if choice == "1" and loot == False:
				equipment.equipment["gold"] += 7
				equipment.equipment["potions"] += 1
				print_stuff(["A search of her body yields 7 gold coins and a healing potion."])
				loot = True
			elif choice == "2":
				print_stuff(["You noticed that her ribs have been broken and she has large bruises. She was bludgeoned to death.",
f"Nearby, you notice some large footprints. You realise an {ogre} could be nearby."])
			elif choice == "3":
				break
		print_stuff(["You step away from the woman's remains and continue along the tunnel. You come across yet another junction."])
		choice = input_stuff("""1. Continue straight ahead.
2. Turn left.
> """, ["1", "2"])
		if choice == "1":
			print_stuff(["You continue to walk straight ahead. After a minute of walking, a foul smell hits your nose.",
"You round a bend and come into a large cavern. There you find the source of the stench.",
"A large humanoid creature with baggy, fatty skin, piggy eyes and a flat face lies asleep, scratching its belly in a dream.",
"It smells pungent, and you see a bit of blood on the creature's knuckles. Clearly it has killed recently.",
f"The creature is an {ogre}, no doubt. This cavern is lit by a large bonfire. You see a chest on the other end of the cavern."])
			input_stuff(f"""1. Attempt to sneak in to loot the chest without being detected. (agility roll for sneaking)
2. Attack the {ogre} in its sleep.
3. Go back the way you came.
> """, ["1", "2"])
			if choice == "1":
				agility_roll = random.randrange(1, 101)
				if agility_roll <= (80 + ability.ability["agility"]):
					equipment.equipment["gold"] += 75
					equipment.equipment["knives"] += 3
					equipment.equipment["oils"] += 2
					equipment.equipment["smoke bombs"] += 1
					print_stuff([f"You manage to traverse the floor without waking the {ogre}. You carefully open the chest and peer inside. You gasp with what you see",
f"Many gold coins lie before you, no doubt taken from the corpses of the {ogre}'s victims. Also impressive, but of no use to you, are weapons, armour, bows and arrows.",
"You take the gold coins, and also find three throwing knives, two vials of sword oil, and a smoke bomb. The coins number seventy five.",
"You also come across a scroll detailing sword maneuvers. You glance over it, then pocket it."])
					ability.gain_xp(encounters.xp_handouts["small"])
					print_stuff(["Satisfied, you leave the cavern and take the other route."])
				else:
					print_stuff(["You are not careful enough, and you kick a stone, which clatters across the floor with alarming loudness.",
f"The {ogre} wakes with a roar and looks around, sees you and jumps to its feet. Growling with anger, it charges."])
					enemy_round.initialize([encounters.monster_access("ogre")])
					if post_combat.victory == False:
						print_stuff([f"{ogre.capitalize()}s like to take valuables from the bodies of their victims. Your equipment will soon join that of others."])
						exit()
					equipment.equipment["gold"] += 75
					equipment.equipment["knives"] += 3
					equipment.equipment["oils"] += 2
					equipment.equipment["smoke bombs"] += 1
					print_stuff([f"You step away from the {ogre}'s corpse, and carefully open the chest. You gasp with what you see",
f"Many gold coins lie before you, no doubt taken from the corpses of the {ogre}'s victims. Also impressive, but of no use to you, are weapons, armour, bows and arrows.",
"You take the gold coins, and also find three throwing knives, two vials of sword oil, and a smoke bomb. The coins number seventy five.",
"You also come across a scroll detailing sword maneuvers. You glance over it, then pocket it."])
					ability.gain_xp(encounters.xp_handouts["small"])
					print_stuff(["Satisfied, you leave the cavern and take the other route."])
			elif choice == "2":
				print_stuff([f"You rush forwards and slash the {ogre} as it sleeps. Though it doesn't die, it roars with a howl of pain.",
"Growling with anger, it turns to face you. It springs to its feet and rushes forwards, hands outstretched, teeth bared."])
				enemy_round.initialize([encounters.monster_access("injured ogre")])
				if post_combat.victory == False:
					print_stuff([f"{ogre.capitalize()}s like to take valuables from the bodies of their victims. Your equipment will soon join that of others."])
					exit()
				equipment.equipment["gold"] += 75
				equipment.equipment["knives"] += 3
				equipment.equipment["oils"] += 2
				equipment.equipment["smoke bombs"] += 1
				print_stuff([f"You step away from the {ogre}'s corpse, and carefully open the chest. You gasp with what you see",
f"Many gold coins lie before you, no doubt taken from the corpses of the {ogre}'s victims. Also impressive, but of no use to you, are weapons, armour, bows and arrows.",
"You take the gold coins, and also find three throwing knives, two vials of sword oil, and a smoke bomb. The coins number seventy five.",
"You also come across a scroll detailing sword maneuvers. You glance over it, then pocket it."])
				ability.gain_xp(encounters.xp_handouts["small"])
				print_stuff(["Satisfied, you leave the cavern and take the other route."])
		print_stuff(["You take the left path, and you follow it without incident. Suddenly, the tunnel gets darker.",
"Ahead, you see a glowing blue light. You continue on for a bit and see that the tunnel leads in four directions.",
"Each path has a different floor. You cannot see far down an individual path. The blue light comes from one of the tunnels, which is full of glowing blue mushrooms."])
		while True:
			path = input_stuff("""1. Go down the path carpeted by red fungus.
2. Go down the path with a flickering crystal floor.
3. Go down the path bordered by glowing blue mushrooms.
4. Go down the path full of fire flies.
> """, ["1", "2", "3", "4"])
			if path == "1":
				print_stuff(["You walk down the path for a while, the red fungus squelching under your boots. Then you reach a dead end.",
	"At the end of the tunnel lies a man's corpse. Red fungus is sprouting from his mouth, nose, ears and the corners of his eyes."])
				choice = input_stuff("""1. Loot the corpse.
2. Go back.
> """, ["1", "2"])
				if choice == "1":
					print_stuff(["You lower yourself down to search the body. As you do, your hand brushes some of the fungus.",
"Suddenly, it feels as if your hand is on fire. You jump to your feet, and before your eyes you see red fungus start sprouting from you hand."])
					choice = input_stuff("""1. Try to burn the fungus of.
2. Scrape the fungus off with your knife.
> """, ["1", "2"])
					if choice == "1":
						print_stuff(["You quickly light a torch and hold your hand over the flame. With horror, you see the fungus begin to spread up your arm.",
"But the fire seems to do the trick. Though it's agony to hold your hand over the open flame, the fungus begins to wither and die, dropping off like dried mud.",
"Not wishing to stay in the cave any longer, you turn back."])
					else:
						print_stuff(["You scrape the fungus off with your sword, but new fungus sprouts up. With horror, you see the fungus begin to spread up your arm.",
"Then the fungus spreads into your torso, and you feel spasms of agony wrench your body back and forth. You are grateful when you black out, never you wake up again."])
						exit()
			elif path == "2":
				break
			elif path == "3":
				print_stuff(["You walk down the cave full of blue mushrooms. The air here is cooler than anywhere else in the cave system. The silence is palpable.",
"The cave ends suddenly, and grave lies at the end. You peer at the grave, but it is in a strange language you don't understand.",
f"You find nothing of interest, and turn to leave. But you find yourself cut off by a group of three {wolves}. Clearly you have trespassed on their territory.",
"They snarl at you and lunge forwards, teeth bared. You jump aside at the last second, drawing your sword."])
				enemies = [encounters.monster_access("wolf"), encounters.monster_access("wolf"), encounters.monster_access("wolf")]
				enemy_round.initialize(enemies)
				if post_combat.victory == False:
					print_stuff([f"These {wolves} live deep in a cave don't get much food. They are grateful for your entrance."])
					exit()
				print_stuff(["Panting for breath after the fight, you walk back the way you came."])
			elif path == "4":
				print_stuff(["You walk into the cave full of fireflies. The orange pinpoints of light part as you walk forwards, making way for you.",
"As you walk down the cave, you see it expands into a large underground lake with a soaring ceiling. More surprising, you see a man hunched over a campfire."])
				choice = input_stuff("""1. Approach the man.
2. Jump in the lake.
3. Go back the way to you came.
> """, ["1", "2", "3"])
				while True:
					if choice == "1":
						print_stuff(["""You approach the man and he turns to face you. "Greetings!" he says merrily. "Take a seat." """,
	"""You sit down and he grins toothily at you. "I don't get many visitors here," he says. "Please, stay a while and rest." """])
					elif choice == "2":
						print_stuff(["You jump in the lake. It is deeper than you thought, and the black waters swirl up to your neck.",
	"You hear a shout and turn. The man is running towards you, shouting and waving his hands. Suddenly, you feel something slimy wrap around your ankle."])
						agility_roll = random.randrange(1, 9)
						if agility_roll <= ability.ability["agility"]:
							print_stuff(["Twist out of the grasping thing and roll onto shore. The man grabs your wrists and hauls you onto dry land, grunting with the effort."])
						else:
							print_stuff(["You are unable to escape the grip and you feel yourself being dragged under. Your head disappears under the black waters, never to emerge again."])
							exit()
						print_stuff([""""You ploughing idiot!" the man growls. "What were you thinking jumping in the lake? Eels swim there." """])
						reply = input_stuff("""1. "Thank you."
2. "Eels?" 
3. "I'm not in the mood to be lectured." 
> """, ["1", "2", "3"])
						if reply == "1":
							print_stuff([""""Your welcome, just don't do anything like that again." """])
						elif reply == "2":
							print_stuff(["""The man waves his hand. "Something like that," he says. "Not many who get grabbed by them live to tell the tale." """])
						elif reply == "3":
							print_stuff([f""""I saved your arse, {character.character['titles']['casual']}," the man grumbles. "A little gratitude would be appreciated." """])
						print_stuff(["The man grasps your arm and pulls you over to his campfire. He none too gently drags you to sit beside him."])
					else:
						break
					print_stuff(["The man pours a cup of some sort of herbal tea into a cup and hands it to you. You take a sip and it tastes good enough.",
f""""I'm {alvyn}. I come into this cave for peace and quiet. Who are you?" """])
					reply = input_stuff(f"""1. "They call me {character.character["firstname"]}."
2. "I don't share my name with strangers." 
> """, ["1", "2"])
					if reply == "1":
						print_stuff([f""""So, {character.character["firstname"]}, bless me with conversation." """])
					if reply == "2":
						print_stuff([""""A paranoid loner, eh? Well, keep your secrets. But do bless me with some conversation." """])
					while True:
						question = input_stuff("""1. "Who are you?" 
2. "Have you seen a man and a woman pass through here, about sixteen years old?" 
3. "How did you manage to get through the monsters?"
4. "What do you like about this cave?"
5. "I think I'll leave now. Thank you for the tea." 
> """, ["1", "2", "3", "4", "5"])
						if question == "1":
							print_stuff([f"""{alvyn} grins. "I'm simply a man who likes nature more than towns. In society I'm poor, but in spirit..." """,
f"""{alvyn} trails off. "I'm happy. I love the world, and the natural beauty of caves. Spelunking is a hobby of mine." """,
""""This place I love escpecially. The calm waters, the blue mushrooms. And the micro-crystals..." He gets up and brings a lantern to bare. """,
""])
						elif question == "2":
							print_stuff([f"""{alvyn} frowns. "Yes, they came through. Stopped by my fire just as you are doing. They said they were treasure hunting." """,
""""I haven't seen them since. It was a while ago I met them. Why do you ask?" """])
							reply = input_stuff("""1. "I've been tasked to look for them." 
2. "That's my private business." 
> """, ["1", "2"])
							if reply == "1":
								print_stuff([""""Mhm. Well I can't help you more than I already have." """])
							if reply == "2":
								print_stuff([""""Alright. I won't pry, in that case." """])
						elif question == "3":
							print_stuff([""])
						elif question == "4":
							print_stuff([""])
						elif question == "5":
							print_stuff([""])



