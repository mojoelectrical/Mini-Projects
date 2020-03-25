import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

URL='https://basketball.realgm.com/nba/stats'
response =requests.get(URL)
soup=BeautifulSoup(response.content, 'html.parser')

columns=['#','Player', 'Team', 'GP','MPG','FGM','FGA','FG','threePM','threePA','threeP','FTM',
         'FTA','FT','TOV','PF','ORB','DRB','RPG','APG','SPG','BPG','PPG']

df=pd.DataFrame(columns=columns)

table=soup.find('table', attrs={'class':'tablesaw'}).tbody

trs=table.find_all('tr')

for tr in trs:
    tds=tr.find_all('td')
    row=[td.text.replace('\n', '') for td in tds]
    df= df.append(pd.Series(row, index=columns), ignore_index=True)
#------------------------PG2---------------------------------------------#
URL1='https://basketball.realgm.com/nba/stats/2020/Averages/Qualified/points/All/desc/2/Regular_Season'
response =requests.get(URL1)
soup=BeautifulSoup(response.content, 'html.parser')

table1=soup.find('table', attrs={'class':'tablesaw','data-tablesaw-mode':'swipe'}).tbody

trs=table1.find_all('tr')

for tr in trs:
    tds=tr.find_all('td')
    row=[td.text.replace('\n', '') for td in tds]
    df= df.append(pd.Series(row, index=columns), ignore_index=True)

#---------------------------------------PG3------------------------------------------------------#
URL2='https://basketball.realgm.com/nba/stats/2020/Averages/Qualified/points/All/desc/3/Regular_Season'
response=requests.get(URL2)
soup=BeautifulSoup(response.content,'html.parser')

table2=soup.find('table', attrs={'class':'tablesaw','data-tablesaw-mode':'swipe'}).tbody

trs=table2.find_all('tr')

for tr in trs:
    tds=tr.find_all('td')
    row=[td.text.replace('\n','') for td in tds]
    df=df.append(pd.Series(row, index=columns), ignore_index=True)

    
df.to_csv('NBA Player stats 2020.csv', index=False)

#make player list'---------------------------------------------------------
data=pd.read_csv('NBA Player stats 2020.csv', names=columns)
names=data.Player.tolist()
k=names.pop(0)
player_array=sorted(np.array(names))
player2_array=sorted(np.array(names))
#print(player_array)
#--------------------------------------------------------------------------------------------------------------

def exit_():
    window.quit()
    window.destroy()
    exit()

def populate_gui_from_dict(stringname):       
    team.set(str(data.loc[data.Player==stringname].Team.values)[2:-2])
    gamesplayed.set(str(data.loc[data.Player==str(stringname)].GP.values)[2:-2])
    minutespergame.set(str(data.loc[data.Player==str(stringname)].MPG.values)[2:-2])
    fieldgoalsmade.set(str(data.loc[data.Player==str(stringname)].FGM.values)[2:-2])
    fieldgoalsattempted.set(str(data.loc[data.Player==str(stringname)].FGA.values)[2:-2])
    fieldgoalpct.set(str(data.loc[data.Player==str(stringname)].FG.values)[2:-2])
    threesmade.set(str(data.loc[data.Player==str(stringname)].threePM.values)[2:-2])
    threesattempted.set(str(data.loc[data.Player==str(stringname)].threePA.values)[2:-2])
    threespct.set(str(data.loc[data.Player==str(stringname)].threeP.values)[2:-2])
    freethrowsmade.set(str(data.loc[data.Player==str(stringname)].FTM.values)[2:-2]) 
    freethrowsattempted.set(str(data.loc[data.Player==str(stringname)].FTA.values)[2:-2])
    freethrowpct.set(str(data.loc[data.Player==str(stringname)].FT.values)[2:-2])  
    turnovers.set(str(data.loc[data.Player==str(stringname)].TOV.values)[2:-2])
    personalfoul.set(str(data.loc[data.Player==str(stringname)].PF.values)[2:-2])
    offensiverebounds.set(str(data.loc[data.Player==str(stringname)].ORB.values)[2:-2]) 
    defensiverebounds.set(str(data.loc[data.Player==str(stringname)].DRB.values)[2:-2])
    reboundspergame.set(str(data.loc[data.Player==str(stringname)].RPG.values)[2:-2])
    assistspergame.set(str(data.loc[data.Player==str(stringname)].APG.values)[2:-2])
    stealspergame.set(str(data.loc[data.Player==str(stringname)].SPG.values)[2:-2]) 
    blockspergame.set(str(data.loc[data.Player==str(stringname)].BPG.values)[2:-2])
    pointspergame.set(str(data.loc[data.Player==str(stringname)].PPG.values)[2:-2])
    
