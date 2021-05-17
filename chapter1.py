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
from functions.loading import save


def ghouls_at_farm():
	save("chapter1.ghouls_at_farm")
	print_stuff(["You make your way outside of Blackburrow. It is late morning, and the sky is a cobalt blue.",
"Birds sing, and the long grass sways in the breeze. The air is cool, but not cold, and fluffy white clouds float in the sky.",
"You steer off the main road and onto a dirt track leading to the Lizardtongue Mountains. About an hour into the journey you come across a farm.",
"Wheat stalks stand golden against the pale grass. You decide to cut through the wheat field, rather than take a detour around it.",
"That's when you hear shouting and cursing. You begin to run, and see a man standing in the front door of his house. He is swinging a pitchfork to and fro.",
"Standing before him are four ghouls; pale, lanky, short and hairless humanoids that feed on rotting flesh. Two other ghouls lie dead and bleeding.",
"The man sees you and screams for help. You see a little girl and a teenage boy standing behind the man, expressions of terror on their faces.",
"You know that the man will not be able to hold the ghouls back forever."])

	choice = input_stuff("""1. Help the farmer.
2. Continue on your way.
> """, ['1', "2"])
	if choice == "1":
		print_stuff([f"You rush forwards, {weapon.weapon['weaponname']} in hand. The ghouls turn to face you now, but one of them continues to focus on the farmer",
"One of the ghouls lunges forward suddenly, and you ready your sword."])
		enemies = [encounters.monster_access("ghoul"), encounters.monster_access("ghoul"), encounters.monster_access("ghoul")]
		gang = enemies
		enemy_round.initialize(gang)
		if post_combat.victory == False:
			print("There is no one to save you. The farmer cannot hold the ghouls back for much longer, and the ghouls will show no mercy to those in the way of their food.")
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
	save("chapter1.hag_lair")
	treasure = 0
	print_stuff(['You continue along the trail, and you pass by a few more farms, and sometimes the people maintaining them, nodding in greeting as you pass.',
'''Finally, the track becomes wilder, the farms become less, before disappearing altogether. Small pockets of trees and undergrowth now dot the countryside.''',
'It is late in the afternoon when the trail splits suddenly. It is clear which path will lead to the mountains. The other pass leads into a small forest.'])
	choice = input_stuff("""1. Explore the forest trail.
2. Take the path to the Lizardtongue Mountains
> """, ['1', "2"])
	if choice == "1":
		print_stuff(['You walk down the forest path. Light from the afternoon sun slants through the thin canopy of leaves, and small critters rustle in the leaflitter.',
'After following the trail for about ten minutes, it ends in a small log cabin. No lights shine through the glass windows, but you can detect some movement from inside.',])
		choice = input_stuff("""1. "Is anyone home?!"
2. Try to open the door.
3. Turn back and head for the Lizardtongue Mountains.
> """, ['1', "2", "3"])
		if choice == "1":
			print_stuff(["You see the movement stop for a moment, then a creature comes hurtling out the door.",
'''"Dinsers!" the creature shrieks with glee. "Dinsers has comses!" The creature is a bone hag.''',
"""It takes on the form of an elderly woman with grey skin that hangs and droops in strange folds, dull black hair and dressed in nothing but a loincloth. 
They have sharp claws on their fingers and toes.""",
f"You also know that hags enjoy to the taste of living flesh, especially that of young people or elves. You draw {weapon.weapon['weaponname']} and ready yourself."])
		elif choice == "2":
			print_stuff(["You move to the door and twist the doorknob. The door swings open, and immediately the smell of rot assaults your nose.",
"Almost everything here is broken or decayed. Only two things seem solid here; a cauldron of meat soup, and a hunched form. The form turns to see, and grins toothily.",
'''"Dinsers!" the creature shrieks with glee. "Dinsers has comses!" The creature is a bone hag.''',
"""It takes on the form of an elderly woman with grey skin that hangs and droops in strange folds, dull black hair and dressed in nothing but a loincloth. 
It has sharp claws on their fingers and toes.""",
"""You also know that hags enjoy to the taste of living flesh. Before you can react, the hag lunges forwards, crashing into you. 
The two of you tumble outside of the cabin and into the forest. You roll to your feet and draw your sword, and the hag rises to its feet, snarling."""])
		else:
			print_stuff(['Deciding not to disturb the inhabitants - whoever they may be - you trace your steps back to the junction in the trail.'])
			return False
		enemy_round.initialize([encounters.monster_access("bone_hag")])
		if post_combat.victory == False:
			print("No one knows you came here, and no one can save you now. Unfortunately, you'll probably end up in the hag's cooking pot.")
			exit()
		print_stuff(["With the bone hag dead, you enter the cabin. You look around, and you see a worn chest, the cauldron of meat soup, a table with papers on it, and a pile of bones."])
		character.story["hag_lair"] = True
		while True:
			investigate = input_stuff("""1. Search the chest.
2. Investigate the cauldron.
3. Check the papers
4. Examine the bones.
5. Leave
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
				treasure += 1
				print_stuff(["""You pick up a piece of paper and read.
	____________________________________________________
		My dearest Chana,
	If I am to die prematurely, you must lift the chest 
	and take the belongings below it. That should be
	enough to keep you alive, and perhaps flourish.
		Denvar
	____________________________________________________"""])
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
>""", ['1', "2"])
						if ring == "1":
							ability.ability["strength"] += 1
							print_stuff(["You feel a tingling sensation as you slip the ring on, and a sudden burst of power.",
"Your Strength has been increased by 1!"])
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
	print_stuff(["You turn onto the path to the Lizardtongue Mountains, and continue your trek."])


