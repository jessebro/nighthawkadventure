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
	print_stuff(["One of the women approach you now. But there is something different about this one."])
	awareness_roll = random.randrange(1, 7)
	if awareness_roll <= ability.ability["awareness"]:
		print_stuff([f"You are {colour_it('aware', Color.AWARENESS)} enough to notice that her eyes are darting, and she looks nervous."])
	else:
		print_stuff([f"You are not {colour_it('aware', Color.AWARENESS)} enough to figure out the discrepancy."])
	print_stuff(["The woman has mousy brown hair tied in a ponytail, and round, blue eyes. She, too, has a curved sword.",
"The woman approaches the locked door, and pulls a key from the leg of her tights. Looking around cautiously, she begins to unlock the cage.",
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
			character.story["tamara"]["name_known"] = tamara
		elif choice == "3":
			print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} lifts an eyebrow. "Then let us meet this Denvar." """])
			descent = "chapter2.descentb"
			break


def descenta():
	micha = colour_it("Micha", Color.NPC)
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	tamara = colour_it("Tamara", Color.NPC)
	print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} nods. "At least let us begone from this mountain," she says. "Even if the journey is long and hard." """,
"""The three of you descend the mountain, haste making the journey a lot quicker. You meet with no dangers on the way down, and no one speaks.""",
f"""As you put distance between yourselves and the cave, you see {character.story['tamara']['name_known']}'s face begin to relax.""",
"""Suddenly, you've reached the base of the mountain. Already the air is warmed, and you feel far more relaxed, though questions still swim in your mind.""",
f""""I'm going back to {blackburrow}," {micha} says. "To get some rest." He looks to both you and {character.story['tamara']['name_known']}. "Thank you. Both of you." """,
f"""{micha} begins walking back towards {blackburrow}. {character.story['tamara']['name_known'].capitalize()} watches {micha} disappear along the trail. Then she turns to you."""])
	if character.story["tamara"]["name_known"] != colour_it("Tamara", Color.NPC):
		print_stuff([f""""I should probably introduce myself," she says. "I'm {tamara}." """])
	print_stuff(["What's your name?"])
	choice = input_stuff(f"""1. "I'm {character.character['firstname']}." 
2. "I'm not sure I trust you." 
> """, ["1", "2"])
	if choice == "2":
		print_stuff([f"""{tamara} raises an eyebrow. "I can't trust you unless you trust me with your name," she warns. Reluctantly, you tell her your name."""])
	print_stuff([f""""I'm glad you told me... {character.character['firstname']}," {tamara} says kindly. "Do you have any questions for me?" """])
	while True:
		quest = colour_it("I have no further questions.", Color.QUEST)
		daughters = colour_it("Daughters of Chaos", Color.ENEMY)
		question = input_stuff(f"""1. "Who were those people?" 
2. "Why did you save me?" 
3. "Who are you?"
4. "You're dressed as those women are. Yet you oppose them?"
5. "{quest}" 
> """, ["1", "2", "3", "4", "5"])
		if question == "1":
			print_stuff([f""""They're called the {daughters}," {tamara} says. "An organisation that wants humanity to return to the old ways of hunting and gathering." """,
""""They are not evil. They are... misguided. And at the moment their leader is more fanatical and insane than any other before them." """])
		elif question == "2":
			print_stuff([f"""{tamara} shrugs. "I figured you could help me. I've been following the {daughters} for a while. I stumbled upon you, and..." Tamara pauses awkwardly. """,
""""I figured you could help me. You look like the fighting sort, so you're exactly what I need." """])
		elif question == "3":
			print_stuff([f""""I've already given you my name," {tamara} says. "I assume your asking what I do in life?" """,
f""""I have a complicated past, but let's just say I have something personal against the {daughters}." """])
		elif question == "4":
			print_stuff([f""""I have their clothes, but I do not follow them. As soon as I have some privacy, I shall change from these garments." """,
f"""{tamara} laughs. "They were too... exposing for me anyway." """])
			awareness_roll = random.randrange(1,10)
			if awareness_roll <= ability.ability["awareness"]:
				aware = colour_it("aware", Color.AWARENESS)
				print_stuff([f"You are {aware} enough to notice her use of past tense."])
				choice = input_stuff("""1. "Why do you use past tense?" 
2. Say nothing.
> """, ["1", "2"])
				if choice == "1":
					print_stuff([f"""You see {tamara} give a start. "No reason," she says quickly. "Or at least, a reason that I do not wish to reveal currently." """])
		elif question == "5":
			break
	print_stuff([f"Suddenly, {tamara} looks over your shoulder and draws her sword. You turn around and see two {daughters} walking towards you.",
f""""I'll take one," {tamara} says quickly. The {daughters} run forwards, swords in hand. {tamara} lunges towards one of them."""])
	enemy_round.initialize([encounters.monster_access("chaos_daughter")])
	if ability.ability['health'] <= 0:
		ability.ability["health"] = (ability.ability["maxhealth"] / 2)
		print_stuff([f"The light returns to your vision and you see {tamara}'s face looking down at you",
""""That was quite a hit you took," she says cheekily. She offers her hand to you to help you up.s"""])
		choice = input_stuff("""1. Take her hand.
2. Get up by yourself.
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f"""You take {tamara}'s hand, and she pulls you to your feet, with surprising strength for someone of her build."""])
		elif choice == "2":
			print_stuff([f"You get to your feet without taking {tamara}'s hand. She gives you a look but says nothing."])
		print_stuff([f"""You look around and see the bodies of the two {daughters} with deep lacerations on them. "My handiwork," {tamara} says. """,
  """"Don't worry though. I forgive you." But you can tell she's joking. """,
f""""We should return to {blackburrow}," {tamara} says. "There is much to discuss." """,
f"""You descend the mountain carefully, returning to the trail and making your way back to {blackburrow}."""])


def descentb():
	micha = colour_it("Micha", Color.NPC)
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	tamara = colour_it("Tamara", Color.NPC)
	denvar = colour_it("Denvar", Color.NPC)
	print_stuff([f"The three of you make your way down the mountain. With your guidance you arrive at {denvar}'s cabin. You notice that {denvar} is home.",
f"Light shines from the windows, and you see movement from inside. You approach the door and knock sharply. Almost instantly, {denvar} answers the knock."])
	if character.story["denvar"]["knows_name"]:
		print_stuff([f""""Greetings, {character.character["firstname"]}," {denvar} says warmly. "How may I help you?" """])
	else:
		print_stuff([f""""Greetings, traveller," {denvar} says warmly. "How may I help you?" """])
	ability.heal(15)
	print_stuff([f"Quickly, you usher {tamara} inside, but {micha} is shaking his head.",
f""""I'm shall return to {blackburrow}," he says. "I've had enough madness for one day." After a brief farewell, {micha} leaves alone, descending the mountain. """,
f"The next thing you know, you and {tamara} are sitting at a table with bowls of steaming meat stew. {denvar} crouches by the fireplace, coaxing a small blaze.",
f"The stew restores 15 health!",
f"""{tamara} looks up at you."""])
	if character.story["tamara"]["name_known"] != tamara:
		print_stuff([f""""I should probably introduce myself," she says. "I'm {tamara}." """])
	print_stuff([f"What's your name, {character.character['titles']['casual']}?"])
	choice = input_stuff(f"""1. "I'm {character.character['firstname']}." 
2. "I'm not sure I trust you." 
> """, ["1", "2"])
	if choice == "2":
		print_stuff([f"""{tamara} raises an eyebrow. "I can't trust you unless you trust me with your name," she warns. Reluctantly, you tell her your name."""])
	print_stuff([f""""I'm glad you told me... {character.character['firstname']}," {tamara} says kindly. "Do you have any questions for me?" """])
	while True:
		quest = colour_it("I have no further questions.", Color.QUEST)
		daughters = colour_it("Daughters of Chaos", Color.ENEMY)
		question = input_stuff(f"""1. "Who were those people?" 
2. "Why did you save me?" 
3. "Who are you?"
4. "You're dressed as those women are. Yet you oppose them?"
5. "{quest}" 
> """, ["1", "2", "3", "4", "5"])
		if question == "1":
			print_stuff([f""""They're called the {daughters}," {tamara} says. "An organisation that wants humanity to return to the old ways of hunting and gathering." """,
""""They are not evil. They are... misguided. And at the moment their leader is more fanatical and insane than any other before them." """])
		elif question == "2":
			print_stuff([f"""{tamara} shrugs. "I figured you could help me. I've been following the {daughters} for a while. I stumbled upon you, and..." Tamara pauses awkwardly. """,
""""I figured you could help me. You look like the fighting sort, so you're exactly what I need." """])
		elif question == "3":
			print_stuff([f""""I've already given you my name," {tamara} says. "I assume your asking what I do in life?" """,
f""""I have a complicated past, but let's just say I have something personal against the {daughters}." """])
		elif question == "4":
			print_stuff([f""""I have their clothes, but I do not follow them. As soon as I have some privacy, I shall change from these garments." """,
f"""{tamara} laughs. "They were too... exposing for me anyway." """])
			awareness_roll = random.randrange(1, 10)
			if awareness_roll <= ability.ability["awareness"]:
				aware = colour_it("aware", Color.AWARENESS)
				print_stuff([f"You are {aware} enough to notice her use of past tense."])
				choice = input_stuff("""1. "Why do you use past tense?" 
2. Say nothing.
> """, ["1", "2"])
				if choice == "1":
					print_stuff([f"""You see {tamara} give a start. "No reason," she says quickly. "Or at least, a reason that I do not wish to reveal currently." """])
		elif question == "5":
			break
	print_stuff([f"Suddenly, you hear the sound of footsteps. {tamara} jumps to her feet and runs to the window.",])
	enemy_round.initialize([encounters.monster_access("chaos_daughter")])
	if ability.ability['health'] <= 0:
		ability.ability["health"] = (ability.ability["maxhealth"] / 2)
		print_stuff([f"The light returns to your vision and you see {tamara}'s face looking down at you",
""""That was quite a hit you took," she says cheekily. She offers her hand to you to help you up.s"""])
		choice = input_stuff("""1. Take her hand.
2. Get up by yourself.
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f"""You take {tamara}'s hand, and she pulls you to your feet, with surprising strength for someone of her build."""])
		elif choice == "2":
			print_stuff([f"You get to your feet without taking {tamara}'s hand. She gives you a look but says nothing."])
		print_stuff([f"""You look around and see the bodies of the two {daughters} with deep lacerations on them. "My handiwork," {tamara} says. """,
""""Don't worry though. I forgive you." But you can tell she's joking. """])
	print_stuff([f"After the fight, you return to {denvar}'s cabin to rest."])
	rest.rest()
	print_stuff([f""""We should return to {blackburrow} also," {tamara} says. "There is much to discuss." """,
f"""After bidding {denvar} farewell and descend the mountain carefully, returning to the trail and making your way back to {blackburrow}."""])


def reeturn():
	save('chapter2.reeturn')
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	tamara = colour_it("Tamara", Color.NPC)
	lizardtongue = colour_it("Lizardtongue Mountains", Color.PLACE)
	print_stuff([f"You retrace your steps along the trail to the {lizardtongue}, this time with another by your side. By the time night falls, the lights of {blackburrow} are visible.",
f"As you settle down to rest, {tamara} away from your camp and changes her clothes. Instead of hte strange, ceremonial appearing apparel she was wearing before, now she wears more traditional clothes.",
"""She wears tight trousers, a shirt and jacket, and her hair is tied back in a loose ponytail. "Does this look any better?" she asks, holding up her arms and spinning around. """])
	choice = input_stuff("""1. "Looks fine." 
2. "Looks terrible." 
> """, ["1", "2"])
	if choice == "1":
		print_stuff([f""""I'm glad you like it!" {tamara} then takes a seat beside you around the meager campfire. """])
	else:
		print_stuff([f"""{tamara} raises an eyebrow but says nothing, then takes a seat beside you around the meager campfire. """])
	print_stuff(['The night begins to grow cold, and the sky gradually fades from a sunset pink-and-orange to a dark blue. Stars appear overhead.',
f"""Eventually, {tamara} turns to you. "What do you say to a bit of sparring?" she asks, rising to her feet. "To tire us out so we sleep better?". """])
	sparring = False
	while True:
		choice = input_stuff("""1. "As you wish. Ready to lose?" 
2. "I don't want to hurt you..."
3. "Sorry. It's not for me."
> """, ["1", "2", "3"])
		if choice == "1":
			sparring = True
			break
		elif choice == "2":
			print_stuff([
f'''{tamara} laughs. "You make it sound so easy," she says. "Or maybe you're just afraid I'll beat you!" '''])
			continue
		elif choice == "3":
			print_stuff([
f'''{tamara} raises an eyebrow. "Why not, may I ask?" '''])
			choice = input_stuff("""1. "I like a challenge." 
2. "I don't want either of us to be injured."
3. "I just don't feel like it."
4. "On second thoughts..."
> """, ["1", "2", "3", "4"])
			if choice == "1":
				print_stuff([f"""{tamara} frowns. "I'm not that bad," she protests. But she sits down again. """])
				break
			elif choice == "2":
				print_stuff([f""""We'd be using the flat of our blades. If you're any good, that shouldn't be too hard." But {tamara} returns to her seat anyway. """])
			elif choice == "3":
				print_stuff([f"""{tamara} shrugs. "That's fair. I won't press you." """])
			elif choice == "4":
				sparring = True
				break
	if sparring == True:
		print_stuff([f"You and {tamara} lock blades together in a mock battle. You prove to be her superior, and the match ends with your tip pressed gently to her breast.",
f""""You're incredible!" {tamara} exclaims with excitement. "Where did you learn that?" """])
		choice = input_stuff(""""1. I'm a Nighthawk." 
2. "A few things along the road." 
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f"""{tamara} gasps in awe. "Amazing!" """])
		print_stuff([f""""However, I think there's something I may be able to add to your repertoire." {tamara} begins to demonstrate a new sword routine to you...""",
""""""])
		weapon.weapon['attacks'][4]['enabled'] = True
	rest.rest()
