from base_bot import BaseBot
from rules import Rules
import random

class Player(BaseBot):
    def choose_card(self, top_card):
        for card in self.hand:
            if card in {"WC", "PC"}:
                color_counts = [c[0] for c in self.hand if c[0] in 'RGBY']
                best_color = max(set(color_counts), key=color_counts.count, default='R')
                return f"{card[0]}{best_color}"
            elif Rules.is_valid_move(card, top_card):
                return card
        return None
