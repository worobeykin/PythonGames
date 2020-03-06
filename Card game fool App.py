#Card game fool
import random

class Card():
    def __init__(self):
        self.card_value = ''
        self.suit = ''
        self.weight = 0
        self.visible = False # Рубашка

        
class Deck():
    def __init__(self):
        self.deck = [] # Колода карт
        self.card_amount = 36
        self.trump = '' # Козырь
        self.turn = False #Очередность хода
        self.flag_hoda = bool 

        
    def define_deck(self):
        
        suits = ['черви', 'пики', 'бубны', 'крести'] #Масть : черви пики бубны крести
        card_values = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'] # Значения карт
        weights = [6, 7, 8, 9, 10, 11, 12, 13, 14] # Вес карты
        for suit in suits:
            for card in card_values:
                value = ['', '', '']
                value[0] = suit
                value[1] = card                              
                value[2] = weights[0+card_values.index(card)]
                
                current_card = Card()
                current_card.card_value = card
                current_card.suit = suit
                current_card.weight = weights[0+card_values.index(card)]
                self.deck.append(current_card)
        self.card_amount = len(self.deck)

#        self.trump = random.choice(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

                  
class Players():
    def __init__(self):
        self.hand = []
        
        

      

class Field():
    def __init__(self):

        self.field = []
        self.beaten = []
        

def razdaca_cards(player, computer, player_winner = False):
    if deck.card_amount !=0:

        if player_winner:
            while len(player.hand) < 6:            
                player.hand.append(deck.deck.pop())
            while len(computer.hand) < 6:                         
                computer.hand.append(deck.deck.pop())
            
        else:
            while len(computer.hand) < 6:                         
                computer.hand.append(deck.deck.pop())
            while len(player.hand) < 6:            
                player.hand.append(deck.deck.pop())
          

        
        deck.card_amount = len(deck.deck)
        if len(deck.deck) == 24:
                deck.trump = random.choice(deck.deck) #Определяем козырь
                deck.deck.remove(deck.trump)
                deck.deck.append(deck.trump)
                
        return True

            
    else:
        return False #No cards in deck

    


def which_first(player, computer, deck):
    min_card = 14
    flag = False
    for card in player.hand:
        if card.suit == deck.trump.suit and card.weight <= min_card:
            min_card = card.weight
    for card in computer.hand:
        if card.suit == deck.trump.suit and card.weight <= min_card:
            flag = True
            break        
    return flag

def sord_hand(hand, mast):
    N = len(hand.hand)

    sort_hand = []
    for i in range(N-1):
        for j in range(N-i-1):
            temp = hand.hand[j].weight
            temp2 = hand.hand[j+1].weight
            if hand.hand[j].suit == mast:
                temp += 10
            if hand.hand[j+1].suit == mast:
                temp2 += 10
                
            if temp > temp2:
                hand.hand[j], hand.hand[j+1] = hand.hand[j+1], hand.hand[j]
    return hand
        
def sord_field(field):
    N = len(field.field)
    sord_field = []
    for i in range(N-1):
        for j in range(N-i-1):
            
                
            if field.field[j].weight > field.field[j+1].weight:
                field.field[j], field.field[j+1] = field.field[j+1], field.field[j]
    return field.field

                
    
    

def ataka(current_player, field, whose_turn):
    
    current_card = Card()
    if len(field.field) == 0:
        print("TEST")
        
#        if whose_turn:  
        current_card = current_player.hand[0]
#        print(current_player.hand[0].card_value)
        current_player.hand.remove(current_card)
            
#            sord_hand(computer, deck.trump.suit)
            
        field.field.append(current_card)
        if whose_turn == False:
            deck.turn = True
        else:
            deck.turn = False
        
#        else:
            
#            current_card = player.hand[0]
#            player.hand.remove(current_card)
            
#            sord_hand(player, deck.trump.suit)
            
#            field.field.append(current_card)
#            deck.turn = True

    else:
        
        temp = sord_field(field)
        play = False
        
#        if whose_turn:
        for card in temp:
            for card_hand in current_player.hand:
                if card.weight == card_hand.weight:
                    current_card = card_hand
                    field.field.append(current_card)
                    current_player.hand.remove(current_card)
                    if whose_turn == False:
                        deck.turn = True
                    else:
                        deck.turn = False
                    play = True
                    break
##        else:
##            for card in temp:
##                for card_hand in player.hand:
##                    if card.weight == card_hand.weight:
##                        current_card = card_hand
##                        field.field.append(current_card)
##                        player.hand.remove(current_card)
##                        deck.turn = True
##                        play = True
##                        break
        if not play:
            
            deck.flag_hoda = False
         
                    
            

#    print("\n", current_card.card_value, current_card.suit)
    return current_card
                
                
def zashita(current_player, field, current_card, whose_turn):

#    current_card = Card()

#    if whose_turn:
##        if len(field.field) == 0:
##            current_card = computer.hand[0]
##            computer.hand.remove(current_card)
##            deck.turn = False
           
    for card in current_player.hand:
        flag = True  
        if card.suit == current_card.suit and card.weight > current_card.weight and flag:
            flag = False   
            current_card2 = card
            print("sf")
            current_player.hand.remove(current_card2)
