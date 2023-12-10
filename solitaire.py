import pygame   # install pygame first
import random   # import random for cards
import arcade   # import component
import math     # import math

58444146689006396979718129993803345527241827678714100506174257132995400407609893249390412898550004713290412360834515837636256992248991022380031529502780259466198206312441621416223090368175605973818721447300410262227823247895707637054743324812873032120129343372818156637738618288630225505886341621096857571308239119249146468073503774392728099005956037095657066136110769529400917847311817333752171535218454222798243649028712057918396926171868216702325269436080099311899882388269464935651070084318587708287244039405410270029750096588971065579366043468651455873814849675421384889944313972544907492129643454045388131273644120639524593099238342449984930681509572894722046396658070246009705343384199736284309051483017902312321831427712055248421679954493598047050424886449671551308530630215001936259458316841710406
"""class Solitaire:

    def __init__(self, cards):
        self.__piles = []
        self.__num_cards = len(cards)
        self.__num_piles = (self.__num_cards // 8) + 3
        self.__max_num_moves = self.__num_cards * 2
        for i in range(self.__num_piles):
            self.__piles.append(CardPile())
        for i in range(self.__num_cards):
            self.__piles[0].add_bottom(cards[i])

    def get_pile(self, i):

        return self.__piles[i]

    def display(self):
        for i in range(self.__num_piles): 
            print(f'{i}: ',end='')
            self.get_pile(i).print_all(i)
    def move(self,p1,p2):
        if p1==0 and p2==0:
            pile=self.__piles[0]
            if pile.size()>0:
                the_card=pile.remove_top()
                result=pile.add_bottom(the_card)
        if p1==0 and p2>0:
            if self.__piles[p2].size()==0:
                the_card=self.__piles[p1].remove_top()
                self.__piles[p2].add_bottom(the_card)
            else:
                the_card=self.__piles[p1].peek_top()
                result=self.__piles[p2].peek_bottom()
                if result-1==the_card:
                    the_card=self.__piles[p1].remove_top()
                    self.__piles[p2].add_bottom(the_card)    
        if p1>0 and p2>0:
            if self.__piles[p2].size()>0:
                the_card=self.__piles[p1].peek_top()
                result=self.__piles[p2].peek_bottom()
                if result-1==the_card:
                    for x in range(self.__piles[p1].size()):
                        the_card=self.__piles[p1].remove_top()
                        self.__piles[p2].add_bottom(the_card)
    def is_complete(self):
        if self.__piles[0].size() == 0:
            all_cards_in_pile = False
            for i in range(1, len(self.__piles)):
                if self.__piles[i].size() == self.__num_cards:
                    all_cards_in_pile = True
            return all_cards_in_pile
        else:
            return False
    
    
    
    
    def play(self):
        print("******************** NEW GAME ****************************")
        move_number=  1
        while move_number <= self.__max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row1 = int(input("Move from row no.:"),10)
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row2 = int(input("Move to row no.:"),10)
            if row1 >= 0 and row2 >= 0 and row1 < self.__num_piles and row2 < self.__num_piles:
                self.move(row1, row2)
            move_number += 1
           
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")"""
                        
                    
            
            
        
    
    
"""class CardPile:
    def __init__(self):
        self.items=[]
    def add_top(self,item):
        self.items.insert(0,item)
    def add_bottom(self,item):
        self.items.append(item)
    def remove_top(self):
        if len(self.items)>0:
            item=self.items[0]
            del self.items[0]
            return item
        return None
    def remove_bottom(self):
        if len(self.items)>0:
            item=self.items.pop()
            return item
        return None
    def size(self):
        return len(self.items)
    def peek_top(self):
        if self.size()>0:
            return self.items[0]
        return None
    def peek_bottom(self):
        if self.size()>0:
            return self.items[len(self.items)-1]
        return None
    def print_all(self, index):
        if self.size()>0:
            if index==0:
                print(self.items[0],end='')
                for i in range(1,self.size()):
                    print(' *',end='')
                print('')
            else:
                for i in range(0,self.size()):
                    print(str(self.items[i])+' ',end='')
                
                print('')
        else:
            print('')"""
