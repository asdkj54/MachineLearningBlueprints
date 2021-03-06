import getData as gd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

spy = gd.spy

spy_c = spy['Close']

fig, ax = plt.subplots(figsize=(15, 10))
spy_c.plot(color='k')
plt.title("SPY", fontsize=20)
#plt.show()

first_open = spy['Open'].iloc[0]
last_open = spy['Close'].iloc[-1]

spy['Daily Change'] = pd.Series(spy['Close'] - spy['Open'])
#print(spy['Daily Change'].sum())

#print(np.std(spy['Daily Change']))

spy['Overnight Change'] = pd.Series(spy['Open'] - spy['Close'].shift(1))
#print(np.std(spy['Overnight Change']))

#print(spy[spy['Daily Change']<0]['Daily Change'].mean())
#print(spy[spy['Overnight Change']<0]['Overnight Change'].mean())

daily_rtn = ((spy['Close'] - spy['Close'].shift(1))/spy['Close'].shift(1)) * 100
id_rtn = ((spy['Close'] - spy['Open'])/spy['Open']) * 100
on_rtn = ((spy['Open'] - spy['Close'].shift(1))/spy['Close'].shift(1)) * 100

def get_stats(s, n=252):
    s = s.dropna()
    wins = len(s[s>0])
    losses = len(s[s<0])
    evens = len(s[s==0])
    mean_w = round(s[s>0].mean(), 3)
    mean_l = round(s[s<0].mean(), 3)
    win_r = round(wins/losses, 3)
    mean_trd = round(s.mean(), 3)
    sd = round(np.std(s), 3)
    max_l = round(s.min(), 3)
    max_w = round(s.max(), 3)
    sharpe_r = round((s.mean()/np.std(s)) * np.sqrt(n), 4)
    cnt = len(s)
    print('Trades:', cnt,
          '\nWins:', wins,
          '\nLosses:', losses,
          '\nBreakeven:', evens,
          '\nWin/Loss Ratio', win_r,
          '\nMean Win:', mean_w,
          '\nMean Loss:', mean_l,
          '\nMean:', mean_trd,
          '\nStd Dev:', sd,
          '\nMax Loss:', max_l,
          '\nMax Win:', max_w,
          '\nSharpe Ratio:', sharpe_r)
get_stats(daily_rtn)
get_stats(id_rtn)
get_stats(on_rtn)