def populate_gui_from_dict2(stringname):       
    team2.set(str(data.loc[data.Player==stringname].Team.values)[2:-2])
    gamesplayed2.set(str(data.loc[data.Player==str(stringname)].GP.values)[2:-2])
    minutespergame2.set(str(data.loc[data.Player==str(stringname)].MPG.values)[2:-2])
    fieldgoalsmade2.set(str(data.loc[data.Player==str(stringname)].FGM.values)[2:-2])
    fieldgoalsattempted2.set(str(data.loc[data.Player==str(stringname)].FGA.values)[2:-2])
    fieldgoalpct2.set(str(data.loc[data.Player==str(stringname)].FG.values)[2:-2])
    threesmade2.set(str(data.loc[data.Player==str(stringname)].threePM.values)[2:-2])
    threesattempted2.set(str(data.loc[data.Player==str(stringname)].threePA.values)[2:-2])
    threespct2.set(str(data.loc[data.Player==str(stringname)].threeP.values)[2:-2])
    freethrowsmade2.set(str(data.loc[data.Player==str(stringname)].FTM.values)[2:-2]) 
    freethrowsattempted2.set(str(data.loc[data.Player==str(stringname)].FTA.values)[2:-2])
    freethrowpct2.set(str(data.loc[data.Player==str(stringname)].FT.values)[2:-2])  
    turnovers2.set(str(data.loc[data.Player==str(stringname)].TOV.values)[2:-2])
    personalfoul2.set(str(data.loc[data.Player==str(stringname)].PF.values)[2:-2])
    offensiverebounds2.set(str(data.loc[data.Player==str(stringname)].ORB.values)[2:-2]) 
    defensiverebounds2.set(str(data.loc[data.Player==str(stringname)].DRB.values)[2:-2])
    reboundspergame2.set(str(data.loc[data.Player==str(stringname)].RPG.values)[2:-2])
    assistspergame2.set(str(data.loc[data.Player==str(stringname)].APG.values)[2:-2])
    stealspergame2.set(str(data.loc[data.Player==str(stringname)].SPG.values)[2:-2]) 
    blockspergame2.set(str(data.loc[data.Player==str(stringname)].BPG.values)[2:-2])
    pointspergame2.set(str(data.loc[data.Player==str(stringname)].PPG.values)[2:-2])

window=tk.Tk()
window.title('NBA Comparisons')

menuBar=Menu()
window.config(menu=menuBar)

#Add menu items
fileMenu=Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=exit_)
menuBar.add_cascade(label='File', menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

tabControl=ttk.Notebook(window)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Compare Players')

tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='Compare Teams')

tab3=ttk.Frame(tabControl)
tabControl.add(tab3,text='Win Chart')

tabControl.pack(expand=1, fill="both")

statsofplayer=ttk.LabelFrame(tab1,text='Player Stats')
statsofplayer.grid(column=0, row=1, padx=8, pady=4)

ENTRY_WIDTH=10

ttk.Label(statsofplayer,text='Team:').grid(column=0, row=1, sticky='E')
team=tk.StringVar()
teamEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=team, state='readonly')
teamEntry.grid(column=1, row=1, sticky='W')

ttk.Label(statsofplayer,text='GP:').grid(column=0, row=2, sticky='E')
gamesplayed=tk.StringVar()
gamesplayedEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=gamesplayed, state='readonly')
gamesplayedEntry.grid(column=1, row=2, sticky='W')

ttk.Label(statsofplayer,text='MPG:').grid(column=0, row=3, sticky='E')
minutespergame=tk.StringVar()
minutespergameEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=minutespergame, state='readonly')
minutespergameEntry.grid(column=1, row=3, sticky='W')

ttk.Label(statsofplayer,text='FGM:').grid(column=0, row=4, sticky='E')
fieldgoalsmade=tk.StringVar()
fieldgoalsmadeEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=fieldgoalsmade, state='readonly')
fieldgoalsmadeEntry.grid(column=1, row=4, sticky='W')

ttk.Label(statsofplayer,text='FGA:').grid(column=0, row=5, sticky='E')
fieldgoalsattempted=tk.StringVar()
fieldgoalsattemptedEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=fieldgoalsattempted, state='readonly')
fieldgoalsattemptedEntry.grid(column=1, row=5, sticky='W')

ttk.Label(statsofplayer,text='FG%:').grid(column=0, row=6, sticky='E')
fieldgoalpct=tk.StringVar()
fieldgoalpctEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=fieldgoalpct, state='readonly')
fieldgoalpctEntry.grid(column=1, row=6, sticky='W')

ttk.Label(statsofplayer,text='3PM:').grid(column=0, row=7, sticky='E')
threesmade=tk.StringVar()
threesmadeEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=threesmade, state='readonly')
threesmadeEntry.grid(column=1, row=7, sticky='W')

ttk.Label(statsofplayer,text='3PA:').grid(column=0, row=8, sticky='E')
threesattempted=tk.StringVar()
threesattemptedEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=threesattempted, state='readonly')
threesattemptedEntry.grid(column=1, row=8, sticky='W')

ttk.Label(statsofplayer,text='3P%:').grid(column=0, row=9, sticky='E')
threespct=tk.StringVar()
threespctEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=threespct, state='readonly')
threespctEntry.grid(column=1, row=9, sticky='W')

ttk.Label(statsofplayer,text='FTM:').grid(column=0, row=10, sticky='E')
freethrowsmade=tk.StringVar()
freethrowsmadeEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=freethrowsmade, state='readonly')
freethrowsmadeEntry.grid(column=1, row=10, sticky='W')

ttk.Label(statsofplayer,text='FTA:').grid(column=0, row=11, sticky='E')
freethrowsattempted=tk.StringVar()
freethrowsattemptedEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=freethrowsattempted, state='readonly')
freethrowsattemptedEntry.grid(column=1, row=11, sticky='W')

