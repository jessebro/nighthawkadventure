import random
from functions import ability
from functions import equipment
from functions import character
from functions import encounters
from functions import enemy_round
from functions import weapon
from functions import rest
from functions.utils import print_stuff
from functions.utils import input_stuff
from functions.utils import colour_it
from functions.utils import Color
from functions.utils import clear
from functions.loading import save
from functions import town
from functions import sounds
from functions.character import story


def beginning():
	global descent_choice
	save('chapter2.beginning')
	elfa = colour_it("Elfa", Color.NPC)
	micha = colour_it("Micha", Color.NPC)  # Word colouring
	sounds.dire()
	character.story["denvar"]["exists"] = True
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
			character.story["descended"] = "a"
			break
		elif choice == "2":
			tamara = colour_it("Tamara", Color.NPC)
			print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} gives an impatient groan. "I'm {tamara}, if you insist," she says finally. """])
			character.story["tamara"]["name_known"] = tamara
		elif choice == "3":
			print_stuff([f"""{character.story['tamara']['name_known'].capitalize()} lifts an eyebrow. "Then let us meet this Denvar." """])
			character.story["descended"] = "b"
			break

def descent():
	if character.story['descended'] == "a":
		descenta()
	else:
		descentb()

def descenta():
	micha = colour_it("Micha", Color.NPC)
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	tamara = colour_it("Tamara", Color.NPC)  # Word colouring
	sounds.travel()
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
	denvar = colour_it("Denvar", Color.NPC)  # Word colouring
	sounds.travel()
	print_stuff([f"The three of you make your way down the mountain. With your guidance you arrive at {denvar}'s cabin. You notice that {denvar} is home.",
f"Light shines from the windows, and you see movement from inside. You approach the door and knock sharply. Almost instantly, {denvar} answers the knock."])
	if character.story["denvar"]["knows_name"]:
		print_stuff([f""""Greetings, {character.character["firstname"]}," {denvar} says warmly. "How may I help you?" """])
	else:
		print_stuff([f""""Greetings, traveller," {denvar} says warmly. "How may I help you?" """])
	ability.heal(15)
	print_stuff([f"Quickly, you usher {character.story['tamara']['name_known']} inside, but {micha} is shaking his head.",
f""""I'm shall return to {blackburrow}," he says. "I've had enough madness for one day." After a brief farewell, {micha} leaves alone, descending the mountain. """,
f"The next thing you know, you and {character.story['tamara']['name_known']} are sitting at a table with bowls of steaming meat stew. {denvar} crouches by the fireplace, coaxing a small blaze.",
f"The stew restores 15 health!",
f"""{character.story['tamara']['name_known']} looks up at you."""])
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
	print_stuff([f"Suddenly, you hear the sound of footsteps. {tamara} jumps to her feet and runs to the window.",
f""""Curses," she groans. "They've caught up with us." She runs outside, sword in hand. You follow suit, drawing {weapon.weapon['weaponname']}.""",
f"""Two of those women stand, ready for battle. "I'll take one," {tamara} says. "Careful; they're quick." """])
	enemy_round.initialize([encounters.monster_access("chaos_daughter")])
	sounds.travel()
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
	micha = colour_it("Micha", Color.NPC)
	tamara = colour_it("Tamara", Color.NPC)
	elfa = colour_it("Elfa", Color.NPC)
	bertholt = colour_it("Bertholt Omar", Color.NPC)
	lizardtongue = colour_it("Lizardtongue Mountains", Color.PLACE)  # Word colouring
	sounds.night()
	print_stuff([f"You retrace your steps along the trail to the {lizardtongue}, this time with another by your side. By the time night falls, the lights of {blackburrow} are visible.",
f"As you settle down to rest, {tamara} walks away from your camp and changes her clothes. Instead of the strange, ceremonial appearing apparel she was wearing before, now she wears more traditional clothes.",
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
		print_stuff([f"You and {tamara} lock blades together in a mock battle. You prove to be her superior, and the match ends with your sword tip pressed gently to her breast.",
f""""You're incredible!" {tamara} exclaims with excitement. "Where did you learn that?" """])
		choice = input_stuff("""1. "I'm a Nighthawk." 
