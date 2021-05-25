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

descent = "chapter2.descenta"


def beginning():
	save('chapter2.beginning')
	elfa = colour_it("Elfa", Color.NPC)
	micha = colour_it("Micha", Color.NPC)
	print_stuff(["You wake up, your head throbbing painfully. You hear voices, but they are echoing and far away. You look around and find yourself sitting in a large cage.",
"The cage itself is made of wood, but all your belongings are gone. The wooden cage's bars and supports are thick, and you cannot break them.",
"To your left is a man and a woman. Each looks only sixteen, and each is covered in blood. It only takes you a moment to realise two things.",
f"These must be {micha} and {elfa}, the baron's children. You also realise that {elfa} is dead. {micha} looks like he's on his last legs also."])
	choice = input_stuff(f"""1. Approach {micha}.
2. Wait. 
> """, ["1", "2"])
	if choice == "1":
		print_stuff([f"You approach {micha} and sit down next to him. He turns to you, and you see his eyes are red and puffy from tears.",
""""What do you want?" he asks, almsot a bit angrily. """])
		reply = input_stuff("""1. "We're in a bit of a sticky situation, aren't we?"
2. "Are you Micha?" 
> """ , ["1", "2"])
		if reply == "1":
			print_stuff([f"""{micha} smiles slightly. "We are indeed," he says with cold humour."""])
		elif reply == "2":
			print_stuff([f""""I am. Have you been sent to look for me?" {micha} sighs. "Then this is my fault, {character.character['titles']['casual']}." """])
		print_stuff([f"""{micha} looks over to {elfa}'s body, and sighs sadly. "If you came here for us..." he starts, then swallows and turns away."""])
		while True:
			quest = colour_it(""""Don't worry; we'll get through this." """, Color.QUEST)
			question = input_stuff(f"""1. "Who are these people?"
2. "What are you doing on the mountain?"
3. "What's the escape plan?"
4. {quest}
> """, ["1", "2", "3", "4"])
			if question == "1":
				print_stuff([f"""{micha} shakes his head. "I don't have a clue," he says. "{elfa} and I were treasure hunting." """,
""""Found this cavern, but soon after us, these women came. They took us prisoner and began to search the place, gathering all the treasures they found." """,
f""""I asked them who they were and why they were here, but got no response. {elfa} insisted that they talked to her and..." He breaks of suddenly and swallows. """])
			elif question == "2":
				print_stuff([""""Treasure hunting, as father no doubt told you. There were tales of treasure, but all it has brought me is misery." """])
			elif question == "3":
				print_stuff([f""""There is none. I've tried many things, but nothing has yielded anything resembling success." {micha} sighs sadly.""",
f""""{elfa} would have figured something out," he murmurs. He turns his head away."""])
				choice = input_stuff("""1. "I'm sorry for your loss." 
2. "Toughen up. There's nothing you can do for her."
3. Say nothing. 
> """, ["1", "2", "3"])
				if choice == "1":
					print_stuff([f"""{micha} nods. "I'm sorry too. I shouldn't let my grief dampen both of our spirits." """])
				elif choice == "2":
					print_stuff([f"""{micha} glares at you. "If you had any loved ones to lose, you wouldn't be saying that," he snaps. """])
			elif question == "4":
				print_stuff([f"""{micha} smiles weakly and closes his eyes. "I trust you, whoever you are," he says softly. Suddenly, he gives a start and looks over your shoulder. """])
				break
	print_stuff(["One of the women approach you know. But there is something different about this one."])
	awareness_roll = random.randrange(1, 7)
	if awareness_roll <= ability.ability["awareness"]:
		print_stuff([f"You are {colour_it('aware', Color.AWARENESS)} enough to notice that her eyes are darting, and she looks nervous."])
	else:
		print_stuff([f"You are not {colour_it('aware', Color.AWARENESS)} enough to figure out the discrepancy."])
	print_stuff(["The woman approaches the locked door, and pulls a key from the leg of her tights. Looking around cautiously, she begins to unlock the cage.",
f"At this, {micha} moves forwards and opens his mouth to speak, but the woman pushes a finger to her lips. Slowly, the cage door opens.",
f"She pulls two backpacks from behind a rock, one of them you recognise as yours. She tosses it to you, and throws the other to {micha}.",
f""""We must leave this place," she says quietly. "Swiftly now!" """])
	choice = input_stuff("""1. Follow the woman.
2. Stay where you are.
> """, ["1", "2"])
	if choice == "2":
		print_stuff([f"You stay put as {micha} and the woman run silently from the cavern. It is not long before some of the strangely dressed women find you.",
"Furious at your escape, they attack without mercy. You are beaten down by a barrage of blows, with far too many opponents and no time to react."])
		exit()
	print_stuff([f"You run silently beside {micha} and behind the woman. She leads you through the cavern, mirroring the route you took. Within minutes, you are under the open sky.",
f""""We must get off the mountain," says the woman rapidly. She looks between both you and {micha}. "Do either of you have a quick way of descending?" """
f"""{micha} shakes his head, and the woman turns to you."""])
	while True:
		if character.story["denvar"]["exists"]:
			choice = input_stuff("""1. "Unfortunately not." 
2. "Slow down. Who are you?"
3. "No, but I know a man named Denvar who may help us." 
> """, ["1", "2", "3"])
		else:
			choice = input_stuff("""1. "Unfortunately not." 
2. "Slow down. Who are you?" 
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} curses under her breath. "Then we must move quickly. They could be onto us at any moment." """])
			break
		elif choice == "2":
			tamara = colour_it("Tamara", Color.NPC)
			print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} gives an impatient groan. "I'm {tamara}, if you insist," she says finally. """])
			character.story["tamara"]["name_known"] = colour_it("Tamara", Color.NPC)
		elif choice == "3":
			print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} lifts an eyebrow. "Then let us meet this Denvar." """])
			descent = "chapter2.descentb"
			break


def descenta():
	micha = colour_it("Micha", Color.NPC)
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} nods. "At least let us begone from this mountain," she says. "Even if the journey is long and hard." """,
"""The three of you descend the mountain, haste making the journey a lot quicker. You meet with no dangers on the way down, and no one speaks.""",
f"""As you put distance between yourselves and the cave, you see {character.story['tamara']['name_known']}'s face begin to relax.""",
"""Suddenly, you've reached the base of the mountain. Already the air is warmed, and you feel far more relaxed, though questions still swim in your mind.""",
f""""I'm going back to {blackburrow}," {micha} says. "To get some rest." He looks to both you and {character.story['tamara']['name_known']}. "Thank you. Both of you." """,
f"""{micha} begins walking back towards {blackburrow}. {character.story['tamara']['name_known'].capitalize()} watches {micha} disappear along the trail. Then she turns to you."""])
	if character.story["tamara"]["name_known"] != colour_it("Tamara", Color.NPC):
		tamara = colour_it("Tamara", Color.NPC)
		print_stuff([f""""I should probably introduce myself," she says. "I'm {tamara}." """])
	print_stuff([""""Do you have any questions for me?" """])
	while True:
		quest = colour_it("I have no further questions.", Color.QUEST)
		question = input_stuff(f"""1. "Who were those people?" 
2. "Why did you save me?" 
3. "Who are you?"
4. "{quest}" 
> """, ["1", "2", "3", "4"])
		if question == "1":
			print_stuff([""])
		elif question == "2":
			print_stuff([""])
		elif question == "3":
			print_stuff([""])
		elif question == "4":
			break

def descentb():
	print_stuff([""])