ttk.Label(statsofplayer,text='FT%:').grid(column=0, row=12, sticky='E')
freethrowpct=tk.StringVar()
freethrowpctEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=freethrowpct, state='readonly')
freethrowpctEntry.grid(column=1, row=12, sticky='W')

ttk.Label(statsofplayer,text='TOV:').grid(column=0, row=13, sticky='E')
turnovers=tk.StringVar()
turnoversEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=turnovers, state='readonly')
turnoversEntry.grid(column=1, row=13, sticky='W')

ttk.Label(statsofplayer,text='FT%:').grid(column=0, row=14, sticky='E')
personalfoul=tk.StringVar()
personalfoulEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=personalfoul, state='readonly')
personalfoulEntry.grid(column=1, row=14, sticky='W')

ttk.Label(statsofplayer,text='ORB:').grid(column=0, row=15, sticky='E')
offensiverebounds=tk.StringVar()
offensivereboundsEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=offensiverebounds, state='readonly')
offensivereboundsEntry.grid(column=1, row=15, sticky='W')

ttk.Label(statsofplayer,text='DRB:').grid(column=0, row=16, sticky='E')
defensiverebounds=tk.StringVar()
defensivereboundsEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=defensiverebounds, state='readonly')
defensivereboundsEntry.grid(column=1, row=16, sticky='W')

ttk.Label(statsofplayer,text='RPG:').grid(column=0, row=17, sticky='E')
reboundspergame=tk.StringVar()
reboundspergameEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=reboundspergame, state='readonly')
reboundspergameEntry.grid(column=1, row=17, sticky='W')

ttk.Label(statsofplayer,text='APG:').grid(column=0, row=18, sticky='E')
assistspergame=tk.StringVar()
assistspergameEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=assistspergame, state='readonly')
assistspergameEntry.grid(column=1, row=18, sticky='W')

ttk.Label(statsofplayer,text='SPG:').grid(column=0, row=19, sticky='E')
stealspergame=tk.StringVar()
stealspergameEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=stealspergame, state='readonly')
stealspergameEntry.grid(column=1, row=19, sticky='W')

ttk.Label(statsofplayer,text='BPG:').grid(column=0, row=20, sticky='E')
blockspergame=tk.StringVar()
blockspergameEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=blockspergame, state='readonly')
blockspergameEntry.grid(column=1, row=20, sticky='W')

ttk.Label(statsofplayer,text='PPG:').grid(column=0, row=21, sticky='E')
pointspergame=tk.StringVar()
pointspergameEntry=ttk.Entry(statsofplayer, width=ENTRY_WIDTH, textvariable=pointspergame, state='readonly')
pointspergameEntry.grid(column=1, row=21, sticky='W')
#------------------------------------------------------------------------------------------------------------------
statsofplayer2=ttk.LabelFrame(tab1, text='Player 2 Stats')
statsofplayer2.grid(column=2, row=1,padx=8, pady=4)

ENTRY_WIDTH=10

ttk.Label(statsofplayer2,text='Team:').grid(column=2, row=1, sticky='E')
team2=tk.StringVar()
team2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=team2, state='readonly')
team2Entry.grid(column=3, row=1, sticky='W')

ttk.Label(statsofplayer2,text='GP:').grid(column=2, row=2, sticky='E')
gamesplayed2=tk.StringVar()
gamesplayed2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=gamesplayed2, state='readonly')
gamesplayed2Entry.grid(column=3, row=2, sticky='W')

ttk.Label(statsofplayer2,text='MPG:').grid(column=2, row=3, sticky='E')
minutespergame2=tk.StringVar()
minutespergame2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=minutespergame2, state='readonly')
minutespergame2Entry.grid(column=3, row=3, sticky='W')

ttk.Label(statsofplayer2,text='FGM:').grid(column=2, row=4, sticky='E')
fieldgoalsmade2=tk.StringVar()
fieldgoalsmadeEntry2=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=fieldgoalsmade2, state='readonly')
fieldgoalsmadeEntry2.grid(column=3, row=4, sticky='W')

ttk.Label(statsofplayer2,text='FGA:').grid(column=2, row=5, sticky='E')
fieldgoalsattempted2=tk.StringVar()
fieldgoalsattempted2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=fieldgoalsattempted2, state='readonly')
fieldgoalsattempted2Entry.grid(column=3, row=5, sticky='W')

ttk.Label(statsofplayer2,text='FG%:').grid(column=2, row=6, sticky='E')
fieldgoalpct2=tk.StringVar()
fieldgoalpct2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=fieldgoalpct2, state='readonly')
fieldgoalpct2Entry.grid(column=3, row=6, sticky='W')

ttk.Label(statsofplayer2,text='3PM:').grid(column=2, row=7, sticky='E')
threesmade2=tk.StringVar()
threesmade2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=threesmade2, state='readonly')
threesmade2Entry.grid(column=3, row=7, sticky='W')

ttk.Label(statsofplayer2,text='3PA:').grid(column=2, row=8, sticky='E')
threesattempted2=tk.StringVar()
threesattempted2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=threesattempted2, state='readonly')
threesattempted2Entry.grid(column=3, row=8, sticky='W')

ttk.Label(statsofplayer2,text='3P%:').grid(column=2, row=9, sticky='E')
threespct2=tk.StringVar()
threespctEntry2=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=threespct2, state='readonly')
threespctEntry2.grid(column=3, row=9, sticky='W')