2. "A few things along the road." 
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f"""{tamara} gasps in awe. "Amazing!" """])
		print_stuff([f""""However, I think there's something I may be able to add to your repertoire." {tamara} begins to demonstrate a new sword routine to you...""",
"""Your learnt Dancing Strike!"""])
		weapon.weapon['attacks'][4]['enabled'] = True
	rest.rest()
	sounds.town()
	print_stuff([f'After your rest, you and {tamara} continue onwards to {blackburrow}. It is late morning when finally you both step through the gates of the town.',
f""""If you need to prepare," {tamara} says. "I'll be at the tavern. Come to me when you're ready; I have some things to tell you." """,
f"""{tamara} disappears into the crowded streets, leaving you alone to do as you wish."""])
	town.town("Blackburrow", "Meet Tamara at the tavern.", True)
	print_stuff([f"""As you make your way to the tavern, you see {micha} approaching you.""",
f""""Greetings!" he says cheerfully, but you see sadness behind his eyes. "I was hoping you would return safetly." """,
""""My father wishes to see you. Something about a reward for finding me." """])
	choice = input_stuff(f"""1. Go with {micha}.
2. Continue towards the tavern.
> """, ["1", "2"])
	if choice == "1":
		print_stuff([f"{micha} leads the way towards {bertholt}'s home, Baron of {blackburrow}. You both step through the large gates.",
f"You are flanked by the Baron's personal guards, but they recognise {micha}, so make no move towards you. The house itself is massive and well kept.",
f"{micha} walks past several rooms through hallways, and ascends two flights of stairs. On the top level, there are only three rooms.",
f"The first room is a large bedroom, full of luxuries and with a large bed, big enough for three people.",
f"The second room has a more messy, smaller bed. Next to it is another bed, but this was one folded. A set of woman's clothes is laid across the made one.",
f"The third room seems to be a study. It's smaller, but probably contains more stuff than any of the other rooms you've seen. Piles of paper are stacked high.",
f"Sitting behind a desk is {bertholt}, his head bent as he is writing. He is a large man, and is wearing a pair of glasses at the moment.",
f"He notices your entry, removes the glasses and looks up. He leans back in his chair.",
f""""Greetings, Nighthawk," the Baron says. "I see you returned. With my son." He raises his eyebrow. "Anyway, here's your reward of seventy five gold." """])
		choice = input_stuff("""1. "Seventy five? We agreed a hundred and fifty!" 
2. "Thanks..." 
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f""""You completed half the task, so you get half the reward," the Baron says angrily. "You were too slow to save {elfa}. Too slow!" """])
			choice = input_stuff("""1. "I'm sorry, but we had a deal."
2. "It's not my fault that she was too stupid to not get herself killed!"
3. "Fair enough." 
> """, ["1", "2", "3"])
			if choice == "1":
				print_stuff([""""Not good enough, Nighthawk. Take the gold, or be out of my sight!" """])
			elif choice == "2":
				print_stuff([""""You dare speak like that about my daughter?! Begone, wretched Nighthawk." """])
			elif choice == "3":
				equipment.equipment['gold'] += 75
				print_stuff([""""I'm glad you see reason. Now take the gold, and begone." """,
f"You leave {bertholt}'s home, a bit disappointed. You make your way to the tavern you agreed to meet {tamara} in."])
				return
			choice = input_stuff("""1. Take the gold.
2. Threaten the Baron with your sword.
> """, ["1", "2"])
			if choice == "1":
				equipment.equipment['gold'] += 75
				print_stuff([ f"You storm out of {bertholt}'s home, a disappointed and angry. You make your way to the tavern you agreed to meet {tamara} in."])
			elif choice == "2":
				character.story['criminal'] = True
				print_stuff([f"You draw your sword and hold it to the Baron's throat. You hear {micha}'s cry of protests.",
f""""What do you want?" {bertholt} gasps. "If you want the full payment, take it!" """])
				choice = input_stuff("""1. "Give it to me." 
2. "You caused me trouble, so I want double." 
> """, ["1", "2"])
				if choice == "1":
					equipment.equipment['gold'] += 150
				elif choice == "2":
					equipment.equipment['gold'] += 300
				print_stuff(["The Baron hastily passes you the gold, and you flee before anyone can raise the alarm."])
				return
		elif choice == "2":
			equipment.equipment['gold'] += 75
			print_stuff([f"You walk from {bertholt}'s home, a little disappointed that you only got paid half. You make your way towards the tavern."])
			return

def answers():
	save('chapter2.answers')
	tamara = colour_it("Tamara", Color.NPC)
	micha = colour_it("Micha", Color.NPC)
	daughters = colour_it("Daughters of Chaos", Color.ENEMY)
	greypass = colour_it("Greypass", Color.PLACE)  # Word colouring
	meal = False
	justice = False
	sounds.town()
	ability.gain_xp([encounters.xp_handouts['medium']])
	print_stuff([f"You enter the tavern and look around. {tamara} is sitting at a table. You quickly take a seat opposite her.",
f""""I've been waiting for you," {tamara} comments. "You certainly took your time." """])
	input_stuff(f"""1. "I had business to attend to." 
2. "I saw {micha} again." 
> """, ["1", "2"])
	print_stuff([f"""{tamara} waves a hand. "I don't mind, really." Suddenly, a serving girl comes up beside you. "What'll it be?" she asks shyly. """,
f"""{tamara} turns to you. "Share a drink with me?" """])
	choice = input_stuff(f"""1. "Gladly." 
2. "No thanks". 
> """, ["1", "2"])
	if choice == "1":
		meal = True
	print_stuff(["The serving girl hurries off. As she walks past a table of a group of men, one of them reaches out and pinches her backside.",
"She gives a start but keeps walking, and the group of men chuckle quietly to themselves."])
	choice = input_stuff("""1. Confront the men.
2. Ignore their antics.
> """, ["1", "2"])
	if choice == "1":
		print_stuff(["You rise to your feet and walk over to the men. They turn to look at you as you approach.",
f""""Can I help you, {character.character['titles']['casual']}?" one of them asks. """])
		choice = input_stuff("""1. "I saw what you did to that serving girl." 
2. "I've come to chat." 
3. "I've come to hurt you." 
> """, ["1", "2", "3"])
		while True:
			justice = True
			if choice == "1" and character.character['gender'] == "female":
				print_stuff(["""The man smiles. "Sorry, lady, but I only do one a day. If you want I can do you tomorrow." """,
	"His friends laugh and slap him on the back."])
			elif choice == "1":
				print_stuff([""""I'm sorry if it offended you, mister, but what I do is my own business. Now push off." """])
			elif choice == "2":
				print_stuff([""""What about? Oh! You mean the girl... right?" """])
			elif choice == "3":
				print_stuff([f"""The man jumps to his feet. "What?" he protests. "What did I do to you, {character.character['titles']['casual']}?" """])
				choice = input_stuff("""1. "It's not about what you did to me." 
2. "You challenged my morals." 
> """, ["1", "2"])
				if choice == "1":
					print_stuff([""""You mean what I did to the girl?" The man slumps back in his chair. "I'm sorry... it was stupid." """])
				elif choice == "2":
					print_stuff([""""However I achieved that, I apologize for it. Please forgive me." """])
				choice = input_stuff("""1. "Don't let me catch you doing it again." 
2. "The funny thing is... I don't believe your apology." [Hit him] 
> """, ["1", "2"])
				if choice == "1":
					print_stuff(["""The man nods his head vigorously. "Thank you. Many apologies for the trouble." """,
f"You walk back to your table, where {tamara} is waiting, an eyebrow cocked up. She says nothing, but her face speaks for her."])
					break
				elif choice == "2":
					print_stuff(["You strike the man a blow, and he falls, senseless.",
f"You walk back to your table, where {tamara} is waiting, an eyebrow cocked up. She says nothing, but her face speaks for her."])
					break
			choice = input_stuff("""1. "Can't let you get away with that."
2. Hit him. 
> """, ["1", "2"])
			if choice == "1":
				print_stuff([""""Oh yeah? So what're you going to do?" """])
				choice = input_stuff("""1. "Make you apologize." [Tap your sword for effect.] 
2. "Hurt you." [Hit him] 
> """, ["1", "2"])
				if choice == "1":
					print_stuff(["The man is already moving towards the serving girl before you lower your hand again.",
"You don't hear the words of his apology, but you hear the tone. You watch with satisfaction as the serving girl slaps him in the face.",
"The man, crestfallen, returns to the table. One of his friends lays a hand on his shoulder.",
f"You walk back to your table, where {tamara} is waiting, an eyebrow cocked up. She says nothing, but her face speaks for her."])
					break
			print_stuff(["You strike the man a blow, and he falls, senseless.",
f"You walk back to your table, where {tamara} is waiting, an eyebrow cocked up. She says nothing, but her face speaks for her."])
			break
	print_stuff([f"""{tamara} frowns at the men and clenches her fists. "Bastards," she mutters. "They deserve a beating; the lot of them." """])
	if justice:
		print_stuff([f""""Although I'm glad you sorted them out. Nicely done, {character.character['firstname']}." """,
""""Now, I have things I want to talk to you about. But before I begin, I will tell you two things. First of all, you owe me for saving your life." """,
""""Second of all, if you help me, I can assure you I will reward you handsomely." """,
f""""Keep those things in mind as I'm talking to you." {tamara} leans back in her chair and bites her lip. "How to begin..." """,
f""""The {daughters} are planning something. Something massive, and it's in all of our interests to stop them." """,
""""I don't know exactly what it is, but I do know that it will result in the destruction of our world as we know it. So I want you to help me stop it." """,
f""""I have a contact in {greypass} who will provide us with not only information, and may also help us as well." """,
""""I want us to go there, learn all that we can from him, then act. Time is of the essence." """,
f"""{tamara} leans forward. "I know it may sound slightly crazy, but I need your help, {character.character['firstname']}. Please, you're the only one I can trust." """])

	quest = colour_it(""""Let's go!" """, Color.QUEST)
	if meal:
		print_stuff(["""The serving girl returns to your table, now carrying a pitcher and two cups of ale."""])
		if justice:
			print_stuff([""""This one's on the house," she says, smiling at you significantly. You nod your head politely. The serving girl than walks away."""])
		else:
			print_stuff([f""""That'll be four gold coins," she says. {tamara} produces the coins and hands them to her. """,
f""""This one's on me," {tamara} says."""])
	while True:
		choice = input_stuff(f"""1. "Why me?" 
2. {quest}
> """, ["1", "2"])
		if choice == "1":
			print_stuff([""""Several reasons. It's in your best interest, as well as mine. And you're a fighter, so I could use your help." """,
""""Those bitches aren't going to stop hunting you know that you've escaped their cluthes. They act in shadows; they want to stay out of sight." """])
			choice = input_stuff("""1. "I see."
2. "Why not tell the authorities?" 
> """, ["1", "2"])
			if choice == "2":
				print_stuff([f"""{tamara} laughs. "You think I haven't tried that? Look." She gets up turns around and lifts the back of her shirt. """,
"""You see red lines running across the small of her back, and disappearing below the waistband of her trousers. She turns around and sits down again.""",
f""""Fifty strokes for the disturbing of the peace," {tamara} says dryly. """,
""""Think about it. An organization that has been peaceful for years, suddenly turning violent and cruel. Sounds like a young fool trying to cause mischeif." """])
				input_stuff("""1. "I take it you're a young fool." 
2. "Don't worry. You may be a fool, just not a young one." 
> """, ["1", "2"])
				print_stuff([""""I'm only twenty-four. Not that old, but not that young either." """])
		else:
			break
	print_stuff([""""Perfect. Let's get going." It is then that the town bells start ringing. """])


def attack():
	save('chapter2.attack')
	tamara = colour_it("Tamara", Color.NPC)
	corocana = colour_it("Corocana", Color.PLACE)
	blackburrow = colour_it("Blackburrow", Color.PLACE)  # Word colouring
	sounds.jungle()
	print_stuff([f"""You hear shouting and a dull roaring from far away. You and {tamara} exchange glances and run outside."""])
	if character.story['criminal']:
		while True:
			persona = colour_it("There seems to be some misunderstanding. I did no such thing.", Color.PERSONA)
			print_stuff(["Suddenly, some guards run up to you. You recognize the personal guards of the Baron.",
f""""You're under arrest {character.character['titles']['formal']}," one of them says. "For the assault of the Baron." """])
			choice = input_stuff(f"""1. "Go ahead and try it." 
2. "Alright." 
3. "{persona}" 
> """, ["1", "2", "3"])
			if choice == "3":
				persona_roll = random.randrange(1, 16)
				if persona_roll <= ability.ability['persona']:
					print_stuff([f"""The guard buys your lie. "Sorry, {character.character['titles']['formal']}," he stammered. "Begging your pardon." """,
f"All of them turn a walk away in unison. {tamara} frowns at you, but you hold up a hand for silence when she tries to speak."])
					break
				else:
					print_stuff([f"""The guard doesn't believe your lie. "Nice try," he says. "But we're taking you in." """])
			print_stuff([f"""Suddenly, {tamara} steps forward. "Can I have a word, guard?" she asks, gesturing to the tavern. The guard stops to think. """,
f""""Alright, miss," he says. Both he and {tamara} enter the tavern. The other guards close in around you, blocking your escape. """])
			awareness_roll = random.randrange(1, 12)
			aware = colour_it("aware", Color.AWARENESS)
			if awareness_roll <= ability.ability['awareness']:
				print_stuff([f"""You are {aware} enough to eavesdrop on the conversation in the tavern.""",
f""""Look at you," says {tamara}'s voice. "A big strong man, but stuck as one of the Baron's henchmen." """,
""""Henchmen? Miss, I think..." """,
""""The pay can't be too good, can it? What if I, say, boosted your wage. In return, I want you to accept that this is all just a big misunderstanding." """,
"""There's the sound of coins clinking.""",
f""""I think I can handle that, miss." There's the sound of chairs scraping, and both the guard and {tamara} exit.""",])
			else:
				print_stuff([f"You are not {aware} enough to hear what's going on in the tavern. After a few seconds, both {tamara} and the guard step back onto the street."])
			print_stuff([""""Come on," the guard yells as his followers. "There's been a mixup. A shapeshifter is on the prowl. Let's move!" With that, the guards leave. """,
f""""It's incredible how guards can be so easily swayed by a woman with a large purse and fluttering eyelids," {tamara} comments. "Not enough women in their lives." """])
			break
	print_stuff(["The street is packed with people moving to the gates. You decide to follow the crowd. Once you reach the gates, your hand flinches to your sword.",
"Standing before you is a massive creature. It's lizard-like in appearance, but walks on its hind legs. It's huge; about as big as a small house.",
"It gnashes its teeth, which are all as long as your forearm. Its arms aren't very long, however, and stick no further out that its thick, squarish snout.",
f"Though you don't know what exactly this creature is, you know it must have come out of the jungles of {corocana}. Riding atop its back is a lizardman.",
"As their name suggests, a lizardman is a humanoid lizard, about as big as a human. They have sharp teeth and a terrible lisp.",
"This lizardman swings a great staff about, and it dressed in colourful robes. You assume them to be a priest of some sort.",
""""Warm-bloodssss!" the lizardman cries, their voice carrying over the hubbub of the crowd. "You have darrrred to trrressssspasssss on the Sacred Earth." """,
""""You have darrred to send your femalessss, arrrmed and fiercccccce, to hurrrrt ussss. Now we will hurrrrt youssss unlessss you call them back." """,
"Many of the citizens have fled from the gates. A crowd of around two score people is around you, and growing smaller as people take shelter in their homes.",
"""Suddenly, a man in fine clothing emerges from the crowd. He appears nervous, but he walks with an air of authority. The crowd parts before him.""",
f""""An envoy from the Baron," {tamara} whispers to you. You nod in conformation as the envoy passes. """,
""""Noble lizardman," the envoy calls, stepping out into the open field between the town and the large creature. "We have no quarrel with you." """,
""""Korrrel?" the lizardman says testingly. The envoy sighs and continues to deliver the message. """,
""""The warmbloods that plague you are no doing of ours. Please leave us in peace." The lizardman laughs, a sound like a cross between a sigh and a cough. """,
""""They are warrrmbloodsssss. They arrre yourrsss. If you can not contrrrol them by authorrrity, then do it by forrrce. You have thrrree weeks..." """,
"Suddenly, the large creature lurches forwards. The lizardman is thrown to the ground hard, hissing in pain. The creature rushes towards the envoy.",
f""""Come on, {character.character['firstname']}," {tamara} says, drawing her sword and running forward.""",
f"""Knowing that you don't really have a choice, you draw {weapon.weapon['weaponname']} with a flourish and charge forwards.""",
"The Baron's envoy is running for his life, the creature hot on his heels."])
	while True:
		if equipment.equipment['knives'] >= 1:
			choice = input_stuff("""1. Use a knife to distract the creature.
2. Do nothing.
> """, ["1", "2"])
			if choice == "1":
				equipment.equipment['knives'] -= 1
				print_stuff(["""The knife connects with the creature, and it turns towards you. The envoy, now free of his pursuer, makes it into town safetly."""])
				break
		print_stuff([f"With a mightly lunge forwards, the creature snatches up the envoy, swallowing him whole. It then turns towards you and {tamara}."])
		break
	print_stuff([f""""We've got to stop it," {tamara} yells. "Before it destroys the town." The creature roars and charges towards the both of you."""])
	enemy_round.initialize([encounters.monster_access("dinosaur")], [encounters.ally_access("tamara")], boss=True)
	sounds.dire()
	if ability.ability['health'] <= 0:
		print_stuff([f'With you out of the picture, {tamara} stands little chance.',
f"Before darkness takes you completely, you see {tamara} falter, the creature strike, a spurt of blood, and {tamara} falls lifeless to the ground."])
		exit()
	print_stuff([f"Panting, you kick the large carcass to make sure the creature is dead. {tamara} sidles up next to you. She's covered in sweat.",
f"""A troop of town guards runs towards you, weapons ready. {tamara} scowls at the guards, hands on hips and her weight shifted onto one leg.""",
f""""Nice of you to show up {colour_it('after', Color.UNDERLINE)} the thing's dead," she says angrily. """])
	input_stuff(f"""1. "Easy there, {tamara}." 
2. "Exactly." 
> """, ["1", "2"])
	print_stuff(["The guards exchange awkward glances. One of them steps forward and points at the lizardman, lying senseless.",
f""""What about that?" she demands. {tamara} bites her lip in thought, then seems to reach a conclusion. """,
""""Leave them with us," she says. "My companion and I will be sure to question them." """,
f""""If they enter {blackburrow} we're going to arrest them," another of the guards warns.""",
f""""Don't worry," {tamara} replies, smiling. "We're leaving anyway." """])


