#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def display_game(game):
    print(game[7] + ' | ' + game[8] + ' | ' + game[9])
    print('******')
    print(game[4] + ' | ' + game[5] + ' | ' + game[6])
    print('******') 
    print(game[1] + ' | ' + game[2] + ' | ' + game[3])


turnongame=True
Player2='O'
while turnongame == True:
    Player1 = (input("Player 1 are you X or O: "))
    if Player1.upper() == 'X':
        Player2 = 'O'
        turnongame = False
    elif Player1.upper() == 'O':
        Player2 = 'X'
        turnongame = False
    else:
        print("Select either X or O to Play")
        turnongame = True

ClearBoard= ["#","", "", "", "", "", "", "", "", ""]
spots=[1,2,3,4,5,6,7,8,9]

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    return 


GameOn=True
match=False
match2=False
while GameOn ==  True:
    test=True
    while test == True:
        value= int(input("Player 1: Enter available spot on board: "))
        if value in spots:
            test=False
        else:
            test=True
    
    print(spots)    
    ClearBoard[value] = Player1
    erase=spots.index(value)
    del spots[erase]       
    display_game(ClearBoard)
    
    if (ClearBoard[1]== Player1 and ClearBoard[2]==Player1 and ClearBoard[3] == Player1) or (ClearBoard[4]==Player1 and ClearBoard[5]==Player1 and ClearBoard[6]==Player1) or (ClearBoard[7]==Player1 and ClearBoard[8]==Player1 and ClearBoard[9]==Player1):
        print('Player 1 you win!')
        GameOn=False
        break
    if (ClearBoard[7]==Player1 and ClearBoard[4]==Player1 and ClearBoard[1] == Player1) or (ClearBoard[8]==Player1 and ClearBoard[5]== Player1 and ClearBoard[2]==Player1) or (ClearBoard[9]==Player1 and ClearBoard[6]==Player1 and ClearBoard[3]==Player1):
        print('Player 1 you win !')
        GameOn=False
        break
    if (ClearBoard[7]==Player1 and ClearBoard[5]==Player1 and ClearBoard[3] == Player1) or (ClearBoard[9]==Player1 and ClearBoard[5]==Player1 and ClearBoard[1]==Player1):
        print('Player 1 you win!')
        GameOn=False
        break



   
    test2=True
    while test2 == True:
        value2 = int(input("Player 2: Enter available spot on board: "))
        if value2 in spots:
            test2=False
        else:
            test2=True
    
    print(spots)    
    ClearBoard[value2] = Player2
    erase2=spots.index(value2)
    del spots[erase2]   
    win_check(ClearBoard,'O')
    display_game(ClearBoard)
    
    if (ClearBoard[1]== Player2 and ClearBoard[2]==Player2 and ClearBoard[3] == Player2) or (ClearBoard[4]==Player2 and ClearBoard[5]==Player2 and ClearBoard[6]==Player2) or (ClearBoard[7]==Player2 and ClearBoard[8]==Player2 and ClearBoard[9]==Player2):
        print('Player 2 you win!')
        GameOn=False
        break
    if (ClearBoard[7]==Player2 and ClearBoard[4]==Player2 and ClearBoard[1] == Player2) or (ClearBoard[8]==Player2 and ClearBoard[5]== Player2 and ClearBoard[2]==Player2) or (ClearBoard[9]==Player2 and ClearBoard[6]==Player2 and ClearBoard[3]==Player2):
        print('Player 2 you win !')
        GameOn=False
        break
    if (ClearBoard[7]==Player2 and ClearBoard[5]==Player2 and ClearBoard[3] == Player2) or (ClearBoard[9]==Player2 and ClearBoard[5]==Player2 and ClearBoard[1]==Player2):
        print('Player 2 you win!')
        GameOn=False
        break