#                two_cards.append(current_card)
            field.field.append(current_card2)
#                deck.turn = False
            if whose_turn == False:
                deck.turn = True
            else:
                deck.turn = False
            deck.flag_hoda = True
            flag = False 
            
            break
       
        if current_card.suit != deck.trump.suit and card.suit == deck.trump.suit and flag:
            current_card2 = card
            current_player.hand.remove(current_card2)
#                two_cards.append(current_card)
            field.field.append(current_card2)
#                deck.turn = False
            if whose_turn == False:
                deck.turn = True
            else:
                deck.turn = False
            deck.flag_hoda = True
            break
        
        else:
            
            deck.flag_hoda = False
#            step = False
    if deck.flag_hoda == False:
        current_player.hand.extend(field.field)

#    print("TEST")
#    if not deck.turn:

##        if not step:    
##            deck.flag_hoda = False
##            current_player.hand.extend(field.field)
##            field.field.clear()

##    else:
####        if len(field.field) == 0:
####            current_card = player.hand[0]
####            computer.hand.remove(current_card)
####            deck.turn = False
##            
##        for card in player.hand:
##            if (card.suit == current_card.suit and card.weight > current_card.weight) or (current_card.suit != deck.trump.suit and card.suit == deck.trump.suit):
##                current_card2 = card
##                player.hand.remove(current_card2)
###                two_cards.append(current_card)
##                field.field.append(current_card2)
##                deck.turn = True
##                deck.flag_hoda = True
##                break
##            
##        print("TEST")
##        if deck.turn:
##            
##            deck.flag_hoda = False
##            player.hand.extend(field.field)    
##            field.field.clear()
                
    print("\nОтбиваемся картой: ", current_card2.card_value, current_card2.suit)
    return current_card2
    
    



#def update(player, computer, player_winner = False):
#    razdaca_cards(player, computer, player_winner = False):
    


def display(deck, user, comp, current_card, field):
    print("Козырь: ", deck.trump.card_value, deck.trump.suit)

    print("\nКарты игрока:", end=' ')
    for i in user.hand:
        print(i.card_value, i.suit, end='; ')

    print("\n\nКарты компьютера:", end=' ')
    for i in comp.hand:
        print(i.card_value, i.suit, end='; ')
    print("\n\nКарт в колоде:", deck.card_amount)
    
    for i in deck.deck:
        print(i.card_value, i.suit, end='; ')
 

    print("\n\nТекущая карта:")
#    for i in deck.deck:
    print(current_card.card_value, current_card.suit, end='; ')

    print("\n\nТекущая поле:")
    for i in field.field:
        print(i.card_value, i.suit, end='; ')
    

def monitor(deck, user, comp, current_card, field):
    
    print("\nКарт в колоде:" + str(deck.card_amount) + " Козыри: " + deck.trump.suit.upper())    
    for i in deck.deck:
        print(i.card_value, i.suit, end='; ')

    print("\n\nКарты игрока:", end=' ')
    for i in user.hand:
        print(i.card_value, i.suit, end='; ')

    print("\n\nКарты компьютера:", end=' ')
    for i in comp.hand:
        print(i.card_value, i.suit, end='; ')
    

    if deck.turn:
        print("\n\nХодит Компьютер" )
    else:
        print("\n\nХодит Игрок" )

    print("\n\t\tТекущая поле:")
    if len(field.field) != 0:
        for i in field.field:
            print(i.card_value, i.suit)
    
        
        
    



    
#Main code

playing = True
while playing:
    deck = Deck()
    deck.define_deck()
    deck.shuffle()

    user = Players()
    comp = Players()
    current_player = Players()

    field = Field()
    current_card = Card()
    winner = False


    game_round = True
    while game_round:

        field.field.clear()

        razdaca_cards(user, comp, winner)

        user = sord_hand(user, deck.trump.suit)
        comp = sord_hand(comp, deck.trump.suit)

        if len(deck.deck) == 24:
            deck.turn = which_first(user, comp, deck)

        

        monitor(deck, user, comp, current_card, field)
        
#        current_card = every_step(user, comp, field, current_card, deck.turn)
#        field.field.append(current_card)    
        
        step = True
        deck.flag_hoda = True
        while deck.flag_hoda:
#            if len(field.field) == 0:

            if deck.turn == True:
                current_player = comp
            else:
                current_player = user

            current_card = ataka(current_player, field, deck.turn)
 
            if step:

                if deck.turn == True:
                    current_player = comp
                else:
                    current_player = user
                current_card2 = zashita(current_player, field, current_card, deck.turn)


            else:
                break
##            ataka()
##            if ataka == True:
##                current_card = ataka(current_player, field, deck.turn)
##                zashita()
##                if zashita == True:
##                    current_card = zashita(current_player, field, current_card, deck.turn)
##                else:
##                    add_to_hand()
##
##
##            else:
##                zashita(current_player, field, current_card, deck.turn)
##                if zashita == False:
##                    uhod_v_bitu()
##                    deck.flag_hoda = False
                    
#                deck.flag_hoda = False
                
            

            monitor(deck, user, comp, current_card2, field)
            
            

            input()









