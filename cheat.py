#coding: utf8
import random


class Card(object):
	'''
	Card class.

	Used to store the rank and suit of a card.
	'''

	SUITS_LEN = 4
	SUITS = {
		'spades': '♠',
		'hearts': '♥',
		'diamonds': '♦',
		'clubs': '♣'
	}

	RANK_LEN = 13
	RANKS = {
		1: 'A',
		2: '2',
		3: '3',
		4: '4',
		5: '5',
		6: '6',
		7: '7',
		8: '8',
		9: '9',
		10: 'T',
		11: 'J',
		12: 'Q',
		13: 'K'
	}

	def __init__(self, rank, suit):
		'''
		Constructor.

		Args:
			rank: Rank of the card.
			suit: Suit of card.
		'''

		super(Card, self).__init__()
		self.rank = rank
		self.suit = suit


	def __str__(self):
		return "%s%s" % (self.rank, self.suit)


	def __repr__(self):
		return self.__str__()



class Deck(list):

	def __init__(self):
		super(Deck, self).__init__()
		self._generate()

	def _generate(self):
		self.clear()
		for s in Card.SUITS:
			suit = Card.SUITS[s]
			for r in Card.RANKS:
				rank = Card.RANKS[r]
				self.append(Card(rank, suit))

	def shuffle(self):
		random.shuffle(self)
		return self



class Player(list):

	def __init__(self):
		super(Player, self).__init__()



class Game(object):

	START_CARDS_LEN = 13
	START_PLAYERS_LEN = 4

	def __init__(self):
		super(Game, self).__init__()
		self.deck = Deck().shuffle()

		self.players = [ Player() for i in range(self.START_PLAYERS_LEN) ]

		for i in range(len(self.players)):
			c = [ self.deck.pop() for j in range(self.START_CARDS_LEN) ]
			self.players[i].extend(c)



	def play(self):

		for p in circ(players):
			# p joga
			# outros player acusam, ou n, p
			# check(mao vazia)
			# primo p












