import numpy as np
import warnings
from typing import Tuple

def RoI(ini_val: float, final_value: float) -> float:
    return round((final_value - ini_val) / ini_val,4)

def winRate(returns: np.array) -> float:
    returns = returns.astype(float)
    win = np.count_nonzero(returns>0)
    total_transaction = np.count_nonzero(returns!=0)
    return round(win / total_transaction *100 ,2)

def MDD(value_history: np.ndarray) -> float:
    value_history = value_history.astype(float)
    peak_value = np.max(value_history)
    trough_value = np.min(value_history)
    return round((peak_value - trough_value) / peak_value * 100, 2)

def odds(returns: np.ndarray) -> float:
    returns = returns.astype(float)
    win = np.count_nonzero(returns>0)
    loss = np.count_nonzero(returns<0)
    if loss == 0.0:
        return np.inf
    return round(win/loss, 4)

def oddsRatio(group1: np.ndarray, group2: np.ndarray) -> Tuple[float, float, float]:
    group1 = odds(group1.astype(float))
    group2 = odds(group2.astype(float))
    if np.isinf(group1) and np.isinf(group2):
        warnings.warn("The odds of group1 and group2 are inf, return nan", UserWarning)
        return group1, group2, np.nan
    if np.isnan(group1):
        warnings.warn("The odds of group1 is inf, return inf", UserWarning)
        return group1, group2, 0
    if np.isnan(group2):
        warnings.warn("The odds of group2 is inf, return 0", UserWarning)
        return group1, group2, np.inf
    return group1, group2, round(group1/group2,4)

def profitFactor(net_returns: np.ndarray) -> float:
    net_returns = net_returns.astype(float)
    goss_profits = np.sum(net_returns[net_returns>0])
    goss_loss = abs(np.sum(net_returns[net_returns<0]))
    if goss_loss == 0.0:
        goss_loss = 0
        warnings.warn("The number of loss trading is 0. The value of odds would be abnomal", UserWarning)
    return round(goss_profits/goss_loss,4)

def sharpRatio(returns: np.ndarray, roi: float) -> float:
    returns = returns.astype(float)
    returns = returns[returns != 0]
    profits_std = returns.std()
    RISK_FREE_RATE = 0.02 #short-term US government bonds rate
    if profits_std == 0.0:
        warnings.warn("The value of std is 0, return inf.", UserWarning)
        return np.inf
    return round((roi - RISK_FREE_RATE) / profits_std, 4)
    
    
    