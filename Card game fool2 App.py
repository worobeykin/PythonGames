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
                deck.card_amount = len(deck.deck)
                if deck.card_amount !=0:
                    player.hand.append(deck.deck.pop())
                else:
                    break
            while len(computer.hand) < 6:
                deck.card_amount = len(deck.deck)
                if deck.card_amount !=0:
                    computer.hand.append(deck.deck.pop())
                else:
                    break
            
        else:
            while len(computer.hand) < 6:
                deck.card_amount = len(deck.deck)
                if deck.card_amount !=0:
                    computer.hand.append(deck.deck.pop())
                else:
                    break
            while len(player.hand) < 6:
                deck.card_amount = len(deck.deck)
                if deck.card_amount !=0:
                    player.hand.append(deck.deck.pop())
                else:
                    break
          

        
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



def zashita(current_player, field, current_card, whose_turn):
    
    for card in current_player.hand:
        flag = True  
        if card.suit == current_card.suit and card.weight > current_card.weight and flag:
            flag = False   
            current_card2 = card
            print("sf")
            current_player.hand.remove(current_card2)

            field.field.append(current_card2)

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

            field.field.append(current_card2)
            
            if whose_turn == False:
                deck.turn = True
            else:
                deck.turn = False
            deck.flag_hoda = True
            break
        
#        else:
            
#            deck.flag_hoda = False

#    if deck.flag_hoda == False:
#        current_player.hand.extend(field.field)

                
#    print("\nОтбиваемся картой: ", current_card2.card_value, current_card2.suit)
    return current_card2





def ataka(current_player, field, whose_turn):
    
    current_card = Card()
    if len(field.field) == 0:
        
        current_card = current_player.hand[0]

        current_player.hand.remove(current_card)
           
        field.field.append(current_card)
        if whose_turn == False:
            deck.turn = True
        else:
            deck.turn = False

    else:
        
        temp = sord_field(field)
        play = False
        flag_break = False

        for card in temp:
            if flag_break:
                break
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
                    flag_break = True
                    break

        if not play:
            
            deck.flag_hoda = False
         
                    
            

#    print("\n", current_card.card_value, current_card.suit)
    return current_card




def ataka_proverka(current_player, field, current_card):
    posibility_ataka = False
    
    if len(current_player.hand) != 0:
        if len(field.field) == 0:        
            posibility_ataka = True

        else:
            temp = sord_field(field)
            for card in temp:
                for card_hand in current_player.hand:
                    if card.weight == card_hand.weight:
                        posibility_ataka = True
                        break
           

       
    return posibility_ataka

def  zashita_proverka(current_player, current_card):
    
    posibility_zashita = False    
    if len(current_player.hand) != 0:
        print("dhgadh")
        for card in current_player.hand:

            if card.suit == current_card.suit and card.weight > current_card.weight:            
                posibility_zashita = True
                break
       
            if current_card.suit != deck.trump.suit and card.suit == deck.trump.suit:
                posibility_zashita = True
                break  
 
        
        
    return posibility_zashita


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
    winner = bool


    game_round = True
    
    while game_round:

        field.field.clear()
        print("очистка")
        for i in field.field:
            print("чистим", i.card_value, i.suit)

        razdaca_cards(user, comp, winner)

        user = sord_hand(user, deck.trump.suit)
        comp = sord_hand(comp, deck.trump.suit)

        if len(deck.deck) == 24:
            deck.turn = which_first(user, comp, deck) # True-computer, False-human

        if deck.turn == True:
            current_player = comp
        else:
            current_player = user

#        monitor(deck, user, comp, current_card, field)
        

        
        step = True
        deck.flag_hoda = True
        while deck.flag_hoda:

#            posibility = ataka_proverka(current_player, field)
            if ataka_proverka(current_player, field, current_card):
                current_card = ataka(current_player, field, deck.turn)
#                print("проверка")

                print("текущая карта", current_card.card_value, current_card.suit)
                
                if deck.turn == True:
                    current_player = comp
                else:
                    current_player = user
                
                if zashita_proverka(current_player, current_card):
                    
                    
                        
                    current_card2 = zashita(current_player, field, current_card, deck.turn)
                    
                    if deck.turn == True:
                        current_player = comp
                    else:
                        current_player = user
                else:
                    if deck.turn == False:
                        current_player = user
                        current_player.hand.extend(field.field)
                        deck.turn = True
                    else:
                        current_player = comp
                        current_player.hand.extend(field.field)
                        deck.turn = False

                    monitor(deck, user, comp, current_card2, field)

#                    current_player.hand.extend(field.field)

                    deck.flag_hoda = False

                    print("Завершение раунда")

                    field.field.clear()
                    
                if len(deck.deck) == 0 and len(current_player.hand) == 0:
                    playing = False
                    game_round = False
                    deck.flag_hoda = False
                    print("Победа курент плеир")
                    break


            else:
#                zashita(current_player, field, current_card, deck.turn)
#                if
##                if deck.turn == False:
##                    deck.turn = True
##                else:
##                    deck.turn = False
                if current_player == user:
                    winner = True
                    deck.turn = True
                else:
                    winner = False
                    deck.turn = False
                    
                    
                deck.flag_hoda = False
                print("Завершение раунда_бито")
                field.field.clear()
#                break
##                 if zashita == False:
##                    uhod_v_bitu()
##                    deck.flag_hoda = False
                    
#                deck.flag_hoda = False
                
            

            monitor(deck, user, comp, current_card2, field)
            
            if len(deck.deck) == 0 and len(current_player.hand) == 0:
                playing = False
                game_round = False
                deck.flag_hoda = False
                print("Победа курент плеир")
                break
                
            

            input()
