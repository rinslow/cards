from pocker.card import Rank, Hand, Card, Suit
from enum import Enum

# evaluation = [hand_strength, kicker_list]

class HandStrengthEvaluation:
    def __init__(self, hand: Hand):
        self.bitmap = {rank: 0 for rank in Rank}
        self.cards = list(hand)
        for card in hand:
            self.bitmap[card.rank] += 1

    def has_pair(self) -> bool:
        return any(count == 2 for count in self.bitmap.values())

    def has_three_of_a_kind(self) -> bool:
        return any(count == 3 for count in self.bitmap.values())

    def has_four_of_a_kind(self) -> bool:
        return any(count == 4 for count in self.bitmap.values())
        

    def has_full_house(self) -> bool:
        return self.has_three_of_a_kind() and self.has_pair()

    def has_two_pair(self) -> bool:
        pair_count = sum(1 for count in self.bitmap.values() if count == 2)
        return pair_count == 2

    def has_straight(self) -> bool:
        """Check if hand contains a straight, including wheel (A-2-3-4-5) and high straight (10-J-Q-K-A)."""
        if len(self.cards) < 5:
            return False
        
        ranks = [card.rank.value for card in self.cards]
        unique_ranks = sorted(set(ranks))
        
        # Need exactly 5 unique ranks for a straight (no duplicates allowed)
        if len(unique_ranks) != 5:
            return False
        
        # Check for wheel (A-2-3-4-5) - Ace low straight (special case)
        wheel_ranks = {Rank.ACE.value, Rank.TWO.value, Rank.THREE.value, Rank.FOUR.value, Rank.FIVE.value}
        if wheel_ranks == set(unique_ranks):
            return True
        
        # Check for regular straight: 5 consecutive unique ranks
        # For a 5-card hand, we only need to check if max - min == 4
        if unique_ranks[4] - unique_ranks[0] == 4:
            return True
        
        return False

    def has_flush(self) -> bool:
        """Check if all cards are of the same suit."""
        if len(self.cards) < 5:
            return False
        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1

    def has_straight_flush(self) -> bool:
        """Check if hand is both a straight and a flush."""
        return self.has_straight() and self.has_flush()

    def has_royal_flush(self) -> bool:
        """Check if hand is A-K-Q-J-10 all of the same suit."""
        if not self.has_flush():
            return False
        
        required_ranks = {Rank.ACE, Rank.KING, Rank.QUEEN, Rank.JACK, Rank.TEN}
        hand_ranks = {card.rank for card in self.cards}
        return required_ranks == hand_ranks
    
    def has_high_card(self) -> bool:
        """A hand with no pairs or other combinations."""
        return not (self.has_pair() or self.has_two_pair() or self.has_three_of_a_kind() or
                    self.has_straight() or self.has_flush() or self.has_full_house() or
                    self.has_four_of_a_kind() or self.has_straight_flush() or self.has_royal_flush())    

class HandStrength(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

def HandStrengthEvaluator(hand: Hand) -> HandStrength:
    evaluator = HandStrengthEvaluation(hand)
    
    if evaluator.has_royal_flush():
        return HandStrength.ROYAL_FLUSH
    if evaluator.has_straight_flush():
        return HandStrength.STRAIGHT_FLUSH
    if evaluator.has_four_of_a_kind():
        return HandStrength.FOUR_OF_A_KIND
    if evaluator.has_full_house():
        return HandStrength.FULL_HOUSE
    if evaluator.has_flush():
        return HandStrength.FLUSH
    if evaluator.has_straight():
        return HandStrength.STRAIGHT
    if evaluator.has_three_of_a_kind():
        return HandStrength.THREE_OF_A_KIND
    if evaluator.has_two_pair():
        return HandStrength.TWO_PAIR
    if evaluator.has_pair():
        return HandStrength.PAIR
    
    return HandStrength.HIGH_CARD