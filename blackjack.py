import random
import character
import equipment
import time
import recreation

def cards(name, objective):
	gamble = False
	stakes = input(f"""You find some people who are willing to play cards with you. Three of you sit down, and one of the strangers deals you both two cards.
Before you begin, your opponent speaks to you.
"The highest total hand value below twenty one wins. Should we do a friendly, no stakes game, {character.character["titles"]['casual']}, or should we play for money?" he asks.

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
	while True:
		deck = list(range(1, 14)) * 4
		start1 = random.choice(deck)
		deck.remove(start1)
		start2 = random.choice(deck)
		deck.remove(start2)
		hand = [start1, start2]
		player_result = player_turn(deck, hand)
		enemy_result = enemy_turn(deck, player_result)
		if player_result > enemy_result:
			print("You win! Your opponent gruffly congratulates, and the other people nearby roar with laughter.")
			time.sleep(3)
			if gamble == True:
				print("You pull in the pile of twenty gold pieces, and leave the table.")
				time.sleep(3)
				equipment.equipment["gold"] += 20
			break
		elif player_result < enemy_result:
			print(f"""You lose! Your opponent leans over the table and shakes your hand.
"It was a pleasure to play with you, {character.character["titles"]['casual']}," they say cheerfully.""")
			time.sleep(5)
			break
		else:
			print("It's a draw, so you must rematch.")
			time.sleep(3)


def player_turn(deck, hand):
	while True:
		action = input(f"""In your hand you have {hand} for a total of {sum(hand)}.
1. Hit (draw a card)
2. Stand (finalize your total)
> """)
		if action == "1":
			drawn = random.choice(deck)
			print(f"You take a card from the deck and look at it's value.")
			time.sleep(5)
			print(f"It has the number {drawn} on it.")
			time.sleep(2)
			deck.remove(drawn)
			hand.append(drawn)
			if sum(hand) > 21:
				print("You went over twenty one, so you lose!")
				final_result = -1
				return final_result
			elif sum(hand) == 21:
				print("You got a perfect hand!")
				final_result = 21
				return final_result
		else:
			print("You lock in your hand.")
			time.sleep(2)
			final_result = sum(hand)
			return final_result


def enemy_turn(deck, target):
	estart1 = random.choice(deck)
	deck.remove(estart1)
	estart2 = random.choice(deck)
	deck.remove(estart2)
	ehand = [estart1, estart2]
	action = random.randrange(15,21)
	if action < sum(ehand) and sum(ehand) > target:
		print(f"Your opponent locks in their hand.")
		time.sleep(5)
		enemy_result = sum(ehand)
		return enemy_result
	else:
		print("Your opponent draws.")
		time.sleep(5)
		drawn = random.choice(deck)
		deck.remove(drawn)
		ehand.append(drawn)
		if sum(ehand) > 21:
			print("Your enemy went over twenty one, so you win!")
			enemy_result = -1
			return enemy_result
		elif sum(ehand) == 21:
			enemy_result = 21
			return enemy_result
