import random
import character
import equipment
import time
import recreation

def cards(name, objective):
	gamble = False
	stakes = input(f"""You find some people who are willing to play cards with you. Three of you sit down, and one of the strangers deals you both two cards.
Before you begin, your opponent speaks to you.
"The total hand value closest to twenty one wins. Should we do a friendly, no stakes game, {character.character["titles"]['casual']}, or should we play for money?" he asks.

1. No stakes game
2. Play for money (10 gold)
> """)
	if stakes == 2:
		if equipment.equipment['gold'] < 10:
			redo = input("""You don't have enough gold for that! Will you...
1. Play a no stakes game
2. Leave the table
> """)
			if redo == 2:
				recreation.inn(name, objective)
				return False
		else:
			gamble = True
			equipment.equipment["gold"] -= 10
			print("You hand over the gold, and a pile forms of twenty gold coins. If you win, it will be yours.")
	deck = list(range(1, 14)) * 4
	while True:
		start1 = random.choice(deck)
		deck.remove(start1)
		start2 = random.choice(deck)
		deck.remove(start2)
		hand = [start1, start2]
		action = input(f"""In your hand you have {", ".join(hand)} for a total of {sum(hand)}.
1. Hit (draw a card)
2. Stand (finalize your total)""")
