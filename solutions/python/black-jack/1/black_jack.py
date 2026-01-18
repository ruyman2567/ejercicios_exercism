"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    integercard= ['2','3','4','5','6','7','8','9','10']
    face_cards = ['J','K','Q']
    if card in face_cards:
        return 10
    elif card == 'A':
        return 1
    elif card in integercard:
        return int(card)


def higher_card(card_one, card_two):
    face_cards = ['J','K','Q']
    if card_one in face_cards and card_two in face_cards:
      return str(card_one), str(card_two)
    elif value_of_card(card_one) == value_of_card(card_two):
      return str(card_one), str(card_two)
    elif ((card_one in face_cards) and (card_two == '10')) or ((card_two in face_cards) and (card_one == '10')):
        return str(card_one), str(card_two)
    elif value_of_card(card_one)> value_of_card(card_two):
        return str(card_one)
    else:
        return str(card_two)
    


def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        return 1
    elif value_of_card(card_one)+value_of_card(card_two)<=10:
        return 11
    else:
      return 1


def is_blackjack(card_one, card_two):
    ten_card= ['J','K','Q','10']
    if (card_one in ten_card and card_two=='A') or (card_two in ten_card and card_one=='A'):
        return True
    else: 
        return False



def can_split_pairs(card_one, card_two):
    return value_of_card(card_one)== value_of_card(card_two)


def can_double_down(card_one, card_two):
    if 9<=(value_of_card(card_one) + value_of_card(card_two))<=11:
        return True    
    else:
        return False