#In pygame we need to determine color
# Define the colors that we gonna use in game:
#----------------------
AQUA = (0,255,255)
BLACK = (0,0,0)
GREEN = (0,128,0)
OLIVE = (128,128,0)
TEAL = (0,128,128)
WHITE = (255,255,255)
.
#-----------------------

class Moved_card(object):
    
    """The class shows the cards that will move on the screen"""
    moved = False #This variable is True when there is a card moving on 
    # the screen.
    moved_card = [] #This variable will contain the name of the card.
    card_d = ()
    cards = None #This is object 
    def click_up(self,deck_list):
        """To help player release their mouse button."""
        if len(self.moved_card) > 0:
            for item in deck_list:      
                if not isinstance(item,Solitaire_2):
                    if item.check_pos() and item.check_card(self.moved_card):
                        item.add_card(self.moved_card)
                        self.moved = False
                        self.moved_card = []
                        if isinstance(self.cards,Solitaire_1):
                            self.cards.show_card()
                        self.cards = None
                        break
            else:
                self.cards.add_card(self.moved_card)
                self.moved = False
                self.moved_card = []
                self.cards = None

    def draw(self,screen,card_dict):
        """That draw the moved cards onto the screen"""
        if self.moved:
            pos = pygame.mouse.get_pos()
            x = pos[0] - self.card_d[0]
            y = pos[1] - self.card_d[1]
            for item in self.moved_card:
                screen.blit(card_dict[item],[x,y])
                y += 32
    
class Deck(object):
    """This is a original class"""
    def __init__(self,x,y):
        self.cards = []
        self.rect = pygame.Rect(x,y,71,96)

    def check_pos(self):
        """This check whether the cursor is on the card or not """
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
            if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
            else:
                return False
        else:
            return False

class Solitaire_1(Deck):
    """This is a update class"""
    def __init__(self,x,y):
        #call parent's constructor:
        Deck.__init__(self,x,y)
        self.y = y
        self.hidden = []

    def extend_list(self,lst):
        self.hidden.extend(lst)
        self.cards.append(self.hidden.pop())
        if len(self.hidden) > 0:
            for i in range(len(self.hidden)):
                self.rect.top += 32
        
    def draw_card(self,screen,card_dict):
        """This will display all the cards on the screen"""
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        i = self.y
        if len(self.hidden) > 0:
            for item in self.hidden:
                pygame.draw.rect(screen,TEAL,[self.rect.left,i,71,96])
                pygame.draw.rect(screen,BLACK,[self.rect.left,i,71,96],2)
                i += 32
        if len(self.cards) > 0:
            for item in self.cards:
                screen.blit(card_dict[item],[self.rect.left,i])
                i += 32
                
    def add_top(self,item):
        self.items.insert(0,item)
        
    def add_card(self,card):
        if len(self.cards) > 0 or len(self.hidden) > 0:
            for i in range(len(card)):
                self.rect.top += 32
        else:
            for i in range(len(card)):
                if i > 0:
                    self.rect.top += 32
        self.cards.extend(card)
    def remove_top(self,card):
        if len(self.cards)>0 or len(self.hidden)>0:
            card=self.cards[0]
            del self.cards[0]
            return card
        return None
    def click_down(self,card):
        """This is used when the player click the mouse button"""
        if len(self.cards) > 0:
            top = self.rect.top
            lst = []
            for i in range(len(self.cards)):
                if self.check_pos():
                    pos = pygame.mouse.get_pos()
                    lst.insert(0,self.cards.pop())
                    card.card_d = (pos[0] - self.rect.left,pos[1] -
                                   self.rect.top)
                    card.moved = True
                    card.cards = self
                    card.moved_card.extend(lst)
                    if len(self.cards) > 0 or len(self.hidden) > 0:
                        self.rect.top -= 32
                    break
                else:
                    lst.insert(0,self.cards.pop())
                    self.rect.top -= 32
            else:
                self.rect.top = top
                self.cards.extend(lst)

    def show_card(self):
        if len(self.cards) == 0 and len(self.hidden) > 0:
            self.cards.append(self.hidden.pop())

    def check_card(self,moved_card):
        card = moved_card[0]
        result = False
        if len(self.cards) == 0:
            if "king" in card:
                result = True
        else:
            if "hearts" in card or "diamonds" in card:
                if "spades" in self.cards[-1] or "clubs" in self.cards[-1]:
                    next_card = "X"
                    if "king" in self.cards[-1]:
                        next_card = "queen"
                    elif "queen" in self.cards[-1]:
                        next_card = "jack"
                    elif "jack" in self.cards[-1]:
                        next_card = "10_"
                    elif "10_" in self.cards[-1]:
                        next_card = "9_"
                    elif "9_" in self.cards[-1]:
                        next_card = "8_"
                    elif "8_" in self.cards[-1]:
                        next_card = "7_"
                    elif "7_" in self.cards[-1]:
                        next_card = "6_"
                    elif "6_" in self.cards[-1]:
                        next_card = "5_"
                    elif "5_" in self.cards[-1]:
                        next_card = "4_"
                    elif "4_" in self.cards[-1]:
                        next_card = "3_"
                    elif "3_" in self.cards[-1]:
                        next_card = "2_"
                    elif "2_" in self.cards[-1]:
                        next_card = "ace"

                    if next_card in card:
                        result = True
            elif "hearts" in self.cards[-1] or "diamonds" in self.cards[-1]:
                next_card = "X"
                if "king" in self.cards[-1]:
                    next_card = "queen"
                elif "queen" in self.cards[-1]:
                    next_card = "jack"
                elif "jack" in self.cards[-1]:
                    next_card = "10_"
                elif "10_" in self.cards[-1]:
                    next_card = "9_"
                elif "9_" in self.cards[-1]:
                    next_card = "8_"
                elif "8_" in self.cards[-1]:
                    next_card = "7_"
                elif "7_" in self.cards[-1]:
                    next_card = "6_"
                elif "6_" in self.cards[-1]:
                    next_card = "5_"
                elif "5_" in self.cards[-1]:
                    next_card = "4_"
                elif "4_" in self.cards[-1]:
                    next_card = "3_"
                elif "3_" in self.cards[-1]:
                    next_card = "2_"
                elif "2_" in self.cards[-1]:
                    next_card = "ace"

                if next_card in card:
                    result = True

        return result