def to_greypass():
	save('chapter2.to_greypass')
	tamara = colour_it("Tamara", Color.NPC)
	corocana = colour_it("Corocana", Color.PLACE)
	blackburrow = colour_it("Blackburrow", Color.PLACE)
	greypass = colour_it("Greypass", Color.PLACE)
	rookwood = colour_it("Rookwood", Color.PLACE)
	daughters = colour_it("Daughters of Chaos", Color.ENEMY)
	bandits = colour_it("bandits", Color.ENEMY)
	sounds.travel()
	print_stuff([f"The road to Greypass is significantly flatter and easier to traverse than the one to the Lizardtongue Mountains.",
f"Your route takes you along the Barkan road, which will take you straight from {blackburrow} to {greypass}.",
"After an hour of walking, the lizardman wakes up once more. At the moment, you are carrying them over your shoulder.",
"The first sign that they are conscious once more is the slapping of their tail against your chest."])
	choice = input_stuff("""1. Put them on the ground.
2. Throw them to the ground.
> """, ["1", "2"])
	if choice == '1':
		print_stuff(["You put the lizardman down, and immediately they jump to their feet, eyeing you warily."])
	elif choice == "2":
		print_stuff(['The lizardman exhales sharply as you throw them down. They scramble to their feet, eyeing you warily.'])
	print_stuff([f""""You need not fear," {tamara} says. "You are safe with us. We rescued you from the... warmbloods." The last word comes from her mouth tentatively.""",
f""""Why?" the lizardman says. "Where am I. Who..." {tamara} waves a hand for silence.""",
f""""As it happens, we need your help," she says. "In return, we'll let you return to {corocana}." {tamara} turns to you. """,
""""You can be the first to ask the questions," she says. Then she turns to the lizardman. "Do try to answer truthfully." """])
	while True:
		quest = colour_it("We're done here.", Color.QUEST)
		choice = input_stuff(f"""1. "Who are you?" 
2. "Why did your creature throw you off?" 
3. "What's happening in {corocana}?"
4. "Do lizardmen eat people?"
5. "Are you male?"
6. "{quest}"
> """, ["1", "2", "3", "4", "5", "6"])
		if choice == "1":
			name = colour_it("Meel-kar", Color.NPC)
			story['meel-kar']['name_known'] = name
			print_stuff([f""""I'm {name}," the lizardman says. "High Priesssst of Quarrrr-Gaxxxx, and sssserrrvant to the Chossssen." """,
""""I wassss ssssent as an envoy to you warrrmbloodsssss, and given a Orrrrah-tai to carrrrry me to you." """,
""""You warrrrmbloodssss have crrrreated trrrrouble in my home. The Chossssen wassss deterrrrmined to ammend the... sssituation." """])
		elif choice == "2":
			print_stuff([f""""I don't know," {story['meel-kar']['name_known']} says. "It ssssuddenly went wild, and I losssst contrrrrol." """,
""""Multiple crrrrreaturrrrresssssss in the jungle have acted ssssstrrrangely, sssssudenly going crrrrrazy." """])
		elif choice == "3":
			print_stuff([f""""Female warrrrmbloodssss arrrrre storrrrming ourrrr home. It'ssssss chaossssss. They ssssssaid that we mussssst give them the Table of Kingsssss... orrrr die." """,
""""The Table of Kingsssss will tell ussss who the next king will be. It issss a sssstrrrrong magic item, and what thosssse warrrrmbloodssssss want with it, I can only guess." """])
		elif choice == "4":
			print_stuff([""""Of coursssssse, but only thossse that dirrrrectly opposssse usssss. Orrrrr corrrpssssessss that arrrre brrrrought to usssss." """])
		elif choice == "5":
			story['meel-kar']['reference']['his'] = "his"
			story['meel-kar']['reference']['him'] = "him"
			story['meel-kar']['reference']['he'] = "he"
			print_stuff([""""Yesssss. Do I look like a female to you?" """])
			input_stuff("""1. "Well..."
2. "It's hard to tell." 
> """, ["1", "2"])
		elif choice == "6":
			break
	print_stuff([f""""Farrrrwell, warrrmbloodssssss," {story['meel-kar']['name_known']} says. "Forrrr some rrrreassson, I trrrusssst you." """,
f""""We'll see if we can fix your situation in the jungles," {tamara} says. "Hopefully, we can." """,
f"""You watch as {story['meel-kar']['name_known']} walks away, leaving you and {tamara} alone on the road once more.""",
f""""No doubt, they were talking about the {daughters}. What could they be doing there?" """])
	choice = input_stuff("""1. "Whoever this contact of yours is, I'm sure he'd be able to shed some light." 
2. "Maybe they want to enslave the lizardmen?" 
> """, ["1", "2"])
	if choice == "1":
		print_stuff([f""""He'd better," {tamara} growls. "We're going through a lot of effort to see him." """])
	elif choice == "2":
		print_stuff([""""Why do I have hunch that you're not too far off track?" """])
	print_stuff([f""""Anyway, we'd best continue on our way. {greypass} is still a while away." """,
f"""You and {tamara} continue continue along the Barkan road. You fit in another few hours of walking before night begins to fall."""])
	sounds.night()
	print_stuff([f"""As you and {tamara} begin searching for a place to stay, you notice a farmhouse to your left."""])
	choice = input_stuff("""1. Investigate the farmhouse.
2. Continue past. 
> """, ["1", "2"])
	if choice == "1":
		print_stuff([f"""{tamara} follows you as you make your way into the farmhouse. It appears to be abandoned, and will provide good shelter."""])
	elif choice == "2":
		print_stuff(["""You ignore the farmhouse and continue past. In the end, you find a nice clearing in a grove of trees."""])
	print_stuff([f"{tamara} takes first watch, and you will go next. You can't be too careful in the wilds."])
	rest.rest()
	sounds.fairy()
	print_stuff([f"""You continue along the road, and finally you reach {rookwood}, the large forest that surrounds {greypass}.""",
"""Birds sing in the trees, the wind rustles the leaves, and feeble branches crackle and creak in the canopy.""",
f""""Beautiful place," {tamara} comments. You look at her, noticing something in the way she said it. """])
	awareness_roll = random.randrange(1,10)
	aware = colour_it("aware", Color.AWARENESS)
	stolen = False
	if awareness_roll <= ability.ability['awareness']:
		print_stuff([f"You are {aware} enough to notice she says it in a way that implies she's been here before, and with good memories."])
		choice = input_stuff("""1. "Been here before?" 
2. Say nothing.
> """, ["1", "2"])
		if choice == "1":
			print_stuff([f""""Mhm," {tamara} says. "I used to travel a lot." She chuckles. "I guess I still am." """])
	print_stuff([f"""It is not long before trouble finds you. Suddenly, a group of five {bandits} jumps out, blocking the path. "Your gold; hand it over." """])
	if equipment.equipment['gold'] >= 30:
		choice = input_stuff("""1. Give them 30 gold to go away.
2. "Kiss my arse".
> """, ["1", "2"])
		if choice == "1":
			stolen = True
			equipment.equipment['gold'] -= 30
			print_stuff([f"""You throw the {bandits} a bag of gold. They exchange smug looks, and ready their weapons."""])
	print_stuff([f"""{tamara} draws her own weapon, but one of the {bandits} pulls out a knife. Before you or {tamara} can react, she throws the knife.""",
f"""It buries itself into {tamara}'s leg. She screams in pain and falls. The blow is not lethal, but you realise she will be of now help now.""",
f"""The {bandits} rush forwards eagerly, weapons ready. You brace yourself for the coming battle."""])
	enemy_round.initialize([encounters.monster_access('mbandit'), encounters.monster_access('fbandit'), encounters.monster_access('mbandit'), encounters.monster_access('fbandit'), encounters.monster_access('cbandit')])
	if ability.ability['health'] <= 0:
		print_stuff([f"With you out of the picture, the {bandits} will make quick work of an injured {tamara}. They'll strip you, and kill you for causing so much trouble."])
		exit()
	sounds.fairy()
	if stolen:
		equipment.equipment['gold'] += 30
		print_stuff([f"""You retrieve the gold that you gave one of the {bandits}, spitting on her body as you do."""])
	print_stuff([f"""You walk over to {tamara}. Her leg is soaked in blood, but she has tied a strip of cloth around it as a makeshift bandage.""",
f""""That hurt," {tamara} says weakly. You bend down and pick her up, supporting her legs and back. She grimaces in pain, but says nothing. This looks to be a long walk. """,
f"""You don't enjoy the picturesque forest anymore. You have more important matters. When {greypass} finally becomes visible, it is a welcome sight indeed."""])