def campers():
	save("chapter1.campers")
	man_name = "the large man"
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
""""I do not believe we have been properly introduced," the lean man says kindly. He lays a hand on his chest. "I'm Eladris. And you are?"
"""])
			reply = input_stuff(f"""1. "I'm {character.character["firstname"]}."
2. "I'd rather not tell you."
> """, ['1', "2"])
			if reply == "1":
				print_stuff([f""""{character.character['firstname']}," Eladris says, testing your name on his tongue."""])
			else:
				print_stuff(["""Eladris laughs. "Keep your secrets then," he chuckles. "But you should learn to be more trusting." """])
			print_stuff([""""So what brings you here? Monsters are roaming the countryside in even greater numbers these days." """])
			reply = input_stuff(f"""1. "I'm looking for some missing people."
2. "I do not fear monsters. It is the other way around." 
> """, ['1', "2"])
			if reply == "1":
				print_stuff([f""""I see," Eladris says. "I will not pry, though my curiosity demands me to do so." """])
			else:
				print_stuff([""""You're a confident one," Eladris says. "Be wary it doesn't become hubris." """])
			while True:
				question = input_stuff(f"""1. "So... what's a half-elf doing out here?"
2. "Who's your cheerful friend?" 
3. "You said monsters were increasing in numbers..."
4. "I'm going to get some sleep." 
> """, ['1', "2", '3', '4'])
				if question == "1":
					print_stuff(["""Eladris grins at you. "You noticed?" he says. "Was it the name, or my appearance?" """,
"""He shrugs. "Honestly, it's reason enough to escape the racists. But you are a 'doyana', so you wouldn't understand." """,
""""Travelling has always calmed my nerves. I do it for the simple purpose of enjoyment." """])
					continue
				elif question == "2":
					print_stuff([""""And good looking too!" he adds, chuckling to himself. "His name is Garurt. Don't mind him; a more distrustful man was never born." """,
""""I keep him around because he's a good fighter. My escort, so to speak." """])
					man_name = "Garurt"
					continue
				elif question == "3":
					print_stuff([""""So I did," he sighs. "There's talk of magical fluctions, and that's what attracting them." """,
""""The source of the disturbances remains unknown, but I'm sure someone will figure it out eventually." """,
""""They are merely rumours, of course," Eladris adds quickly. "But rumours can be built on truth." """])
					continue
				else:
					print_stuff([f"""Eladris nods. "Sweet dreams," he says. Just as you are beginning to pull out your blankets, {man_name} returns from his walk.""",
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
f"""Once you return, you notice that both Eladris and {man_name} are speaking to each other."""])
			if ability.ability['awareness'] > 5:
				print_stuff(["You able to hear what they are saying.",
f""""I say we kill {character.character["titles"]['him']}, grab the loot and run," {man_name} says. """,
f""""Not this one," Eladris says. "I've talked with {character.character["titles"]['him']}, and {character.character["titles"]['he']}'s a kind person. {character.character["titles"]['he'].capitalize()} doesn't deserve that." """,
""""It's not about what they deserve. It's about what we need!" """])
			else:
				print_stuff(["You are unable to hear what they are saying. You move closer to try and listen."])
				agility_roll = random.randrange(1,101)
				if agility_roll <= (75 + ability.ability['agility']):
					print_stuff(["You enter earshot of them without being noticed.",
f""""I say we kill {character.character["titles"]['him']}, grab the loot and run," {man_name} says. """,
f""""Not this one," Eladris says. "I've talked with {character.character["titles"]['him']}, and {character.character["titles"]['he']}'s a kind person. {character.character["titles"]['he'].capitalize()} doesn't deserve that." """,
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
					print_stuff(["You wake up, bruised and scratched. You look around and realise that you are in the remains of the campsight.",
"You also realise that almost all your belongings are gone. Your sword, your food, and your items remain. However, you money and knives are gone.",
"You pick yourself up and gather your equipment. It is day time, and despite being knocked unconscious, you feel slightly refreshed.",
"You continue on your journey, despite the sour defeat."])
					equipment.equipment['gold'] = 0
					equipment.equipment['knives'] = 0
					return False
				else:
					print_stuff([f"""You stand over {man_name}'s corpse. You stop when you here the sound of clapping.""",
""""That was quite a show you put on," Eladris says. "Where did you learn that?" """])
					reply = input_stuff("""1. "Don't look so cocky. You're next."
2. "Why did he attack me?" 
> """, ['1', "2"])
					if reply == "1":
						print_stuff(["""At this, Eladris chuckles. "Kill me then. I do not fear death. At least let me explain." """])
				print_stuff([f""""Please forgive Garurt," Eladris says cooly, not a hint of worry in his voice. "We were just discussing robbing you when you burst in." """,
""""We're bandits. We were thrown out of society because of my half-blood status and his friendship with me. We've had to live robbing and hiding for many years.""",
"""Eladris looks up at you. "Kill me if you will," he says. "My existence can only get sadder." """])
				action = input_stuff("""1. Kill Eladris
2. Walk away.
> """, ['1', "2"])
				if action == "1":
					print_stuff(["""You step forward, sword in hand. Eladris closes his eyes, and you impale his heart. His death is painless, and he doesn't even flinch.""",
"""You search Eladris' bags and come away with 27 gold coins, a healing potion, and two throwing knives."""])
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
	save("chapter1.thief")
	equipment.equipment["gold"] -= 15
	if equipment.equipment["gold"] < 0:
		equipment.equipment["gold"] = 0
	print_stuff(["You wake up the following morning. You sling on your backpack and strap on your belt.",
"It is then that you realise that some of your gold has vanished.",
"You look around to see if you dropped it. Quickly, you notice something else. Footprints."])
	direction = input_stuff("""1. Follow the footprints.
2. Accept the loss and continue to the Lizardtongue mountains.
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
"Two pointy ears like those of a wolf adorn each head, as well as a long snout. You recognise the monsters as lalikins."
"The lalikins turn to you and growl, showing off white, pointy teeth. They flex their claws and begin to approach you.",
f"You hold {weapon.weapon['weaponname']} at the ready, and the lalikins charge."])
			enemy_round.initialize([encounters.monster_access("lalikin"), encounters.monster_access("lalikin")])
			if post_combat.victory == False:
				print_stuff(["The lalikins were already feeding on the woman. They will not complain about extra food."])
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
	print_stuff(["You continue along the trail to the Lizardtongue Mountains, wondering when you'll get a day of piece and quiet."])

def ascent():
	save("chapter1.ascent")
	print_stuff(["It's the middle of the day when you finally reach the base of the Lizardtongue Mountains.",
"As you climb the largest mountain, the terrain gets steeper and rockier. Many times you stumble on loose gravel.",
"The wind becomes stronger as you climb, and the air becomes cooler. You know the cave that is your objective is close to the summit.",
"Finally, after an hour of scrambling over boulders, you have had enough. You throw down your pack and take out some of your supplies.",
"Your intention is to take a quick rest before continuing."])
	rest.rest()
	print_stuff(["As your making your way up the mountain, your foot finds a patch of loose gravel. You feet the ground slide out from under you.",
"Desperately, you try to jump to safety."])
	agility_roll = random.randrange(1,9)
	if agility_roll <= ability.ability["agility"]:
		print_stuff(["You fall, but hit the ground in a roll. You are agile enough to roll to you feet and avoid the tunbling gravel."])
	else:
		print_stuff(["You slip and fall. You try to roll back to your feet, but you are not agile enough.",
"You tumble down the side of the mountain, but somehow avoid serious harm. Suddenly, you find yourself lying on the ground.",
"Dazed, you rise to your feet. You look around, and that's when you see it; a hulking mass of rock approaching you.",
"The creature appears to be a large, bald humanoid, ten feet tall at least. It is made completely of boulders at least the size of your head."
"Every step it takes send vibrations in the ground. You know this monster to be a crag.",
"A beast of animated rock, a crag will attack all living creatures it encounters.", "Sword in hand you run forwards.",
"The crag swings at you, but you drop and slid between it's legs. The crag's fist hits the ground, blasting rocks to pieces.",
"You realise that the creature may be slow, but if you get hit, your situation will be grave indeed."])
		enemy_round.initialize([encounters.monster_access("crag")])
		if post_combat.victory == False:
			print_stuff(["The crag cares nothing for food, but it does enjoy killing. Unconscious, you do not see the crag raise it's mighty fists."])
			exit()
		print_stuff(["Panting for breath, you watch the crag's body crumble into a pile of boulders and dust.",
"You continue your climb, and soon reach the place where you fell, careful not to step in any more gravel patches."])
	print_stuff(["You continue to climb up the mountain, the final remains of sleepiness gone from you, due to the intense events.",
"Once more, you find yourself out of breath and in need of rest. You turn and look out over the nearby countryside.",
"The view is spectacular. Everything is tiny, as if you were staring at an embroided tapestry. Blackburrow is a dark cluster in the distance.",
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
""""Before you answer, allow me to introduce myself. I'm Denvar. Who are you?" """])
			input_stuff()
