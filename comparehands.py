from card import Rank, Hand, Card, Suit
from strength import HandStrengthEvaluation, HandStrengthEvaluator, HandStrength

class CompareHand:
    def compare(self, hand1: Hand, hand2: Hand) -> int:
        """Compare two hands and return:
        - 1 if hand1 is stronger
        - -1 if hand2 is stronger
        - 0 if they are equal
        """
        strength1: HandStrength = HandStrengthEvaluator(hand1)
        strength2: HandStrength = HandStrengthEvaluator(hand2)

        if strength1.value > strength2.value:
            return 1
        elif strength1.value < strength2.value:
            return -1

        # Continue with other hand rankings...

        return 0  # Placeholder for equal hands