import numpy as np
import pandas as pd
import json
import src.utils as utils
import src.indicator as indicator
from tabulate import tabulate

# Load the history data
trade_history = utils.loadTrades('./trades.json')
INI_VAL = 8000

# Define the trade history
returns = pd.to_numeric(trade_history['fillPnl']) # The return
fees = -pd.to_numeric(trade_history['fee'])
net_returns = returns - fees
value_history = utils.valueHistory(INI_VAL, net_returns)
long_trade_history = trade_history[trade_history['posSide'] == "long"]
short_trade_history = trade_history[trade_history['posSide'] == "short"]
ETH_trade_history = trade_history[trade_history['instId'].str.contains("ETH")]
BTC_trade_history = trade_history[trade_history['instId'].str.contains("BTC")]

# Calculate the indicator values
roi = indicator.RoI(INI_VAL, value_history[-1])*100
win_rate = indicator.winRate(returns)
mdd = indicator.MDD(value_history)
BTC_odds, ETH_odds, odds_ratio = indicator.oddsRatio(BTC_trade_history['fillPnl'], ETH_trade_history['fillPnl'])
profit_factor = indicator.profitFactor(net_returns)
sharp_ratio = indicator.sharpRatio(returns, roi)


# Plot the table of indicator values
data = [
    ["ROI", f"{roi}%"],
    ["Win Rate", f"{win_rate}%"],
    ["MDD", f"{mdd}%"],
    ["BTC Odds", BTC_odds],
    ["ETH Odds", ETH_odds],
    ["Odds Ratio", odds_ratio],
    ["Profit Factor", profit_factor],
    ["Sharp Ratio", sharp_ratio]
]
table = tabulate(data, headers=["Indicator", "Value"], tablefmt="grid")
print(table)