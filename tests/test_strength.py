from pocker.card import Rank, Hand, Card, Suit
from pocker.strength import HandStrengthEvaluation

def test_high_card():
    """Test that a hand with no pairs is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.KING),
            Card(Suit.CLUBS, Rank.QUEEN),
            Card(Suit.SPADES, Rank.JACK),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert not eval.has_pair()
    assert not eval.has_two_pair()
    assert not eval.has_three_of_a_kind()
    assert not eval.has_straight()
    assert not eval.has_flush()


def test_pair():
    """Test that a pair is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.QUEEN),
            Card(Suit.SPADES, Rank.JACK),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert eval.has_pair()
    assert not eval.has_two_pair()
    assert not eval.has_three_of_a_kind()
    assert not eval.has_full_house()


def test_two_pair():
    """Test that two pair is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.KING),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert eval.has_pair()
    assert eval.has_two_pair()
    assert not eval.has_three_of_a_kind()
    assert not eval.has_full_house()


def test_three_of_a_kind():
    """Test that three of a kind is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert not eval.has_pair()  # Three of a kind is not a pair
    assert not eval.has_two_pair()
    assert eval.has_three_of_a_kind()
    assert not eval.has_full_house()


def test_full_house():
    """Test that full house is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.KING),
        ])
    )
    assert eval.has_pair()
    assert not eval.has_two_pair()  # Full house is not two pair
    assert eval.has_three_of_a_kind()
    assert eval.has_full_house()


def test_four_of_a_kind():
    """Test that four of a kind is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.SPADES, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
        ])
    )
    assert not eval.has_pair()  # Four of a kind is not a pair
    assert not eval.has_two_pair()
    assert not eval.has_three_of_a_kind()  # Four of a kind is not three of a kind
    assert eval.has_four_of_a_kind()
    assert not eval.has_full_house()


def test_straight_low():
    """Test low straight (2-3-4-5-6)."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.THREE),
            Card(Suit.CLUBS, Rank.FOUR),
            Card(Suit.SPADES, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SIX),
        ])
    )
    assert eval.has_straight()
    assert not eval.has_flush()
    assert not eval.has_straight_flush()


def test_straight_mid():
    """Test middle straight (5-6-7-8-9)."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.FIVE),
            Card(Suit.DIAMONDS, Rank.SIX),
            Card(Suit.CLUBS, Rank.SEVEN),
            Card(Suit.SPADES, Rank.EIGHT),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert eval.has_straight()
    assert not eval.has_flush()


def test_straight_high():
    """Test high straight (10-J-Q-K-A)."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TEN),
            Card(Suit.DIAMONDS, Rank.JACK),
            Card(Suit.CLUBS, Rank.QUEEN),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.ACE),
        ])
    )
    assert eval.has_straight()
    assert not eval.has_flush()
    assert not eval.has_royal_flush()  # Not all same suit


def test_straight_wheel():
    """Test wheel straight (A-2-3-4-5) - Ace low."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.TWO),
            Card(Suit.CLUBS, Rank.THREE),
            Card(Suit.SPADES, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
        ])
    )
    assert eval.has_straight()
    assert not eval.has_flush()


def test_straight_not_consecutive():
    """Test that non-consecutive cards are not a straight."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.FOUR),
            Card(Suit.CLUBS, Rank.SIX),
            Card(Suit.SPADES, Rank.EIGHT),
            Card(Suit.HEARTS, Rank.TEN),
        ])
    )
    assert not eval.has_straight()


def test_straight_with_gap():
    """Test that cards with a gap are not a straight."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.THREE),
            Card(Suit.CLUBS, Rank.FOUR),
            Card(Suit.SPADES, Rank.SIX),
            Card(Suit.HEARTS, Rank.SEVEN),
        ])
    )
    assert not eval.has_straight()


def test_flush():
    """Test that a flush is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.JACK),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert eval.has_flush()
    assert not eval.has_straight()  # Not consecutive
    assert not eval.has_straight_flush()


def test_flush_different_suits():
    """Test that mixed suits are not a flush."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.KING),
            Card(Suit.CLUBS, Rank.QUEEN),
            Card(Suit.SPADES, Rank.JACK),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert not eval.has_flush()


def test_straight_flush():
    """Test that a straight flush is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SIX),
        ])
    )
    assert eval.has_straight()
    assert eval.has_flush()
    assert eval.has_straight_flush()
    assert not eval.has_royal_flush()


def test_straight_flush_high():
    """Test high straight flush (not royal)."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.NINE),
            Card(Suit.HEARTS, Rank.TEN),
            Card(Suit.HEARTS, Rank.JACK),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.KING),
        ])
    )
    assert eval.has_straight()
    assert eval.has_flush()
    assert eval.has_straight_flush()
    assert not eval.has_royal_flush()  # Missing Ace


