from random import sample
from JMP import JUMPSTART
from player import Player
from collections import Counter




#the deck selection and formatting
def generate_decks(player):
    pool = list(JUMPSTART) # this is the list the various sets will be added to. it will take sets by 3 letter MTG code
    deck_types = sample(pool,k=2) # from the varied themes in the pool it will select 2 at random
    print(deck_types)
    player.deck_types = deck_types
    format_deck(player) # should pass the whole object so we can keep all the data tidy? probably doesnt matter but w/e



def format_deck(player):
    joined_deck = []
    for type in player.deck_types:
        joined_deck += JUMPSTART[type] #combines the decks

    counted_cards = Counter(joined_deck) # turns them into card:number pairs in a dict

    formatted_deck = ""
    for card, count in counted_cards.items(): #breaks the dict into a string and formats it per line 
        formatted_deck += f"{count} {card}\n"
    player.full_deck = formatted_deck    

    print(f"{player.name} deck created using {player.deck_types}")

    