ttk.Label(statsofplayer2,text='FTM:').grid(column=2, row=10, sticky='E')
freethrowsmade2=tk.StringVar()
freethrowsmade2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=freethrowsmade2, state='readonly')
freethrowsmade2Entry.grid(column=3, row=10, sticky='W')

ttk.Label(statsofplayer2,text='FTA:').grid(column=2, row=11, sticky='E')
freethrowsattempted2=tk.StringVar()
freethrowsattempted2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=freethrowsattempted2, state='readonly')
freethrowsattempted2Entry.grid(column=3, row=11, sticky='W')

ttk.Label(statsofplayer2,text='FT%:').grid(column=2, row=12, sticky='E')
freethrowpct2=tk.StringVar()
freethrowpctEntry2=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=freethrowpct2, state='readonly')
freethrowpctEntry2.grid(column=3, row=12, sticky='W')

ttk.Label(statsofplayer2,text='TOV:').grid(column=2, row=13, sticky='E')
turnovers2=tk.StringVar()
turnovers2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=turnovers2, state='readonly')
turnovers2Entry.grid(column=3, row=13, sticky='W')

ttk.Label(statsofplayer2,text='FT%:').grid(column=2, row=14, sticky='E')
personalfoul2=tk.StringVar()
personalfoul2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=personalfoul2, state='readonly')
personalfoul2Entry.grid(column=3, row=14, sticky='W')

ttk.Label(statsofplayer2,text='ORB:').grid(column=2, row=15, sticky='E')
offensiverebounds2=tk.StringVar()
offensiverebounds2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=offensiverebounds2, state='readonly')
offensiverebounds2Entry.grid(column=3, row=15, sticky='W')

ttk.Label(statsofplayer2,text='DRB:').grid(column=2, row=16, sticky='E')
defensiverebounds2=tk.StringVar()
defensiverebounds2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=defensiverebounds2, state='readonly')
defensiverebounds2Entry.grid(column=3, row=16, sticky='W')

ttk.Label(statsofplayer2,text='RPG:').grid(column=2, row=17, sticky='E')
reboundspergame2=tk.StringVar()
reboundspergame2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=reboundspergame2, state='readonly')
reboundspergame2Entry.grid(column=3, row=17, sticky='W')

ttk.Label(statsofplayer2,text='APG:').grid(column=2, row=18, sticky='E')
assistspergame2=tk.StringVar()
assistspergame2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=assistspergame2, state='readonly')
assistspergame2Entry.grid(column=3, row=18, sticky='W')

ttk.Label(statsofplayer2,text='SPG:').grid(column=2, row=19, sticky='E')
stealspergame2=tk.StringVar()
stealspergame2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=stealspergame2, state='readonly')
stealspergame2Entry.grid(column=3, row=19, sticky='W')

ttk.Label(statsofplayer2,text='BPG:').grid(column=2, row=20, sticky='E')
blockspergame2=tk.StringVar()
blockspergame2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=blockspergame2, state='readonly')
blockspergame2Entry.grid(column=3, row=20, sticky='W')

ttk.Label(statsofplayer2,text='PPG:').grid(column=2, row=21, sticky='E')
pointspergame2=tk.StringVar()
pointspergame2Entry=ttk.Entry(statsofplayer2, width=ENTRY_WIDTH, textvariable=pointspergame2, state='readonly')
pointspergame2Entry.grid(column=3, row=21, sticky='W')


#------------------------------------------------------------------------------------------------------------------

for child in statsofplayer.winfo_children(): 
        child.grid_configure(padx=4, pady=2) 
for child in statsofplayer2.winfo_children(): 
        child.grid_configure(padx=4, pady=2) 
        
Playerselection=ttk.LabelFrame(tab1, text='Select')
Playerselection.grid(column=0, row=0, padx=4, pady=4)
ttk.Label(Playerselection, text="Player 1: ").grid(column=0, row=0) # empty space for alignment

Playerselection2=ttk.LabelFrame(tab1, text='Select')
Playerselection2.grid(column=2, row=0, padx=4, pady=4)
ttk.Label(Playerselection2, text="Player 2: ").grid(column=3, row=0) # empty space for alignment

# ---------------------------------------------------------------
station_id = tk.StringVar()
station_id_combo = ttk.Combobox(Playerselection, width=20, textvariable=station_id)    
station_id_combo['values'] = player_array
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0) 

#-----------------------------------------------------------------------------------
station_id2 = tk.StringVar()
station_id2_combo = ttk.Combobox(Playerselection2, width=20, textvariable=station_id2)    
station_id2_combo['values'] = player2_array
station_id2_combo.grid(column=3, row=0)
station_id2_combo.current(0) 

#---------------------------------------------------------------------------------

def _get_station():
    station = station_id_combo.get()
    populate_gui_from_dict(station)

def _get_station2():
    station = station_id2_combo.get()
    populate_gui_from_dict2(station)
    


get_stats_btn = ttk.Button(Playerselection,text='Get Stats', command=_get_station).grid(column=2, row=0)
get_stats_btn2 = ttk.Button(Playerselection2,text='Get Stats', command=_get_station2).grid(column=4, row=0)


columns1=['#','Team','GP','MPG','FGM','FGA','FG','threePM','threePA','threeP','FTM',
         'FTA','FT','TOV','PF','ORB','DRB','RPG','APG','SPG','BPG','PPG']

