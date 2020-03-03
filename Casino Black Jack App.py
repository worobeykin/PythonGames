#Casino Black Jack App
import random, time

class Card():
    """Simulate a single card with rank, value, and suit."""
    
    def __init__(self, rank, value, suit):
        """Initialize card attributes"""
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        """Show the rank and suit of an individual card."""
        print(self.rank + " of " + self.suit)
        
class Deck():
    """Simulate a deck of 52 individual playing cards."""
    
    def __init__(self):
        self.cards = []

    def build_deck(self):
        """Build a deck consisting of 52 unique cards."""
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = {
            '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11,
            }
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)
            
    def shuffle_deck(self):
        """Shuffle a deck of cards"""
        random.shuffle(self.cards)

    def deal_card(self):
        """Remove a card from the deck to be dealt."""
        card = self.cards.pop()
        return card
        
class Player():
    """A class for the user to play Black Jack."""
    
    def __init__(self):
        """Initialize card into hand"""
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        """Deal the players starting hand"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Display hand results"""
        print("\nThe player's hand:")
        for card in self.hand:
            card.display_card()

    def hit(self, deck):
        """Built hand"""
        card = deck.deal_card()
        self.hand.append(card)

    def get_hand_value(self):
        """Get value from hand"""
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
            
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print("Total value: " + str(self.hand_value))

    def update_hand(self, deck):
        """Update hand"""
        if self.hand_value < 21:
            choice = input("\nWhould you like to hit another card?(y/n): ").lower()
            if choice == 'y':
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False
            
class Dealer():
    """A class simulating the black jack dealer. They must hit up to 17 and they must reveal their first card."""

    def __init__(self):
        """Initialize the dealer"""
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        """Deal the dealers starting hand"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Show the dealers hand one card at a time."""
        input("\nPress enter to reveal the dealer's hand. ")
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def hit(self, deck):
        """The dealer must hit until they have reached 17, then they stop."""
        self.get_hand_value()

        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
            print("\nDealer is set with a total of " + str(len(self.hand)) + " cards.")

    def get_hand_value(self):
        """Compute the value of the dealers hand."""
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
            if self.hand_value > 21 and ace_in_hand:
                self.hand_value -= 10


class Game():
    """A class to hold bets and payouts"""

    def __init__(self, money):
        """Initialize attributes"""
        self.money =int(money)
        self.bet = 20
        self.winner = ""

    def set_bet(self):
        """Get a users bet for a hand of black jack."""
        betting = True
        while betting:
            bet = int(input("What would you like to bet (minimum bet of 20): "))
            if bet < 20:
                bet = 20
            if bet > self.money:
                print("Sorry, you can't afford that bet.")
            else:
                self.bet = bet
                betting = False

    def scoring(self, p_value, d_value):
        """Score a round of black jack."""
        if p_value == 21:
            print("You got BLACK JACK!!! You win!")
            self.winner = 'p'
        elif d_value == 21:
            print("The dealer got black jack...You loose!")
            self.winner = 'd'
        elif p_value > 21:
            print("You went over 21...You loose!")
            self.winner = 'd'
        elif d_value > 21:
            print("Dealer went over 21! You win!")
            self.winner = 'p'
        else:
            if p_value > d_value:
                print("Dealer gets " + str(d_value) + ". You win!")
                self.winner = 'p'
            elif d_value > p_value:
                print("Dealer gets " + str(d_value) + ". You loose.")
                self.winner = 'd'
            else:
                print("Dealer gets " + str(d_value) + ". It's a push...")
                self.winner = 'tie'

    def payout(self):
        """Update the money attribute based on who won a hand."""
        if self.winner == 'p':
            self.money += self.bet
        elif self.winner == 'd':
            self.money -= self.bet
    
    def display_money(self):
        """Display current money for the overall game"""
        print("\nCurrent Money: $" + str(self.money))

    def display_money_and_bet(self):
        """Display the current money and bet for a game round."""
        print("\nCurrent Money: $" + str(self.money) + "\t\tCurrent Bet: $" +
        str(self.bet))

#Main Code
print("Welcome to the Casino Blackjack App")
print("The minimum bet at this table is $20.")

money = int(input("\nHow much money are you willing to play with today: "))
game = Game(money)

playing = True
while playing:
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    player = Player()
    dealer = Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    game.display_money_and_bet()
    print("The dealer is showing a " + dealer.hand[0].rank + " of " + dealer.hand[0].suit + ".")

    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.money < 20:
        playing = False
        print("Sorry, you ran out of money. Please try again.")



