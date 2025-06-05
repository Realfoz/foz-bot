

class Player:
    def __init__(self, user):
        self.user = user              # discord.User 
        self.name = user.display_name
        self.deck_types = []          # the 2 type names will be addeed here
        self.full_deck = []           # full combined card list for formatting later
        self.wins = 0
        self.losses = 0
        self.draw = 0                 # for future use, not sure how ide track this lot but we can dream 

    def __str__(self):
        return f"{self.name} ({', '.join(self.deck_types)})"