def at_greypass():
	save('chapter2.at_greypass')
	greypass = colour_it("Greypass", Color.PLACE)
	tamara = colour_it("Tamara", Color.NPC)
	fenroche = colour_it("Fenroche", Color.NPC)
	rookwood = colour_it("Rookwood", Color.PLACE)
	caelfin = colour_it("Caelfin", Color.PLACE)
	daughters = colour_it("Daughters of Chaos", Color.ENEMY)
	misunderstand = False
	sounds.village()
	print_stuff([f"""Your arms are tired from carrying {tamara}, but you know that you have almost reached your goal. You continue onwards.""",
f"""{greypass} is only a cluster of about a score of buildings in a large clearing, next to the Raven River. The town itself is in the middle of {rookwood}.""",
f"""One of the townsfolk approaches you. "Alright there, {character.character['titles']['formal']}?" he asks. {tamara} looks at him.""",
""""We're fine," she says, her voice husky. "We can take care of ourselves." The man looks at you and you nod in confirmation.""",
""""If you need help, just give a holler. Say, what was it that injured you? I'll be knowing there's some mosnters lurking about." """])
	choice = input_stuff("""1. "Bandits attacked us." 
2. "Doesn't matter. I sorted out the danger." 
> """, ["1", "2"])
	if choice == "1":
		print_stuff([""""Bandits, you say? Well, I'm glad you sorted them out." """])
	else:
		print_stuff([""""Good. I'm glad that you have ridded this region of another ne'er do well." """])
	print_stuff([f"""The man walks away. You look around and see people staring and pointing. You also realise that {tamara} is dripping blood onto the ground.""",
f""""Go South, on the other side of the Raven River," {tamara} says. "There'll be a house over a small bridge." Obeying {tamara}'s direction, you begin to move.""",
f"""After a minute, you come to a small wooden bridge, spanning a thinner part of the Raven River. On the other side is the Gladepass Road, leading to {caelfin}.""",
f"""Branching off from the road is a small trail that leads up to a small house nestled atop a hill. It's simple enough; stone walls, a roof of wooden planks...""",
"""But something is clearly wrong. The windows are boarded up, and there doesn't seem to be any sign of life from inside.""",
f""""What happened?" {tamara} says aloud. "Be wary, {character.character['firstname']}. I fear danger may be close." """])
	awareness_roll = random.randrange(1, 13)
	aware = colour_it("aware", Color.AWARENESS)
	if awareness_roll <= ability.ability['awareness']:
		print_stuff([f"""You are {aware} enough to notice, only for a second, a pair of human eyes looking out of some bushes."""])
	print_stuff([f"""Keeping your eyes peeled, you carry {tamara} to the door of the house. As you reach the door, she knocks weakly. For a moment, there is no response.""",
f"""Suddenly, a rectangle of the door slides away, revealing a pair of eyes. "Who..." a gravelly voice begins, but then the eyes travel to {tamara}.""",
f""""Oh, {tamara}," the voice says. "I see you've gotten yourself into deeper shit than usual." {tamara} glares at the eyes.""",
f""""Hurry up, {fenroche}," {tamara} hisses. The door swings open, and you hurry inside. As soon as you're inside, the door closes. You turn to look at your host. """,
f"""He's a tall man, with black hair, a thick beard, dark eyes, and strong looking muscles. He has an air of power around him.""",
f""""Damn it, {tamara}," he growls in his grating voice. "You've gotten blood all over my nice floor." But he moves to take her from you.""",
"""As you are revelling in the sudden lightness and freedom of your arms, you look around the house. It seems simple enough.""",
"""A dining and cooking area, a single wooden chair by a fireplace... and a trapdoor. The trapdoor, other than the man himself, is the only abnormal object.""",
f"""The man lays {tamara} down on his table. It's long enough to support her entire body. "Come and help me, would you?" the man asks you. You oblige.""",
f""""First, we'll take a look at the wound." {tamara} is lying compliantly with her eyes closed as you and the man operate.""",
f"""As you and the man are cutting away part of {tamara}'s trousers, the man speaks. "I'm {fenroche}," he says, not taking his eyes from {tamara}."""])
	choice = input_stuff(f"""1. "Greetings, {fenroche}. I'm {character.character['firstname']}." 
2. "Good." 
> """, ["1", "2"])
	if choice == "2":
		print_stuff([f"""In your silence, {tamara} pipes up. "{character.character['he'].capitalize()}'s {character.character['firstname']}," she says. "You can trust {character.character['him']}." """])
	print_stuff([f""""So, {character.character['firstname']}, what are you doing with... such fine company?" {fenroche} asks. """])
	choice = input_stuff(f"""1. "{tamara} saved my life." 
2. "Met her on the road." 
3. "I keep her around because she can fight." 
> """, ["1", "2", "3"])
	if choice == "1":
		print_stuff([f""""Of course she did. And I take it wasn't long before it started to go the other way around?" """])
	elif choice == "2":
		print_stuff([f""""The road? What on earth was she doing on the road?" But the question is rhetorical. """])
	elif choice == "3":
		print_stuff([f""""That's all she's good for," {fenroche} agrees. "But even then, she'd get her arse beaten by a drunk, half-blind badger." """])
	print_stuff([f""""Your comments are as hilarious as they are flattering," {tamara} says, unsuccessfully trying to hide a smile. "I may be dying, but let me do it in dignity." """,
f""""Don't be silly. You're not going to d... wow." You and {fenroche} have just cut through the final part of {tamara}'s trousers and can see the wound. """,
"""There is a deep wound, surrounded by blood. Half her leg has been tinted red, and the wound itself is a dark, blackish colour. """,
f""""I'll handle this," {fenroche} says. "You go and rest." You happily take {fenroche} up on his offer. """])
	rest.rest()
	print_stuff([f"""You complete your short rest, and return to {fenroche} and {tamara}. {tamara} is fast asleep now, and {fenroche} is sitting nearby, watchful.""",
f""""Poor girl," he says. "She's exhausted from the pain." You are slightly taken aback by this sudden change in attitude.""",
f"{fenroche} reaches out and strokes a lock of {tamara}'s hair, still not taking his eyes off her."])
	choice = input_stuff("""1. "Watch the hands." 
2. Do nothing.
> """, ["1", "2"])
	if choice == "1":
		misunderstand = True
		print_stuff([f"""{fenroche} laughs. "Clearly you have no idea..." he says, but stops before he is done. He takes his hand away though. """])
	print_stuff([f""""Now, I do believe some questions and answers are in order. {tamara} has told me of you, so now you will get a chance to know me." """])
	while True:
		quest = colour_it(""""I've no further questions." """, Color.QUEST)
		question = input_stuff(f"""1. "What are you doing here?" 
2. "Apparently you know things about the {daughters}..." 
3. "What's your relationship with {tamara}?" 
4. {quest}
> """, ["1", "2", "3", "4"])
		if question == "1":
			print_stuff([f""""I've been on the hunt for those accursed {daughters}. Finally, I had a theory of what they were up to, but I couldn't be sure." """,
f""""I came to {greypass} to experiment, but I fear my stay will be long." """])
		elif question == "2":
			print_stuff([""""I do indeed. Firstly, they are collecting magic items, and I think I know why. However, I need to make sure that I am correct before I begin to act." """,
""""Secondly, they are trying to cause mayhem. Political upheaval, war, all to cover their tracks and weaken their enemies." """,
""""For example, they are fighting on both sides for the racial attacks, both defending and aggravating nonhumans." """])
		elif question == "3":
			print_stuff([""""I'm not sure she'd be eager for you to know... However, I will tell you a little bit." """,
f""""{tamara} met me after an attack by the {daughters}. My small farm and my family were lost that day, and they gave me this." """,
f"""{fenroche} pulls down the neck of his shirt. There, you can see a jagged red line running across his carotid artery.""",
f""""As I lay, bleeding and dying, {tamara} happened past. She nursed me back to health, and by some miracle I regained my strength." """,
f""""{tamara} was furious at the {daughters} for what they did, and I wasn't too happy either. Together, we began to attempt to foil their schemes." """])
		elif question == "4":
			break
	print_stuff([f"""{fenroche} turns to {tamara} once again. "Night is falling," he says. "You'd best get some rest." """,
f"""You oblige {fenroche}, laying your blankets down on the floor close to the wall. It is not long before sleep finds you."""])
	sounds.play_combat("human")
	print_stuff([f"""You are woken early in the morning by a smashing sound. You jump to your feet, sword in hand. You watch as the door gets kicked in.""",
f"""Three {daughters} jump through the opening, swords at the ready. They lunge forwards, but suddenly {fenroche} is there.""",
f"""In one hand he holds a hand crossbow, and in another a knife. With a flick of his wrist, the crossbow fires, the bolt piercing his target's neck.""",
f"""The remaining two {daughters}, caught off guard by this new adversary, are unprepared as {fenroche} lunges forwards.""",
f"""With a graceful twirl, he slits the throat of another foe. Spinning again, he stabs, burying the knife up to the hilt into the stomach of his last enemy."""])
	print_stuff([f"""The two {daughters} with severed necks are still lying on the ground, gasping and choking for air. {fenroche} approaches each one and finishes them off.""",])
	sounds.dire()
	print_stuff([f""""Impressed?" he grins at you, seemingly unconcerned at the three bodies, and the three pools of blood now lying at his front door.""",
f"""{tamara} hobbles into the room, clearly favouring one leg. Her eyes widen in shock when she sees the three corpses.""",
f""""Who..." she stammers. "How... What the hell is going on?" {fenroche} turns to her, grinning. """,
f""""Nothing much," he says. "Just another attempted attack." {tamara} frowns. """,
f""""Nothing much," she echoes. "Just {colour_it('another', Color.UNDERLINE)} attack. Has this happened before?" """,
f""""Every now and then, they try to attack me. Of course, now I have to mend my door, dismember the bodies and throw them outside, but other than that..." """])
	choice = input_stuff(f"""1. "Why are the {daughters} attacking you?" 
2. "You handled that well." 
> """, ["1", "2"])
	if choice == "1":
		print_stuff([""""Because I'm meddling in their affairs. They don't want me to disrupt their operations." """])
	elif choice == "2":
		print_stuff([""""Of course I did. I have sent nearly a dozen of those women tumbling into Hell." """])
	print_stuff([f""""But by coming here, {fenroche}," {tamara} cuts in. "Have we..." """,
f""""Yes. You've put yourselves in danger. But you did so when you came to my door. The best thing I could do was take you in. Then you'd be safer." """,
f""""You're always getting yourself into trouble, aren't you?" {tamara} says coldly."""])
	if misunderstand:
		story['told_romance'] = True
		print_stuff([f""""Speaking of trouble," {fenroche} says. "When you were unconscious, I brushed a bit of your hair." """,
f"""You watch for {tamara}'s reaction and see that she is unconcerned. "And?" she prompts. """,
f""""Wonder{character.character['titles']['contempt']} here snapped at me." You see {tamara}'s face tense up. You realise she's holding back a laugh for your sake."""])
		input_stuff("""1. "Did I act out of line?" 
2. "What's the big joke?" 
> """, ["1", "2"])
		print_stuff([f""""{character.character['firstname']}..." {tamara} begins. She exchanges a glance with {fenroche}, who nods. """,
f""""The relationship between {fenroche} and myself is... of a romantic sort." {tamara} goes a bit red, but {fenroche} is grinning broadly."""])
		choice = input_stuff(f"""1. "Oh... I see."
2. "But you two seem to hate each other." 
3. "Seriously? You went for {colour_it('him', Color.UNDERLINE)}?" 
> """, ["1", "2", "3"])
		if choice == "2":
			print_stuff([""""We don't hate each other. We just... rouse on each other a lot for our mistakes." """])
		elif choice == "3":
			print_stuff([""""I know, I'm such an ignoramus. Look at him... ugly, brutish, and he just slaughtered a group of women without a thought." """])
		print_stuff([""""Anyway, we're getting side tracked. Let us return to the matter at hand." """])
	print_stuff([f""""I think it's time I showed both of you something," {fenroche} says. He walks over to the trap door and opens it, revealing stairs leading downwards. """,
f""""After you, {character.character['firstname']}," {fenroche} says, gesturing towards the stairs. Carefully, you begin to descend.""",
f"""As you reach the bottom of the stairs, you gasp in awe. You have found yourself in what may have previously been a sort of cellar.""",
f"""However, now the place is full of contraptions you've never seen before. Also lying around are books, wands and strange plants.""",
f"""{fenroche} is coming up behind you, but stops and looks back up the stairs. {tamara} is awkwardly trying to descend, but with her bad leg, its impossible.""",
f"""{fenroche} moves back up the stairs, and picks {tamara} up, supporting her legs and back. Gently, he carries her down the stairs."""])
	choice = input_stuff("""1. "Care to tell me what all this hocus pocus is?" 
2. Walk around and examine the objects.
> """, ["1", "2"])
	if choice == "2":
		print_stuff(["""You walk around, but don't completely understand what is being achieved here. You notice the plants look like they may have come from the jungles.""",
f"""Other than that, you feel like some of these objects are magical, but their purpose is undetermined. "If you're done snooping around..." {fenroche} calls. """])