class Solitaire_2(Deck):
    def __init__(self,x,y):
        #This is parent's constructor:
        Deck.__init__(self,x,y)
        self.hidden_cards = []
        self.cards_list = []
        self.x = x
    
    def click_down(self,card):
        """This is used when the player press the mouse button"""
        if self.check_pos() and len(self.cards) > 0:
            pos = pygame.mouse.get_pos()
            c = self.cards.pop()
            card.moved_card.append(c)
            self.cards_list.remove(c)
            card.card_d = (pos[0] - self.rect.left,pos[1] - self.rect.top)
            card.moved = True
            card.cards = self
            self.rect.left -= 20
        else:
            pos = pygame.mouse.get_pos()
            flag = False
            if pos[0] >= 30 and pos[0] <= 101:
                if pos[1] >= 30 and pos[1] <= 126:
                    flag = True
            if flag:
                self.rect.left = self.x
                if len(self.hidden_cards) > 0:
                    self.cards = []
                    for i in range(3):
                        c = self.hidden_cards.pop()
                        self.cards_list.insert(0,c)
                        self.cards.append(c)
                        if len(self.hidden_cards) == 0 and i < 2:
                            break
                        
                else:
                    self.hidden_cards.extend(self.cards_list)
                    self.cards_list = []
                    self.cards = []

                if len(self.cards) > 1:
                    for i in range(len(self.cards)):
                        if i > 0:
                            self.rect.left += 20

    def draw_card(self,screen,card_dict):
        """This will show all the cards on the screen"""
        x = self.x
        if len(self.hidden_cards) > 0:
            pygame.draw.rect(screen,TEAL,[30,30,71,96])
            pygame.draw.rect(screen,BLACK,[30,30,71,96],2)
            if len(self.cards_list) > 0 and len(self.cards) > 0:
                for item in self.cards:
                    screen.blit(card_dict[item],[x,self.rect.top])
                    x += 20
        else:
            if len(self.cards_list) > 0 and len(self.cards) > 0:
                for item in self.cards:
                    screen.blit(card_dict[item],[x,self.rect.top])
                    x += 20
            pygame.draw.ellipse(screen,OLIVE,[40,40,60,60],5)

    def add_card(self,card):
        self.cards.extend(card)
        self.cards_list.extend(card)
        self.rect.left += 20
    def peek_top(self):
        if len(self.cards)>0:
            return self.cards[0]
        return None
