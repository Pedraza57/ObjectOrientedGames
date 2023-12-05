import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

##################################Playing is true to start playing 
playing = True

##################################SETTING UP EACH CARD IN CLASSES 
class Card:
    
    def __init__(self,rank, suit):
        self.rank = rank
        self.suit = suit
        
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

##################################SETTING UP THE DECK 
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    ######PRINT THE DECK OUT IF NEEDED       
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f'The deck has: {deck_comp}'
                                 
    ####SHUFFLE THE DECK
    def shuffle(self):
        random.shuffle(self.deck)
    ####TAKE ONE CARD FROM THE DECK    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
##################################SET UP EACH PLAYERS HAND 
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    #######ADD CARDS TO EACH HAND PLAYER
    def add_card(self,card):
        ###how does it know it comes form Deck.deal() 
        self.cards.append(card)
        self.value += values[card.rank]
        
        #####Track access
        if card.rank == 'Ace':
            self.aces += 1
        
    #########ADJUSTING ACES 11 OR 1    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

##################################STARTING UP CHIPS TO 100  PLAYER
class Chips:
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    #########IF WIN ADD TO THE TOTAL    
    def win_bet(self):
        self.total += self.bet

    #########IF LOSEE SUBTRAC  TO THE TOTAL   
    def lose_bet(self):
        self.total -= self.bet



##################################HOW MUCH WOULD YOU LIKE TO BET FUNCTION
def take_bet(chips):
    
    while True: 
        try:
            chips.bet = int(input('How much would you like to bet?: '))
            
        except:
            print('Sorry you provided invalid number')
        else:
            if chips.bet > chips.total:
                print(f'Sorry you dont have enough chips! you have {chips.total}')
            else:
                break


###############################HIT FUNCTION
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

############################### if you want to stay 
def hit_or_stand(deck, hand):
    global playing 
    
    while True:
        x = input('Hit or Stand? enter h or s: ')
        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print('Player Stands Dealers Turn')
            playing = False

        else:
            print('Sorry please only enter s or h')
            continue
        break

###############################show part or the cards Dealers and players
def show_some(player, dealer):
    
    #show one card of the dealer
    print('\n Dealer hand: ')
    print('first card hidden!')
    print(dealer.cards[1])
    
    
    #show two cards of the player
    print('\n Players hand: ')
    for card in player.cards:
        print(card)
        

def show_all(player, dealer):
    
    #show all the dealers card
    print('\n dealers hand: ')
    for card in dealer.cards:
        print(card)
        
    #calculate and display value
    print(f'value of Dealers hand is: {dealer.value}')
    
    #show all players cards
    print('\n Players hand: ')
    for card in player.cards:
        print(card)
    print(f'value of Player hand is: {player.value}')


def player_busts(player,dealer,chips):
    print('Bust Player')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Player wins!!! Dealer busts')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player,dealer,chips):
    print('Dealer and player tie! push')



while True:
    #Opening statement
    print('WELCOME TO BLACKJACK')
    
    #Creaate and suffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    #set up players chips
    player_chips = Chips()

    #prompt the player for the bet
    take_bet(player_chips)

    #show cards (but keep one from the dealers hand hidden)
    show_some(player_hand, dealer_hand) 


    while playing: ## from hit_or_stand function
        
        #player hit or stand
        hit_or_stand(deck,player_hand)

        #show cards (but keep one card hidden)
        show_some(player_hand, dealer_hand)

        #if players hand exceeds 21 run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    #if player has not busted, play dealer's ahdn until dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        #show all cards
        show_all(player_hand, dealer_hand)

        #Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    #show player his chips 
    print(f'\n player total chips are at {player_chips.total}')

    #new game
    new_game = input('Would you like to play again? yes or no: ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing! ')
        break