def test_royal_flush():
    """Test that a royal flush is correctly identified."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.JACK),
            Card(Suit.HEARTS, Rank.TEN),
        ])
    )
    assert eval.has_straight()
    assert eval.has_flush()
    assert eval.has_straight_flush()
    assert eval.has_royal_flush()


def test_royal_flush_different_suit():
    """Test royal flush with different suit."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.SPADES, Rank.ACE),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.SPADES, Rank.QUEEN),
            Card(Suit.SPADES, Rank.JACK),
            Card(Suit.SPADES, Rank.TEN),
        ])
    )
    assert eval.has_royal_flush()


def test_royal_flush_wrong_ranks():
    """Test that A-K-Q-J-9 is not a royal flush (wrong ranks)."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.JACK),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert not eval.has_straight()  # Not consecutive
    assert eval.has_flush()
    assert not eval.has_straight_flush()
    assert not eval.has_royal_flush()


def test_royal_flush_wrong_suit():
    """Test that A-K-Q-J-10 with mixed suits is not a royal flush."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.KING),
            Card(Suit.CLUBS, Rank.QUEEN),
            Card(Suit.SPADES, Rank.JACK),
            Card(Suit.HEARTS, Rank.TEN),
        ])
    )
    assert eval.has_straight()
    assert not eval.has_flush()
    assert not eval.has_straight_flush()
    assert not eval.has_royal_flush()


def test_edge_case_two_pair_vs_full_house():
    """Test that two pair is not confused with full house."""
    # Two pair: A-A-K-K-9
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.KING),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.NINE),
        ])
    )
    assert eval.has_pair()
    assert eval.has_two_pair()
    assert not eval.has_three_of_a_kind()
    assert not eval.has_full_house()


def test_edge_case_three_of_a_kind_not_pair():
    """Test that three of a kind does not count as a pair."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
        ])
    )
    assert not eval.has_pair()  # Three of a kind is not a pair
    assert eval.has_three_of_a_kind()


def test_edge_case_four_of_a_kind_not_three():
    """Test that four of a kind does not count as three of a kind."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.SPADES, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
        ])
    )
    assert not eval.has_three_of_a_kind()
    assert eval.has_four_of_a_kind()


def test_edge_case_straight_with_duplicate_ranks():
    """Test straight detection with potential duplicate ranks (shouldn't happen in poker but test robustness)."""
    # This shouldn't happen in real poker, but test that our logic handles it
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.THREE),
            Card(Suit.CLUBS, Rank.FOUR),
            Card(Suit.SPADES, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SIX),
        ])
    )
    assert eval.has_straight()


def test_edge_case_straight_not_all_same_suit():
    """Test that a straight with mixed suits is not a straight flush."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.DIAMONDS, Rank.THREE),
            Card(Suit.CLUBS, Rank.FOUR),
            Card(Suit.SPADES, Rank.FIVE),
            Card(Suit.HEARTS, Rank.SIX),
        ])
    )
    assert eval.has_straight()
    assert not eval.has_flush()
    assert not eval.has_straight_flush()


def test_edge_case_wheel_straight_flush():
    """Test wheel straight flush (A-2-3-4-5 all same suit)."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.TWO),
            Card(Suit.HEARTS, Rank.THREE),
            Card(Suit.HEARTS, Rank.FOUR),
            Card(Suit.HEARTS, Rank.FIVE),
        ])
    )
    assert eval.has_straight()
    assert eval.has_flush()
    assert eval.has_straight_flush()
    assert not eval.has_royal_flush()  # Wheel is not royal flush


def test_edge_case_almost_straight():
    """Test hand that is almost a straight but has a gap."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.TWO),
            Card(Suit.CLUBS, Rank.THREE),
            Card(Suit.SPADES, Rank.FOUR),
            Card(Suit.HEARTS, Rank.SIX),  # Gap at 5
        ])
    )
    assert not eval.has_straight()


def test_edge_case_almost_flush():
    """Test hand that is almost a flush but has one different suit."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.JACK),
            Card(Suit.DIAMONDS, Rank.NINE),  # Different suit
        ])
    )
    assert not eval.has_flush()


def test_edge_case_full_house_not_two_pair():
    """Test that full house does not count as two pair."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.ACE),
            Card(Suit.CLUBS, Rank.ACE),
            Card(Suit.SPADES, Rank.KING),
            Card(Suit.HEARTS, Rank.KING),
        ])
    )
    assert not eval.has_two_pair()  # Full house is not two pair
    assert eval.has_full_house()


def test_edge_case_hand_with_fewer_than_five_cards():
    """Test that hands with fewer than 5 cards cannot be straights or flushes."""
    eval = HandStrengthEvaluation(
        Hand([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.JACK),
        ])
    )
    assert not eval.has_straight()
    assert not eval.has_flush()  # Need 5 cards for a flush
    assert not eval.has_straight_flush()
    assert not eval.has_royal_flush()
