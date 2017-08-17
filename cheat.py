#coding: utf8
import random


class Card(object):

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
		super(Card, self).__init__()
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return "[" + i.rank + "," + i.suit + "]"	

class Deck(object):

	def __init__(self):
		super(Deck, self).__init__()
		self.cards = []

	def generate(self):
		self.cards.clear()
		for s in Card.SUITS:
			suit = Card.SUITS[s]
			for r in Card.RANKS:
				rank = Card.RANKS[r]
				self.cards.append(Card(rank, suit))

	#def __str__(self):
		#return '[{}, {}]'.format(self)



d = Deck()
d.generate()
for i in d.cards:
	print(i)