import random
suits=("Spades","Hearts","Diamonds","Clubs")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack":10, "Queen":10, "King":10, "Ace":11}
Deckofcards=[]
state=[True,False,False,False]
chips=[]
Dealer=[]
Player1=[]
Player2=[]
Player3=[]
resultsum=[]
num=[]
out=[0,0,0,0]
playing=1
class Cards():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def deck(self):
        for self.suit in suits:
            for self.rank in ranks:
                Deckofcards.append((self.suit,self.rank))
                
    def __str__(self):
        print("Card: {} of {} ".format(self.suit,self.rank))
    
    def shuffle(self):
        random.shuffle(Deckofcards)

f= Cards(suit=suits, rank=ranks)
f.deck()
f.shuffle()

class Players():
    def __init__(self,num):
        self.num=num
        
    def asking(self):
        ask=1
        while True:
            self.num=int(input("How many players are playing this round: \n"))
            if self.num > 0 and self.num < 4:
                num.append(self.num)
                break
            else:
                print("A maximum of three players can play this round")
            continue
        while ask <= self.num:
            deposit=int(input("How many chips will you put down Player" +str(ask)+": \n"))
            chips.append(deposit)
            ask += 1
    
    def dealcard(self):
        while True:
            if out[1] < 22 and Dealer < 22:
                go1=(input("Do you want another card: y or n \n")).lower()
                if go1 == 'y':
                    if len(Deckofcards) > 1:
                        Player1.append(Deckofcards[0])
                        del Deckofcards[0]
                        ad.array(1,Player1)
                    else:
                        print("Deck of cards is finished")
                elif go1 == 'n':
                    break
                else:
                    continue
                
            if out[2] < 22 and Dealer < 22:
                go1=(input("Do you want another card: y or n \n")).lower()
                if go1 == 'y':
                    if len(Deckofcards) > 1:
                        Player2.append(Deckofcards[0])
                        del Deckofcards[0]
                        ad.array(2,Player2)
                    else:
                        print("Deck of cards is finished")
                elif go1 == 'n':
                    break
                else:
                    continue
            
            if out[3] < 22 and Dealer < 22:
                go1=(input("Do you want another card: y or n \n")).lower()
                if go1 == 'y':
                    if len(Deckofcards) > 1:
                        Player3.append(Deckofcards[0])
                        del Deckofcards[0]
                        ad.array(3,Player3)
                    else:
                        print("Deck of cards is finished")
                elif go1 == 'n':
                    break
                else:
                    continue    
                False

class Deal():
    def __init__(self,num):
        self.num=num
        
        
        
    def dealt(self):
        ask=self.num
        if ask == 1:
            state[1]=True
            
            Dealer.append(Deckofcards[0])
            Dealer.append(Deckofcards[1])
            Player1.append(Deckofcards[2])
            Player1.append(Deckofcards[3])
            
            del Deckofcards[3]
            del Deckofcards[2]
            del Deckofcards[1]
            del Deckofcards[0]
        if ask == 2:
            state[1]=True
            state[2]=True
            
            Dealer.append(Deckofcards[0])
            Dealer.append(Deckofcards[1])
            Player1.append(Deckofcards[2])
            Player1.append(Deckofcards[3])
            Player2.append(Deckofcards[4])
            Player2.append(Deckofcards[5])
            
            del Deckofcards[5]
            del Deckofcards[4]
            del Deckofcards[3]
            del Deckofcards[2]
            del Deckofcards[1]
            del Deckofcards[0]
        
        if ask == 3:
            state[1]=True
            state[2]=True
            state[3]=True
            
            Dealer.append(Deckofcards[0])
            Dealer.append(Deckofcards[1])
            Player1.append(Deckofcards[2])
            Player1.append(Deckofcards[3])
            Player2.append(Deckofcards[4])
            Player2.append(Deckofcards[5])
            Player3.append(Deckofcards[6])
            Player3.append(Deckofcards[7])
            
            del Deckofcards[7]
            del Deckofcards[6]
            del Deckofcards[5]
            del Deckofcards[4]
            del Deckofcards[3]
            del Deckofcards[2]
            del Deckofcards[1]
            del Deckofcards[0]
            
class addup():
    
    def addarray(self,num1,arr):
        result=0
    # adds value in array and gives sum to the out array
        for x,y in arr:
            result += values[y]
        if num1 == 0:
            out[0]=result
        if num1 == 1:
            out[1]=result
        if num1 == 2:
            out[2]= result
        if num1 == 3:
            out[3]=result
    #adds a card to the deck
    def addcard(self,num,arr1):
        if num ==0:
            Dealer.append(Deckofcards[0])
            del Deckofcards[0]
        if num == 1:
            Player1.append(Deckofcards[0])
            del Deckofcards[0]
        if num == 2:
            Player2.append(Deckofcards[0])
            del Deckofcards[0]
        if num == 3:
            Player3.append(Deckofcards[0])
            del Deckofcards[0]
            

