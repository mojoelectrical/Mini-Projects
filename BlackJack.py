#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creates the deck of cards
import random
Sections=['Spades','Hearts','Diamonds','Clubs']
Face=[2,3,4,5,6,7,8,9,10,10,10,10,11]
Cards=[]
for i in range(len(Sections)):
    for r in range(len(Face)):
        Cards1=[(Sections[i],Face[r])]
        Cards.append(Cards1)
random.shuffle(Cards)

#creates the list of numbers in the deck that are randomized
spot=list(range(1,53))
#Asks how many players will be playing with a maximum of 4 players 
while True:
    NumofPlayers=int(input("How many people are playing this round: "))
    if NumofPlayers > 3:
        print("Too many players")
        continue
    else:
        NumofPlayers=NumofPlayers
        break

deal_bank=[]
play1_bank=[]
play2_bank=[]
play3_bank=[]
#takes each players deposit into bank
def bank(num):
    i=1
    while i <= num:
        mainbank= 'play'+str(i)+'_bank'
        if mainbank == 'play1_bank':
            deposit=int(input("Enter your deposit Player1: "))
            play1_bank.append(deposit)
            i += 1
        if mainbank == 'play2_bank':
            deposit=int(input("Enter your deposit Player2: "))
            play2_bank.append(deposit)
            i += 1
        if mainbank == 'play3_bank':
            deposit=int(input("Enter your deposit Player3: "))
            play3_bank.append(deposit)
            i += 1
        

bank(NumofPlayers)

status=[True,True,True,True]
def statusfunc(ls):
    if Dsum[-1] > 21 :
        status[0]= False
    if P1[-1] > 21:
        status[1] = False
    if P2[-1] > 21 or len(Player2) < 2:
        status[2]= False
    if P3[-1] > 21 or len(Player3)<2:
        status[3]=False

    
    
#creates the list of cards that have been drawn and erases the cards from the existing pile from the deck
Dealer=[]
Player1=[]
Player2=[]
Player3=[]
Player4=[]
    
#adds number to list when number is less than 17
def add_one_player(num):
    if len(spot) > 1:
        lo=spot[0]
        pin="Player"+ str(num)
        if pin == 'Player1':
            Player1.append(Cards[lo])
            del spot[0]
        elif pin == 'Player2':
            Player2.append(Cards[lo])
            del spot[0]
        elif pin == 'Player3':
            Player3.append(Cards[lo])
            del spot[0]
        elif pin == 'Player0':
            Dealer.append(Cards[lo])
            del spot[0]
    else:
        print("There is not enough available cards")
            
#This will take in the number of players playing and give two cards to each player
def twocards(num):
    firstspot=spot[0]
    secondspot=spot[1]
    thirdspot=spot[2]
    fourthspot=spot[3]
    if num == 1:
        Dealer.append(Cards[firstspot])
        Player1.append(Cards[secondspot])
        del spot[1]
        del spot[0]
        
    elif num == 2:
        Dealer.append(Cards[firstspot])
        Player1.append(Cards[secondspot])
        Player2.append(Cards[thirdspot])
        del spot[2]
        del spot[1]
        del spot[0]
    elif num == 3:
        Dealer.append(Cards[firstspot])
        Player1.append(Cards[secondspot])
        Player2.append(Cards[thirdspot])
        Player3.append(Cards[fourthspot])
        del spot[3]
        del spot[2]
        del spot[1]
        del spot[0]

twocards(NumofPlayers)
twocards(NumofPlayers)
#This function prints the players cards that they have in their hand
def printCards(num,arr1,arr2,arr3):
    i=1
    arr=0
    while i <= num:
        printer="arr" + str(i)
        if printer == "arr1":
            arr=arr1
        if printer == "arr2":
            arr=arr2
        if printer == "arr3":
            arr=arr3
        print("Player{} set of cards are {}".format(i,arr))
        i += 1 
        
printCards(NumofPlayers,Player1,Player2,Player3)

#This funtion will ask each player whether they want to add a card
def card_appender(num):
    i=1
    while i <= (num):
        arr1st=[]
        arr2st=[]
        arr3rd=[]
        play1='Player' + str(i)
        if play1 == 'Player1':
            while True:
                ask2=input("{} do you want another card: ".format(play1)).lower()
                spot1=spot[0]
                if ask2 == 'yes' :
                    Player1.append(Cards[spot1])
                    print("Card added to hand")
                    del spot[0]
                elif ask2 =='no':
                    i += 1
                    break
                else:
                    continue

        if play1 == 'Player2':
                ask2=input("{} do you want another card: ".format(play1)).lower()
                spot1=spot[0]
                if ask2 == 'yes' :
                    Player2.append(Cards[spot1])
                    print("Card added to hand")
                    del spot[0]
                elif ask2 =='no':
                    i += 1
                    continue
                else:
                    continue
        
        if play1 == 'Player3':
                ask2=input("{} do you want another card: ".format(play1)).lower()
                spot1=spot[0]
                if ask2 == 'yes' :
                    Player3.append(Cards[spot1])
                    print("Card added to hand")
                    del spot[0]
                elif ask2 =='no':
                    i += 1 
                    break
                else:
                    continue
        print("---------------------------------------------------------")

