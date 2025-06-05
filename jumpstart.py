from random import sample
from JMP import JUMPSTART





#the deck selection and formatting
def generate_decks():
    pool = list(JUMPSTART) # this is the list the various sets will be added to. it will take sets by 3 letter MTG code
    picked = sample(pool,k=4) # from the varied themes in the pool it will select 4 to make the 2 decks
    deck1 = picked[2:] # not the most fair way to split but i am very lazy
    deck2 = picked[:2]
    print(deck1)
    print(deck2)
    return deck1, deck2



#deck distribution