class Comparator():
    def __init__(self, equal21,over21,under17):
        self.equal21=equal21
        self.over21=over21
        self.under17=under17
        
    def equal(self):
        self.equal21=21
        global state
        if out[0]==21 and (out[1]==21 or out[2]==21 or out[3]==21):
            print('Players tied')
            playing=0
            state[0]=False
        if out[0]==21 and (out[1] !=21 or out[2]!=21 or out[3]!=21):
            print("Dealer wins all")
            state=[False,False,False,False]
            playing=0
        if out[1]==21:
            chips[0]=chips[0]*1.5
            print('Player 1 wins 1.5 times his chips')
            state[1]=False
        if out[2] == 21:
            chips[1]=chips[1]*1.5
            print('Player 2 wins 1.5 times his chips')
            state[2]=False
        if out[3] == 21:
            chips[2]=chips[2]*1.5
            print('Player 3 wins 1.5 times his chips')
            state[3]=False
    
    def determine_winner(self):
        if state[1]==True:
            if out[0]<out[1] and out[0]<21:
                print('Player 1 won double the chips')
                chips[0]=chips[0]*2
                state[1]=False
        if state[2]==True and out[0]<21:
            if out[0]<out[2]:
                print('Player 2 won double the chips')
                chips[1]=chips[1]*2
                state[2]=False
        if state[3]==True and out[0]<21:
            if out[0]<out[3]:
                print('Player 3 won double the chips')
                chips[2]=chips[2]*2
                state[3]=False
        if state[0]==False:
            if state[1] == True:
                print('Player 1 won double the chips')
                chips[0]=chips[0]*2
                state[1]=False
        if state[0]==False:
            if state[2] == True:
                print('Player 2 won double the chips')
                chips[1]=chips[1]*2
                state[2]=False
        if state[0]==False:
            if state[3] == True:
                print('Player 3 won double the chips')
                chips[2]=chips[2]*2
                state[3]=False
        
    
    def dlr_under_17(self):
        while out[0] < 17:
            if len(Deckofcards) > 1:
                Dealer.append(Deckofcards[0])
                del Deckofcards[0]
                ad.array(0,Dealer)
            else:
                break
    
    def bust(self,arr):
        if arr[0] > 21:
            print("Dealer busted all remaining players win")
            state[0]=False
        if arr[1] > 21:
            print('Player 1 busted')
            state[1]=False
        if arr[2]> 21:
            print('Player 2 busted')
            state[2]=False
        if arr[3] > 21:
            print('Player 3 busted')
            state[3]=False
            
class Take_Card():
    def __init__(self,ask2):
        self.ask2=ask2
    
    def ask4(self,arr):
        if arr[1]==True:
            while True:
                ask2=input("Would you like another card Player 1: y or n: \n")
                if ask2 == 'y':
                    if len(Deckofcards) > 1:
                        Player1.append(Deckofcards[0])
                        ad.addarray(1,Player1)
                        del Deckofcards[0]
                    else:
                        print('No more cards available')
                elif ask2 == 'n':
                    False
                    break
                else:
                    print('Enter only y or n')
                    continue
        if arr[2]==True:
            while True:
                ask2=input("Would you like another card Player 2: y or n: \n")
                if ask2 == 'y':
                    if len(Deckofcards) > 1:
                        Player2.append(Deckofcards[0])
                        ad.addarray(2,Player2)
                        del Deckofcards[0]
                    else:
                        print('No more cards available')
                elif ask2 == 'n':
                    False
                    break
                else:
                    print('Enter only y or n')
                    continue
        if arr[3]==True:
            while True:
                ask2=input("Would you like another card Player 3: y or n: \n")
                if ask2 == 'y':
                    if len(Deckofcards) > 1:
                        Player3.append(Deckofcards[0])
                        ad.addarray(3,Player3)
                        del Deckofcards[0]
                    else:
                        print('No more cards available')
                elif ask2 == 'n':
                    False
                    break
                else:
                    print('Enter only y or n')
                    continue
    
    def un17(self):
        while out[0] < 17:
            if len(Deckofcards) >1:
                Dealer.append(Deckofcards[0])
                ad.addarray(0,Dealer)
                del Deckofcards[0]
    
    def endgame(self):
        global playing
        if playing==1:
            if state==[False,False,False,False]:
                playing=0
        


while playing ==1:
    p=Players(0)
    p.asking()                #gets the amount of players that are playing in the round
    d=Deal(num[0])
    d.dealt()                 #deals two cards to each player playing
    print(Dealer,Player1,Player2,Player3)
    ad=addup()
    ad.addarray(0,Dealer)
    ad.addarray(1,Player1)
    ad.addarray(2,Player2)
    ad.addarray(3,Player3)     #adds all arrays
    com=Comparator(21,21,17) 
    com.equal()             # if dealer or anyone equals 21 the chips are doubled
    com.bust(out)
    print(out)
    print(state)
    print(chips)
    test=Take_Card(0)
    test.ask4(state)
    test.un17()
    com.bust(out)
    com.equal()             # if dealer or anyone equals 21 the chips are doubled
    print(out)
    com.determine_winner()
    print(state)
    test.endgame()