#-----------------------------------------------------------
data2=pd.read_csv('NBA Team stats 2020.csv', names=columns1)
names=data2.Team.tolist()
k=names.pop(0)
team_array=sorted(np.array(names))
team2_array=sorted(np.array(names))

#--------TAB2-------------------#

TeamURL='https://basketball.realgm.com/nba/team-stats'
response1 =requests.get(TeamURL)
soup1=BeautifulSoup(response1.content, 'html.parser')

df1=pd.DataFrame(columns=columns1)

table1=soup1.find('table', attrs={'class':'tablesaw'}).tbody

trs1=table1.find_all('tr')

for tr in trs1:
    tds=tr.find_all('td')
    row1=[td.text.replace('\n', '') for td in tds]
    df1= df1.append(pd.Series(row1, index=columns1), ignore_index=True)

#Load Tab2 with data        
    
df1.to_csv('NBA Team stats 2020.csv', index=False)

statsofteam=ttk.LabelFrame(tab2,text='Team Stats')
statsofteam.grid(column=0, row=1, padx=8, pady=4)

statsofteam2=ttk.LabelFrame(tab2, text='Team 1 Stats')
statsofteam2.grid(column=2, row=1,padx=8, pady=4)


ttk.Label(statsofteam,text='GP:').grid(column=0, row=2, sticky='E')
gamesplayed3=tk.StringVar()
gamesplayed3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=gamesplayed3, state='readonly')
gamesplayed3Entry.grid(column=1, row=2, sticky='W')

ttk.Label(statsofteam,text='MPG:').grid(column=0, row=3, sticky='E')
minutespergame3=tk.StringVar()
minutespergame3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=minutespergame3, state='readonly')
minutespergame3Entry.grid(column=1, row=3, sticky='W')

ttk.Label(statsofteam,text='FGM:').grid(column=0, row=4, sticky='E')
fieldgoalsmade3=tk.StringVar()
fieldgoalsmade3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=fieldgoalsmade3, state='readonly')
fieldgoalsmade3Entry.grid(column=1, row=4, sticky='W')

ttk.Label(statsofteam,text='FGA:').grid(column=0, row=5, sticky='E')
fieldgoalsattempted3=tk.StringVar()
fieldgoalsattempted3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=fieldgoalsattempted3, state='readonly')
fieldgoalsattempted3Entry.grid(column=1, row=5, sticky='W')

ttk.Label(statsofteam,text='FG%:').grid(column=0, row=6, sticky='E')
fieldgoalpct3=tk.StringVar()
fieldgoalpct3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=fieldgoalpct3, state='readonly')
fieldgoalpct3Entry.grid(column=1, row=6, sticky='W')

ttk.Label(statsofteam,text='3PM:').grid(column=0, row=7, sticky='E')
threesmade3=tk.StringVar()
threesmade3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=threesmade3, state='readonly')
threesmade3Entry.grid(column=1, row=7, sticky='W')

ttk.Label(statsofteam,text='3PA:').grid(column=0, row=8, sticky='E')
threesattempted3=tk.StringVar()
threesattempted3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=threesattempted3, state='readonly')
threesattempted3Entry.grid(column=1, row=8, sticky='W')

ttk.Label(statsofteam,text='3P%:').grid(column=0, row=9, sticky='E')
threespct3=tk.StringVar()
threespct3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=threespct3, state='readonly')
threespct3Entry.grid(column=1, row=9, sticky='W')

ttk.Label(statsofteam,text='FTM:').grid(column=0, row=10, sticky='E')
freethrowsmade3=tk.StringVar()
freethrowsmade3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=freethrowsmade3, state='readonly')
freethrowsmade3Entry.grid(column=1, row=10, sticky='W')

ttk.Label(statsofteam,text='FTA:').grid(column=0, row=11, sticky='E')
freethrowsattempted3=tk.StringVar()
freethrowsattempted3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=freethrowsattempted3, state='readonly')
freethrowsattempted3Entry.grid(column=1, row=11, sticky='W')

ttk.Label(statsofteam,text='FT%:').grid(column=0, row=12, sticky='E')
freethrowpct3=tk.StringVar()
freethrowpct3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=freethrowpct3, state='readonly')
freethrowpct3Entry.grid(column=1, row=12, sticky='W')

ttk.Label(statsofteam,text='TOV:').grid(column=0, row=13, sticky='E')
turnovers3=tk.StringVar()
turnovers3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=turnovers3, state='readonly')
turnovers3Entry.grid(column=1, row=13, sticky='W')

ttk.Label(statsofteam,text='FT%:').grid(column=0, row=14, sticky='E')
personalfoul3=tk.StringVar()
personalfoul3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=personalfoul3, state='readonly')
personalfoul3Entry.grid(column=1, row=14, sticky='W')

ttk.Label(statsofteam,text='ORB:').grid(column=0, row=15, sticky='E')
offensiverebounds3=tk.StringVar()
offensiverebounds3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=offensiverebounds3, state='readonly')
offensiverebounds3Entry.grid(column=1, row=15, sticky='W')

ttk.Label(statsofteam,text='DRB:').grid(column=0, row=16, sticky='E')
defensiverebounds3=tk.StringVar()
defensiverebounds3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=defensiverebounds3, state='readonly')
defensiverebounds3Entry.grid(column=1, row=16, sticky='W')