class Solitaire_3(Deck):
    def check_card(self,moved_card):
        result = False
        if len(moved_card) == 1:
            card = moved_card[0]
            if len(self.cards) == 0:
                if card[:3] == 'ace':
                    result = True
            else:
                suit = self.cards[0][4:]
                next_card = ''
                if suit in card:
                    if 'ace' in self.cards[-1]:
                        next_card = '2_' + suit
                    elif '2_' in self.cards[-1]:
                        next_card = '3_' + suit
                    elif '3_' in self.cards[-1]:
                        next_card = '4_' + suit
                    elif '4_' in self.cards[-1]:
                        next_card = '5_' + suit
                    elif '5_' in self.cards[-1]:
                        next_card = '6_' + suit
                    elif '6_' in self.cards[-1]:
                        next_card = '7_' + suit
                    elif '7_' in self.cards[-1]:
                        next_card = '8_' + suit
                    elif '8_' in self.cards[-1]:
                        next_card = '9_' + suit
                    elif '9_' in self.cards[-1]:
                        next_card = '10_' + suit
                    elif '10_' in self.cards[-1]:
                        next_card = 'jack_' + suit
                    elif 'jack_' in self.cards[-1]:
                        next_card = 'queen_' + suit
                    elif 'queen_' in self.cards[-1]:
                        next_card = 'king_' + suit

                    if next_card == card:
                        result = True
        return result

    def click_down(self,card):
        """This is used when the player click the mouse button"""
        if self.check_pos() and len(self.cards) > 0:
            pos = pygame.mouse.get_pos()
            card.moved_card.append(self.cards.pop())
            card.card_d = (pos[0] - self.rect.left,pos[1] - self.rect.top)
            card.moved = True
            card.cards = self

    def add_card(self,card):
        self.cards.extend(card)

    def draw_card(self,screen,card_dict):
        """This will display all the cards on the screen"""
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        if len(self.cards) > 0:
            screen.blit(card_dict[self.cards[-1]],[self.rect.left,self.rect.top])
    def move(self,p1,p2):
        if p1==0 and p2==0:
            pile=self.__piles[0]
            if pile.size()>0:
                the_card=pile.remove_top()
                result=pile.add_bottom(the_card)
        if p1==0 and p2>0:
            if self.__piles[p2].size()==0:
                the_card=self.__piles[p1].remove_top()
                self.__piles[p2].add_bottom(the_card)
            else:
                the_card=self.__piles[p1].peek_top()
                result=self.__piles[p2].peek_bottom()
                if result-1==the_card:
                    the_card=self.__piles[p1].remove_top()
                    self.__piles[p2].add_bottom(the_card)    
        if p1>0 and p2>0:
            if self.__piles[p2].size()>0:
                the_card=self.__piles[p1].peek_top()
                result=self.__piles[p2].peek_bottom()
                if result-1==the_card:
                    for x in range(self.__piles[p1].size()):
                        the_card=self.__piles[p1].remove_top()
                        self.__piles[p2].add_bottom(the_card)
def shuffle_cards():
    
    """It washes the cards"""
    r = []
    lst = ["ace_clubs","2_clubs","3_clubs","4_clubs","5_clubs","6_clubs",
           "7_clubs","8_clubs","9_clubs","10_clubs","jack_clubs","queen_clubs",
           "king_clubs","ace_spades","2_spades","3_spades","4_spades",
           "5_spades","6_spades","7_spades","8_spades","9_spades","10_spades",
           "jack_spades","queen_spades","king_spades","ace_hearts","2_hearts",
           "3_hearts","4_hearts","5_hearts","6_hearts","7_hearts","8_hearts",
           "9_hearts","10_hearts","jack_hearts","queen_hearts","king_hearts",
           "ace_diamonds","2_diamonds","3_diamonds","4_diamonds","5_diamonds",
           "6_diamonds","7_diamonds","8_diamonds","9_diamonds","10_diamonds",
           "jack_diamonds","queen_diamonds","king_diamonds"]

    length = len(lst)
    for i in range(length):
        if len(lst) > 1:
            c = random.choice(lst)
            r.append(c)
            lst.remove(c)
        else:
            c = lst.pop()
            r.append(c)

    return r


