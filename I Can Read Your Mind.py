from getpass import getpass


left_deck = [
	{'rank':'King','suit':'Clubs'}, # King of Clubs (Black)
	{'rank':'King','suit':'Spades'}, # King of Spades (Black)
	{'rank':'Queen','suit':'Clubs'}, # Queen of Clubs (Black)
	{'rank':'Queen','suit':'Spades'}, # Queen of Spades (Black)
]
right_deck = [
	{'rank':'King','suit':'Hearts'}, # King of Hearts (Red)
	{'rank':'King','suit':'Diamonds'}, # King of Diamonds (Red)
	{'rank':'Queen','suit':'Hearts'}, # Queen of Hearts (Red)
	{'rank':'Queen','suit':'Diamonds'}, # Queen of Diamonds (Red)
]


def print_deck(prefix,deck):
	for card in deck:
		print('{}{} of {}'.format(prefix,card['rank'],card['suit']))


def shuffle_deck(deck, left, right):
	left.clear()
	right.clear()

	for index in range(1,len(deck)+1):

		if index % 2 == 0:
			right.append(deck[index-1])
		else:
			left.append(deck[index-1])


def print_deck_get_input_then_switch_if_yes(message, left_side, right_side, flip=False):
	print(f'\n{message}')
	
	if flip:
		print_deck('- ', left_side)
	else:
		print_deck('- ', right_side)

	while True:
		user_input = input(': ').lower()

		if user_input == 'yes':
			deck = right_side + left_side
		elif user_input == 'no':
			deck = left_side + right_side
		else:
			print('ERROR: \'Yes\' or \'No\' answers only...')
			continue
		break

	return deck


print('\nChoose a card from the below set of cards:')
print('- King of Clubs')
print('- King of Hearts')
print('- King of Spades')
print('- King of Diamonds')
print('- Queen of Clubs')
print('- Queen of Hearts')
print('- Queen of Spades')
print('- Queen of Diamonds')

print('\nThis program will try to guess it even if you didn\'t say it')
getpass('Press \'ENTER\' key to continue...')

# ROUND 1
deck_of_cards = print_deck_get_input_then_switch_if_yes('Does this set include your card?', left_deck, right_deck)

# ROUND 2
shuffle_deck(deck_of_cards, left_deck, right_deck)
deck_of_cards = print_deck_get_input_then_switch_if_yes('How about in this set?', right_deck, left_deck, True)

# ROUND 3
shuffle_deck(deck_of_cards, left_deck, right_deck)
deck_of_cards = print_deck_get_input_then_switch_if_yes('How about this one?', left_deck, right_deck)

# REVELATION
shuffle_deck(deck_of_cards, left_deck, right_deck)
deck_of_cards = left_deck + right_deck

# Determine the chosen card
chosen_card = deck_of_cards[1]

print('\n\nYou\'re thinking of {} of {}!\n'.format(chosen_card['rank'],chosen_card['suit']))

getpass('\nAmazing isn\'t it? Press \'ENTER\' to exit the program')