ttk.Label(statsofteam,text='RPG:').grid(column=0, row=17, sticky='E')
reboundspergame3=tk.StringVar()
reboundspergame3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=reboundspergame3, state='readonly')
reboundspergame3Entry.grid(column=1, row=17, sticky='W')

ttk.Label(statsofteam,text='APG:').grid(column=0, row=18, sticky='E')
assistspergame3=tk.StringVar()
assistspergame3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=assistspergame3, state='readonly')
assistspergame3Entry.grid(column=1, row=18, sticky='W')

ttk.Label(statsofteam,text='SPG:').grid(column=0, row=19, sticky='E')
stealspergame3=tk.StringVar()
stealspergame3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=stealspergame3, state='readonly')
stealspergame3Entry.grid(column=1, row=19, sticky='W')

ttk.Label(statsofteam,text='BPG:').grid(column=0, row=20, sticky='E')
blockspergame3=tk.StringVar()
blockspergame3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=blockspergame3, state='readonly')
blockspergame3Entry.grid(column=1, row=20, sticky='NSEW')

ttk.Label(statsofteam,text='PPG:').grid(column=0, row=21, sticky='E')
pointspergame3=tk.StringVar()
pointspergame3Entry=ttk.Entry(statsofteam, width=ENTRY_WIDTH, textvariable=pointspergame3, state='readonly')
pointspergame3Entry.grid(column=1, row=21, sticky='NSEW')
#------------------------------------------------------------------------------------------------------------
ttk.Label(statsofteam2,text='GP:').grid(column=2, row=2, sticky='E')
gamesplayed4=tk.StringVar()
gamesplayed4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=gamesplayed4, state='readonly')
gamesplayed4Entry.grid(column=3, row=2, sticky='W')

ttk.Label(statsofteam2,text='MPG:').grid(column=2, row=3, sticky='E')
minutespergame4=tk.StringVar()
minutespergame4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=minutespergame4, state='readonly')
minutespergame4Entry.grid(column=3, row=3, sticky='W')

ttk.Label(statsofteam2,text='FGM:').grid(column=2, row=4, sticky='E')
fieldgoalsmade4=tk.StringVar()
fieldgoalsmade4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=fieldgoalsmade4, state='readonly')
fieldgoalsmade4Entry.grid(column=3, row=4, sticky='W')

ttk.Label(statsofteam2,text='FGA:').grid(column=2, row=5, sticky='E')
fieldgoalsattempted4=tk.StringVar()
fieldgoalsattempted4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=fieldgoalsattempted4, state='readonly')
fieldgoalsattempted4Entry.grid(column=3, row=5, sticky='W')

ttk.Label(statsofteam2,text='FG%:').grid(column=2, row=6, sticky='E')
fieldgoalpct4=tk.StringVar()
fieldgoalpct4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=fieldgoalpct4, state='readonly')
fieldgoalpct4Entry.grid(column=3, row=6, sticky='W')

ttk.Label(statsofteam2,text='3PM:').grid(column=2, row=7, sticky='E')
threesmade4=tk.StringVar()
threesmade4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=threesmade4, state='readonly')
threesmade4Entry.grid(column=3, row=7, sticky='W')

ttk.Label(statsofteam2,text='3PA:').grid(column=2, row=8, sticky='E')
threesattempted4=tk.StringVar()
threesattempted4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=threesattempted4, state='readonly')
threesattempted4Entry.grid(column=3, row=8, sticky='W')

ttk.Label(statsofteam2,text='3P%:').grid(column=2, row=9, sticky='E')
threespct4=tk.StringVar()
threespct4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=threespct4, state='readonly')
threespct4Entry.grid(column=3, row=9, sticky='W')

ttk.Label(statsofteam2,text='FTM:').grid(column=2, row=10, sticky='E')
freethrowsmade4=tk.StringVar()
freethrowsmade4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=freethrowsmade4, state='readonly')
freethrowsmade4Entry.grid(column=3, row=10, sticky='W')

ttk.Label(statsofteam2,text='FTA:').grid(column=2, row=11, sticky='E')
freethrowsattempted4=tk.StringVar()
freethrowsattempted4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=freethrowsattempted4, state='readonly')
freethrowsattempted4Entry.grid(column=3, row=11, sticky='W')

ttk.Label(statsofteam2,text='FT%:').grid(column=2, row=12, sticky='E')
freethrowpct4=tk.StringVar()
freethrowpct4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=freethrowpct4, state='readonly')
freethrowpct4Entry.grid(column=3, row=12, sticky='W')

ttk.Label(statsofteam2,text='TOV:').grid(column=2, row=13, sticky='E')
turnovers4=tk.StringVar()
turnovers4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=turnovers4, state='readonly')
turnovers4Entry.grid(column=3, row=13, sticky='W')

ttk.Label(statsofteam2,text='FT%:').grid(column=2, row=14, sticky='E')
personalfoul4=tk.StringVar()
personalfoul4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=personalfoul4, state='readonly')
personalfoul4Entry.grid(column=3, row=14, sticky='W')

ttk.Label(statsofteam2,text='ORB:').grid(column=2, row=15, sticky='E')
offensiverebounds4=tk.StringVar()
offensiverebounds4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=offensiverebounds4, state='readonly')
offensiverebounds4Entry.grid(column=3, row=15, sticky='W')

