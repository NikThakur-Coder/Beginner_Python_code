import random

suits = ('Diamonds', 'Spades', 'Hearts', 'Clubs')
ranks = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


# creating Card Class here

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # self.value=values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# creating Deck Class here

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Creating a Hand Class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        # if total value > 21 and i still have an ACE
        # then change my Ace to 1 from 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


# creating chips class
class Chips:
    def __init__(self, total=100):
        self.total = total  # this can be set as default value or entered by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would u like to bet? :  '))
        except:
            print('Please Enter Integer or Whole number only')
        else:
            if chips.bet > chips.total:
                print('Sorry u dont have enough chips!')
                print(f'You have only {chips.total}')
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("Please enter any of the choice either 'Hit' or 'Stand': ")
        if x.lower() == 'hit':
            hit(deck, hand)
        elif x.lower() == 'stand':
            print("Player stands, dealer's turn")
            playing = False
        else:
            print('Please enter Hit or Stand only')
            continue
        break


def show_some(player, dealer):
    # show only one of the dealer cards
    print("\n Dealer's Hand: ")
    print("First Card Hidden!")
    print(dealer.cards[1])
    # show all the cards at player's hand
    print("\nPlayer's Hands'")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    # show all the dealer's cards
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)
    # print("\n Dealer's Hand: ",*dealer.cards,sep='\n')
    # calculate and display value
    print(f"Value in dealer's hand is {dealer.value}")
    # show all the player's cards
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value in Player's hand is {player.value}")


def player_busts(player, dealer, chips):
    print('Player Lose!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player Win!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('dealer Lose!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('dealer Win!')
    chips.lose_bet()


def push():
    print('Player and dealer tie, PUSH!')


while True:
    print('Welcome to BlackJack')
    # create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # setup the player'schips
    player_chips = Chips()

    # Prompt the player for their bet
    take_bet(player_chips)

    # show cards(But Keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Propmt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # show cards(but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # if Player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # if Player hasn't busted, play Dealer's hand untill Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:

            hit(deck, dealer_hand)

            # show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > 17:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < 17:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        # Inform Player of their Chips total
        print(f'\n Player total chips are at: {player_chips.total}')

        # Ask to play again
        new_game = input('Would you like to play another hand? y/n')
        if new_game[0].lower() == 'y':
            player = True
            continue
        else:
            print('Thank you for playing!')
            break
