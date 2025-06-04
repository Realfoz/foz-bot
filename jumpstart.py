from random import sample
from jumpstart_sets import JUMPSTART_SETS

#the discord message on activation - logs which sets are requested and players in the game. includes 5 min time out if no player 2



#the deck selection and formatting

pool = list(JUMPSTART_SETS["JMP"].keys()) # this is the list the various sets will be added to. it will take sets by 3 letter MTG code
picked = sample(pool,k=4) # from the varied themes in the pool it will select 4 to make the 2 decks
deck1 = picked[2:] # not the most fair way to split but i am very lazy
deck2 = picked[:2]
print(deck1)


#deck distribution




