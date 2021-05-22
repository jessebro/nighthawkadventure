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


def beginning():
	save('chapter2.beginning')
	elfa = colour_it("Elfa", Color.NPC)
	micha = colour_it("Micha", Color.NPC)
	print_stuff(["You wake up, your head throbbing painfully. You hear voices, but they are echoing and far away. You look around and find yourself sitting in a large cage.",
"The cage itself is made of wood, but all your belongings are gone. The wooden cage's bars and supports are thick, and you cannot break them.",
"To your left is a man and a woman. Each looks only sixteen, and each is covered in blood. It only takes you a moment to realise two things.",
f"These must be {micha} and {elfa}, the baron's children. You also realise that {elfa} is dead. {micha} looks like he's on his last legs also."])
	choice = input_stuff(f"""1. Approach {micha}.
2. Wait. """, ["1", "2"])
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
