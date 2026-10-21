import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]   # 11 is an ace


class Hand:
    """A blackjack hand: the cards held and how to score them."""

    def __init__(self):
        """Start with no cards."""
        self.cards = []

    def add_card(self):
        """Deal one random card onto this hand."""
        self.cards.append(random.choice(CARDS))

    def score(self):
        """Return the hand's score: 0 for a blackjack, aces drop from 11 to 1 if needed."""
        total = sum(self.cards)
        aces = self.cards.count(11)
        if total == 21 and len(self.cards) == 2:
            return 0                       # blackjack
        while total > 21 and aces > 0:
            total -= 10                    # count one ace as 1 instead of 11
            aces -= 1
        return total


def compare(user_score, computer_score):
    """Return a message saying who won."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, the opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "The opponent went over. You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    """Play one round of blackjack against the computer."""
    user_hand = Hand()
    computer_hand = Hand()
    for _ in range(2):
        user_hand.add_card()
        computer_hand.add_card()

    game_over = False
    while not game_over:
        user_score = user_hand.score()
        computer_score = computer_hand.score()
        print(f"  Your cards: {user_hand.cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_hand.cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        elif input("Type 'y' to get another card, 'n' to pass: ") == "y":
            user_hand.add_card()
        else:
            game_over = True

    while computer_hand.score() != 0 and computer_hand.score() < 17:
        computer_hand.add_card()          # dealer plays to 17

    print(f"  Your final hand: {user_hand.cards}, final score: {user_hand.score()}")
    print(f"  Computer's final hand: {computer_hand.cards}, final score: {computer_hand.score()}")
    print(compare(user_hand.score(), computer_hand.score()))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