ttk.Label(statsofteam2,text='DRB:').grid(column=2, row=16, sticky='E')
defensiverebounds4=tk.StringVar()
defensiverebounds4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=defensiverebounds4, state='readonly')
defensiverebounds4Entry.grid(column=3, row=16, sticky='W')

ttk.Label(statsofteam2,text='RPG:').grid(column=2, row=17, sticky='E')
reboundspergame4=tk.StringVar()
reboundspergame4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=reboundspergame4, state='readonly')
reboundspergame4Entry.grid(column=3, row=17, sticky='W')

ttk.Label(statsofteam2,text='APG:').grid(column=2, row=18, sticky='E')
assistspergame4=tk.StringVar()
assistspergame4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=assistspergame4, state='readonly')
assistspergame4Entry.grid(column=3, row=18, sticky='W')

ttk.Label(statsofteam2,text='SPG:').grid(column=2, row=19, sticky='E')
stealspergame4=tk.StringVar()
stealspergame4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=stealspergame4, state='readonly')
stealspergame4Entry.grid(column=3, row=19, sticky='W')

ttk.Label(statsofteam2,text='BPG:').grid(column=2, row=20, sticky='E')
blockspergame4=tk.StringVar()
blockspergame4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=blockspergame4, state='readonly')
blockspergame4Entry.grid(column=3, row=20, sticky='W')

ttk.Label(statsofteam2,text='PPG:').grid(column=2, row=21, sticky='E')
pointspergame4=tk.StringVar()
pointspergame4Entry=ttk.Entry(statsofteam2, width=ENTRY_WIDTH, textvariable=pointspergame4, state='readonly')
pointspergame4Entry.grid(column=3, row=21, sticky='W')
#------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------------------------------------------------------

Teamselection=ttk.LabelFrame(tab2, text='City')
Teamselection.grid(column=0, row=0, padx=4, pady=4)
ttk.Label(Teamselection, text="Team 1: ").grid(column=0, row=0) # empty space for alignment

Teamselection2=ttk.LabelFrame(tab2, text='City 2')
Teamselection2.grid(column=2, row=0, padx=4, pady=4)
ttk.Label(Teamselection2, text="Team 2: ").grid(column=3, row=0) # empty space for alignment

# ---------------------------------------------------------------
station_id3= tk.StringVar()
station_id3_combo = ttk.Combobox(Teamselection, width=13, textvariable=station_id3)    
station_id3_combo['values'] = team_array
station_id3_combo.grid(column=1, row=0)
station_id3_combo.current(0) 

#-----------------------------------------------------------------------------------
station_id4 = tk.StringVar()
station_id4_combo = ttk.Combobox(Teamselection2, width=13, textvariable=station_id4)    
station_id4_combo['values'] = team2_array
station_id4_combo.grid(column=3, row=0)
station_id4_combo.current(0) 


def _get_station3():
    station = station_id3_combo.get()
    populate_gui_from_dict3(station)

def _get_station4():
    station = station_id4_combo.get()
    populate_gui_from_dict4(station)
    
def populate_gui_from_dict3(stringname):       
    gamesplayed3.set(str(df1.loc[df1.Team==str(stringname)].GP.values)[2:-2])
    minutespergame3.set(str(df1.loc[df1.Team==str(stringname)].MPG.values)[2:-2])
    fieldgoalsmade3.set(str(df1.loc[df1.Team==str(stringname)].FGM.values)[2:-2])
    fieldgoalsattempted3.set(str(df1.loc[df1.Team==str(stringname)].FGA.values)[2:-2])
    fieldgoalpct3.set(str(df1.loc[df1.Team==str(stringname)].FG.values)[2:-2])
    threesmade3.set(str(df1.loc[df1.Team==str(stringname)].threePM.values)[2:-2])
    threesattempted3.set(str(df1.loc[df1.Team==str(stringname)].threePA.values)[2:-2])
    threespct3.set(str(df1.loc[df1.Team==str(stringname)].threeP.values)[2:-2])
    freethrowsmade3.set(str(df1.loc[df1.Team==str(stringname)].FTM.values)[2:-2]) 
    freethrowsattempted3.set(str(df1.loc[df1.Team==str(stringname)].FTA.values)[2:-2])
    freethrowpct3.set(str(df1.loc[df1.Team==str(stringname)].FT.values)[2:-2])  
    turnovers3.set(str(df1.loc[df1.Team==str(stringname)].TOV.values)[2:-2])
    personalfoul3.set(str(df1.loc[df1.Team==str(stringname)].PF.values)[2:-2])
    offensiverebounds3.set(str(df1.loc[df1.Team==str(stringname)].ORB.values)[2:-2]) 
    defensiverebounds3.set(str(df1.loc[df1.Team==str(stringname)].DRB.values)[2:-2])
    reboundspergame3.set(str(df1.loc[df1.Team==str(stringname)].RPG.values)[2:-2])
    assistspergame3.set(str(df1.loc[df1.Team==str(stringname)].APG.values)[2:-2])
    stealspergame3.set(str(df1.loc[df1.Team==str(stringname)].SPG.values)[2:-2]) 
    blockspergame3.set(str(df1.loc[df1.Team==str(stringname)].BPG.values)[2:-2])
    pointspergame3.set(str(df1.loc[df1.Team==str(stringname)].PPG.values)[2:-2])