def labratory():
	save('chapter2.labratory')
	tamara = colour_it("Tamara", Color.NPC)
	fenroche = colour_it("Fenroche", Color.NPC)
	daughters = colour_it("Daughters of Chaos", Color.ENEMY)
	corocana = colour_it("Corocana", Color.PLACE)
	sounds.dire()
	print_stuff([f"""{fenroche} places {tamara} back on the ground. "It's testing equipment," he says. "The plants are from {corocana}." """,
""""I'm testing how they react to magic. An animal from the jungle would be good as well, but the lizardmen would eat me alive." """,
""""My results, though inconclusive, have proven to shed light on some very interesting information." He walks over to one of the tables. """,
f""""Watch." He pulls out a wand. "This wand is imbued with strong Lunar focus. Look what happens when I hold it close to this flower from {corocana}." """,
f"""You watch in amazement as the flower begins to become less defined. It seems to blur and swirl before your eyes. "Lunar magic," {fenroche} elaborates. """,
f""""Are you familiar with what Lunar focus does?" """])
	choice = input_stuff("""1. "Yes."
2. "No."
> """, ["1", "2"])
	if choice == "2":
		print_stuff([""""Lunar focus is concerned with how something is perceived. Illusions are the main kind of magic concerned with Lunar focus." """,
""""That is why the flower is behaving like that. It is reacting to the magical impulses, changing the way it's perceived, just like an illusion." """])
	print_stuff([f""""This clearly shows that the plants in {corocana}, and possibly the animals, have a strong magical connections." {tamara} sucks in a breath. """,
f""""I've heard tales of great natural events occurring in {corocana}," she says. "They come from nowhere. Could that be a reaction to focus?" """,
f"""{fenroche} nods. "It adds up. When the lizardmen believe that something will happen - truly believe - it will happen simply because of their combined faith." """])
	choice = input_stuff("""1. "So with strong magic you could potentially control the jungle?" 
2. "I'm so confused." 
> """, ["1", "2"])
	if choice == "2":
		while True:
			print_stuff([f"""{fenroche} sighs. "Focus, as you should probably know, is the magical energy that touches every object, living or nonliving." """,
f""""Focus has multiple branches, six in total. Some objects are more susceptible to magic than others. {corocana} is an example of a highly sensetive area." """,
f""""With strong magical acts, the surrounding area could also be effected. In {corocana}, this could have awesome results." """,
f""""If done the right way, you could have absolute power over the jungle, and do as you wish with such power. Do you need me to explain it again?" """])
			choice = input_stuff("""1. "I think I've got it." 
2. "Run through it again." 
> """, ["1", "2"])
			if choice == "1":
				break
	print_stuff([f"""{fenroche} nods. "I'm glad you understand. What the {daughters} will do with such power, I can only guess." """,
f""""You think the {daughters} want to have the jungle as their own?" {tamara} asks. """,
f""""Of course. It would explain their sudden move into {corocana}. But the only way to prove their intentions is to go there ourselves." He looks you in the eye. """,
f""""It will be dangerous, and it will be a journey into the unknown. Our knowledge of the jungles is limited, so we must be ready for anything." """,
f""""But the first step is to get out of here," {tamara} puts in. {fenroche} nods.""",
f""""We'll construct a plan," he says. "There's no time like the present to make moves. Besides..." He shoots a glance at {tamara}. "What choice do we have?" """,
f""""None, as far as I can tell," {tamara} says. "And I think I know where to begin." {fenroche} looks up at her. """,
f""""The {daughters} are after {fenroche}," {tamara} begins slowly. "So we need a diversion." She smiles knowingly, and {fenroche} groans. """,
f""""No way. Not with that injured leg of yours. And for my sake?" {fenroche} shakes his head. "Maybe it would work, but the risk is too great." """,
f""""Before you go making such statements, maybe you'd like to hear my plan in full?" {tamara} raises an eyebrow. "Alright, now here's the idea." """])
	sounds.jungle()
	print_stuff([""""They're watching the house, so we can't leave... unless they are looking at something else." """,
f""""What I propose is that after dark, I leave out the front, with a dummy of sorts wrapped in your cloak, {fenroche}. In the darkness, hopefully the facade will hold." """,
f""""Because they're after you, {fenroche}, they'll follow, allowing you and {character.character['firstname']} to exit through a back window." """,
f""""Meanwhile, as soon as the {daughters} show themselves, I'll make myself scarce. We'll regroup a mile upstream of the Raven River." """])
	while True:
		quest = colour_it(""""Let's get this done." """, Color.QUEST)
		choice = input_stuff(f"""1. "So much can go wrong." 
2. "I'll come with you as a decoy." 
3. "What if you can't get away?" 
4. {quest}
> """, ["1", "2", "3", "4"])
		if choice == "1":
			print_stuff([f""""It's not the best plan, but until we have any better ideas... Time is of the essense. Every second is another step closer the {daughters} get to their goal." """])
		elif choice == "2":
			print_stuff([f""""No. For all I know, I'll have a hundred foes on my tail. One is harder to follow than two." """])
		elif choice == "3":
			print_stuff([f"""{tamara} smiles weakly. "Then you can save the money for my drink at the tavern," she jests grimly. """])
		elif choice == "4":
			break
	print_stuff([f"""{fenroche} nods. "I agree. Time is against us." He leads you and {tamara} upstairs, and pulls his cloak down from a peg on the wall.""",
f"""Meanwhile, {tamara} is busily forming a crude model of a human form. It consists of a broom attached to a sack of flour, with a large round fruit on top.""",
f""""Not my best work," {tamara} says grimly. "But it will have to do." With that, everything is ready. The three of you sit in silence as the sun begins to set. """])