card_appender(NumofPlayers)

#This will add everyone's card value 
Dsum=[]
P1=[]
P2=[]
P3=[]
def add_arrays(deal,hand1,hand2,hand3):
    sum_dealer=0
    sum_p1=0
    sum_p2=0
    sum_p3=0
    
    for i in Dealer:
        for x,y in i:
            sum_dealer += y
    Dsum.append(sum_dealer)
    
    sum_player1=0
    for i in Player1:
        for x,y in i:
            sum_p1 += y
    P1.append(sum_p1)

    sum_player2=0
    for i in Player2:
        for x,y in i:
            sum_p2 += y
    P2.append(sum_p2)

    sum_player3=0
    for i in Player3:
        for x,y in i:
            sum_p3 += y
    P3.append(sum_p3)

add_arrays(Dealer,Player1,Player2,Player3)
    
print(Dsum,P1,P2,P3)
statusfunc(status)
print(status)
#function will take all added arrays and if a number is less than 17 it will add another number to the list
#function will check if any number == 21 to check if a player won
#function will take out any Player with a value greater than 21

def over_21(arr):
    if status[0]==True:
        if Dsum[-1] > 21:
            status[0]= False
    if status[1]==True:
        if P1[-1] > 21:
            status[1] = False
    if status[2]== True:
        if P2[-1] > 21:
            status[2] = False
    if status[3]==True:
        if P3[-1] > 21:
            status[3]=False
            
def twentyone(arr):
    if status[0]==True and status[1]== 21:
        play1_bank[-1]=play1_bank[-1]*1.5
    if status[0]==True and status[2] == 21:
        play2_bank[-1]=play2_bank[-1]*1.5
    if status[0]==True and status[3] == 21:
        play3_bank[-1]=play3_bank[-1]*1.5

def under_17(arr):
    asc=1
    asc2=1
    asc3=1
    while Dsum[-1] < 17 and arr[0]== True:
        add_one_player(0)
        add_arrays(Dealer,Player1,Player2,Player3)
        print("Sum was below 17,Dealer added a card")
    if P1[-1] < 17 and arr[1]==True:
        while P1[-1] < 17:
            add_one_player(1)
            print("Player 1 added another card. Hand < 17")
            add_arrays(Dealer,Player1,Player2,Player3)

    if P2[-1] < 17 and arr[2] == True:
        while P2[-1] < 17:
            add_one_player(2)
            print("Player 2 added another card. Hand < 17")
            add_arrays(Dealer,Player1,Player2,Player3)

    if P3[-1] < 17 and arr[3] == True:
        while P3[-1] < 17:
            add_one_player(3)
            print("Player 3 added another card. Hand < 17")
            add_arrays(Dealer,Player1,Player2,Player3)

def elimated(arr):
    if status[0]== False:
        if status[1] ==True:
            play1_bank[-1]=play1_bank[-1]*2
            print("Player 1 you just doubled your loot to ${}".format(play1_bank[-1]))
        if status[2] == True:
            play2_bank[-1]=play2_bank[-1]*2
            print("Player 2 you just doubled your loot to ${}".format(play2_bank[-1]))
        if status[3] ==True:
            play3_bank[-1]=play3_bank[-1]*2
            print("Player 3 you just doubled your loot to ${}".format(play3_bank[-1]))
over_21(status)
twentyone(status)
elimated(status)
under_17(status)
add_arrays(Dealer,Player1,Player2,Player3)
over_21(status)

def winner(arr):
    if status[1]==True and status[0] == True:
        if P1[-1] > Dsum[-1]:
            play1_bank[-1]=play1_bank[-1]*2
            print("Player 1 won double amount")
        else:
            play1_bank[-1]=0
    if status[2]==True and status[0] == True:
        if P2[-1] > Dsum[-1]:
            play2_bank[-1]=play2_bank[-1]*2
            print("Player 2 won double amount")
        else:
            play2_bank[-1]=0
    if status[3]==True and status[0] == True:
        if P3[-1] > Dsum[-1]:
            play3_bank[-1]=play3_bank[-1]*2
            print("Player 3 won double amount")
        else:
            play3_bank[-1]=0
    if status[0] == True and status[1]==False and status[2]== False and status[3]==False:
        deal_bank[-1]=play1_bank[-1] + play2_bank[-1] + play3_bank[-1]
        print("Dealer won all funds {}".format(deal_bank[-1]))
    if status[0]==True:
        if Dsum[-1] > P1[-1] and Dsum[-1] > P2[-1] and Dsum[-1] > P3[-1]:
            deal_bank[-1]=play1_bank[-1] + play2_bank[-1] + play3_bank[-1]
            print("Dealer won all funds {}".format(deal_bank[-1]))

            

            
    

winner(status)
print(status)
print(deal_bank,play1_bank,play2_bank,play3_bank)