def main():
    pygame.init()

    # Setup the width and height of the screen [width, height]
    
    screen = pygame.display.set_mode([764,650])
    
    Player_name=str(input("Please Enter Your Name!"))
    pygame.display.set_caption("Solitaire Game"+Player_name)

    #Loop until the player left clicks the close button.
    done = False

    # Used to determine how fast the screen updates
    clock = pygame.time.Clock()
    #-------------------------------------------
    card_dict = {} #This variable will contain all the images of the cards
    img = pygame.image.load("playing_cards/ace_clubs.png").convert()
    card_dict["ace_clubs"] = img
    img = pygame.image.load("playing_cards/2_clubs.png").convert()
    card_dict["2_clubs"] = img
    img = pygame.image.load("playing_cards/3_clubs.png").convert()
    card_dict["3_clubs"] = img
    img = pygame.image.load("playing_cards/4_clubs.png").convert()
    card_dict["4_clubs"] = img
    img = pygame.image.load("playing_cards/5_clubs.png").convert()
    card_dict["5_clubs"] = img
    img = pygame.image.load("playing_cards/6_clubs.png").convert()
    card_dict["6_clubs"] = img
    img = pygame.image.load("playing_cards/7_clubs.png").convert()
    card_dict["7_clubs"] = img
    img = pygame.image.load("playing_cards/8_clubs.png").convert()
    card_dict["8_clubs"] = img
    img = pygame.image.load("playing_cards/9_clubs.png").convert()
    card_dict["9_clubs"] = img
    img = pygame.image.load("playing_cards/10_clubs.png").convert()
    card_dict["10_clubs"] = img
    img = pygame.image.load("playing_cards/jack_clubs.png").convert()
    card_dict["jack_clubs"] = img
    img = pygame.image.load("playing_cards/queen_clubs.png").convert()
    card_dict["queen_clubs"] = img
    img = pygame.image.load("playing_cards/king_clubs.png").convert()
    card_dict["king_clubs"] = img
    img = pygame.image.load("playing_cards/ace_spades.png").convert()
    card_dict["ace_spades"] = img
    img = pygame.image.load("playing_cards/2_spades.png").convert()
    card_dict["2_spades"] = img
    img = pygame.image.load("playing_cards/3_spades.png").convert()
    card_dict["3_spades"] = img
    img = pygame.image.load("playing_cards/4_spades.png").convert()
    card_dict["4_spades"] = img
    img = pygame.image.load("playing_cards/5_spades.png").convert()
    card_dict["5_spades"] = img
    img = pygame.image.load("playing_cards/6_spades.png").convert()
    card_dict["6_spades"] = img
    img = pygame.image.load("playing_cards/7_spades.png").convert()
    card_dict["7_spades"] = img
    img = pygame.image.load("playing_cards/8_spades.png").convert()
    card_dict["8_spades"] = img
    img = pygame.image.load("playing_cards/9_spades.png").convert()
    card_dict["9_spades"] = img
    img = pygame.image.load("playing_cards/10_spades.png").convert()
    card_dict["10_spades"] = img
    img = pygame.image.load("playing_cards/jack_spades.png").convert()
    card_dict["jack_spades"] = img
    img = pygame.image.load("playing_cards/queen_spades.png").convert()
    card_dict["queen_spades"] = img
    img = pygame.image.load("playing_cards/king_spades.png").convert()
    card_dict["king_spades"] = img
    img = pygame.image.load("playing_cards/ace_hearts.png").convert()
    card_dict["ace_hearts"] = img
    img = pygame.image.load("playing_cards/2_hearts.png").convert()
    card_dict["2_hearts"] = img
    img = pygame.image.load("playing_cards/3_hearts.png").convert()
    card_dict["3_hearts"] = img
    img = pygame.image.load("playing_cards/4_hearts.png").convert()
    card_dict["4_hearts"] = img
    img = pygame.image.load("playing_cards/5_hearts.png").convert()
    card_dict["5_hearts"] = img
    img = pygame.image.load("playing_cards/6_hearts.png").convert()
    card_dict["6_hearts"] = img
    img = pygame.image.load("playing_cards/7_hearts.png").convert()
    card_dict["7_hearts"] = img
    img = pygame.image.load("playing_cards/8_hearts.png").convert()
    card_dict["8_hearts"] = img
    img = pygame.image.load("playing_cards/9_hearts.png").convert()
    card_dict["9_hearts"] = img
    img = pygame.image.load("playing_cards/10_hearts.png").convert()
    card_dict["10_hearts"] = img
    img = pygame.image.load("playing_cards/jack_hearts.png").convert()
    card_dict["jack_hearts"] = img
    img = pygame.image.load("playing_cards/queen_hearts.png").convert()
    card_dict["queen_hearts"] = img
    img = pygame.image.load("playing_cards/king_hearts.png").convert()
    card_dict["king_hearts"] = img
    img = pygame.image.load("playing_cards/ace_diamonds.png").convert()
    card_dict["ace_diamonds"] = img
    img = pygame.image.load("playing_cards/2_diamonds.png").convert()
    card_dict["2_diamonds"] = img
    img = pygame.image.load("playing_cards/3_diamonds.png").convert()
    card_dict["3_diamonds"] = img
    img = pygame.image.load("playing_cards/4_diamonds.png").convert()
    card_dict["4_diamonds"] = img
    img = pygame.image.load("playing_cards/5_diamonds.png").convert()
    card_dict["5_diamonds"] = img
    img = pygame.image.load("playing_cards/6_diamonds.png").convert()
    card_dict["6_diamonds"] = img
    img = pygame.image.load("playing_cards/7_diamonds.png").convert()
    card_dict["7_diamonds"] = img
    img = pygame.image.load("playing_cards/8_diamonds.png").convert()
    card_dict["8_diamonds"] = img
    img = pygame.image.load("playing_cards/9_diamonds.png").convert()
    card_dict["9_diamonds"] = img
    img = pygame.image.load("playing_cards/10_diamonds.png").convert()
    card_dict["10_diamonds"] = img
    img = pygame.image.load("playing_cards/jack_diamonds.png").convert()
    card_dict["jack_diamonds"] = img
    img = pygame.image.load("playing_cards/queen_diamonds.png").convert()
    card_dict["queen_diamonds"] = img
    img = pygame.image.load("playing_cards/king_diamonds.png").convert()
    card_dict["king_diamonds"] = img
    #This variable below will contain all the names of the cards.
    card_list = shuffle_cards()
    #The list below will contain all the deck-objects.
    deck_list = [Solitaire_2(130,30),Solitaire_1(30,160),Solitaire_1(130,160),Solitaire_1(230,160),
                 Solitaire_1(330,160),Solitaire_1(430,160),Solitaire_1(530,160),
                 Solitaire_1(630,160),Solitaire_3(330,30),Solitaire_3(430,30),Solitaire_3(530,30),
                 Solitaire_3(630,30)]
    m_card = Moved_card()
    #The code below will set all the cards on the lists up.
    deck_list[1].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[2].extend_list(card_list[:2])
    del card_list[:2]
    deck_list[3].extend_list(card_list[:3])
    del card_list[:3]
    deck_list[4].extend_list(card_list[:4])
    del card_list[:4]
    deck_list[5].extend_list(card_list[:5])
    del card_list[:5]
    deck_list[6].extend_list(card_list[:6])
    del card_list[:6]
    deck_list[7].extend_list(card_list[:7])
    del card_list[:7]
    
    deck_list[0].hidden_cards.extend(card_list)
    game_over = False
    font = pygame.font.Font(None,25)
    text = font.render("Congratulations, You Won!",True,BLACK)
    def play(self):
        print("********************** NEW GAME *****************************")
        move_number=  1
        while move_number <= self.__max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row1 = int(input("Move from row no.:"),10)
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row2 = int(input("Move to row no.:"),10)
            if row1 >= 0 and row2 >= 0 and row1 < self.__num_piles and row2 < self.__num_piles:
                self.move(row1, row2)
            move_number += 1
           
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
            text = font.render("Congratulations, You Won!",True,BLACK)
        else:
            text = font.render("Sorry, You Lose!",True,BLACK)
            print("You Lose!\n")
    # -------- This is main Program  -----------using while and for loop at the same time
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): # Player click something
            if event.type == pygame.QUIT: # If player clicked close. The program needs to shutdown
                done = True # Show that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in deck_list:
                    item.click_down(m_card)

            if event.type == pygame.MOUSEBUTTONUP:
                m_card.click_up(deck_list)

        # --- This is game rule 
        for item in deck_list:
            if isinstance(item,Solitaire_3):
                if len(item.cards) != 13:
                    break
        else:
            game_over = True
        # First, clear the screen to light color. 
        # above this, or they will be erased with this command.
        screen.fill((TEAL))

        # --- Drawing code 
        for item in deck_list:
            item.draw_card(screen,card_dict)
        m_card.draw(screen,card_dict)
        if game_over:
            pygame.draw.rect(screen,PINK,[245,246,250,25])
            screen.blit(text,[250,250])
            print("********************** NEW GAME *****************************")
        # --- Carry on and update the screen with what we've shown.
        pygame.display.flip()

        # --- We limit time within 20 frames per second
        clock.tick(20)

    # Close game and quit.
    
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':