def escape():
	save('chapter2.escape')
	greypass = colour_it("Greypass", Color.PLACE)
	tamara = colour_it("Tamara", Color.NPC)
	fenroche = colour_it("Fenroche", Color.NPC)
	daughter = colour_it("Daughter of Chaos", Color.ENEMY)
	corocana = colour_it("Corocana", Color.PLACE)
	smoke_bomb = False
	sounds.jungle()
	print_stuff([f""""Night has fallen. The time to act has come." {tamara} is the one speaking, and you hear her voice crack with nervous excitement. {fenroche} has his crowbow loaded.""",
f""""Come, {character.character['firstname']}," {fenroche} says. He rises, and draws his dagger. {tamara} rises also, and takes hold of the dummy.""",
f"""You approach {tamara} one last time."""])
	if equipment.equipment['smoke bombs'] >= 1:
		choice = input_stuff("""1. "Good luck." 
2. "Remember, your life is more important than the mission." 
3. "If it gets too tough, use this." [Give smoke bomb] 
> """, ["1", "2", "3"])
	else:
		choice = input_stuff("""1. "Good luck." 
2. "Remember, your life is more important than the mission." 
> """, ["1", "2"])
	if choice == "3":
		smoke_bomb = True
		equipment.equipment['smoke bombs'] -= 1
		print_stuff([f"""{tamara} accepts the smoke bomb, and puts it in a pocket. """""])
	elif choice == "2":
		print_stuff([""""Perhaps. But if the mission fails, then our lives won't be worth much in any case." """])
	print_stuff([f""""Thank you, {character.character['firstname']}," {tamara} says. "For everything. With any luck, I'll see you soon." """,
f"With that, {tamara} sprints through the hole that used to be the front door. {fenroche} begins to remove the boards from one of the windows.",
f"""It is not long before you hear a shout, and running feet. "The decoy worked," {fenroche} says as he removes the last of the window's wooden boards. """,
f"""Stealthily, the two of you creep out into the night. In the darkness, you can hardly see. The only light comes from the full moon overhead.""",
f"""You take point, sneaking away a solid twenty paces ahead of {fenroche}. So it is that you are the first to see a {daughter}.""",
f"""She has her back turned to you, and with relative ease you rush up behind her, one arm wrapped around her neck, preventing her from uttering a sound.""",
f"""She squirms in your grip, trying to release herself."""])
	choice = input_stuff("""1. Kill her.
2. Knock her out.
> """, ["1", "2"])
	if choice == "1":
		print_stuff(["With the most subtle scraping noise, you draw you knife and plunge it deep into her back. She struggles for a bit longer, her eyes wide with shock.",
"Then blood begins to trickle out of her mouth, and she stops moving. Silently, you lower her body to the grass."])
	elif choice == "2":
		print_stuff(["You tighten your grip, cutting off her air supply. She struggles for a bit longer, then ceases to move, unconscious."])
	equipment.equipment['gold'] += 8
	equipment.equipment['oils'] += 1
	print_stuff([f"""A quick search of the {daughter}'s pockets yields 8 gold and a sword {colour_it('oil', Color.LOOT)}.""",
f"""At this point, {fenroche} catches up to you, and nods his approval. "Quick," he says. "There may be more of them." You continue onwards.""",
f"""You are able to get away without incident, but dimly you hear the sounds of battle, and shouting. {fenroche} frowns.""",
f""""I should never have let her go alone," he snarls, almost to himself. A few agonising minutes later, you finally get to a safe distance from {fenroche}'s house.""",
f"""You continue to walk through the night, more at ease. {fenroche}, despite his worries for {tamara}, is smiling. "First time out of the house," he explains.""",
f"""You reach the Raven River, then follow it upstream. You count your steps, and stop at about a mile upriver."""])
	sounds.night()
	print_stuff([f"""{fenroche} sits down, and you follow suit. "We shall wait till {tamara} arrives," he says in a tone that invites no argument."""])
	if smoke_bomb:
		character.story['crossroads1'] = "chapter3_jungle_tamara"
		print_stuff([f"""In about ten minutes, {tamara} suddenly steps from the bushes, causing both you and {fenroche} to flinch towards weapons. You never realised how quietly she could move.""",
f""""Made it," {tamara} comments, both addressing you and herself. "And all thanks to you, {character.character['firstname']}. If you hadn't given me that smoke bomb I surely wouldn't have made it." """,
f""""With that behind us, we can continue on our way." The three of you set off for the jungles, only stopping to rest once you are another couple of miles away."""])
	else:
		print_stuff([f"""However, you wait for a full hour, and there is no sign of {tamara}. Suddenly, {fenroche} gives a start. "Hide!" he hisses with urgency. """,
f"""He swiftly rolls behinds some bushes, and you crouch behind some rocks. You watch as a large row boat moves upstream. From the boat, you hear voices."""])
		awareness = random.randrange(1,11)
		if awareness <= ability.ability['awareness']:
			print_stuff([f"""You are {colour_it('aware', Color.AWARENESS)} enough to hear what they are saying.""",
f""""...three of them. Two of them escaped, but we got {tamara}." There's the sound of an evil chuckle. "Oh, I can't wait to give her a punch in that treacherous face." """,
f""""But what of the others? Shouldn't we be searching for them?" """,
f""""I have a feeling they will be coming to..." The boat gets too far away to hear any more. From the look on {fenroche}'s face, he also heard."""])
		else:
			print_stuff([f"""You are not {colour_it('aware', Color.AWARENESS)} enough to hear what they are saying. But clearly {fenroche} is."""])
		print_stuff([f""""They have {tamara}," he says angrily. "We must go after them." """])
		input_stuff(f"""1. "What about getting to {corocana}?" 
> """, ["1"])
		print_stuff([f"""{fenroche} swears under his breath. "I don't know what we should do, but I don't think there's a correct answer. Personally, I think we should rescue {tamara}." """,
f""""However, I shall let you have the final decision." """])
		while True:
			clear()
			choice = input_stuff(f"""1. "We should come to {tamara}'s aid first." 
2. "To much is at stake. We go to {corocana}, then get {tamara} afterwards." 
> """, ["1", "2"])
			prompt = """Are you sure you want to take this course of action?"""
			if choice == "1":
				character.story['crossroads1'] = "chapter3_tamara"
				prompt += f""" You will rescue {tamara} but events in {corocana} will escalate. (y/n)
> """
			else:
				character.story['crossroads1'] = "chapter3_jungle"
				prompt += f""" You will respond to the events in {corocana} but {tamara} will remain imprisoned. (y/n)
> """
			confirm = input_stuff(prompt, ["y", "n"])
			if confirm == "y":
				break