def populate_gui_from_dict4(stringname):       
    gamesplayed4.set(str(df1.loc[df1.Team==str(stringname)].GP.values)[2:-2])
    minutespergame4.set(str(df1.loc[df1.Team==str(stringname)].MPG.values)[2:-2])
    fieldgoalsmade4.set(str(df1.loc[df1.Team==str(stringname)].FGM.values)[2:-2])
    fieldgoalsattempted4.set(str(df1.loc[df1.Team==str(stringname)].FGA.values)[2:-2])
    fieldgoalpct4.set(str(df1.loc[df1.Team==str(stringname)].FG.values)[2:-2])
    threesmade4.set(str(df1.loc[df1.Team==str(stringname)].threePM.values)[2:-2])
    threesattempted4.set(str(df1.loc[df1.Team==str(stringname)].threePA.values)[2:-2])
    threespct4.set(str(df1.loc[df1.Team==str(stringname)].threeP.values)[2:-2])
    freethrowsmade4.set(str(df1.loc[df1.Team==str(stringname)].FTM.values)[2:-2]) 
    freethrowsattempted4.set(str(df1.loc[df1.Team==str(stringname)].FTA.values)[2:-2])
    freethrowpct4.set(str(df1.loc[df1.Team==str(stringname)].FT.values)[2:-2])  
    turnovers4.set(str(df1.loc[df1.Team==str(stringname)].TOV.values)[2:-2])
    personalfoul4.set(str(df1.loc[df1.Team==str(stringname)].PF.values)[2:-2])
    offensiverebounds4.set(str(df1.loc[df1.Team==str(stringname)].ORB.values)[2:-2]) 
    defensiverebounds4.set(str(df1.loc[df1.Team==str(stringname)].DRB.values)[2:-2])
    reboundspergame4.set(str(df1.loc[df1.Team==str(stringname)].RPG.values)[2:-2])
    assistspergame4.set(str(df1.loc[df1.Team==str(stringname)].APG.values)[2:-2])
    stealspergame4.set(str(df1.loc[df1.Team==str(stringname)].SPG.values)[2:-2]) 
    blockspergame4.set(str(df1.loc[df1.Team==str(stringname)].BPG.values)[2:-2])
    pointspergame4.set(str(df1.loc[df1.Team==str(stringname)].PPG.values)[2:-2])
    
for child in statsofteam.winfo_children(): 
        child.grid_configure(padx=4, pady=2) 
for child in statsofteam2.winfo_children(): 
        child.grid_configure(padx=4, pady=2) 
    
get_stats_btn = ttk.Button(Teamselection,text='Get Stats', command=_get_station3).grid(column=2, row=0)
get_stats_btn2 = ttk.Button(Teamselection2,text='Get Stats', command=_get_station4).grid(column=4, row=0)
##################_______________________TAB3________________##########################
#######################################################################################
   
WinURL="https://www.basketball-reference.com/leagues/NBA_wins.html"
response2=requests.get(WinURL)
soup2=BeautifulSoup(response2.content, 'html.parser')

columns3=['Season','lg_id','ATL','BOS','BRK','CHI','CHO','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC',
          'LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']

teamdf=pd.DataFrame(columns=columns3)
teamdf.fillna(0,inplace=True)
table3 = soup2.find('table', {'id':"active_franchises"}).tbody
#print(table3)

trs3=table3.find_all('tr')
for tr in trs3:
    tds=tr.find_all('td')
    row=[td.text.replace('\n', '') for td in tds]
    try:
        teamdf=teamdf.append(pd.Series(row, index=columns3), ignore_index=True)
    except:
        ValueError:('Length of passed values is 0, index implies 32')

teamdf.to_csv('Team Wins.csv', index=False)

data5=pd.read_csv('Team Wins.csv', names=columns3)
names5=data5.columns.tolist()
l=names5.pop(0)
l2=names5.pop(0)
plot_array=sorted(np.array(names5))

plotselection=ttk.LabelFrame(tab3, text='City')
plotselection.grid(column=0, row=0, padx=4, pady=4)
ttk.Label(plotselection, text=" ").grid(column=0, row=0) # empty space for alignment

station_id5= tk.StringVar()
station_id5_combo = ttk.Combobox( plotselection, width=5, textvariable=station_id5)    
station_id5_combo['values'] = plot_array
station_id5_combo.grid(column=1, row=0)
station_id5_combo.current(0)
 

def makePlot():
   
    vc=str(station_id5_combo.get())
    seasonarray=[]
    team_=[]
    y=teamdf.Season.values
    x=teamdf[vc]
    for i in range(0,len(y)):
        makeint=int(y[i][0:4])
        seasonarray.append(makeint)
    newarr=[]
    for j in range(0,len(x)):
        if len(x[j]) > 0 :
            team_.append(int(x[j]))
            newarr.append(seasonarray[j])
    yValues=team_
    xValues=newarr
    f = Figure(figsize=(4, 4), dpi=100)
    a = f.add_subplot(111)
    a.plot(xValues,yValues)
    a.set_xlabel('Year')
    a.set_ylabel('Wins')
    a.set_title('Total wins')
    canvas = FigureCanvasTkAgg(f, tab3)
    canvas.draw_idle()
    canvas.get_tk_widget().grid(column=2, row=0, columnspan=2, sticky='NSEW')

get_plot_btn = ttk.Button(plotselection,text='Plot', command=makePlot).grid(column=2, row=0)

window.mainloop()