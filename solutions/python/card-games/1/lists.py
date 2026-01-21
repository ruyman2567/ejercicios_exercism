"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    lista1 = [number,number+1,number+2]
    return lista1


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2


def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    first = hand[0]
    last = hand[len(hand)-1]
    aveg = (first+last)/2 
    return aveg == card_average(hand) or (hand[(len(hand)-1)//2]) == card_average(hand)



def average_even_is_average_odd(hand):
    pares_even=hand[1::2]
    impares_odd=hand[::2]
    return card_average(pares_even) == card_average(impares_odd)


def maybe_double_last(hand):
    last_card=hand[len(hand)-1]
    if last_card == 11:
        last_card= last_card*2
        hand[len(hand)-1]=last_card
        return hand
    else:
        return hand