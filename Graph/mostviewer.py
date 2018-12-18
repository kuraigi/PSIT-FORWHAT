# -*- coding: utf-8 -*-
"""
Top 10 The Most Viwed of Games
"""

import pandas as pd
names = ['fn', 'lol', 'ssbu', 'chat', 'dota2', 'ht', 'pubg', 'csbo4', 'poe', 'csgo']
games = ['Fortnite', 'League of Legends', 'Super Smash Bros. Ultimate', 'Just Chatting', 'Dota2', 'Hearthstone', 'PUBG', 'Call of Duty:Black Ops 4', 'Path of Exile', 'Counter-Strike: Global Offensive']
data_dict = {'name': pd.Series(names), 'game': pd.Series(games)}
dframe = pd.DataFrame(data_dict)
dframe.index
dframe.columns
viewer = [2129766, 1629649, 1123121, 928661, 800058, 761407, 606964, 586345, 578018, 391746]
dframe['viewer'] = pd.Series(viewer)
dframe.plot.bar(x='game', y='viewer')

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10,6)
plt.style.available
import matplotlib
matplotlib.style.use('ggplot')