#Here are codes of section 1 to section 4.I split it into parts and put in into Solitaire to create cards.
    main()
class Solitaire:
    def __init__(self, cards):
        self.__piles = []
        self.__num_cards = len(cards)
        self.__num_piles = (self.__num_cards // 8) + 3
        self.__max_num_moves = self.__num_cards * 2
        for i in range(self.__num_piles):
            self.__piles.append(CardPile())
        for i in range(self.__num_cards):
            self.__piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        
        return self.__piles[i]

    def display(self):
        for i in range(self.__num_piles): 
            print(f'{i}: ',end='')
            self.get_pile(i).print_all(i)
    def move(self,p1,p2):
        if p1==0 and p2==0:
            pile=self.__piles[0]
            if pile.size()>0:
                the_card=pile.remove_top()
                result=pile.add_bottom(the_card)
        if p1==0 and p2>0:
            if self.__piles[p2].size()==0:
                the_card=self.__piles[p1].remove_top()
                self.__piles[p2].add_bottom(the_card)
            else:
                the_card=self.__piles[p1].peek_top()
                result=self.__piles[p2].peek_bottom()
                if result-1==the_card:
                    the_card=self.__piles[p1].remove_top()
                    self.__piles[p2].add_bottom(the_card)    
        if p1>0 and p2>0:
            if self.__piles[p2].size()>0:
                the_card=self.__piles[p1].peek_top()
                result=self.__piles[p2].peek_bottom()
                if result-1==the_card:
                    for x in range(self.__piles[p1].size()):
                        the_card=self.__piles[p1].remove_top()
                        self.__piles[p2].add_bottom(the_card)
    def is_complete(self):
        if self.__piles[0].size() == 0:
            all_cards_in_pile = False
            for i in range(1, len(self.__piles)):
                if self.__piles[i].size() == self.__num_cards:
                    all_cards_in_pile = True
            return all_cards_in_pile
        else:
            return False
    
    
    
    """Overwrite play function"""
    def play(self):
        print("********************** NEW GAME *****************************")
        move_number=  1
        while move_number <= self.__max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row1 = int(input("Move from row no.:"),10)
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row2 = int(input("Move to row no.:"),10)
            if row1 >= 0 and row2 >= 0 and row1 < self.__num_piles and row2 < self.__num_piles:
                self.move(row1, row2)
            move_number += 1
           
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")
                        
                    
            
            
        
    
    
class CardPile:
    def __init__(self):
        self.items=[]
    def add_top(self,item):
        self.items.insert(0,item)
    def add_bottom(self,item):
        self.items.append(item)
    def remove_top(self):
        if len(self.items)>0:
            item=self.items[0]
            del self.items[0]
            return item
        return None
    def remove_bottom(self):
        if len(self.items)>0:
            item=self.items.pop()
            return item
        return None
    def size(self):
        return len(self.items)
    def peek_top(self):
        if self.size()>0:
            return self.items[0]
        return None
    def peek_bottom(self):
        if self.size()>0:
            return self.items[len(self.items)-1]
        return None
    def print_all(self, index):
        if self.size()>0:
            if index==0:
                print(self.items[0],end='')
                for i in range(1,self.size()):
                    print(' *',end='')
                print('')
            else:
                for i in range(0,self.size()):
                    print(str(self.items[i])+' ',end='')
                
                print('')
        else:
            print(' ')
    
