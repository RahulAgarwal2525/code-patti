from base_bot import BaseBot
from rules import Rules

class PracticeBot(BaseBot):
    def choose_card(self, top_card):
        for card in self.hand:
            if Rules.is_valid_move(card, top_card):
                return card
        return None
