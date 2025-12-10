import random
import sys
from typing import list, operational, Tuple

RANKS = list(range(1, 14)) # 1 = Ace --- 13 = king
RANK_STR = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
SUITS = ["♠", "♥", "♦", "♣"]
SUIT_COLOR = {"♠": "black", "♣": "black", "♥": "red", "♦": "red"}

class Card:
    def _init_(self, rank: int, suit: str, face_up: bool = False):