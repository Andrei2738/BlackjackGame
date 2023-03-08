import random

class Card:
    def __init__(self, value, suit):
        values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        self.value = values[value]
        self.suit = suit

    def __str__(self):
        return f'|{self.value} {self.suit}|'

# class Player:
#     def __init__(self, name):
#         self.name = name
#
# class Dealer(Player):
#     Player().name = 'Dealer'
#     def shouldIHit(self, currentSum):
#         if currentSum < 17:
#             return True
#         return False
#
# class PlayerNormal(Player):
#     def shouldIHit(self, currentSum):
#         pass
#
# class PlayerAI(Player):
#     def shouldIHit(self, currentSum):
#         if currentSum < 15 + random.nextInt(3):
#             return True
#         return False

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['♥', '♦', '♣', '♠']
        values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
                  'Queen': 10, 'King': 10}
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value

        if card.value == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1

class Game():
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.computer_hand = Hand()

    def play(self):
        self.deck.shuffle()

        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.computer_hand.add_card(self.deck.deal())

    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.computer_hand = Hand()
        self.credits = 1000
        self.bet = 0

    def place_bet(self):
        while True:
            try:
                self.bet = int(input("Enter the bet size (minimum $10): "))
                if self.bet < 10:
                    raise ValueError
                if self.bet > self.credits:
                    print("You don't have enough credits.")
                    raise ValueError
                self.credits -= self.bet
                break
            except ValueError:
                print("Invalid bet size. Please enter a number greater than or equal to 10 and less than your credits.")

    def play(self):
        while True:
            self.place_bet()
            self.play_round()
            self.check_result()
            self.print_balance()
            if self.play_again() == False:
                break

    def play_round(self):
        self.deck.shuffle()
        self.player_hand = Hand()
        self.computer_hand = Hand()
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.computer_hand.add_card(self.deck.deal())
        Hand().adjust_for_ace()
        self.show_player_cards()
        self.show_computer_cards()
        self.player_hit_or_stand()

    def player_hit_or_stand(self):
        while True:
            choice = input("Do you want to hit or stand? ").lower()
            if choice == "hit":
                card = self.deck.deal()
                self.player_hand.add_card(card)
                self.player_hand.adjust_for_ace()
                print("Your cards:")
                for card in self.player_hand.cards:
                    print(card)
                print("Your total:", self.player_hand.value)
                if self.player_hand.value > 21:
                    return
            elif choice == "stand":
                return
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

    def check_result(self):
        if self.player_hand.value > 21:
            print("You lose! Your hand exceeds 21.")
        elif self.computer_hand.value > 21:
            print("You win! Computer's hand exceeds 21.")
            self.credits += self.bet * 2
        elif self.player_hand.value > self.computer_hand.value:
            print("You win!")
            self.credits += self.bet * 2

    def show_computer_cards(self):
        print("\nComputer's cards:")
        for card in self.computer_hand.cards:
            print(card)
        print("Computer's total:", self.computer_hand.value)

    def show_player_cards(self):
        print("\nYour cards:")
        for card in self.player_hand.cards:
            print(card)
        print("Your total:", self.player_hand.value)

    def print_balance(self):
        print("Your balance: ", self.credits)

    def play_again(self):
        choice = input("Do you want to play again? (yes/no)").lower()
        if choice != "yes":
            return False
        else:
            return True


# class Player:
#     def __init__(self, name, cards):
#         self.name = name
#         self.cards = cards
#         self.player_hand = []
#         for i in range(2):
#             self.player_hand.append(random.choice(self.cards))
#         self.regulaUnsprezece()
#
#     def regulaUnsprezece(self):
#         for i, card in enumerate(self.player_hand):
#             if card == 11 and sum(self.player_hand) > 21:
#                 self.player_hand[i] = 1
#                 return self.player_hand
#
# class showPlayerHand:
#     def __init__(self, player):
#         self.player = player
#     def showHands(self):
#         print("Your cards:")
#         for card in self.player.player_hand:
#             print(card)
#         print("Your total:", sum(self.player.player_hand))
#
# deck = Deck()
# game = GameTable("BlackJack", deck)
# player1 = Player("John", deck.cards)
# show_hand = showPlayerHand(player1)
# show_hand.showHands()
#


Game().play()

