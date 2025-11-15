import random
from enum import Enum
from typing import Iterator


class Suit(Enum):
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"


SUIT_ASCII = {
    Suit.HEARTS: "♥",
    Suit.DIAMONDS: "♦",
    Suit.CLUBS: "♣",
    Suit.SPADES: "♠",
}


class Rank(Enum):
    ACE = "ace"
    KING = "king"
    QUEEN = "queen"
    JACK = "jack"
    TEN = "ten"
    NINE = "nine"
    EIGHT = "eight"
    SEVEN = "seven"
    SIX = "six"
    FIVE = "five"
    FOUR = "four"
    THREE = "three"
    TWO = "two"


RANK_ASCII = {
    Rank.ACE: "A",
    Rank.KING: "K",
    Rank.QUEEN: "Q",
    Rank.JACK: "J",
    Rank.TEN: "10",
    Rank.NINE: "9",
    Rank.EIGHT: "8",
    Rank.SEVEN: "7",
    Rank.SIX: "6",
    Rank.FIVE: "5",
    Rank.FOUR: "4",
    Rank.THREE: "3",
    Rank.TWO: "2",
}


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    @classmethod
    def random(cls) -> "Card":
        return Card(
          random.choice(list(Suit)),
          random.choice(list(Rank))
        )

    def __str__(self):
        return f"{RANK_ASCII[self.rank]}{SUIT_ASCII[self.suit]}"

    def __repr__(self):
        return f"Card(suit={self.suit.value}, rank={self.rank.value})"


class Game:
    pass


class Player:
    pass


class Hand:
    """A hand is a collection of cards."""

    def __init__(self, cards: list[Card] = []):
        self.cards = cards

    @classmethod
    def random(cls, size: int = 5) -> "Hand":
        return Hand([Card.random() for _ in range(size)])

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __str__(self):
        if len(self) == 0:
            return "<Empty hand>"
        return ", ".join([str(card) for card in self.cards])


class Deck:
    def __init__(self, shuffled: bool = True):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

        if shuffled:
            self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def draw_cards(self, count: int = 1) -> list[Card]:
        return [self.cards.pop() for _ in range(count)]

    def __str__(self):
        card_strs = [str(card) for card in self.cards]
        lines = []
        for i in range(0, len(card_strs), 13):
            line = ", ".join(card_strs[i : i + 13])
            lines.append(line)
        return ",\n".join(lines)


if __name__ == "__main__":
    hand = Hand.random()
    print(hand)
